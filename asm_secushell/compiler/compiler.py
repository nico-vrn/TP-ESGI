import struct
import sys
import os

# Définition des instructions
INSTRUCTIONS = {
    'mov': 0xB8,
    'push': 0x50,
    'pop': 0x58,
    'call': 0xE8,
    'add': 0x03,
    'sub': 0x2B,
    'cmp': 0x3B,
    'je': [0x0F, 0x84],  # Opcode en deux parties pour je
    'jmp': 0xE9,
    'ret': 0xC3,
    'int': 0xCD,
    'xor': 0x33,
    'syscall': [0x0F, 0x05]
}

# Définition des registres
REGISTERS = {
    'rax': 0, 'eax': 0,
    'rbx': 3, 'ebx': 3,
    'rcx': 1, 'ecx': 1,
    'rdx': 2, 'edx': 2,
    'rsi': 6, 'esi': 6,
    'rdi': 7, 'edi': 7,
    'rbp': 5, 'ebp': 5,
    'rsp': 4, 'esp': 4,
    'r8': 8, 'r9': 9, 'r10': 10, 'r11': 11, 'r12': 12, 'r13': 13, 'r14': 14, 'r15': 15
}

# En-tête ELF pour x86-64
ELF_HEADER = b'\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
             b'\x02\x00\x3e\x00\x01\x00\x00\x00\x08\x00\x40\x00\x00\x00' \
             b'\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
             b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
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
    text_address = 0x400000 + len(ELF_HEADER) + len(PROGRAM_HEADER)
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
    
    encoded = []
    
    if instruction == 'mov':
        if len(operands) < 1:
            raise ValueError(f"Nombre d'opérandes insuffisant pour l'instruction {instruction}")
        elif len(operands) == 1:
            # Traitement pour l'instruction mov avec un seul opérande
            register = REGISTERS.get(operands[0])
            if register is None:
                raise ValueError(f"Registre non supporté: {operands[0]}")
            encoded.extend([opcode | register])
        else:
            # Traitement pour l'instruction mov avec deux opérandes
            register = REGISTERS.get(operands[0])
            if register is None:
                raise ValueError(f"Registre non supporté: {operands[0]}")
            
            if operands[1].startswith('0x'):
                value = int(operands[1], 16)
            else:
                value = int(operands[1], 0)
            
            encoded.extend([opcode | (register << 24), value & 0xFF, (value >> 8) & 0xFF, (value >> 16) & 0xFF, (value >> 24) & 0xFF])
    elif instruction == 'int':
        value = int(operands[0], 16)
        encoded.extend([opcode, value])
    elif instruction == 'syscall':
        encoded.extend(opcode)
    elif instruction == 'je':
        # Instruction à deux octets
        encoded.extend(opcode)
        if len(operands) != 1:
            raise ValueError(f"Nombre d'opérandes incorrect pour l'instruction {instruction}")
        encoded.append(int(operands[0], 16))
    elif instruction == 'push' or instruction == 'pop':
        encoded.append(opcode)
        if len(operands) != 1:
            raise ValueError(f"Nombre d'opérandes incorrect pour l'instruction {instruction}")
        register = REGISTERS.get(operands[0])
        if register is None:
            raise ValueError(f"Registre non supporté: {operands[0]}")
        encoded.append(register)
    elif instruction == 'stp':
        # Instruction stp pour ARM64
        encoded.append(0x29)  # Opcode pour stp
        
        # Encodage des registres
        reg1 = REGISTERS.get(operands[0])
        reg2 = REGISTERS.get(operands[1])
        if reg1 is None or reg2 is None:
            raise ValueError(f"Registre non supporté: {operands[0]} ou {operands[1]}")
        encoded.append((reg1 << 4) | reg2)
        
        # Encodage de l'adresse de base
        base_reg = REGISTERS.get(operands[2][1:-1])  # Suppression des crochets
        if base_reg is None:
            raise ValueError(f"Registre non supporté: {operands[2][1:-1]}")
        encoded.append(base_reg << 5)
        
        # Encodage de l'offset (si présent)
        if len(operands) > 3:
            offset = int(operands[3], 16)
            encoded.append(offset >> 4)
            encoded.append((offset & 0xF) << 1)
    else:
        # Instructions à un octet
        encoded.append(opcode)
        if len(operands) > 0:
            raise ValueError(f"Nombre d'opérandes incorrect pour l'instruction {instruction}")
    
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
