class MyQueue:

    def __init__(self):
        # Initialize two stacks
        self.stack1 = []  # stack to hold the incoming elements
        self.stack2 = []  # stack to hold the elements in correct order for pop/peek

    def push(self, x: int) -> None:
        # Push element x onto stack1
        self.stack1.append(x)

    def pop(self) -> int:
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Pop the element from stack2 (the front of the queue)
        return self.stack2.pop()

    def peek(self) -> int:
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Peek the element from stack2 (the front of the queue)
        return self.stack2[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.stack1 and not self.stack2
