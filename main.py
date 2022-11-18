from src.Node import Node
from src.BCalc import BCalc

elem = Node("%")
elem.left = Node(0)
elem.right = Node(0)

if __name__ == '__main__':
    calc = BCalc()
    print(calc.calculate(elem))
