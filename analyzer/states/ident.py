from analyzer.lexical_analyzer import LexicalAnalyzer
from analyzer.result_type import ResultType


class IdentState:
    def __init__(self, remainder: str = ''):
        self.remainder = remainder

    def input(self, la: LexicalAnalyzer, symb: str) -> ResultType:
        if not symb.isalpha() and not symb.isdigit():
            from analyzer.states.wait import WaitState
            la.state = WaitState(symb)
            return ResultType.ident
        la.word += symb
        return ResultType.ignore
