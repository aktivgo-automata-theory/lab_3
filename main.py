LEXEMS_FILE_PATH = 'input/lexem.txt'
PROGRAM_FILE_PATH = 'input/program.txt'


def load_lexems(file_path: str) -> dict:
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
    lexems = load_lexems(LEXEMS_FILE_PATH)
    print(lexems)
    program = load_program(PROGRAM_FILE_PATH)
    print(program)

