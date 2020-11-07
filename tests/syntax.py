import unittest
from Dayuri.parser import (
    gen_parser,
    Desugar
)

from pathlib import Path

base_path = Path("tests/syntax")


def parse(path, rule_name):
    with open(path, "r") as fh:
        source = fh.read()
    parser = gen_parser(rule_name, transformer=Desugar)
    tree = parser.parse(source)
    return tree

class TestSyntax(unittest.TestCase):
    def test_type_expression(self):
        parse(
            base_path / "type_expression.dy", "test_type_expression"
        )

    def test_declaration(self):
        tree = parse(
            base_path / "declaration.dy", "test_declaration"
        )
        #print(tree.pretty())

if __name__ == "__main__":
    unittest.main()
