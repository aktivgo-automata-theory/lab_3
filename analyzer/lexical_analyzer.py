from analyzer.result_type import ResultType

from analyzer.states.wait import WaitState


class LexicalAnalyzer:
    def __init__(self, service_words: dict):
        self.service_words = service_words

        self.state = WaitState()
        self.word = ''

        self.lexems = []
        self.idents = []
        self.consts = []

    def input(self, symb: str):
        res = self.state.input(self, symb)
        if res == ResultType.ignore:
            return
        match res:
            case ResultType.ident:
                if self.word not in self.idents:
                    self.idents.append(self.word)
                self.lexems.append((200, self.idents.index(self.word)))
            case ResultType.service_or_ident:
                if self.word in self.service_words:
                    self.lexems.append((0, self.service_words[self.word]))
                else:
                    if self.word not in self.idents:
                        self.idents.append(self.word)
                    self.lexems.append((200, self.idents.index(self.word)))
            case ResultType.const:
                if self.word not in self.consts:
                    self.consts.append(self.word)
                self.lexems.append((300, self.consts.index(self.word)))
        if self.state.remainder != '' and not self.state.remainder.isspace():
            rem = self.state.remainder
            self.state.remainder = ''
            self.input(rem)
