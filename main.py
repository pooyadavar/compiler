from antlr4 import FileStream, CommonTokenStream
from obfuscator.parser.ObfuMiniCLexer import ObfuMiniCLexer
from obfuscator.parser.ObfuMiniCParser import ObfuMiniCParser

def main():
    input_stream = FileStream("input/input.mc")
    lexer = ObfuMiniCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ObfuMiniCParser(stream)

    tree = parser.compilationUnit()
    print(tree.toStringTree(recog=parser))  

if __name__ == '__main__':
    main()
