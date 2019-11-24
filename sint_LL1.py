# -*- coding: utf-8 -*-
from nltk.draw import tree

from lex import qlex


grammarstr = """
S -> program ID STATSMENT_BLOCK end.

STATSMENT_BLOCK -> DIM
STATSMENT_BLOCK -> IO  
STATSMENT_BLOCK -> IF
STATSMENT_BLOCK -> LOOP
STATSMENT_BLOCK -> EXPR

DIM -> dim ID as TYPE

IF -> if CONDITION then STATESMENT_BLOCK else STATESMENT_BLOCK end
IF -> if CONDITION then STATESMENT_BLOCK end

CONDITION -> ID COMPARSION ID
CONDITION -> ID



"""

grammarstr = """
S -> T OR S
S -> T
T -> E AND T
T -> E
E -> 0
E -> 1
AND -> and
OR -> or
"""


class Parser:
    def __init__(self, grammarstr):
        self.grammarstr = grammarstr
        self.grammar = self.grparse(self.grammarstr)
        self.predict = None
        self.predict_stack = []
        self.expr = []
    def grparse(self, grammer):
        grstrs = filter(lambda x: x != '', grammer.split('\n'))
        grtpls = (grstr.split('->') for grstr in grstrs)
        grtpls = [[grtpl[0], grtpl[1].split('|')] for grtpl in grtpls]
        grexprs = []
        for grtpl in grtpls:
            for parse in grtpl[1]:
                grexprs.append((grtpl[0].strip(), parse.strip().split(' ')))
        return grexprs
    def isTerminalRule(self, rule):
        return len(rule[1]) == 1 and rule[1][0] not in map(lambda x: x[0], self.grammar)
            
    def get_token(self, tokens):
        self.expr.append(tokens.pop(0))
        
    def parse(self, tokens, start = 'S'):
        # ожидаемый символ - начальный символ        
        awaits = start
        # стартовый символ 0
        stsymb = 0
        # для визуализации парсинга: смещение = 2
        offset = 2
        return self.parse_block(tokens, awaits, stsymb, offset)
    
    def parse_block(self, tokens, awaits, stsymb, offset):
        lst = list(filter(lambda rule: rule[0] == awaits, self.grammar))
        for rule in filter(lambda rule: rule[0] == awaits, self.grammar):
            print(f'{"-"*offset}Ожидается {rule[0]}({rule[1]})')
            if self.isTerminalRule(rule):
                token = tokens[stsymb]
                if token == rule[1][0]:
                    print(f'{"-"*offset}->Получено {token}')
                    return (rule, 1)
                else:
                    print(f'{"-"*offset}Неверный токен, правило отвергается')
            
            else:         
                # для всех элетентов вывода
                tree = (awaits, [])
                for aw in rule[1]:
                    # рекурсивно углубляемся в правило
                    ret = self.parse_block(tokens, aw, stsymb, offset + 2)
                    # если не происходит ошибка вывода
                    if ret:
                        print(f'{"-"*offset}->Получено {ret[0]} | сдвиг {ret[1]}')
                        stsymb += ret[1]
                        tree[1].append(ret[0])
                    else:
                        return None
                print(f'{"-"*offset}Получено {tree} | сдвиг {stsymb}')
                return (tree, stsymb)
                    
#        else:
#            for rule in filter(lambda rule: rule[0] == awaits, self.grammar):
#                print(f'{"-"*offset}Ожидается {rule[0]}')
#                for drule in rule[1]:
#                    self.parse(tokens, drule, 0, offset + 2)
    
        
tokens = "1 and 0 or 1".split()
pr = Parser(grammarstr)
stree = pr.parse(tokens, start = 'S')

