from antlr4 import FileStream, CommonTokenStream
from obfuscator.parser.ObfuMiniCLexer import ObfuMiniCLexer
from obfuscator.parser.ObfuMiniCParser import ObfuMiniCParser
from obfuscator.ast_builder import ASTBuilder
from obfuscator.obfuscator import NameObfuscator 
from obfuscator.deadcode import DeadCodeInserter
from obfuscator.expression_transform import ExpressionTransformer


def main():
    input_stream = FileStream("input/input.mc") 
    lexer = ObfuMiniCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ObfuMiniCParser(stream)

    tree = parser.compilationUnit()
    ast = ASTBuilder().visit(tree)

    #change name of variables
    obfuscator = NameObfuscator()
    obfuscator.obfuscate(ast)

    #add dead code 
    dead_inserter = DeadCodeInserter()
    dead_inserter.insert(ast)

    transformer = ExpressionTransformer()
    transformer.transform(ast)

    print(ast)

if __name__ == '__main__':
    main()