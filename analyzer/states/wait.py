from analyzer.result_type import ResultType


class WaitState:

    def __init__(self, remainder: str = ''):
        self.remainder = remainder

    def input(self, la, symb: str) -> ResultType:
        if symb.isspace():
            return ResultType.ignore
        la.word = ''
        la.word += symb
        if symb.isalpha() or symb.isdigit():
            if symb.isdigit():
                from analyzer.states.const import ConstState
                la.state = ConstState()
            else:
                from analyzer.states.word import WordState
                la.state = WordState()
            return ResultType.ignore
        return ResultType.service_or_ident
