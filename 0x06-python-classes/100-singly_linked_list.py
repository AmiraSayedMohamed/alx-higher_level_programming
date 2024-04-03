#!/usr/bin/python3
"""Defines the classes Node and SinglyLinkedList"""


class Node:
    """
    Class that defines properties Node.

    Attributes:
        data: data field of node.
    """
    def __init__(self, data, next_node=None):
        """Creates new instances of node.

        Args:
            __data : data field of node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data field instance.

        Returns: the data field of a node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Propery setter for data.

        Args:
            value (int): data field of a node.

        Raises:

