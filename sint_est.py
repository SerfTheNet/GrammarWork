# -*- coding: utf-8 -*-
from nltk.draw import tree
from nltk import CFG, parse

from lex import qlex

#tr =  tree.Tree.fromstring('(корень (дерева мудрости (которое всех достало)))')
#tr.draw()
#normal_grammer = grammer.chomsky_normal_form(new_token_padding='_')

gr1 = """S -> T | S OR_EX T
 T -> E | T AND_EX E
 E -> '0' | '1'
 OR_EX -> 'or'
 AND_EX -> 'and'"""


grammarstring = """
S -> PRORGAM_KW ID STATSMENT_BLOCK END_DOT_KW
STATESMENT_BLOCK -> STATESMENT | STATESMENT_BLOCK DELIMETER STATESMENT
STATESTMENT -> DIM | IF | LOOP | EXPRESSION | IO
DIM -> DIM_KW ID AS_KW TYPE
IF -> IF_KW CONDITION THEN_KW STATESMENT_BLOCK ELSE_KW STATESMENT_BLOCK END_KW | IF_KW CONDITION THEN_KW STATESMENT_BLOCK END_KW
CONDITION -> ID | ID COMPARSION ID
LOOP -> WHILE_KW CONDITION DO_KW STATESMENT_BLOCK END_KW
IO -> INPUT_KW | OUTPUT_KW STRING
EXPRESSION -> ID EQ_KW ID OPERATION ID | ID EQ_KW ID OPERATION CONST

TYPE -> 'int' | 'string'
CONST -> 'const'
DELIMETER -> ';'
COMPARSION -> '==' | '>' | '<' | '<=' | '>='
OPERATION -> '+' | '-' | '/' | '*'

STRING -> 'str'
INT -> 'ii'
ID -> 'id'

PRORGAM_KW -> 'program'
END_DOT_KW -> 'end.'
DIM_KW -> 'dim'
AS_KW -> 'as'
IF_KW -> 'if'
THEN_KW -> 'then'
ELSE_KW -> 'else'
END_KW -> 'end'
WHILE_KW -> 'while'
DO_KW -> 'do'
INPUT_KW -> 'input'
OUTPUT_KW -> 'output'
EQ_KW ->  '='
"""
grammer = CFG.fromstring(grammarstring)



program = """program id
dim id as string ;
dim id as int ;
id = input ;
if 
    id == str
then
    while
        id == int
    do
        id = id + ii ;
        output id
    end ;
else
     output str
end ;
end.
"""

program = """program id
dim id as string ;
output str
end.
"""


class Parser:
    def __init__(self, grammarstr):
        self.grammarstr = grammarstr
        self.grammar = self.grparse(self.grammarstr)
        self.predict = None
        self.predict_stack = []
        self.expr = []
    def grparse(grammer):
        grstrs = filter(lambda x: x != '', grammer.split('\n'))
        grtpls = (grstr.split('->') for grstr in grstrs)
        grtpls = [[grtpl[0], grtpl[1].split('|')] for grtpl in grtpls]
        grexprs = []
        for grtpl in grtpls:
            for parse in grtpl[1]:
                grexprs.append((grtpl[0].strip(), parse.strip().split(' ')))
        return grexprs
    def get_token(self, tokens):
        self.expr.append(tokens.pop(0))
    def parse(self, tokens):
        while True:
            if True:
                pass
            elif True:
                pass
            else:
                self.get_token()
    
        
tokens = program.split()

prs = parse.earleychart.IncrementalChartParser(grammer, trace = 1)






lexarr = qlex()
