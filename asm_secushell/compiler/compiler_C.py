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

    def compile(self, source_file):
        obj_file = "output.o"
        subprocess.run(["gcc", "-c", source_file, "-o", obj_file], check=True)
        os.system(f"gcc -o output {obj_file}")
        print(f"Compilation réussie. Exécutable créé: output")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python compiler_C.py <fichier.c>")
        sys.exit(1)

    source_file = sys.argv[1]
    compiler = SimpleCCompiler()
    compiler.compile(source_file)
