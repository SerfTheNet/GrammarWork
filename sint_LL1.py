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
        self.stsymb = 0
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
        self.stsymb = 0
        # для визуализации парсинга: смещение = 2
        offset = 2
        return self.parse_block(tokens, awaits, offset)
    
    def parse_block(self, tokens, awaits, offset):
        lst = list(filter(lambda rule: rule[0] == awaits, self.grammar))
        for rule in filter(lambda rule: rule[0] == awaits, self.grammar):
            retval = None
            print(f'{"-"*offset}Ожидается {rule[0]}({rule[1]})')
            if self.stsymb >= len(tokens):
                    print(f'{"-"*offset}Конец входной строки, правило отвергается')
                    break
            if self.isTerminalRule(rule):
                token = tokens[self.stsymb]
                if token == rule[1][0]:
                    print(f'{"-"*offset}->Получено {token}')
                    #return (rule, 1)
                    retval = rule
                    self.stsymb += 1
                    break
                else:
                    print(f'{"-"*offset}Неверный токен, правило отвергается')
            
            else:
                tree = [awaits, []]
                # для всех элетентов вывода
                for aw in rule[1]:
                    # рекурсивно углубляемся в правило
                    ret = self.parse_block(tokens, aw, offset + 2)
                    # если не происходит ошибка вывода
                    if ret:
                        print(f'{"-"*offset}->Получено {ret[0]}')
                        tree[1].append(ret)
                    else:
                        retval = None
                        break
                print(f'{"-"*offset}Получено {tree}')
                retval = tree
                break
        return retval
    
    def gettrstr(node):
        if isinstance(node, str):
            return node
        else:
            allstr = []
            for chnode in node[1]:
                allstr.append(Parser.gettrstr(chnode))
            chstr = ' '.join(allstr)
            return f'({node[0]} {chstr})'
        
    
    def getTree(stree):
        tr = tree.Tree.fromstring(Parser.gettrstr(stree))
        tree.draw_trees(tr)
        
tokens = "1 and 0 and 1 or 1 or 0 and 1".split()
pr = Parser(grammarstr)
stree = pr.parse(tokens, start = 'S')
Parser.getTree(stree)
