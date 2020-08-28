import sys
from enum import Enum, unique
from typing import List, Optional

from antlr4 import *
from .antlr_generated import CsvLexer, CsvParser

from .listener import CsvToPythonListener 


def parse(csv_data: str) -> List:
    stream = InputStream(csv_data)
    lexer = CsvLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = CsvParser(stream)
    tree = parser.csv()

    csv_to_python_listener = CsvToPythonListener()
    walker = ParseTreeWalker()
    walker.walk(csv_to_python_listener, tree)
    return csv_to_python_listener.output
