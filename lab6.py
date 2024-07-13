import sys


def read_file(file_path):

    with open(file_path, 'r') as file:
        return file.read()


def get_file_extension(file_path):

    return file_path.split('.')[-1].lower()


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: lab6.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    input_format = get_file_extension(input_path)
    output_format = get_file_extension(output_path)

    input_data = read_file(input_path)