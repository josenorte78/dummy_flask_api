import sys
import json

def read_text(file_name):
    txt = ""
    with open(file_name) as f:
        txt = f.read()
    return txt

def parse_version(text):
    version = ""

    json_obj = json.loads(text)

    if 'Major' in json_obj:
        version += f'{json_obj["Major"]}'
    
    if 'Minor' in json_obj:
        version += f'.{json_obj["Minor"]}'
        
    if 'Patch' in json_obj:
        version += f'.{json_obj["Patch"]}'
        
    if 'Build' in json_obj:
        version += f'.{json_obj["Build"]}'
        
    if 'Prerelease' in json_obj:
        version += f'.{json_obj["Prerelease"]}'

    return version

def replace_version_in_text(text, version):
    return text.replace('<version>', version)

def write_to_file(text, file_name):
    with open(file_name, 'w') as f:
        f.write(text)

if (__name__ == "__main__"):
    
    raw_ymal = read_text(sys.argv[1])

    raw_json_text = read_text(sys.argv[2])
    
    version = parse_version(raw_json_text)

    populated_text = replace_version_in_text(raw_ymal, version)

    print(populated_text)

    write_to_file(populated_text, sys.argv[3])

    print('-------------')
    print('---> New file is created with version!!!')
    print('-------------')