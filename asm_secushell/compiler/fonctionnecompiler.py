import struct
import sys
import os

# Définition des instructions
INSTRUCTIONS = {
    'mov': 0xB8,
    'push': 0x68,
    'pop': 0x58,
    'call': 0xE8,
    'add': 0x03,
    'sub': 0x2B,
    'cmp': 0x3B,
    'je': 0x74,
    'jmp': 0xE9,
    'ret': 0xC3,
    'int': 0xCD,
    'xor': 0x31
}

# Définition des registres
REGISTERS = {
    'eax': 0,
    'ebx': 3,
    'ecx': 1,
    'edx': 2,
    'esi': 6,
    'edi': 7
}

# En-tête ELF pour x86-64
ELF_HEADER = b'\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
             b'\x02\x00\x3e\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
             b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
             b'\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
             b'\x00\x00\x40\x00\x38\x00\x01\x00\x00\x00\x00\x00\x00\x00'
             
# En-tête programme ELF
PROGRAM_HEADER = b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x08\x00\x00' \
                 b'\x00\x00\x00\x00\x04\x08\x00\x00\x00\x00\x00\x00\x01' \
                 b'\x00\x00\x00\x05\x00\x00\x00'

# Fonction pour créer un fichier exécutable
def create_executable(text_segment, data_segment, filename):
    # Alignement des sections
    text_segment = text_segment.ljust((len(text_segment) + 15) // 16 * 16, b'\x00')
    data_segment = data_segment.ljust((len(data_segment) + 15) // 16 * 16, b'\x00')
    
    # Adresses de sections
    text_address = 0x08048000 + len(ELF_HEADER) + len(PROGRAM_HEADER)
    data_address = text_address + len(text_segment)
    
    # Mise à jour du header de programme avec les bonnes tailles et adresses
    program_header = struct.pack(
        '<IIIIIIII',
        1,         # Type de segment (LOAD)
        0,         # Offset du segment dans le fichier
        text_address, # Adresse virtuelle du segment
        text_address, # Adresse physique du segment
        len(text_segment) + len(data_segment), # Taille du segment dans le fichier
        len(text_segment) + len(data_segment), # Taille du segment en mémoire
        5,         # Droits d'accès du segment (lecture/exécution)
        0x1000     # Alignement du segment
    )
    
    with open(filename, 'wb') as f:
        f.write(ELF_HEADER)
        f.write(program_header)
        f.write(text_segment)
        f.write(data_segment)
    
    # Rendre le fichier exécutable sur Unix/Linux
    os.chmod(filename, 0o755)

# Fonction pour encoder une instruction
def encode_instruction(instruction, operands):
    opcode = INSTRUCTIONS.get(instruction)
    if opcode is None:
        raise ValueError(f"Instruction non supportée: {instruction}")
    
    encoded = [opcode]
    
    if instruction == 'mov':
        if operands[0] == 'eax':
            if operands[1].startswith('0x'):
                value = int(operands[1], 16)
            else:
                value = int(operands[1], 0)
            encoded.extend(struct.pack('<I', value))
    elif instruction == 'int':
        value = int(operands[0], 16)
        encoded.extend(struct.pack('<B', value))
    
    return bytes(encoded)

# Fonction pour compiler un programme
def compile(asm_code):
    text_segment = b''
    data_segment = b''
    in_text_section = False
    in_data_section = False
    
    for line in asm_code.split('\n'):
        line = line.strip()
        if not line or line.startswith(';'):
            continue
        
        if line.startswith('section'):
            in_text_section = (line == 'section .text')
            in_data_section = (line == 'section .data')
            continue

        if line.startswith('global'):
            continue

        if line.endswith(':'):
            continue

        if in_text_section:
            parts = line.split()
            instruction = parts[0]
            operands = parts[1:]
            encoded = encode_instruction(instruction, operands)
            text_segment += encoded
        elif in_data_section:
            parts = line.split()
            if len(parts) >= 3 and parts[1] == 'db':
                label = parts[0][:-1]
                data = parts[2].replace("'", "").encode('ascii')
                data_segment += data + b'\x00'
    
    return text_segment, data_segment

# Fonction principale
def main():
    if len(sys.argv) < 2:
        print("Utilisation : python compiler.py <fichier.asm>")
        return

    asm_file = sys.argv[1]
    with open(asm_file, 'r') as f:
        asm_code = f.read()

    text_segment, data_segment = compile(asm_code)
    executable_file = asm_file.replace('.asm', '')
    create_executable(text_segment, data_segment, executable_file)
    print(f"Exécutable généré : {executable_file}")

if __name__ == "__main__":
    main()
