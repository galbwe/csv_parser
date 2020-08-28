# Generated from Csv.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CsvParser import CsvParser
else:
    from CsvParser import CsvParser

# This class defines a complete listener for a parse tree produced by CsvParser.
class CsvListener(ParseTreeListener):

    # Enter a parse tree produced by CsvParser#csv.
    def enterCsv(self, ctx:CsvParser.CsvContext):
        pass

    # Exit a parse tree produced by CsvParser#csv.
    def exitCsv(self, ctx:CsvParser.CsvContext):
        pass


    # Enter a parse tree produced by CsvParser#line.
    def enterLine(self, ctx:CsvParser.LineContext):
        pass

    # Exit a parse tree produced by CsvParser#line.
    def exitLine(self, ctx:CsvParser.LineContext):
        pass


    # Enter a parse tree produced by CsvParser#cell.
    def enterCell(self, ctx:CsvParser.CellContext):
        pass

    # Exit a parse tree produced by CsvParser#cell.
    def exitCell(self, ctx:CsvParser.CellContext):
        pass


    # Enter a parse tree produced by CsvParser#field.
    def enterField(self, ctx:CsvParser.FieldContext):
        pass

    # Exit a parse tree produced by CsvParser#field.
    def exitField(self, ctx:CsvParser.FieldContext):
        pass



del CsvParser