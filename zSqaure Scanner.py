import enum

class Tokens(enum.Enum):
    ADD = "Addition Operator"
    SUB = "Subtraction Operator"
    MUL = "Multiplication Operator"
    DIV = "Division Operator"
    MOD = "Modolus Operator"
    ASSM = "Assignment Operator"
    AASSM = "Addition Assignment Operator(Compound)"
    SASSM = "Subtraction Assignment Operator(Compound)"
    MASSM = "Multiplication Assignment Operator(Compound)"
    DASSM = "Division Assignment Operator(Compound)"
    MODASSM = "Modulus Assignment Operator(Compound)"
    UNADD = "Uniary Addition Operator"
    UNSUB = "Uniary Subtraction Operator"
    EQ = "Equal Comparison Operator"
    NEQ = "Not Equal Comparison Operator"
    LT = "Less Than Comaprison Operator"
    GT = "Greater Than Comparison Operator"
    LEQ = "Less Than or Equal To Comparison Operator"
    GEQ = "Greator Than or Equal To Comparison Operator"
    AND = "Logical and Operator"
    OR = "Logical or Operator"
    NOT = "Logical not Operator"
    SCOLON = "Semicolon"
    COLON = "Colon"
    STER = "Statement Termination Operator"
    COMMA = "Comma"
    OPENBRAC = "Open Bracket"
    CLOSEBRAC = "Close Bracket"
    OPENCUR = "Open Curley Bracket"
    CLOSECUR = "Close Curley Bracket"
    OPENSQR = "Open Square Bracket"
    CLOSESQR = "Close Square Bracket"
    EOF = "End of File"
    ID = "Identifier"
    INTCON = "Integer Constant"
    DECCON = "Decimal Constant"
    STRCON = "String Constant"
    CHARCON = "Character Constant"
    COM = "Comment"
    BOOL_KEY = "boolean_keyword"
    INT_KEY = "integer_keyword"
    DEC_KEY = "decimal_keyword"
    CHAR_KEY = "char_keyword"
    TEXT_KEY = "text_keyword"
    PUT_KEY = "put_keyword"
    GET_KEY = "get_keyword"
    CHECKIF_KEY = "checkif_keyword"
    ELIF_KEY = "elif_keyword"
    ELSE_KEY = "else_keyword"
    LOOP_KEY = "loop_keyword"
    UNTIL_KEY = "until_keyword"
    REP_KEY = "repeat_keyword"
    FUN_KEY = "function_keyword"
    VOID_KEY = "void_keyword"
    NEW_KEY = "new_keyword"
    THROW_KEY = "throw_keyword"
    FUNC_NAME = "function_name"
    ERR = "Invalid Token"

def getChar():
    if getChar.index == len(content):
        return -1
    c = content[getChar.index]
    getChar.index += 1
    return c
getChar.index = 0

def validToken(ch):
    if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '%' or ch == '=' or ch == ':' or ch == '[' or ch == ']' or ch == '{' or ch == '}' or ch == '(' or ch == ')' or ch == '<' or ch == '>' or ch == ',' or ch == '\n' or ch == ' ':
        return True
    return False
        
