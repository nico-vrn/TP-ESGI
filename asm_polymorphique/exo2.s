section .data
    filePath db 'input.txt', 0    ; Chemin vers le fichier à lire

section .bss
    buffer resb 64                ; Réserve un espace de 64 octets pour le buffer de lecture
    fileDescriptor resq 1         ; Réserve un espace pour le descripteur de fichier

section .text
global _start                    ; Symbole global nécessaire pour le point d'entrée du programme

_start:
    ; Ouvrir le fichier pour lecture
    mov rax, 2                   ; syscall pour sys_open
    mov rdi, filePath            ; Le premier argument de sys_open est le chemin du fichier
    mov rsi, 0                   ; Le deuxième argument de sys_open sont les flags (0 pour lecture seule)
    syscall                      ; Exécute l'appel système
    mov [fileDescriptor], rax    ; Stocke le descripteur de fichier

    ; Lire depuis le fichier
    mov rax, 0                   ; syscall pour sys_read
    mov rdi, [fileDescriptor]    ; Le premier argument de sys_read est le descripteur de fichier
    mov rsi, buffer              ; Le deuxième argument de sys_read est le buffer où stocker les données lues
    mov rdx, 64                  ; Le troisième argument de sys_read est le nombre d'octets à lire
    syscall                      ; Exécute l'appel système

    ; Fermer le fichier
    mov rax, 3                   ; syscall pour sys_close
    mov rdi, [fileDescriptor]    ; Le premier argument de sys_close est le descripteur de fichier
    syscall                      ; Exécute l'appel système

    ; Écrire le contenu lu sur STDOUT
    mov rax, 1                   ; syscall pour sys_write
    mov rdi, 1                   ; Le premier argument de sys_write est le file descriptor pour STDOUT
    mov rsi, buffer              ; Le deuxième argument de sys_write est le buffer contenant les données à écrire
    mov rdx, 64                  ; Le troisième argument de sys_write est le nombre d'octets à écrire
    syscall                      ; Exécute l'appel système

    ; Terminer le programme
    mov rax, 60                  ; syscall pour sys_exit
    xor rdi, rdi                 ; Le premier argument de sys_exit est le code de sortie, 0 indique une sortie sans erreur
    syscall                      ; Exécute l'appel système
