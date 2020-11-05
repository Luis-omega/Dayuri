from lark import Transformer, Tree, Token


from Dayuri.ast_types import *


class Desugar(Transformer):
    def type_atom(nodes):
        if len(nodes) == 1:
            return TypeVariable(nodes[0], None)
        return nodes[1]

    def type_constructor(nodes):
        name = nodes[0]
        arguments = nodes[1:]
        return TypeConstructor(name, arguments)

    def type_function(nodes):
        domain = nodes[0]
        for codomain in nodes[1:]:
            domain = TypeFunction(domain, codomain)
        return domain

    def type_annotation(nodes):
        return nodes[1]

    def new_type(nodes):
        name = nodes[1]
        if nodes[2]:
            type_vars = nodes[2].children
        else:
            type_vars = []
        if isinstance(nodes[4], Token):
            constructors = nodes[5:-1]
            return DataType(name, type_vars, constructors)
        constructor = nodes[4]
        return DataType(name, type_vars, [constructor])

    def new_type_constructor_inner(nodes):
        if len(nodes) == 1:
            return TypeVariable(nodes[0], None)
        return Variable(nodes[1], nodes[2])

    def new_type_constructor(nodes):
        return Constructor(nodes[0], nodes[1:-1])


class Desugar_old(Transformer):
    def type_atom(nodes):
        return nodes[1]

    def type_annotation(nodes):
        return nodes[1]

    def new_type(nodes):
        name = nodes[1]
        type_vars = nodes[2]
        if isinstance(nodes[4], Token):
            constructors = nodes[5:-1]
            return DataType(name, type_vars, constructors)
        constructor = nodes[4]
        return DataType(name, type_vars, [constructor])

    def new_type_constructor_inner(nodes):
        return Tree("annotated_expr", [nodes[1], nodes[2]])

    def new_type_constructor(nodes):
        return Tree("constructor", nodes[:-1])
