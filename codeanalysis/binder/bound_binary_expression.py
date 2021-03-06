from .bound_expression import BoundExpression
from .bound_node_kind import BoundNodeKind


class BoundBinaryExpression(BoundExpression):

    def __init__(self, left, operator, right):
        super().__init__(BoundNodeKind.BINARY_EXPRESSION)
        self.left = left
        self.operator = operator
        self.right = right
        self.type = operator.result_type
