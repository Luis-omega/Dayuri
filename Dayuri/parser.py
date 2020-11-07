from typing import Optional, Union, Type, TypeVar

from lark import Lark, Transformer, Tree, Token

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


class Desugar(Transformer):
    def type_atom(nodes):
        if len(nodes) == 1:
            return BaseTypeInt
        return nodes[1]

    def type_arrow(nodes):
        if len(nodes) == 1:
            return nodes[0]
        nodes = nodes[::-1]
        codomain = nodes[0]
        for domain in nodes[2::2]:
            codomain = Tree("arrow", [domain, codomain])
        return codomain

    def type_expression(nodes):
        return nodes[0]

    def declaration(nodes):
        return Tree("declaration", [nodes[0], nodes[2]])




DayuriType = Union["Type[BaseTypeInt]", "Arrow"]

class BaseTypeInt:
    pass


map_string2types_aux = {"int": BaseTypeInt}


def name2type(name: str) -> Optional[DayuriType]:
    return map_string2types_aux.get(name, None)



class Arrow:
    def __init__(
        self,
        domain: DayuriType,
        codomain: DayuriType,
    ):
        self.domain = domain
        self.codomain = codomain

    def __str__(self):
        return f"({self.domain}->{self.codomain})"


class Declaration:
    def __init__(self, name:str, domain: DayuriType):
        self.name = name
        self.domain = domain



class Desugar2Ast(Transformer):
    @staticmethod
    def arrow(nodes):
        left, right = nodes
        if isinstance(left, Token):
            left = name2type(left)
        if isinstance(right, Token):
            right = name2type(right)
        return Arrow(left, right)
   
    @staticmethod
    def declaration(nodes):
        name, domain = nodes
        return Declaration(name, domain)


def ast2string(node: DayuriType):
    if isinstance(node, Arrow):
        left = ast2string(node.domain)
        right = ast2string(node.codomain)
        return f"({left}->{right})"
    if isinstance(node, Declaration):
        domain = ast2string(node.domain)
        return f"{node.name} : {domain};"
    if node is BaseTypeInt:
        return "int"

