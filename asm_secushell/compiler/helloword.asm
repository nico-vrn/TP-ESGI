section .data
    msg db 'Hello World!', 0xA  ; La chaîne à afficher, terminée par un saut de ligne (0xA)

section .text
    global _start

_start:
    mov rax, 1          ; Appel système pour écrire (sys_write)
    mov rdi, 1          ; Descripteur de fichier 1 (stdout)
    mov rsi, msg        ; Pointeur vers la chaîne à afficher
    mov rdx, 14         ; Longueur de la chaîne
    syscall             ; Appel système

    mov rax, 60         ; Appel système pour quitter (sys_exit)
    xor rdi, rdi        ; Code de sortie 0
    syscall             ; Appel système
