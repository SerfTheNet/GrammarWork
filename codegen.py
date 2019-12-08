# -*- coding: utf-8 -*-
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
        data = io_node[1][1]
        return f'printf("%d?", {data}); \n'
    # иначе
    else:
        ids = io_node[1][0]
        return f'scanf("%d?", &{ids}); \n'

def condition(cond_node):
    # убираем тип
    cond_node[1][-1] = cond_node[1][-1].split('|')[0]
    return ' '.join(cond_node[1])

def ifs(if_node):
    if len(if_node[1]) == 8:
        return f'if ({condition(if_node[1][1])}) {{\n{codegen_recursive(if_node[1][3])} }} \nelse \n{{ \n{codegen_recursive(if_node[1][6])}}}'
    else:
        return f'if ({condition(if_node[1][1])}) {{\n{codegen_recursive(if_node[1][3])}}}'

def loop(while_node):
    return f'while ({condition(while_node[1][1])}) {{\n{codegen_recursive(while_node[1][3])}}}'

def expression(expr_node):
    return f'{" ".join(expr_node[1])}; \n'

print(intro(stree))
