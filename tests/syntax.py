import unittest
from Dayuri.parser import gen_parser

from pathlib import Path

base_path = Path("tests/syntax_samples")


def parse(path, rule_name):
    with open(path, "r") as fh:
        source = fh.read()
    parser = gen_parser(rule_name)
    parser.parse(source)


class TestSyntax(unittest.TestCase):
    def test_types(self):
        parse(base_path / "type_definition.dy", "test_new_type")


if __name__ == "__main__":
    unittest.main()
