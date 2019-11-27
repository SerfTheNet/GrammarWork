# -*- coding: utf-8 -*-

import re

lex_regulars = [
        (r'(^dim$)|(^program$)|(^as$)|(^if$)|(^then$)|(^else$)|(^input$)|(^output$)|(^while$)|(^do$)|(^end$)|(^atoi$)|(^itoa$)|(^end.$)', 'keyword'),
        (r'(^=$)|(^-$)|(^\+$)|(^/$)|(^\*$)|(^%$)|(^//$)', 'operator'),
        (r'(^==$)|(^>$)|(^<$)|(^>=$)|(^<=$)|(^!=$)', 'logic'),
        (r'(^;$)', 'block delimeter'),
        (r'(^string$)|(^int$)', 'type'),
        (r'(^"[^"]*"$)|(^-?\d+$)', 'const'),
        (r'^[a-zA-Z_@#!][a-zA-Z_\d]*$', 'id'),     
        ]

def get_tokens(filename):
    with open(filename, 'r') as file:
        progstring  = file.read()
    # сплит со строками
    tokens = []
    token = ''
    quotes_flag = False
    for i in progstring + ' ':
        if ((i not in (' ', '\n', '\t')) or quotes_flag):
            token += i
        else:
            if token != '':
                tokens.append(token)
            token = ''
        if i == '"':
            quotes_flag = not quotes_flag
    return tokens
def lexify_tokens(tokens, lex_regulars):
    lexical_table = []
    # В этом цикле лексемы берутся из списка lex_arr и последовательно...
    # ...проверяются по списку регулярных выражений
    for i in tokens:
        def_f = True
        for j in lex_regulars:
            if re.match(j[0], i):
                lexical_table.append([i, j[1]])
                #print([i, j[1]])
                def_f = False
                break
        if def_f:
            raise SystemExit(f'Undefined lexeme "{i}"')
    # print lexical_table
    return lexical_table

class token:
    def __init__(self, word, l_type):
        self.word = word
        self.l_type = l_type
    def __repr__(self):
        return f'{self.word}({self.l_type})'
    def __str__(self):
        if self.l_type in ['id', 'const']:
            return self.l_type
        else:
            return self.word
    def __iter__(self):
        return([self.word, self.l_type])
    def __eq__(self, string):
        if self.l_type in ['id', 'type', 'operator', 'logic']:
            return self.l_type == string
        else:
            return self.word
            
            

def qlex(program_file):
   tokens = get_tokens(program_file)
   lexarr = lexify_tokens(tokens, lex_regulars)
   return [token(*lex) for lex in lexarr]