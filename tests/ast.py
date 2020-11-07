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
    return tree

class TestSyntax(unittest.TestCase):
    def test_type_expression(self):
        tree = parse(
            base_path / "type_expression.dy", "test_type_expression"
        )
        outs=[
"int",
"(int->int)",
"(int->(int->int))",
"(int->(int->(int->int)))",
"(int->((int->int)->int))",
"(int->((int->(int->int))->(int->((int->int)->int))))",
            ]
        for line, expected in zip(tree.children[::2], outs):
            out = ast2string(line)
            self.assertEqual(out, expected)
            

    def test_type_expression(self):
        tree = parse(
            base_path / "declaration.dy", "test_declaration"
        )
        outs=[
                "some : int;",
                "some1 : (int->int);",
                "some2 : (int->((int->int)->int));",
            ]
        for line, expected in zip(tree.children[::2], outs):
            out = ast2string(line)
            print(out)
            self.assertEqual(out, expected)

if __name__ == "__main__":
    unittest.main()
