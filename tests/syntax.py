import unittest
from Dayuri.parser import (
    gen_parser,
    Desugar,
    Desugar2Ast,
    ast2string,
)

from pathlib import Path

base_path = Path("tests/syntax")


def parse(path, rule_name):
    with open(path, "r") as fh:
        source = fh.read()
    parser = gen_parser(rule_name, transformer=Desugar)
    tree = parser.parse(source)
    tree = Desugar2Ast().transform(tree)
    # print(tree)
    for line in tree.children[::2]:
        print(ast2string(line))


class TestSyntax(unittest.TestCase):
    def test_type_expression(self):
        parse(
            base_path / "type_expression.dy", "test_type_expression"
        )


if __name__ == "__main__":
    unittest.main()
