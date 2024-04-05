section .data
filename db 'output.txt', 0      ; Nom du fichier
content  db '1', 0               ; Contenu à écrire dans le fichier - initialisé à '1'

section .bss
fileDescriptor resq 1            ; Réserve un espace pour le descripteur de fichier (64 bits)

section .text
global _start

_start:
    ; Ouvrir ou créer le fichier
    mov rax, 2                   ; syscall pour sys_open
    mov rdi, filename            ; premier argument: nom du fichier
    mov rsi, 0101h               ; deuxième argument: flags (O_WRONLY | O_CREAT)
    mov rdx, 0666o               ; troisième argument: mode (permissions)
    syscall
    mov [fileDescriptor], rax    ; sauvegarder le descripteur de fichier

write_loop:                       ; Étiquette pour la boucle d'écriture
    ; Écrire dans le fichier
    mov rax, 1                   ; syscall pour sys_write
    mov rdi, [fileDescriptor]    ; premier argument: descripteur de fichier
    mov rsi, content             ; deuxième argument: buffer de données
    mov rdx, 2                   ; troisième argument: nombre d'octets à écrire
    syscall

    ; Incrémenter le caractère
    inc byte [content]           ; Incrémente le caractère à écrire

    ; Condition pour continuer/arrêter la boucle (ex: après '9')
    cmp byte [content], '9'+1    ; Vérifier si le caractère dépasse '9'
    jle write_loop               ; Si <= '9', continuer la boucle

    ; Fermer le fichier
    mov rax, 3                   ; syscall pour sys_close
    mov rdi, [fileDescriptor]    ; premier argument: descripteur de fichier
    syscall

    ; Terminer le programme
    mov rax, 60                  ; syscall pour sys_exit
    xor rdi, rdi                 ; code de sortie 0
    syscall
