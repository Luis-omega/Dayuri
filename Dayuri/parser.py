from lark import Lark, Transformer
from typing import Optional

with open("grammar.lark", "r") as fh:
    grammar = fh.read()


def gen_parser(
    start: str = "start",
    debug: bool = False,
    transformer: Optional[Transformer] = None,
):
    if transformer:
        return Lark(
            grammar=grammar,
            debug=debug,
            start=start,
            maybe_placeholders=True,
            keep_all_tokens=True,
            parser="lalr",
            transformer=transformer,
        )

    return Lark(
        grammar=grammar,
        debug=debug,
        start=start,
        maybe_placeholders=True,
        keep_all_tokens=True,
        parser="lalr",
    )
