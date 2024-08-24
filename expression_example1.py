from parse_tree import VariableParseTree, NumberParseTree, AssignmentParseTree, MultiplicationParseTree, SequentialCompositionParseTree

x = VariableParseTree('x')
two = NumberParseTree(2)
assignment1 = AssignmentParseTree(x, two)
expression1 = MultiplicationParseTree(x, x)
assignment2 = AssignmentParseTree(x, expression1)
program1 = SequentialCompositionParseTree(assignment1, assignment2)

print(program1)
