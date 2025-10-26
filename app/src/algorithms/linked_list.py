from typing import Self


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class LinkedList:
    def __init__(self, values: list[int]) -> None:
        self.root: Node | None = None
        if values:
            self._create_from_list(values)

    def _create_from_list(self, values: list[int]) -> None:
        self.root = Node(values[0])

        def _helper(vals: list[int], node: Node) -> Node | None:
            if not vals:
                return None

            node.next = Node(vals[0])
            node.next.prev = node
            node.next.next = _helper(vals[1:], node.next)

            return node.next

        _helper(values[1:], self.root)

    def __iter__(self) -> Self:
        return self

    def __next__(self):
        if not self.root:
            raise StopIteration

        value = self.root.value
        self.root = self.root.next
        return value


def get_linked_list_values(node: Node | None):
    values = []

    def _helper(node: Node):
        nonlocal values

        values.append(node.value)
        if node.next:
            _helper(node.next)

    if node:
        _helper(node)
    return values
