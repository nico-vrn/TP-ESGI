section .data
    filename db 'output.bin', 0  ; Nom du fichier à créer/écrire

section .bss
    fileDescriptor resq 1        ; Réserver un espace pour le descripteur de fichier (suffisamment grand pour un descripteur de fichier sur x64)

section .text
global _start

_start:
    ; Réserver 100 octets sur la pile et les initialiser à 0x90
    sub rsp, 100                 ; Réserver 100 octets sur la pile
    mov rdi, rsp                 ; Pointeur vers le début de la zone réservée
    mov rcx, 100                 ; Nombre d'octets à initialiser
init_loop:
    mov byte [rdi], 0x90         ; Initialiser l'octet à 0x90
    inc rdi                      ; Passer à l'octet suivant
    loop init_loop               ; Répéter pour tous les 100 octets

    ; Appliquer XOR à chaque octet avec 0xAA
    mov rdi, rsp                 ; Réinitialiser RDI au début de la zone réservée
    mov rcx, 100                 ; Nombre d'octets à traiter
xor_loop:
    xor byte [rdi], 0xAA         ; Appliquer XOR 0xAA à l'octet
    inc rdi                      ; Passer à l'octet suivant
    loop xor_loop                ; Répéter pour tous les 100 octets

    ; Ouvrir/Créer le fichier
    mov rax, 2                   ; syscall pour sys_open
    mov rdi, filename            ; Premier argument: chemin du fichier
    mov rsi, 0201h               ; Deuxième argument: flags (O_WRONLY | O_CREAT)
    mov rdx, 0644h               ; Troisième argument: mode (permissions)
    syscall
    mov [fileDescriptor], rax    ; Sauvegarder le descripteur de fichier

    ; Écrire dans le fichier
    mov rax, 1                   ; syscall pour sys_write
    mov rdi, [fileDescriptor]    ; Premier argument: descripteur de fichier
    mov rsi, rsp                 ; Deuxième argument: buffer (données à écrire)
    mov rdx, 100                 ; Troisième argument: nombre d'octets à écrire
    syscall

    ; Fermer le fichier
    mov rax, 3                   ; syscall pour sys_close
    mov rdi, [fileDescriptor]    ; Premier argument: descripteur de fichier
    syscall

    ; Terminer le programme
    add rsp, 100                 ; Nettoyer la pile (restaurer rsp)
    mov rax, 60                  ; syscall pour sys_exit
    xor rdi, rdi                 ; Code de sortie 0
    syscall