def scan():
    checkDot = False
    ch = getChar()
    while(True):
        if ch == -1:
            break
        elif ch == ';':
            print(Tokens.SCOLON.value)
            ch = getChar()
        elif ch == ':':
            print(Tokens.COLON.value)
            ch = getChar()
        elif ch == '.':
            if checkDot == True:
                print(Tokens.STER.value)
                checkDot = False
                ch = getChar()
            else:
                ch = getChar()
                if ch != -1 and ch.isdigit():
                    isValid = True
                    while True:
                        ch = getChar()
                        if ch == -1:
                            break
                        elif ch.isdigit():
                            pass
                        elif ch == '.':
                            checkDot = True
                            isValid = True
                            break
                        elif not validToken(ch):
                            isValid = False
                        elif ch == '!':
                            if getChar() == '=':
                                getChar.index -= 1
                                break
                            else:
                                getChar.index -= 1
                                isValid = False
                        elif ch == '.':
                            if getChar().isdigit():
                                getChar.index -= 1
                                isValid = False
                            else:
                                getChar.index -= 1
                                break
                        else:
                            break
                    if isValid == False:
                        print(Tokens.ERR.value)
                    else:
                        print(Tokens.DECCON.value)
                else:
                    print(Tokens.STER.value)
                    ch = getChar()
        elif ch == ',':
            print(Tokens.COMMA.value)
            ch = getChar()
        elif ch == '(':
            print(Tokens.OPENBRAC.value)
            ch = getChar()
        elif ch == ')':
            print(Tokens.CLOSEBRAC.value)
            ch = getChar()
        elif ch == '{':
            print(Tokens.OPENCUR.value)
            ch = getChar()
        elif ch == '}':
            print(Tokens.CLOSECUR.value)
            ch = getChar()
        elif ch == '[':
            print(Tokens.OPENSQR.value)
            ch = getChar()
        elif ch == ']':
            print(Tokens.CLOSESQR.value)
            ch = getChar()
        elif ch == '=':
            ch = getChar()
            if ch == '=':
                print(Tokens.EQ.value)
                ch = getChar()
            else:
                print(Tokens.ASSM.value)
        elif ch == '+':
            ch = getChar()
            if ch == '=':
                print(Tokens.AASSM.value)
                ch = getChar()
            elif ch == '+':
                print(Tokens.UNADD.value)
                ch = getChar()
            else:
                print(Tokens.ADD.value)
        elif ch == '-':
            ch = getChar()
            if ch == '=':
                print(Tokens.SASSM.value)
                ch = getChar()
            elif ch == '-':
                print(Tokens.UNSUB.value)
                ch = getChar()
            else:
                print(Tokens.SUB.value)
        elif ch == '*':
            ch = getChar()
            if ch == '=':
                print(Tokens.MASSM.value)
                ch = getChar()
            else:
                print(Tokens.MUL.value)
        elif ch == '/':
            ch = getChar()
            if ch == '=':
                print(Tokens.DASSM.value)
                ch = getChar()
            else:
                print(Tokens.DIV.value)
        elif ch == '%':
            ch = getChar()
            if ch == '=':
                print(Tokens.MODASSM.value)
                ch = getChar()
            else:
                print(Tokens.MOD.value)
        elif ch == '<':
            ch = getChar()
            if ch == '=':
                print(Tokens.LEQ.value)
                ch = getChar()
            else:
                print(Tokens.LT.value)
        elif ch == '>':
            ch = getChar()
            if ch == '=':
                print(Tokens.GEQ.value)
                ch = getChar()
            else:
                print(Tokens.GT.value)
        elif ch == '!':
            ch = getChar()
            if ch == '=':
                print(Tokens.NEQ.value)
                ch = getChar()
            else:
                print(Tokens.ERR.value)
        elif ch == '\\':
            ch = getChar()
            if ch == '*':
                while True:
                    ch = getChar()
                    if ch == -1:
                        print("Error! EOF while incomment")
                        break
                    elif ch == '*':
                        ch = getChar()
                        if ch == '\\':
                            print(Tokens.COM.value)
                            break
                ch = getChar()
            else:
                print(Tokens.ERR.value)
        elif ch == '"':
            while True:
                ch = getChar()
                if ch == -1:
                    print(Tokens.ERR.value)
                    break
                elif ch == '"':
                    print(Tokens.STRCON.value)
                    ch = getChar()
                    break
        elif ch == "'":
            ch =getChar()
            ch1 = getChar()
            if ch1 == "'":
                print(Tokens.CHARCON.value)
                ch = getChar()
            else:
                getChar.index -= 1
                while True:
                    ch = getChar()
                    if ch == -1:
                        break
                    elif ch == "'":
                        ch = getChar()
                        break
                print(Tokens.ERR.value)
        elif str(ch).isdigit():
            decimal = False
            isValid = True
            count = 0
            
            while True:
                ch = getChar()
                if ch == -1:
                    break
                if ch == '.':
                    if count == 1 and isValid == True:
                        checkDot = True
                        break
                    count += 1
                    ch = getChar()
                    if ch == '.':
                        isValid = False
                    if ch == -1:
                        ch = '.'
                        break
                    if ch.isdigit():
                        if decimal == True:
                            isValid = False
                        decimal = True
                    elif not validToken(ch):
                        isValid = False
                    else:
                        break
                elif not ch.isdigit():
                    if not validToken(ch):
                        isValid = False
                    else:
                        break
            if isValid == False:
                print(Tokens.ERR.value)
            elif decimal == True:
                print(Tokens.DECCON.value)
            else:
                print(Tokens.INTCON.value)
        elif str(ch).isupper():
            while True:
                ch = getChar()
                if validToken(ch) or ch == '.' or ch == -1:
                    break
                elif ch == '!':
                    if getChar() == '=':
                        getChar.index -= 1
                        break
                    else:
                        getChar.index -= 1
            print(Tokens.ERR.value)
        elif str(ch).islower():
            word = ch
            while True:
                ch = getChar()
                if validToken(ch) or ch == '.' or ch == ' ' or ch == -1 or ch == '\n':
                    break
                elif ch == '!':
                    if getChar() == '=':
                        getChar.index -= 1
                        break
                    else:
                        getChar.index -= 1
                word += ch
            keysList = list(keywords.keys())
            if keysList.count(word) > 0:
                print(keywords[word])
            elif ch == 'and':
                print(Tokens.AND.value)
            elif ch == 'or':
                print(Tokens.OR.value)
            elif ch == 'not':
                print(Tokens.NOT.value)
            elif ch == '(':
                print(Tokens.FUNC_NAME.value)
            else:
                print(Tokens.ERR.value)
        elif ch == '$':
            isValid = True
            while True:
                ch = getChar()
                if ch == -1:
                    break
                elif ch.isdigit() or ch.isalpha() or ch == '_':
                    pass
                elif validToken(ch) or ch == '.' or ch == ' ' or ch == '\n':
                    break
                elif ch == '!':
                    if getChar() == '=':
                        getChar.index -= 1
                        break
                    else:
                        getChar.index -= 1
                        isValid = False
                else:
                    isValid = False
            if isValid == True:
                print(Tokens.ID.value)
            else:
                print(Tokens.ERR.value)
        elif ch == ' ':
            ch = getChar()
        elif ch == '\n':
            ch = getChar()
        elif ch == '\t':
            ch = getChar()
        else:
            while True:
                ch = getChar()
                if validToken(ch) or ch == '.' or ch == -1:
                    break
            print(Tokens.ERR.value)


keywords = {"boolean":Tokens.BOOL_KEY.value, "integer": Tokens.INT_KEY.value, "decimal": Tokens.DEC_KEY.value, "char":Tokens.CHAR_KEY.value, "text":Tokens.TEXT_KEY.value, "put":Tokens.PUT_KEY.value, "get":Tokens.GET_KEY.value, "checkif":Tokens.CHECKIF_KEY.value, "elif":Tokens.ELIF_KEY.value, "else": Tokens.ELSE_KEY.value, "loop":Tokens.LOOP_KEY.value, "until":Tokens.UNTIL_KEY.value, "repeat":Tokens.REP_KEY.value, "function": Tokens.FUN_KEY.value, "void":Tokens.VOID_KEY.value, "new":Tokens.NEW_KEY.value, "throw":Tokens.THROW_KEY.value, "and":Tokens.AND.value, "or":Tokens.OR.value, "not":Tokens.NOT.value}
filepath = ""
print("Enter complete file path: ")
filepath = input()
file = open(filepath, 'r')
content = file.read()
scan()