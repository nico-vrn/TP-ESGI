section .data
helloMessage db 'Hello world', 0xA  ; Message à afficher avec un saut de ligne à la fin

section .text
global _start

_start:
    ; Écrire le message dans STDOUT
    mov rax, 1                  ; syscall numéro pour sys_write
    mov rdi, 1                  ; file descriptor 1 pour STDOUT
    mov rsi, helloMessage       ; adresse du message
    mov rdx, 13                 ; longueur du message ("Hello world" + saut de ligne)
    syscall                     ; effectuer l'appel système

    ; Terminer le programme
    mov rax, 60                 ; syscall numéro pour sys_exit
    xor rdi, rdi                ; status de sortie 0
    syscall                     ; effectuer l'appel système
