# -*- encoding: utf-8 -*-
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._list = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._list.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        re = self._list[0]
        self._list = self._list[1::]
        return re

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._list[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self._list) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    obj = MyQueue()
    print(obj.empty())
