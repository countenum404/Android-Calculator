from src.Node import Node


class BCalc:
    def __init__(self):
        self.operations = ['+', '-', '*', '/', '%']

    def calculate(self, head: Node):
        """
            Keyword arguments:
            head -- Node from Node.py which is previously were filled by parser
            :returns a calculated result
        """
        if head.left.data in self.operations:
            head.left.data = self.calculate(head.left)
        if head.right.data in self.operations:
            head.right.data = self.calculate(head.right)
        return self._opp(head.left.data, head.data, head.right.data)

    def _opp(self, left, operation, right) -> float:
        """
        simplest operations supported by BCalc
        :returns a result of basic equation
        """
        if operation == '+':
            return left + right
        elif operation == '-':
            return left - right
        elif operation == '*':
            return left * right
        elif operation == '/':
            try:
                return left / right
            except ZeroDivisionError:
                return 0
        elif operation == '%':
            try:
                return left % right
            except ZeroDivisionError:
                return 0
