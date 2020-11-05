from typing import Literal, List, Union


class TypeExpressionParent:
    pass


class TypeVariable(TypeExpressionParent):
    def __init__(self, name: str, domain):
        self.name = name
        self.domain = domain

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"TypeVariable({self.name}, {repr(self.domain)})"


class TypeConstructor(TypeExpressionParent):
    def __init__(self, name: str, arguments: List[TypeVariable]):
        self.name = name
        self.arguments = arguments

    def __str__(self):
        return f"{self.name} {[str(t) for t in self.arguments]}"

    def __repr__(self):
        return f"TypeConstructor({self.name}, {repr(self.arguments)})"


class TypeFunction(TypeExpressionParent):
    def __init__(self, domain, codomain):
        self.domain = domain
        self.codomain = codomain

    def __str__(self):
        return f"({self.domain}->{self.codomain})"

    def __repr__(self):
        return f"TypeFunction({repr(self.domain)}, {repr(self.codomain)})"


class ExpressionParent:
    pass


class Variable(ExpressionParent):
    def __init__(self, name: str, domain):
        self.name = name
        self.domain = domain

    def __str__(self):
        return f"{self.name} : {self.domain}"

    def __repr__(self):
        return f"Variable({repr(self.name)}, {repr(self.domain)})"


class Constructor(ExpressionParent):
    def __init__(
        self,
        name: str,
        arguments: List[Union[Variable, TypeVariable]],
    ):
        self.name = name
        self.arguments = arguments

    def __str__(self):
        return f"{self.name} {' '.join('('+str(t)+')' for t in self.arguments)}"

    def __repr__(self):
        return (
            f"{self.name} {' '.join(repr(t) for t in self.arguments)}"
        )


class StatementParent:
    pass


class DataType(StatementParent):
    def __init__(
        self,
        name: str,
        enviroment_vars: List[TypeVariable],
        constructors: List[Constructor],
    ):
        self.name = name
        print(enviroment_vars)
        self.enviroment_vars = enviroment_vars
        self.constructors = constructors

    def __str__(self):
        variables = " ".join(i for i in self.enviroment_vars)
        args = ";\n".join(str(t) for t in self.constructors)
        return f"type {self.name} {variables} = {{ {args} ;}}"

    def __repr__(self):
        variables = " ".join(i for i in self.enviroment_vars)
        args = ";\n".join(repr(t) for t in self.constructors)
        return f"type {self.name} {variables} = {{ {args} ;}}"
