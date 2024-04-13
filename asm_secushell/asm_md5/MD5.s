extern MD5_Init
extern MD5_Update
extern MD5_Final

%define BUFFER_SIZE 1024

section .data
    file_path   db 'fichier.txt', 0    ; Chemin du fichier
    md5_res     times 16 db 0          ; Buffer pour stocker le résultat du hachage MD5
    buffer      times BUFFER_SIZE db 0 ; Buffer pour lire le fichier
    md5_ctx     times 104 db 0         
    hex_digits  db '0123456789abcdef'  ; Caractères hexadécimaux pour la conversion
    newline     db 0xa                 ; Caractère de nouvelle ligne

section .bss
    hex_buffer  resb 33                ; Buffer pour stocker le hachage MD5

section .text
    global _start

_start:
    mov rdi, md5_ctx
    call align_buffer

    ; Initialiser le contexte MD5.
    lea rdi, [md5_ctx]       ; pointeur vers md5_ctx
    call MD5_Init

    ; Ouvrir le fichier en lecture seule.
    mov rax, 2               
    mov rdi, file_path       ; chemin du fichier
    xor rsi, rsi             
    syscall
    cmp rax, 0               ; Vérifier si l'appel système a réussi
    jl  error_exit           
    mov rbx, rax             ; Sauvegarder le descripteur de fichier dans rbx

read_loop:
    ; Lire le contenu du fichier par blocs.
    mov rax, 0               
    mov rdi, rbx             
    mov rsi, buffer          
    mov rdx, BUFFER_SIZE     
    syscall
    cmp rax, 0               ; Vérifier si la fin du fichier a été atteinte ou une erreur s'est produite
    jle md5_end              ; Si rax est 0 ou négatif, fin du fichier ou erreur

    ; Afficher le contenu du buffer
    mov rdx, rax             
    mov rax, 1               
    mov rdi, 1               ; Sortie standard (écran)
    mov rsi, buffer          
    syscall

    ; Mettre à jour le contexte MD5 avec le bloc lu.
    mov rdi, md5_ctx         ; contexte MD5
    mov rsi, buffer          ; données à hacher
    mov rdx, rax             ; nombre d'octets lus
    call MD5_Update
    jmp read_loop

md5_end:
    ; Finaliser le hachage MD5.
    mov rdi, md5_ctx         
    lea rsi, [md5_res]       
    call MD5_Final

    ; Afficher une nouvelle ligne.
    mov rax, 1               
    mov rdi, 1               ; Sortie standard (écran)
    mov rsi, newline         ; Pointeur vers le caractère de nouvelle ligne
    mov rdx, 1               ; Nombre d'octets à afficher (1 caractère)
    syscall

    ; Afficher le résultat du hachage MD5 sous forme hexadécimale.
    lea rsi, [md5_res]       ; Pointeur vers le résultat du hachage MD5
    lea rdi, [hex_buffer]    
    call print_md5_hex

    ; Afficher la représentation hexadécimale du hachage MD5.
    mov rax, 1               
    mov rdi, 1               
    mov rsi, hex_buffer      
    mov rdx, 32              
    syscall

    ; Afficher une nouvelle ligne.
    mov rax, 1               
    mov rdi, 1               ; Sortie standard (écran)
    mov rsi, newline         
    mov rdx, 1               
    syscall

    ; Fermer le fichier
    mov rax, 3               
    mov rdi, rbx             
    syscall

    ; Sortie du programme
    mov rax, 60             
    xor rdi, rdi             
    syscall

print_md5_hex:
    ; Fonction pour convertir le résultat du hachage MD5 en représentation hexadécimale.
    ; rsi : pointeur vers le résultat du hachage MD5
    push rax
    push rbx
    push rcx
    xor rax, rax
    xor rbx, rbx

print_md5_hex_loop:
    mov bl, byte [rsi + rax]
    shr bl, 4
    mov cl, hex_digits[rbx] 
    mov byte [rdi + rax * 2], cl
    and bl, 0fh
    mov cl, hex_digits[rbx] 
    mov byte [rdi + rax * 2 + 1], cl
    inc rax
    cmp rax, 16
    jne print_md5_hex_loop

    mov byte [rdi + 32], 0   

    pop rcx
    pop rbx
    pop rax
    ret

align_buffer:
    ; Fonction pour aligner un tampon sur une frontière de 8 octets.
    push rbx
    mov rbx, rdi
    and rbx, 0x7             
    jz  aligned              ; Si rbx est nul, le tampon est déjà aligné
    add rdi, 8
    sub rdi, rbx             ; Ajuster le pointeur du tampon

aligned:
    mov rax, rdi
    pop rbx
    ret

error_exit:
    ; Code pour gérer les erreurs (fermeture de fichiers, libération de la mémoire, etc.)
    mov rax, 60              ; Appel système exit
    mov rdi, 1               ; Code de sortie 1 (erreur)
    syscall