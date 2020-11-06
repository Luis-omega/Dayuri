import unittest
from Dayuri.parser import gen_parser

from pathlib import Path

base_path = Path("tests/syntax_samples")


def parse(path, rule_name):
    with open(path, "r") as fh:
        source = fh.read()
    parser = gen_parser(rule_name)
    tree = parser.parse(source)
    print(tree.pretty())


class TestSyntax(unittest.TestCase):
    def test_basic_binding(self):
        parse(base_path / "basic_binding.dy", "test_binding")


if __name__ == "__main__":
    unittest.main()
