# -*- coding: utf-8 -*-
def intro(tree):
    return f"""
    #include "stdio.h"
    void main() {
    {codegen_recursive(tree)}
    }
"""

def codegen_recursive(tree):
    codestr = ''
    for node in tree[1]:
        if isinstance(node, str):
            continue
        elif node[0] not in ['DIM', 'IO']:
            codestr += codegen_recursive(node)
        else:
            if node[0] == 'DIM':
                codestr += dim(node)
            if node[0] == 'IO':
                codestr += io(node)
    return codestr

def dim(dim_node):
    types = 'char[80]' if dim_node[1][3] == 'string' else 'int'
    ids = dim_node[1][1]
    return f"""{types} {ids}; \n"""
def io(io_node):
    # если вывод
    if len(io_node[1]) == 2:
        data = io_node[1][1]
        return f'printf("%d?", {data}); \n'
    # иначе
    else:
        ids = io_node[1][0]
        return f'scanf("%d?", &{ids}); \n'



print(str(intro(stree)))