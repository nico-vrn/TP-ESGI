<h1 align="center">TP Compileur C<h1>

<p>Ce repo est destiné à mon TP pour faire un compilateur de fichier C en Python.<br>
</p>

3 manières de faire ont été exploré afin d'arriver à mes fins

## Pré-requis
### Dépendances Python 
Assurez-vous d'avoir les dépendances suivantes installés 
- Python 3.6 ou + 
- llvmlite
- pcpp
- pycparser
- gcc

Vous pouvez installer les packages Python nécessaires en utilisant pip :
```sh
pip install llvmlite pcpp pycparser
```
### Pré-requis système 
Pour certains des fichiers il faut utiliser le compilateur "gcc". Assurez-vous que gcc est installé sur votre système. Vous pouvez vérifier cela en exécutant gcc --version dans votre terminal. Si ce n'est pas installé, vous pouvez l'installer en utilisant le gestionnaire de packages de votre système (par exemple, apt pour Ubuntu/Debian, brew pour macOS).

## Instalation 
1. Clonez le dépôt.
2. Assurez-vous que toutes les dépendances sont installées comme mentionné ci-dessus.

## Compilateur C
### Fichier CompilerC
Usage: python3 compilerC.py <fichier.c>

Le fichier "compilerC.py" est le plus abouti, il utilise toutes une logique afin de: 
- Pré-traité le code C en utilisant pcpp
- Le code prétraité est néttoyé afin de supprimer les directives du préprocesseurs, les commentaires et les lignes vides
- Le code est ensuite analysé pour créer un AST en utilisant pycparser
- Le code est enfin compilé en un fichier .o 
- Le code est finalement Linker en utilisant gcc afin de créer un exéctuable fini et fonctionnel. 

Après test, voici les sorties pour les 2 fichiers de test : 
Helloworld.c : 
```sh 
$ python3 compilerC.py helloworld.c
$ Compilation réussie. Exécutable créé: output
$ ./output
$ Hello, world!\n
```

Fibonacci.c : 
```sh
$ python3 compilerC.py fibonacci.c
$ Compilation réussie. Exécutable créé: output
$ ./output
$ -1787386600 Les 5001458 premiers termes de la suite de Fibonacci sont :\n
```

On voici ici aucune erreur pour helloworld.c, en revanche le fichier Fibonacci.c ne fonctionne pas, le code prend mal en compte l'appel de fonction et je n'ai pas réussi à corriger cette erreur.

### Fichier CompilerC2
Usage: python3 compilerC2.py <fichier.c>

Le fichier "compilerC2" compile correctement les fichier "hello_world.c" et "fibonacci.c" en revanche il exécute simplement des compilateurs systèmes. 


### Fichier CompilerC3
Usage: python compiler.py <input_file.c> <output_file>

Le fichier "compilerC3.py", effectue toutes les étapes de compilation sans utiliser de compilateur externe. En revanche celui-ci ne goncionne pas. 

#### Sortie :
Il y a de la gestion des erreurs afin d'essayer de déboguer, en revanche je n'ai pas réussi. 
```sh 
$ python3 compilerC3.py helloworld.c output
$ Preprocessed Code:
 #line 2 "headers/stdio.h"
typedef struct _IO_FILE FILE;
extern FILE* stdin;
extern FILE* stdout;
extern FILE* stderr;
int printf(const char* format, ...);
#line 3
int main() {
    printf("Hello, world!\n");
    return 0;
}

Tokens:
 [('ID', 'typedef'), ('ID', 'struct'), ('ID', '_IO_FILE'), ('ID', 'FILE'), ('SEMI', ';'), ('ID', 'extern'), ('ID', 'FILE'), ('OP', '*'), ('ID', 'stdin'), ('SEMI', ';'), ('ID', 'extern'), ('ID', 'FILE'), ('OP', '*'), ('ID', 'stdout'), ('SEMI', ';'), ('ID', 'extern'), ('ID', 'FILE'), ('OP', '*'), ('ID', 'stderr'), ('SEMI', ';'), ('KEYWORD', 'int'), ('ID', 'printf'), ('LPAREN', '('), ('ID', 'const'), ('KEYWORD', 'char'), ('OP', '*'), ('ID', 'format'), ('COMMA', ','), ('DOT', '.'), ('DOT', '.'), ('DOT', '.'), ('RPAREN', ')'), ('SEMI', ';'), ('KEYWORD', 'int'), ('ID', 'main'), ('LPAREN', '('), ('RPAREN', ')'), ('LBRACE', '{'), ('ID', 'printf'), ('LPAREN', '('), ('STRING', '"Hello, world!\\n"'), ('RPAREN', ')'), ('SEMI', ';'), ('KEYWORD', 'return'), ('NUMBER', '0'), ('SEMI', ';'), ('RBRACE', '}'), ('EOF', 'EOF')]
An error occurred during compilation: object of type 'int' has no len()
```

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

