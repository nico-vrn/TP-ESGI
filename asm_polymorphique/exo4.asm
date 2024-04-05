section .data
filename db 'output.txt',0        ; Nom du fichier
mode     db 'w',0                 ; Mode d'ouverture du fichier (écrire)

section .bss
file     resb 1                   ; Réserve un espace pour le descripteur de fichier

section .text
global _start

_start:
    ; Ouvrir le fichier (syscall open)
    mov rax, 2                    ; Syscall numéro pour sys_open
    mov rdi, filename             ; Pointeur vers le nom du fichier
    mov rsi, 0                    ; Flags (O_RDONLY, etc. 0 pour créer)
    mov rdx, 0777                 ; Permissions
    syscall

    ; Stocker le descripteur de fichier
    mov [file], rax

    ; Écrire dans le fichier (syscall write)
    mov rax, 1                    ; Syscall numéro pour sys_write
    mov rdi, [file]               ; Descripteur de fichier
    mov rsi, filename             ; Buffer à écrire ("1" est déjà dans 'filename', astuce pour simplifier)
    mov rdx, 1                    ; Nombre de bytes à écrire
    syscall

    ; Fermer le fichier (syscall close)
    mov rax, 3                    ; Syscall numéro pour sys_close
    mov rdi, [file]               ; Descripteur de fichier
    syscall

    ; Terminer le programme (syscall exit)
    mov rax, 60                   ; Syscall numéro pour sys_exit
    xor rdi, rdi                  ; Status
    syscall
