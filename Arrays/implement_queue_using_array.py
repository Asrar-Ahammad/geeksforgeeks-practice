from collections import deque
class MyQueue:
    def __init__(self):
        self.queue = deque()

    # Function to push an element x in a queue.
    def push(self, x):
        self.queue.append(x)

    # Function to pop an element from queue and return that element.
    def pop(self):
        if not self.queue:
            return -1
        return self.queue.popleft()
    def display(self):
       print(self.queue)

queue = MyQueue()

queue.push(3)
queue.push(4)
queue.push(5)

queue.pop()

queue.display()

