from rply import ParserGenerator
import curses
pg = ParserGenerator(["INT", "STR", "FLT", "PLUS", "MINUS", "TIMES", "DIVIDE", "LEFT_PAR", "RIGHT_PAR", "ECHO", "TOINT", "TOFLT", "TOSTR"], precedence=[("left", ['INT', 'STR', 'FLT', 'TOSTR', 'TOFLT', 'TOINT', 'TIMES', 'DIVIDE', "PLUS", "MINUS"])], cache_id="myparser")

@pg.production("main : expr")
def main(p):
    # p is a list, of each of the pieces on the right hand side of the
    # grammar rule
    return p[0]
@pg.production("expr : STR")
def expr_str(p):
    return str(p[0].getstr())
@pg.production("expr : INT")
def expr_int(p):
    return int(p[0].getstr())
@pg.production("expr : FLT")
def expr_flt(p):
    return float(p[0].getstr())
@pg.production("expr : LEFT_PAR expr RIGHT_PAR")
def expr_pars(p):
    return p[1]
@pg.production("expr : ECHO expr")
def expr_echo(p):
    if type(p[1]) is str:
        return p[1][1:-1]
    else:
        return p[1]
@pg.production("expr : TOINT expr")
@pg.production("expr : TOFLT expr")
@pg.production("expr : TOSTR expr")
def expr_totype(p):
    if type(p[1]) is str: l = p[1][1:-1]
    else: l = p[1]
    
    if p[0].gettokentype() == "TOINT":
        return int(l)
    elif p[0].gettokentype() == "TOFLT":
        return float(l)
    elif p[0].gettokentype() == "TOSTR":
        return str(l)
@pg.production("expr : expr PLUS expr")
@pg.production("expr : expr MINUS expr")
@pg.production("expr : expr TIMES expr")
@pg.production("expr : expr DIVIDE expr")
def expr_op(p):
    if type(p[0]) is str: _0 = p[0][1:-1]
    else: _0 = p[0]
    if type(p[2]) is str: _2 = p[2][1:-1]
    else: _2 = p[2]
    
    if p[1].gettokentype() == "PLUS":
        return _0 + _2
    elif p[1].gettokentype() == "MINUS":
        return _0 - _2
    elif p[1].gettokentype() == "TIMES":
        return _0 * _2
    elif p[1].gettokentype() == "DIVIDE":
        return _0 / _2
parser = pg.build()