import unittest
from pathlib import Path

from Dayuri.parser import gen_parser
from Dayuri.desugar import Desugar


base_path = Path("tests/syntax_samples")


def parse(path, rule_name):
    with open(path, "r") as fh:
        source = fh.read()
    parser = gen_parser(rule_name, transformer=Desugar)
    return parser.parse(source)


class TestDeSugar(unittest.TestCase):
    def test_types(self):
        tree = parse(
            base_path / "type_definition.dy", "test_new_type"
        )
        print(tree.pretty())
        for i in tree.children:
            print(repr(i))


if __name__ == "__main__":
    unittest.main()
