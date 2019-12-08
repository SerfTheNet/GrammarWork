# -*- coding: utf-8 -*-

# требования к программе: Python 3.7, nltk, ghostcript, компилятор?
#
import codegen
from lex import qlex
from sint import Parser
from semant import semant


program_file = 'data/prog.pr'
grammar_file = 'data/grammar.gr'

tokens = qlex(program_file)
token_sint_map = list(map(str, tokens))

parser = Parser(grammar_file)
stree = parser.parse(token_sint_map, tokens, start = 'S')
id_type_dict = semant(stree, tokens)
Parser.drawTree(stree)
compilate(r'tcc\tcc.exe', stree)