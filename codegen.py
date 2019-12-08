# -*- coding: utf-8 -*-
from os import system

def compilate(compiler_path, tree):
    with open('temp.c', 'w') as f:
        f.write(intro(tree))
    system(f"{compiler_path} temp.c")
    
    

def intro(tree):
    return f"""
#include "stdio.h"
    
void main() {{
{codegen_recursive(tree)}
return 0;
}}
"""

def codegen_recursive(tree):
    codestr = ''
    for node in tree[1]:
        if isinstance(node, str):
            continue
        elif node[0] not in ['DIM', 'IO', 'IF', 'LOOP', 'EXPRESSION']:
            codestr += codegen_recursive(node)
        else:
            if node[0] == 'DIM':
                codestr += dim(node)
            if node[0] == 'IO':
                codestr += io(node)
            if node[0] == 'IF':
                codestr += ifs(node)
            if node[0] == 'LOOP':
                codestr += loop(node)
            if node[0] == 'EXPRESSION':
                codestr += expression(node)
                
    return codestr

def dim(dim_node):
    ids = dim_node[1][1]
    if dim_node[1][3] == 'string':
        return f'char {ids}[80]; \n'''
    elif dim_node[1][3] == 'int':
        return f'int {ids} = 0; \n'
    
    
def io(io_node):
    # если вывод
    if len(io_node[1]) == 2:
        del_type(io_node, 1)
        data = io_node[1][1]
        modyfier = '%s' if id_type_dict[data] == 'str' else '%d'
        return f'printf("{modyfier}", {data}); \n'
    # иначе
    else:
        ids = io_node[1][0]
        modyfier = '%s' if id_type_dict[ids] == 'str' else '%d'
        return f'scanf("{modyfier}", &{ids}); \n'

def condition(cond_node):
    # убираем тип
    del_type(cond_node, -1)
    return ' '.join(cond_node[1])

def ifs(if_node):
    if len(if_node[1]) == 8:
        return f'if ({condition(if_node[1][1])}) {{\n{codegen_recursive(if_node[1][3])} }} \nelse \n{{ \n{codegen_recursive(if_node[1][6])}}}'
    else:
        return f'if ({condition(if_node[1][1])}) {{\n{codegen_recursive(if_node[1][3])}}}'

def loop(while_node):
    return f'while ({condition(while_node[1][1])}) {{\n{codegen_recursive(while_node[1][3])}}}'

def expression(expr_node):
    del_type(expr_node, 2)
    del_type(expr_node, 4)
    return f'{" ".join(expr_node[1])}; \n'

def del_type(node, typed_const_position):
    # убираем тип на позиции 
    node[1][typed_const_position] = node[1][typed_const_position].split('|')[0]

#print(intro(stree))
