from analyzer.result_type import ResultType


class ConstState:

    def __init__(self, remainder: str = ''):
        self.remainder = remainder

    def input(self, la, symb: str) -> ResultType:
        if not symb.isdigit():
            from analyzer.states.wait import WaitState
            la.state = WaitState(symb)
            return ResultType.const
        la.word += symb
        return ResultType.ignore
