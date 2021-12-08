import re
report = open('LexicalAnalysis.txt', 'w')
report.write('')
report.close()


class LexicalAnalyzer:
    # Token row
    lin_num = 1

    def tokenize(self, code):
        rules = [
            # Meta
            ('PROGRAM', r'(?i)PROGRAM'),
            ('PROCEDURE', r'(?i)PROCEDURE'),
            ('PARAMETERS', r'(?i)PARAMETERS'),

            ('DECLARE', r'(?i)DECLARE'),
            ('CALL', r'(?i)CALL'),
            ('CALL_FUNCTION',
             r'(?i)(?<=CALL ).*?[a-zA-Z(a-zA-Z(a-zA-Z+)(\s)*(\,(a-zA-Z+))*]+'),
            ('SET', r'(?i)SET'),

            # Data Types
            ('INTEGER_DT', r'(?i)INTEGER'),
            ('REAL_DT', r'(?i)REAL'),
            ('STRING_ID', r'(?i)STRING'),
            ('STRING_DT', r'\"(.*)\"'),
            ('NUM_CONST_DT', r'\d(\d)*(\.\d(\d)*)?'),

            # if condition
            ('IF', r'(?i)IF'),
            ('THEN', r'(?i)THEN'),
            ('ELSE', r'(?i)ELSE'),
            ('ENDIF', r'(?i)ENDIF'),

            # While Loop
            ('WHILE', r'(?i)WHILE'),
            ('DO', r'(?i)DO'),
            ('ENDWHILE', r'(?i)ENDWHILE'),

            # Until condition
            ('UNTIL', r'(?i)WHILE'),
            ('ENDUNTIL', r'(?i)ENDWHILE'),

            # Read/Write ops
            ('READ', r'(?i)READ'),
            ('WRITE', r'(?i)WRITE'),

            ('BEGIN', r'(?i)BEGIN'),
            ('END', r'(?i)END'),

            ('LEFT_BRACKET', r'\('),
            ('RIGHT_BRACKET', r'\)'),
            ('COMMA', r','),
            ('SEMI_COLON', r';'),

            ('COMMENT', r'\{(.|\n)*?\}'),
            ('LEFT_BRACE', r'\{'),
            ('RIGHT_BRACE', r'\}'),

            # Relational operators
            ('EQUALS', r'='),
            ('NOT_EQUALS', r'!'),
            ('LESS_THAN', r'<'),
            ('GREATER_THAN', r'>'),

            # Arthemetic operators
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MULT', r'\*'),
            ('DIV', r'\/'),

            ('IDENTIFIER', r'(?i)[a-zA-Z]\w*'),
            ('NEWLINE', r'\n'),
            ('SKIP', r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)

        # It analyzes the code to find the lexemes and their respective Tokens
        for m in re.finditer(tokens_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'NEWLINE':
                self.lin_num += 1
            elif token_type == 'SKIP' or token_type == 'COMMENT':
                continue
            elif token_type == 'MISMATCH':
                raise RuntimeError('%r Undefined token on line %d' %
                                   (token_lexeme, self.lin_num))
            else:
                report = open('LexicalAnalysis.txt', 'a')
                report.write('Token = {0},\t\t\t\t\t Lexeme = \'{1}\',\t\t\t\t\t Row = {2}'.format(
                    token_type, token_lexeme, self.lin_num)+'\n')
                report.close()
