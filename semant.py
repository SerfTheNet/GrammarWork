# -*- coding: utf-8 -*-

## также необходима проверка длины строковой константы < 80

def semant(tree, tokens):
    id_type_dict = {}
    recursive_search(tree, id_type_dict)
    
    for token in tokens:
                if token.l_type == 'const':
                    id_type_dict[token.word] = token.inprog_type
    
    return id_type_dict
    
def recursive_search(tree, id_type_dict):
    for node in tree[1]:
        if node[0] == 'DIM':
            inprog_type = 'str' if node[1][3] == 'string' else 'int'
            id_type_dict[node[1][1]] = inprog_type
        elif isinstance(node, str):
            continue
        else:
            recursive_search(node, id_type_dict)
        