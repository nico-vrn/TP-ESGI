<h1 align="center">TP ASSEMBLEUR MD5<h1>

<p>Ce repo est destiné à mon TP pour faire un hash md5 en asm.<br>

2 manières de faire ont été exploré afin d'arriver à mes fins </p>

<h2 align="center">Les Dossiers<h2>

## asm_md5
Le fichier "MD5.s" est censé faire un hash md5 d'un fichier. 

Le fichier à hash est modifiable ligne 9 du fichier, par défaut c'est "fichier.txt".

En revanche il ne fonctionne pas bien. 

Il affiche le contenu du fichier et un hash mais le hash est faux et je n'ai pas réussi à corriger le problème.
Par contre le nombre de carractère Hexadécimal est correct.

### Compilation 
Pour compiler le code correctement et le rendre exécutable : 
```sh 
nasm -f elf64 MD5.s 
```
```sh
ld -o MD5 MD5.o -lc -dynamic-linker /lib64/ld-linux-x86-64.so.2 -lcrypto
```
```sh
./MD5
```

### Sortie
```sh
L'assembleur c'est l'enfer.

2c3948cacc3fe672c7d9583abe93beec
```

### Erreur 
Après vérification, le hash est censé être : e165f7c4925635da0d0ba02f232040a7

Donc le fichier ne fonctionne pas.

<br> <br>

## md5_asm_c
Ce dossier contient 2 fichiers : 

### md5.c
Ce code en C effectue le hash md5 du fichier. 

### md5c.asm 
Ce code en assembleur appel la fonction C et lui donne en objet le fichier à hasher. 

Le fichier à hash est modifiable ligne 8 du fichier, par défaut c'est "fichier.txt".

### Compilation 
Pour compiler le code correctement et le rendre exécutable : 
```sh
gcc -c md5.c -o md5hash.o
```
```sh
nasm -f elf64 -g md5c.asm -o assembleur.o
```
```sh
gcc -o programme_final assembleur.o md5hash.o -lcrypto -nostartfiles -no-pie
```

### Sortie 
MD5 hash of "fichier.txt": 65a8e27d8879283831b664bd8b7f0ad4
