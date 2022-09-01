from task_1 import Stack

brackets = {
    '(': ')',
    '{': '}',
    '[': ']'
}


def is_balanced(string: str):
    if string[0] in brackets.values() or string[-1] in brackets.keys():
        return 'Imbalanced'
    else:
        tmp_stack = Stack()
        for char in string:
            if char in brackets.values() and tmp_stack.is_empty_stack():
                return 'Imbalanced'
            elif char in brackets.keys():
                tmp_stack.push(char)
            elif char == brackets[tmp_stack.peek()]:
                tmp_stack.pop()
            else:
                return 'Imbalanced'
        if tmp_stack.is_empty_stack():
            return 'Balanced'
        else:
            return 'Imbalanced'
