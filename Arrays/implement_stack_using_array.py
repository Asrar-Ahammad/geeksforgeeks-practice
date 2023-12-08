class MyStack:
    def __init__(self):
        self.arr = []

    # Function to push an integer into the stack.
    def push(self, data):
        # add code here
        return self.arr.append(data)

    # Function to remove an item from top of the stack.
    def pop(self):
        # add code here
        return self.arr.pop()

    def display(self):
        print(self.arr)


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
stack.display()
