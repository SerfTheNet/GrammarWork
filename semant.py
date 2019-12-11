# -*- coding: utf-8 -*-
import re

## также необходима проверка длины строковой константы < 80

def semant(tree, tokens):
    id_type_dict = {}
    recursive_search(tree, id_type_dict)
    for token in tokens:
                if token.l_type == 'const':
                    
                    id_type_dict[token.word] = token.inprog_type
                    
                    if '"' in token.word and len(re.sub('"', '', token.word)) >=80:
                       raise SystemExit('Длина строки превышена. Максимальное количество элементов - 80. ' , token.word)
    
    return id_type_dict


def EXPRESSION(node, id_type_dict):
    signs = ['+','-','*','/']
    if node[0] not in id_type_dict.keys():
        raise SystemExit('Переменная не объявлена ',node[0])
    
    str_node=node.copy()[2:]
    
    if len(str_node) == 1:
        
        if '|' not in str_node[0] and str_node[0] not in id_type_dict.keys():
            raise SystemExit('Переменная не объявлена ',str_node[0])
            
        check_type=id_type_dict[str_node[0]] if str_node[0] in id_type_dict.keys() else str_node[0]
        
        if id_type_dict[node[0]] not in check_type and id_type_dict[node[0]] == 'int':
            raise SystemExit('К целочисленной переменной невозможно присвоить строковую переменную')
            
        elif id_type_dict[node[0]] not in check_type and id_type_dict[node[0]] == 'str':
            raise SystemExit('К строковой переменной невозможно присвоить целочисленную переменную')
            
        
    elif len(str_node) > 1:
        
        del_znak=[i for i in str_node if i not in signs]
        for i in del_znak:
           if '|' not in i and i not in id_type_dict.keys():
            raise SystemExit('Переменная не объявлена ',i)
            
        new_type_check=[id_type_dict[i] if i in id_type_dict.keys() else i for i in str_node]
        
        if id_type_dict[node[0]] == 'str':
            check_int=[i for i in new_type_check if 'int' in i]
            if check_int:
                raise SystemExit('К строковой переменной невозможно присвоить целочисленную переменную')
        
        if id_type_dict[node[0]] == 'int':
            check_int=[i for i in new_type_check if 'str' in i]
            if check_int:
                raise SystemExit('К целочисленной переменной невозможно присвоить строковую переменную')


def CONDITION(node, id_type_dict):
    
    variables=[node[0],node[2]]
    for i in variables:
        if '|' not in i and i not in id_type_dict.keys():
            raise SystemExit('Переменная не объявлена ',i)
    
    variables_type=[id_type_dict[i] if i in id_type_dict.keys() else i for i in variables] 
    if variables_type[0] not in variables_type[1]:
        raise SystemExit('Конфликт типов при сравнении')

    
    
    
def recursive_search(tree, id_type_dict):
    
    for node in tree[1]:
        
        if node[0] == 'DIM':
            
            inprog_type = 'str' if node[1][3] == 'string' else 'int'
            id_type_dict[node[1][1]] = inprog_type
        
        if node[0] == 'EXPRESSION':
            
            EXPRESSION(node[1], id_type_dict)
            
        if node[0] == 'CONDITION':
            
            CONDITION(node[1], id_type_dict)
                    
        elif isinstance(node, str):
            continue
        else:
            recursive_search(node, id_type_dict)
            


            
            
            
        