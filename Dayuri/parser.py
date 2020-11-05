from lark import Lark
from typing import Optional
from desugar import Desguar

with open("grammar.lark", "r") as fh:
    grammar = fh.read()


def gen_parser(start: str = "start", debug: bool = False):
    parser = Lark(
        grammar=grammar,
        debug=debug,
        start=start,
        maybe_placeholders=True,
        keep_all_tokens=True,
        parser="lalr",
        transformer=Desugar,
    )
    return parser
