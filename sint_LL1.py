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
S -> T or S
S -> T
T -> E and T
E -> 0
E -> 1
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
    def isTerminal(token):
        return token not in map(lambda x: x[0], pr.grammar)
            
    def get_token(self, tokens):
        self.expr.append(tokens.pop(0))
    def parse(self, tokens, awaits, stsymb, offset):
        for rule in filter(lambda rule: rule[0] == awaits, self.grammar):
            print(f'{"-"*offset}Ожидается {rule[0]}')
            for drule in rule[1]:
                self.parse(tokens, drule, 0, offset + 2)
    
        
tokens = "1 and 0 or 1".split()
pr = Parser(grammarstr)
#pr.parse(tokens, 'S', 0 ,0)

