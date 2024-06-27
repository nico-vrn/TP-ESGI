import os
import sys
import subprocess

class SimpleCCompiler:
    def __init__(self):
        pass

    def preprocess(self, source_file):
        preprocessed_file = "preprocessed.c"
        with open(source_file, 'r') as f:
            code = f.read()
        
        # Ajouter l'inclusion de stdio.h si elle n'est pas présente
        if '#include <stdio.h>' not in code:
            code = '#include <stdio.h>\n' + code

        with open(preprocessed_file, 'w') as f:
            f.write(code)
        
        return preprocessed_file

    def compile(self, source_file):
        preprocessed_file = self.preprocess(source_file)
        
        # Compiler le fichier source pré-traité en fichier objet
        obj_file = "output.o"
        subprocess.run(["gcc", "-c", preprocessed_file, "-o", obj_file], check=True)
        
        # Créer un exécutable statique
        subprocess.run(["gcc", "-static", "-o", "output", obj_file], check=True)
        
        print(f"Compilation réussie. Exécutable créé: output")
        
        # Nettoyer le fichier pré-traité
        os.remove(preprocessed_file)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python compiler_C.py <fichier.c>")
        sys.exit(1)

    source_file = sys.argv[1]
    compiler = SimpleCCompiler()
    compiler.compile(source_file)
