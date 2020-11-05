from lark import Tree, Token, Transformer

from Dayuri.ast_types import *


class MakeAst(Transformer):
    def annotation(nodes):
        if len(nodes) == 1:
            return nodes[0]
        name = nodes[0]
        args = nodes[1:]
        return Constructor(nodes, args)
