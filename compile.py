# -*- coding: utf-8 -*-

from lex import qlex
from sint import Parser

program_file = 'data/prog.pr'
grammar_file = 'data/grammar.gr'

tokens = qlex(program_file)
token_sint_map = list(map(str, tokens))

parser = Parser(grammar_file)
stree = parser.parse(token_sint_map, tokens, start = 'S')
Parser.drawTree(stree)
