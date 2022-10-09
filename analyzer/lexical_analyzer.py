from analyzer.analyze_result import AnalyzeResult


class LexicalAnalyzer:

    def __init__(self, service_words: dict):
        self.service_words = service_words
        self.ignore_symbols = ['\n', '\r', '\t']
        self.switch = False

    def __is_ignore_symb(self, symb: str) -> bool:
        return symb.isspace() or symb in self.ignore_symbols

    def __is_service_words(self, string: str) -> bool:
        return string in self.service_words

    def analyze(self, program: str) -> AnalyzeResult:
        result = AnalyzeResult()

        word = ''
        for i in range(len(program)):
            if self.__is_ignore_symb(program[i]):
                continue

            if self.switch:
                print()
                word = ''

            word += program[i]

            if self.__is_service_words(program[i]):
                result.add_lexem(0, self.service_words[word])

        return result
