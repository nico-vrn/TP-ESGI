section .data
    filename db 'fichier.txt', 0  ; Nom du fichier à hacher

section .text
    global _start
    extern compute_md5  ; Déclare la fonction externe

_start:
    mov rdi, filename  
    call compute_md5   ; Appelle la fonction C
    mov eax, 60        
    xor edi, edi       
    syscall