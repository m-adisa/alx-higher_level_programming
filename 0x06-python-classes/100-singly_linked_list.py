#!/usr/bin/python3
"""Defines classes for a linked list"""


class Node:
    """Represents a node in a linked list"""
    def __init__(self, data, next_node=None):
        """Initialize the node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data from the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets data into the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves from the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node Objext")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list"""

    def __init__(self):
        """Initialize a new Singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node in a sorted linked list"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__node
            self.__node = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_done.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines the print() representation of the linked list"""
        myval = ""
        node = self.__head
        while node:
            myval += str(node.data)
            myval += '\n'
            node = node.next_node
        return myval[:-1]
