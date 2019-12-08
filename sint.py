# -*- coding: utf-8 -*-
from nltk.draw import tree
from IPython.display import display
from lex import qlex

class Parser:
    def __init__(self, grammar_file):
        self.read_grammar(grammar_file)
        self.grammar = self.grparse(self.grammarstr)
        self.predict = None
        self.predict_stack = []
        self.expr = []
        self.stsymb = 0
    def read_grammar(self, grammar_file):
        with open(grammar_file, 'r') as f:
            self.grammarstr = f.read()
    def grparse(self, grammer):
        grstrs = filter(lambda x: x != '', grammer.split('\n'))
        grtpls = [grstr.split('->') for grstr in grstrs]
        grtpls = [[grtpl[0], grtpl[1].split('|')] for grtpl in grtpls]
        grexprs = []
        for grtpl in grtpls:
            for parse in grtpl[1]:
                grexprs.append((grtpl[0].strip(), parse.strip().split(' ')))
        return grexprs
    def isTerminalRule(self, rule):
        return len(rule[1]) == 1 and rule[1][0] not in map(lambda x: x[0], self.grammar)
        
    def parse(self, tokens: object, tok_orig: object, start: object = 'S') -> object:
        # ожидаемый символ - начальный символ        
        awaits = start
        # стартовый символ 0
        self.stsymb = 0
        # для визуализации парсинга: смещение = 2
        offset = 5
        #
        return self.parse_block(tokens, awaits, offset, tok_orig)
    
    def parse_block(self, tokens, awaits, offset, tok_orig):
        retval = None
        # для каждого правила с предсказаных заголовком
        for rule in filter(lambda rule: rule[0] == awaits, self.grammar):
            retval = None
            interrupted_flag = False
            # запоминаем состояние распознавателя
            backtrack = self.stsymb
            #print(f'{"-"*offset}Ожидается {rule[0]}({rule[1]})')
            # если длина правила заведомо больше числа имеющихся токенов, отвергаем его
            if self.stsymb >= len(tokens):
                #print(f'{"-"*offset}Конец входной строки, правило отвергается')
                continue
            # если правило терминальное:
            if self.isTerminalRule(rule):
                # читаем текущий токен
                token = tokens[self.stsymb]
                #print(f'{"-"*offset}->Чтение {token}')
                # если полученный токен удовлетворяет предсказанию                
                if token == rule[1][0]:
                    #print(f'{"-"*offset}->Токен {token} удовлетворяет предсказанию')
                    # устанавливаем значение возврата на это правило
                    retval = tok_orig[self.stsymb].getToTree()
                    # сдвигаем указатель распознавателя на 1 символ вперед
                    self.stsymb += 1
                    break
                # иначе рассматриваемое правило отвергается
                else:
                    #print(f'{"-"*offset}Неверный токен {token}, правило отвергается')
                    # откатываем указатель до состояния в начале правила
                    pass

            # если правило нетерминальное
            else:
                tree = [awaits, []]
                # для каждого выврдимого символа правила
                for aw in rule[1]:
                    # рекурсивно углубляемся в правило
                    ret = self.parse_block(tokens, aw, offset + 2, tok_orig)
                    # если не произошло отката правила
                    if ret:
                        #print(f'{"-"*offset}->В дерево добавлено {ret}')
                        tree[1].append(ret)
                    # откат правила
                    else:
                        # откатываем указатель до состояния в начале правила
                        self.stsymb = backtrack
                        # правило уже не будет распознано; цикл можно прервать
                        #print(f'{"-"*offset}Не удалось распознать правило {rule}, выбираем следующее правило; указатель {self.stsymb}')
                        interrupted_flag = True
                        break
                # если правило распозналось
                if not interrupted_flag:
                    #print(f'{"-"*offset}Прочитано дерево {tree}')
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
        
    def drawTree(stree):
        tr = tree.Tree.fromstring(Parser.gettrstr(stree))
        tree.draw_trees(tr)
        return tr