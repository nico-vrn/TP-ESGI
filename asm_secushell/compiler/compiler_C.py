import llvmlite.binding as llvm
import os
import sys
import subprocess

class SimpleCCompiler:
    def __init__(self):
        self.module = None
        self.engine = self.create_execution_engine()

    def create_execution_engine(self):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        target = llvm.Target.from_default_triple()
        target_machine = target.create_target_machine()
        backing_mod = llvm.parse_assembly("")
        engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
        return engine

    def compile_ir(self, llvm_ir):
        mod = llvm.parse_assembly(llvm_ir)
        mod.verify()
        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()
        return mod

    def save_object_file(self, llvm_module, output_file):
        target = llvm.Target.from_default_triple()
        target_machine = target.create_target_machine()
        with open(output_file, 'wb') as f:
            f.write(target_machine.emit_object(llvm_module))

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

    def compile_to_llvm_ir(self, source_file):
        llvm_ir_file = "temp.ll"
        # Utiliser clang pour générer le code LLVM IR à partir du fichier source C
        subprocess.run(["clang", "-emit-llvm", "-S", source_file, "-o", llvm_ir_file], check=True)
        with open(llvm_ir_file, 'r') as f:
            llvm_ir = f.read()
        os.remove(llvm_ir_file)
        return llvm_ir

    def compile(self, source_file):
        preprocessed_file = self.preprocess(source_file)
        llvm_ir = self.compile_to_llvm_ir(preprocessed_file)
        
        llvm_module = self.compile_ir(llvm_ir)
        obj_file = "output.o"
        self.save_object_file(llvm_module, obj_file)

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
