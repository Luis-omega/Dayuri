from lark import Transformer, Tree, Token


class Desugar(Transformer):
    def type_atom(nodes):
        return nodes[1]

    def type_annotation(nodes):
        return Tree("annotation", nodes[1:])

    def new_type(nodes):
        name = nodes[1]
        type_vars = nodes[2]
        if isinstance(nodes[4], Token):
            constructors = nodes[5:-1]
            return Tree("type", [name, type_vars, *constructors])
        constructor = nodes[4]
        return Tree("type", [name, type_vars, constructor])

    def new_type_constructor_inner(nodes):
        return Tree("annotated_expr", [nodes[1], nodes[2]])

    def new_type_constructor(nodes):
        return Tree("constructor", nodes[:-1])
