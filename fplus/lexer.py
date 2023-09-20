from rply import LexerGenerator

lg = LexerGenerator()

# define all tokens
lg.add("PLUS", r"\+")
lg.add("MINUS", r"-")
lg.add("TIMES", r"\*")
lg.add("DIVIDE", r"\/")
lg.add("FLT", r"((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))")
lg.add("INT", r"\d+")
lg.add("STR", r'\".*?\"')
lg.add("LEFT_PAR", r"\(")
lg.add("RIGHT_PAR", r"\)")
lg.add("ECHO", r"echo")
lg.add("TOINT", r"int")
lg.add("TOFLT", r"flt")
lg.add("TOSTR", r"str")
lg.ignore(r"\s+")

lexer = lg.build()