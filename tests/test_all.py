import os
import json



def test_all():

    temp_file = 'temp_file.txt'
    os.system(f'python -m admiral test -s str -i 1 2 -f 1.02 > {temp_file}')

    with open(temp_file, 'r', encoding='utf8') as f:
        result = json.load(f)
    os.remove(temp_file)
    
    assert result == {
        'float': [1.02], 
        'int': [1, 2], 
        'string': ['str']
    }