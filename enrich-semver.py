import sys
import json

def read_text(file_name):
    txt = ""
    with open(file_name) as f:
        txt = f.read()
    return txt

def read_text_line_by_line(file_name):
    txt = ""
    with open(file_name) as f:
        txt = f.readlines()
    return txt

def read_dictionary(file_name):
    wholeText = read_text_line_by_line(file_name)
    params = dict()

    for txt in wholeText:
        if ':' not in txt:
            continue
        values = txt.split(':', maxsplit=1)

        params[values[0].strip()] =  values[1].strip().removesuffix("\n")
        
    return params

def parse_to_json(text):
    return json.loads(text)   

def enrich_json(json, variables):
    key = "Prerelease"
    
    if key in variables:
        if key in json:
            json[key] += variables[key]
        else:
            json[key] = variables[key]
    
    return json

def write_to_file(text, file_name):
    with open(file_name, 'w') as f:
        f.write(text)

if (__name__ == "__main__"):
    
    
    original_text = read_text(sys.argv[1])

    variables = read_dictionary(sys.argv[2])

    parsed_json = parse_to_json(original_text)

    enriched_json = enrich_json(parsed_json, variables)

    print(enriched_json)

    write_to_file(json.dumps(enriched_json), sys.argv[3])
    
    print('-------------')
    print('---> New file created!')
    print('-------------')