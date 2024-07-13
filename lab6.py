import sys
import json
import yaml
import xmltodict


def read_file(file_path):

    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, data):

    with open(file_path, 'w') as file:
        file.write(data)

def convert_data(input_data, input_format, output_format):

    if input_format == 'json':
        data = json.loads(input_data)
    elif input_format in ['yml', 'yaml']:
        data = yaml.safe_load(input_data)
    elif input_format == 'xml':
        data = xmltodict.parse(input_data)
    else:
        raise ValueError(f"Unsupported input format: {input_format}")
    
    if output_format == 'json':
        return json.dumps(data, indent=4)
    elif output_format in ['yml', 'yaml']:
        return yaml.dump(data, sort_keys=False)
    elif output_format == 'xml':
        return xmltodict.unparse(data, pretty=True)
    else:
        raise ValueError(f"Unsupported output format: {output_format}")


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
    output_data = convert_data(input_data, input_format, output_format)
    write_file(output_path, output_data)
    print(f"Converted {input_path} ({input_format}) to {output_path} ({output_format}) successfully.")