class Node:
    """
    Base class for all DAOS nodes.
    Every node should implement the run() method.
    """
    def __init__(self, name):
        self.name = name

    def run(self, **kwargs):
        raise NotImplementedError("Each node must implement run()")

"""
"""