class Element:
    def __init__(self, elem_id, value, below):
        self.id = elem_id
        self.value = value
        self.below = below


class Stack:
    def __init__(self):
        self.content = []
        # points to the top element. Position starts from 0 (bottom)
        self.pointer = 0
        # points to an element while iterating
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index == -1 * self.size():
            raise StopIteration
        return self.content[self.index].value

    # returns True if Stack has no elements; False if there is one or more elements
    def is_empty_stack(self):
        return self.pointer == 0

    # adds new element with 'value' to the top of Stack. Returns nothing
    def push(self, value):
        new_element = Element(self.pointer + 1, value, self.pointer)
        self.content.append(new_element)
        self.pointer = new_element.id
        return None

    # deletes the top element. Returns this element
    def pop(self):
        if self.pointer == 0:
            return 'The stack is empty'
        else:
            on_top = self.content[-1]
            self.pointer = on_top.below
            self.content.pop()
            return on_top.value

    # returns the upper element without changing the stack
    def peek(self):
        return self.content[-1].value

    # returns number of elements in Stack
    def size(self):
        return self.content[-1].id
