# -*- coding: utf-8 -*-
import re

## также необходима проверка длины строковой константы < 80

def semant(tree, tokens):
    id_type_dict = {}
    recursive_search(tree, id_type_dict)
    check_type(tree, id_type_dict)
    for token in tokens:
        
                if token.l_type == 'const':
                    if ('"' in token.word and len(re.sub('"', '', token.word))) <=80 or '"' not in token.word:
                       
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
            

def check_type(tree, id_type_dict):
    
    for node in tree[1]:
        if node[0] == 'EXPRESSION':
            try:
                id_type_dict[node[1][0]]
                str_node=node[1].copy()
                del str_node[0]
                del str_node[0]
                if len(str_node) == 1:
                    if id_type_dict[node[1][0]] in str_node[0]:
                        pass
                    elif id_type_dict[node[1][0]] == id_type_dict[str_node[0]]:
                        pass
                    else:
                        try:
                            raise SystemExit(id_type_dict[node[1][0]],' не может быть ', str_node[0].split('|')[1])
                        except:
                            raise SystemExit(id_type_dict[node[1][0]],' не может быть ', id_type_dict[str_node[0]])
                else:
                    new_type_check=[]
                    for i in str_node:
                        
                        try:
                            new_type_check.append(id_type_dict[i])
                        except:
                            new_type_check.append(i)
                                 
                    if id_type_dict[node[1][0]] == 'str':
                        id_type=[i for i in new_type_check if 'int' in i]
                        if id_type:
                            raise SystemExit('Нельзя int использовать с str')
                        elif '*' in new_type_check or '-' in new_type_check or '/' in new_type_check:
                            raise SystemExit('Можно сложить только строки')
                    elif id_type_dict[node[1][0]] == 'int':
                        id_type=[i for i in new_type_check if 'str' in i]
                        if id_type:
                            raise SystemExit('Нельзя int использовать с str')
    
                            
     
                        
                        
                
                
            except Exception as exc:
                raise SystemExit('Переменная не объявлена ',exc)
            
            
            
        elif isinstance(node, str):
            continue
        else:
            check_type(node, id_type_dict)
            
            
            
        