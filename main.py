from analyzer.lexical_analyzer import LexicalAnalyzer

SERVICE_WORDS_FILE_PATH = 'input/service_words.txt'
PROGRAM_FILE_PATH = 'input/program.txt'


def load_service_words(file_path: str) -> dict:
    result = {}
    with open(file_path, 'r') as file:
        for line in file:
            splitted = line.split('\t')
            result[splitted[0]] = int(splitted[1].replace('\n', ''))
    return result


def load_program(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()


if __name__ == "__main__":
    service_words = load_service_words(SERVICE_WORDS_FILE_PATH)
    program = load_program(PROGRAM_FILE_PATH)

    print(service_words)
    print(program)

    analyzer = LexicalAnalyzer(service_words)

    for s in program:
        analyzer.input(s)

    print('lexems: ', analyzer.lexems)
    print('indents: ', analyzer.idents)
    print('consts: ', analyzer.consts)