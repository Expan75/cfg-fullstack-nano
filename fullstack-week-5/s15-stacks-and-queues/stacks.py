# STACK


class StackList:
    """
    Stack Implementation using a List
    """

    def __init__(self, size):
        self.container = [None] * size
        self.capacity = size
        self.top = -1

    def push(self, x):
        """
        Method to add an element `x` to the stack 
        """
        if self.is_full():
            print("Stack is full! Calling exit()…")
            exit(1)

        print("Inserting", x, "into the stack…")
        self.top = self.top + 1
        self.container[self.top] = x

    def pop(self):
        """
        Method to pop a top element from the stack
        """
        if self.is_empty():
            print("Stack is empty! Calling exit()…")
            exit(1)

        print("Removing", self.peek(), "from the stack")

        # decrease stack size by 1 and (optionally) return the popped element
        top = self.container[self.top]
        self.top = self.top - 1
        return top

    def peek(self):
        """
        Method to return the top element of the stack 
        """
        if self.is_empty():
            exit(1)
        return self.container[self.top]

    def size(self):
        """
        Method to return the size of the stack
        """
        return self.top + 1

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity


# SHOW EXAMPLES BELOW, then encourage students to try out different methods.
stack = StackList(3)

stack.push(1)
stack.push(2)

stack.pop()
stack.pop()

stack.push(3)

print("Top element is", stack.peek())
print("The stack size is", stack.size())

stack.pop()

if stack.is_empty():
    print("The stack is empty")
else:
    print("The stack is not empty")


#####################################################

"""
Stack implementation using deque class in Python
"""

from collections import deque

# NB: module deque alredy has useful methods, so we don't need to re-implement them
stack = deque()


stack.append('1')
stack.append('2')
stack.append('3')
stack.append('4')

print("Top element is", stack[-1])  # prints the stack's top (4)

print("Removing", stack.pop(), "from the stack")  # removing the top element (4)
print("Removing", stack.pop(), "from the stack")  # removing the next top (3)

# returns the total number of elements present in the stack
print("Stack size is", len(stack))

print("Removing", stack.pop(), "from the stack")  # removing the top element (2)
print("Removing", stack.pop(), "from the stack")  # removing the next top (1)

# check if the stack is empty
if len(stack) == 0:
    print("The stack is empty")
else:
    print("The stack is not empty")

###############################################

# QUEUE

"""
Queue Implementation using a List
"""


class MyQueue:

    def __init__(self, size):
        self.q = [None] * size  # list to store queue elements
        self.capacity = size  # maximum capacity of the queue
        self.front = 0  # front points to the front element in the queue
        self.rear = -1  # rear points to the last element in the queue
        self.count = 0  # current size of the queue

    def pop(self):
        if self.is_empty():
            print("Queue Underflow!! Terminating process.")
            exit(1)

        print("Removing element…", self.q[self.front])

        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1

    def append(self, value):
        if self.is_full():
            print("Queue is full! Terminating process.")
            exit(1)

        print("Inserting element…", value)

        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    def peek(self):
        if self.is_empty():
            print("Queue is empty!! Terminating process.")
            exit(1)

        return self.q[self.front]

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity

# RUN QUEUE

q = MyQueue(5)

q.append(1)
q.append(2)
q.append(3)

print("The queue size is", q.size())
print("The front element is", q.peek())
q.pop()
print("The front element is", q.peek())

q.pop()
q.pop()

if q.is_empty():
    print("The queue is empty")
else:
    print("The queue is not empty")


"""
Queue implementation using deque class in Python
"""

# NB: module deque alredy has useful methods, so we don't need to re-implement them
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print("The front element is", queue[0])  # 1

queue.popleft()  # removing the front element (1)
queue.popleft()  # removing the front element (2)

# Print front item of the queue
print("The front element is", queue[0])  # 3

print("The queue size is", len(queue))  # 2

# check whether the queue is empty
if len(queue) == 0:
    print("The queue is empty")
else:
    print("The queue is not empty")
