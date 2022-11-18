
class Node:
    """
        Basic implementation of binary tree
    """
    def __init__(self, data):
        """"
            Constructor
            Keyword arguments:
            data -- is the data that you want to store in the Node
        """
        self._data = data
        self._left = None
        self._right = None

    @property
    def data(self):
        """"
            getter
        """
        return self._data

    @data.setter
    def data(self, data):
        """"
            setter
            Keyword arguments:
            data -- is the data that you want to store in the Node
        """
        self._data = data

    @property
    def left(self):
        """"
            getter
        """
        return self._left

    @left.setter
    def left(self, element):
        """"
            setter
            Keyword arguments:
            element -- it's expects to store another Node of binary tree
        """
        self._left = element

    @property
    def right(self):
        """"
            getter
        """
        return self._right

    @right.setter
    def right(self, element):
        """"
            setter
            Keyword arguments:
            element -- it's expects to store another Node of binary tree
        """
        self._right = element

    def __str__(self):
        """
            representation of the data that stores a Node
        """
        return f'{self._data}'

    def __repr__(self):
        """
            all the data that stores a Binary Tree
        """
        return f'{self.data}, {self.left}, {self.right}'
