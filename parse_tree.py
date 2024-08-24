from custom_exception import DivisionByZeroException
from command import Command
from cname import CName

class ExpressionParseTree():
    def __str__(self) -> str:
        return ''
    def interpret(self) -> int | float:
        return 0.0
    def compile(self):
        pass

class NumberParseTree(ExpressionParseTree):
    def __init__(self, n: int) -> None:
        self.num = n
    def __str__(self) -> str:
        return str(self.num)
    def interpret(self) -> int:
        return self.num
    def compile(self):
        return [Command(CName.PUSH, self.num)]

class UnaryMinusParseTree(ExpressionParseTree):
    def __init__(self, expression: ExpressionParseTree) -> None:
        self.expression = expression
    def __str__(self) -> str:
        return f'(-{self.expression})'
    def interpret(self) -> float:
        return -1 * self.expression.interpret()
    def compile(self):
        cl1 = self.expression.compile()
        return cl1 + [Command(CName.MONE, None)]

class AdditionParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} + {self.expression2})'
    def interpret(self) -> float:
        return self.expression1.interpret() + self.expression2.interpret()
    def compile(self):
        cl1 = self.expression1.compile()
        cl2 = cl1 + self.expression2.compile()
        return cl2 + [Command(CName.ADD, None)]

class SubtractionParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} - {self.expression2})'
    def interpret(self) -> float:
        return self.expression1.interpret() - self.expression2.interpret()
    def compile(self):
        cl1 = self.expression1.compile()
        cl2 = cl1 + self.expression2.compile()
        return cl2 + [Command(CName.SUB, None)]

class MultiplicationParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} * {self.expression2})'
    def interpret(self) -> float:
        return self.expression1.interpret() * self.expression2.interpret()
    def compile(self):
        cl1 = self.expression1.compile()
        cl2 = cl1 + self.expression2.compile()
        return cl2 + [Command(CName.MUL, None)]


class DivisionParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} / {self.expression2})'
    def interpret(self) -> float:
        if self.expression2.interpret() == 0:
            raise DivisionByZeroException('division by zero')
        else:
            return self.expression1.interpret() / self.expression2.interpret()
    def compile(self):
        cl1 = self.expression1.compile()
        cl2 = cl1 + self.expression2.compile()
        return cl2 + [Command(CName.DIV, None)]

class RemainderParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} % {self.expression2})'
    def interpret(self) -> int | float:
        if self.expression2.interpret() == 0:
            raise DivisionByZeroException('division by zero')
        else:
            return self.expression1.interpret() % self.expression2.interpret()
    def compile(self):
        cl1 = self.expression1.compile()
        cl2 = cl1 + self.expression2.compile()
        return cl2 + [Command(CName.REM, None)]


class LessThanParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} < {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() < self.expression2.interpret():
            return 1
        else:
            return 0
    def compile(self):
        cl1 = self.expression1.compile()
        cl2 = cl1 + self.expression2.compile()
        return cl2 + [Command(CName.LT, None)]

class GreaterThanParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} > {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() > self.expression2.interpret():
            return 1
        else:
            return 0
    def compile(self):
        cl1 = self.expression1.compile()
        cl2 = cl1 + self.expression2.compile()
        return cl2 + [Command(CName.GT, None)]

class EqualsParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} = {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() == self.expression2.interpret():
            return 1
        else:
            return 0
    def compile(self):
        cl1 = self.expression1.compile()
        cl2 = cl1 + self.expression2.compile()
        return cl2 + [Command(CName.EQ, None)]

class NotEqualsParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} != {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() != self.expression2.interpret():
            return 1
        else:
            return 0
    def compile(self):
        cl1 = self.expression1.compile()
        cl2 = cl1 + self.expression2.compile()
        return cl2 + [Command(CName.NEQ, None)]

class AndParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} && {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() == 0 or self.expression2.interpret() == 0:
            return 0
        else:
            return 1
    def compile(self):
        cl1 = self.expression1.compile()
        cl2 = cl1 + self.expression2.compile()
        return cl2 + [Command(CName.AND, None)]

class OrParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} || {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() == 0 and self.expression2.interpret() == 0:
            return 0
        else:
            return 1
    def compile(self):
        cl1 = self.expression1.compile()
        cl2 = cl1 + self.expression2.compile()
        return cl2 + [Command(CName.OR, None)]

class VariableParseTree(ExpressionParseTree):
    def __init__(self, name: str) -> None:
        self.name = name
    def __str__(self) -> str:
        return self.name

class StatementParseTree():
    def __str__(self):
        pass

class AssignmentParseTree(StatementParseTree):
    def __init__(self, variable: VariableParseTree, expression: ExpressionParseTree) -> None:
        self.variable = variable
        self.expression = expression
    def __str__(self) -> str:
        return f'({self.variable.name} := {self.expression};)'

class SequentialCompositionParseTree(StatementParseTree):
    def __init__(self, statement1: StatementParseTree, statement2: StatementParseTree) -> None:
        self.statement1 = statement1
        self.statement2 = statement2
    def __str__(self) -> str:
        return f'({self.statement1} {self.statement2})'
