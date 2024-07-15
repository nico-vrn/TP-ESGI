import os
import sys
import io
import re
import subprocess
import llvmlite.binding as llvm
import llvmlite.ir as ir
from pcpp import Preprocessor as PCPPPreprocessor
from pycparser import c_parser, c_ast

class SimpleCCompiler:
    def __init__(self):
        self.module = ir.Module(name="simple_module")
        self.engine = self.create_execution_engine()
        self.printf = None
        self.string_count = 0

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
        pp = PCPPPreprocessor()
        pp.add_path(os.path.dirname(source_file))
        pp.add_path("headers") 
        
        with open(source_file, 'r') as f:
            content = f.read()
        
        output = io.StringIO()
        pp.parse(content)
        pp.write(output)
        preprocessed_code = output.getvalue()

        # Inclure les définitions minimales pour pycparser
        fake_libc_definitions = '''
        typedef int va_list;
        typedef int FILE;
        typedef int size_t;
        typedef int fpos_t;
        #define NULL ((void*)0)
        int printf(const char *, ...);
        int fprintf(FILE *, const char *, ...);
        '''

        return fake_libc_definitions + preprocessed_code

    def clean_preprocessed_code(self, preprocessed_code):
        # Supprimer les directives de préprocesseur
        cleaned_code = re.sub(r'#.*', '', preprocessed_code)
        # Supprimer les commentaires
        cleaned_code = re.sub(r'/\*.*?\*/', '', cleaned_code, flags=re.DOTALL)
        cleaned_code = re.sub(r'//.*', '', cleaned_code)
        # Supprimer les lignes vides
        cleaned_code = os.linesep.join([s for s in cleaned_code.splitlines() if s.strip()])
        return cleaned_code

    def generate_llvm_ir(self, preprocessed_code):
        parser = c_parser.CParser()
        ast = parser.parse(preprocessed_code)

        self.printf = ir.Function(self.module, ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True), name="printf")

        func_ty = ir.FunctionType(ir.IntType(32), [])
        func = ir.Function(self.module, func_ty, name="main")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        self.visit(ast, builder)

        builder.ret(ir.IntType(32)(0))
        return str(self.module)

    def visit(self, node, builder):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node, builder)

    def generic_visit(self, node, builder):
        for _, child in node.children():
            self.visit(child, builder)

    def visit_Constant(self, node, builder):
        if node.type == 'string':
            c_str_val = bytearray(node.value[1:-1] + '\0', 'utf8')
            c_str = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(c_str_val)), name=f"str_{self.string_count}")
            self.string_count += 1
            c_str.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(c_str_val)), c_str_val)
            c_str.linkage = 'internal'
            ptr = builder.gep(c_str, [ir.IntType(32)(0), ir.IntType(32)(0)])
            return ptr

    def visit_FuncCall(self, node, builder):
        if node.name.name == 'printf':
            arg = self.visit(node.args.exprs[0], builder)
            builder.call(self.printf, [arg])

    def compile(self, source_file):
        preprocessed_code = self.preprocess(source_file)

        # Diagnostic: Sauvegarder le code préprocessé pour inspection
        #with open("preprocessed_debug.c", "w") as f:
         #   f.write(preprocessed_code)

        #print("Preprocessed Code:\n", preprocessed_code)  # Ajouter pour diagnostiquer

        cleaned_code = self.clean_preprocessed_code(preprocessed_code)

        #print("Cleaned Preprocessed Code:\n", cleaned_code)  # Ajouter pour diagnostiquer

        llvm_ir = self.generate_llvm_ir(cleaned_code)

        llvm_module = self.compile_ir(llvm_ir)
        obj_file = "output.o"
        self.save_object_file(llvm_module, obj_file)

        subprocess.run(["gcc", "-static", "-o", "output", obj_file], check=True)
        
        print(f"Compilation réussie. Exécutable créé: output")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python compilerC.py <fichier.c>")
        sys.exit(1)

    source_file = sys.argv[1]
    compiler = SimpleCCompiler()
    compiler.compile(source_file)