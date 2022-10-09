from analyzer.result_type import ResultType


class WordState:
    def __init__(self, remainder: str = ''):
        self.remainder = remainder

    def input(self, la, symb: str) -> ResultType:
        if not symb.isalpha() and not symb.isdigit():
            from analyzer.states.wait import WaitState
            la.state = WaitState()
            return ResultType.service_or_ident
        la.word += symb
        if symb.isdigit():
            from analyzer.states.ident import IdentState
            la.state = IdentState()
        return ResultType.ignore
