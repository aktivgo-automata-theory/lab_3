class AnalyzeResult:

    def __init(self):
        self.lexems = {}
        self.idents = []
        self.consts = []

    def add_lexem(self, type: int, code: int):
        self.lexems[type] = code

    def add_ident(self, ident: str):
        self.idents.append(ident)

    def add_const(self, const: str):
        self.consts.append(const)