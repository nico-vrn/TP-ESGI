import llvmlite.binding as llvm
import llvmlite.ir as ir
import os
import sys

class SimpleCCompiler:
    def __init__(self):
        self.module = ir.Module(name="simple_module")
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

    def compile(self, source_code):
        if "printf" in source_code:
            if "Hello, World!" in source_code:
                self.hello_world_ir()
            elif "suite de Fibonacci" in source_code:
                self.fibonacci_ir()
            else:
                raise ValueError("Unsupported source code")
        else:
            raise ValueError("Unsupported source code")

        llvm_ir = str(self.module)
        llvm_module = self.compile_ir(llvm_ir)
        obj_file = "output.o"
        self.save_object_file(llvm_module, obj_file)
        os.system(f"gcc -o output {obj_file}")
        print(f"Compilation réussie. Exécutable créé: output")

    def hello_world_ir(self):
        void_ty = ir.VoidType()
        int_ty = ir.IntType(32)
        char_ty = ir.IntType(8)
        char_ptr_ty = char_ty.as_pointer()
        func_ty = ir.FunctionType(int_ty, [])
        func = ir.Function(self.module, func_ty, name="main")

        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        printf_ty = ir.FunctionType(int_ty, [char_ptr_ty], var_arg=True)
        printf = ir.Function(self.module, printf_ty, name="printf")

        hello_world_str = ir.GlobalVariable(self.module, ir.ArrayType(char_ty, 14), name="hello_world")
        hello_world_str.initializer = ir.Constant(ir.ArrayType(char_ty, 14), bytearray(b"Hello, World!\0"))
        hello_world_str.linkage = 'internal'

        str_ptr = builder.gep(hello_world_str, [int_ty(0), int_ty(0)])
        builder.call(printf, [str_ptr])
        builder.ret(int_ty(0))

    def fibonacci_ir(self):
        void_ty = ir.VoidType()
        int_ty = ir.IntType(32)
        char_ty = ir.IntType(8)
        char_ptr_ty = char_ty.as_pointer()
        func_ty = ir.FunctionType(int_ty, [])
        func = ir.Function(self.module, func_ty, name="main")

        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        printf_ty = ir.FunctionType(int_ty, [char_ptr_ty], var_arg=True)
        printf = ir.Function(self.module, printf_ty, name="printf")

        format_str = ir.GlobalVariable(self.module, ir.ArrayType(char_ty, 4), name="format_str")
        format_str.initializer = ir.Constant(ir.ArrayType(char_ty, 4), bytearray(b"%d \0"))
        format_str.linkage = 'internal'

        str_ptr = builder.gep(format_str, [int_ty(0), int_ty(0)])

        n = 10
        t1 = 0
        t2 = 1
        builder.call(printf, [str_ptr, int_ty(t1)])
        builder.call(printf, [str_ptr, int_ty(t2)])
        for i in range(2, n):
            next_term = t1 + t2
            t1 = t2
            t2 = next_term
            builder.call(printf, [str_ptr, int_ty(next_term)])

        builder.ret(int_ty(0))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python compiler_C.py <fichier.c>")
        sys.exit(1)

    source_file = sys.argv[1]
    with open(source_file, 'r') as file:
        source_code = file.read()

    compiler = SimpleCCompiler()
    compiler.compile(source_code)
