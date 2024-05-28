; Programme asm qui hash en MD5
extern MD5_Init
extern MD5_Update
extern MD5_Final

%define BUFFER_SIZE 1024 ; défini la taille du buffer

section .data
    file_path db 'fichier.txt', 0 ;le fichier à Hash
    md5_res times 16 db 0
    buffer times BUFFER_SIZE db 0
    md5_ctx times 104 db 0
    hex_digits db '0123456789abcdef', 0
    newline db 0xa, 0             

section .bss
    hex_buffer resb 33

section .text
    global _start

_start:
    ; Initialisation 
    lea rdi, [md5_ctx]
    call MD5_Init

    ; Ouvrir le fichier
    mov rax, 2              
    lea rdi, [file_path]    
    xor rsi, rsi            ; mode lecture
    syscall
    test rax, rax
    js _error               ; si erreur
    mov rbx, rax            

_read:
    ; Lire le fichier
    mov rax, 0              
    mov rdi, rbx            
    lea rsi, [buffer]       ; buffer
    mov rdx, BUFFER_SIZE    
    syscall
    test rax, rax
    jle _done_reading       

    ; Afficher le contenu du fichier
    mov rdx, rax            
    mov rax, 1             
    mov rdi, 1              
    lea rsi, [buffer]      
    syscall

    ; Mettre à jour le hash MD5
    lea rdi, [md5_ctx]
    lea rsi, [buffer]
    mov rdx, rax
    call MD5_Update

    jmp _read

_done_reading:
    ; Finaliser le hash MD5
    lea rdi, [md5_ctx]
    lea rsi, [md5_res]
    call MD5_Final

    ; Print une nouvelle ligne
    mov rax, 1              
    mov rdi, 1              
    lea rsi, [newline]
    mov rdx, 1
    syscall

    ; Convertir le hash MD5 en hexadécimal
    lea rsi, [md5_res]
    lea rdi, [hex_buffer]
    call to_hex

    ; Afficher le hash hexadecimal MD5 
    mov rax, 1              
    mov rdi, 1              
    lea rsi, [hex_buffer]
    mov rdx, 32
    syscall

    ; Print une nouvelle ligne
    mov rax, 1              
    mov rdi, 1              
    lea rsi, [newline]
    mov rdx, 1
    syscall

    ; Exit
    mov rax, 60             
    xor rdi, rdi            
    syscall

to_hex:
    ; rsi = input buffer (MD5 hash)
    ; rdi = output buffer (hexadecimal string)
    push rbx
    push rcx
    xor rax, rax

convert_loop:
    mov bl, byte [rsi + rax]
    shr bl, 4
    mov cl, [hex_digits + rbx]
    mov byte [rdi + rax * 2], cl
    mov bl, byte [rsi + rax]
    and bl, 0xF
    mov cl, [hex_digits + rbx]
    mov byte [rdi + rax * 2 + 1], cl
    inc rax
    cmp rax, 16
    jne convert_loop

    mov byte [rdi + rax * 2], 0
    pop rcx
    pop rbx
    ret

_error:
    mov rax, 60             
    mov rdi, 1              ; sortie propre
    syscall
