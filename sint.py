# -*- coding: utf-8 -*-
from nltk.draw import tree
from nltk import CFG, parse

from lex import qlex

#tr =  tree.Tree.fromstring('(корень (дерева мудрости (которое всех достало)))')
#tr.draw()
#normal_grammer = grammer.chomsky_normal_form(new_token_padding='_')


#grammer = CFG.fromstring("""
#S -> PRORGAM_KW ID STATSMENT_BLOCK END_DOT_KW
#STATESMENT_BLOCK -> STATESMENT | STATESMENT_BLOCK DELIMETER STATESMENT
#STATESTMENT -> DIM | IF | LOOP | EXPRESSION | IO
#DIM -> DIM_KW ID AS_KW TYPE
#IF -> IF_KW CONDITION THEN_KW STATESMENT_BLOCK ELSE_KW STATESMENT_BLOCK END_KW | IF_KW CONDITION THEN_KW STATESMENT_BLOCK END_KW
#CONDITION -> ID | ID COMPARSION ID
#LOOP -> WHILE_KW CONDITION DO_KW STATESMENT_BLOCK END_KW
#IO -> INPUT_KW | OUTPUT_KW STRING
#EXPRESSION -> ID EQ_KW ID OPERATION ID | ID EQ_KW ID OPERATION CONST
#
#TYPE -> 'int' | 'string'
#CONST -> 'const'
#DELIMETER -> ';'
#COMPARSION -> '==' | '>' | '<' | '<=' | '>='
#OPERATION -> '+' | '-' | '/' | '*'
#
#STRING -> 'str'
#INT -> 'ii'
#ID -> 'id'
#
#PRORGAM_KW -> 'program'
#END_DOT_KW -> 'end.'
#DIM_KW -> 'dim'
#AS_KW -> 'as'
#IF_KW -> 'if'
#THEN_KW -> 'then'
#ELSE_KW -> 'else'
#END_KW -> 'end'
#WHILE_KW -> 'while'
#DO_KW -> 'do'
#INPUT_KW -> 'input'
#OUTPUT_KW -> 'output'
#EQ_KW ->  '='
#""")
#
#program = """program id
#dim id as string ;
#dim id as int ;
#id = input ;
#if 
#    id == str
#then
#    while
#        id == int
#    do
#        id = id + ii ;
#        output id
#    end ;
#else
#     output str
#end ;
#end.
#"""
#tokens = program.split()
#
#prs = parse.earleychart.IncrementalChartParser(grammer, trace = 1)






lexarr = qlex()
