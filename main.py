class Stack:
    # верхний элемент стека расположен в конце списка
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def is_balanced(text, brackets="<>()[]{}"):
    opening, closing = brackets[::2], brackets[1::2]
    stack = []
    for character in text:
        if character in opening:
            stack.append(opening.index(character))
        elif character in closing:
            if stack and stack[-1] == closing.index(character):
                stack.pop()
            else:
                return 'Не сбалансировано'
    return 'Сбалансировано'
