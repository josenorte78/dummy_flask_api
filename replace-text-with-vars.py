import sys

def read_text(file_name):
    txt = ""
    with open(file_name) as f:
        txt = f.readlines()
    return txt

def read_dictionary(file_name):
    wholeText = read_text(file_name)
    params = dict()

    for txt in wholeText:
        if ':' not in txt:
            continue

        values = txt.split(':', maxsplit=1)

        params["<" + values[0].strip() + ">"] =  values[1].strip().removesuffix("\n")
        
    return params

def replace_text(whole_text, params):
    text = ''.join(whole_text)

    for key in params:
        text = text.replace(key, params[key])
    return text

def write_to_file(text, file_name):
    with open(file_name, 'w') as f:
        f.write(text)

if (__name__ == "__main__"):
    
    original_text = read_text(sys.argv[1])

    variables = read_dictionary(sys.argv[2])
    
    new_text = replace_text(original_text, variables)

    print(new_text)

    write_to_file(new_text, sys.argv[3])
    print('-------------')
    print('---> New file created!')
    print('-------------')