from .lexer import lexer
from .parser import parser

def _run(text):
    return parser.parse(lexer.lex(text))
