#!/usr/bin/python3
"""Creating singly linked list in python"""


class Node:
    """class Node, nodes of sigly linked list

    Attributes:
        __data (int): value stored in node
        __next_node (Node): pointer to next node
    """
    def __init__(self, data, next_node=None):
        """Initialize node

        Args:
            data (int): value in node
            next_node (Node): point ti next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data field

        setter validates type before assignment
        must be int type
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for next node field

        setter validates node before assignment
        and raises error accordingly
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """class List, create list

    Attributes:
        __head (Node): start of list
    """

    def __init__(self):
        """Initialize list"""
        self.__head = None

    def __str__(self):
        """yield each node value for printing"""
        tmp = self.__head
        val = 0
        if tmp is None:
            return ""

        new = ''
        while tmp is not None:
            val = tmp.data
            tmp = tmp.next_node
            new += "{:d}{}".format(val, '\n' if tmp else '')
        return new

    def sorted_insert(self, value):
        """insert into list in order

        Args:
            value (Node): node to insert
        """
        new = Node(value)
        tmp = self.__head
        if self.__head is None:
            self.__head = new
        elif tmp.data > value:
            new.next_node = tmp
            self.__head = new
        else:
            while tmp.next_node is not None:
                if tmp.next_node.data > value:
                    new.next_node = tmp.next_node
                    tmp.next_node = new
                    return
                tmp = tmp.next_node
            tmp.next_node = new
