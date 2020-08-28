from .antlr_generated import CsvParser, CsvListener

class CsvToPythonListener(CsvListener):
    def __init__(self):
        super().__init__()
        self.output = None

    def enterCsv(self, ctx: CsvParser.CsvContext):
        self.output = []

    def enterLine(self, ctx: CsvParser.LineContext):
        newline = list()
        self.output.append(newline)

    def enterField(self, ctx: CsvParser.FieldContext):
        if ctx.INTEGER():
            entry = int(ctx.INTEGER().getText())
        elif ctx.FLOAT():
            entry = float(ctx.FLOAT().getText())
        elif ctx.STRING():
            entry = ctx.STRING().getText()[1:-1]
        else:
            raise TypeError('Could not determine type for field.')
        self.output[-1].append(entry)



    
