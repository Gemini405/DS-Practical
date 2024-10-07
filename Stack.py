def createStack():
    stack = []
    return stack

def checkEmpty(stack):
    return (len(stack) == 0)

def push(stack, item):
    stack.append(item)
    print("pushed item:" + item)

def pop(stack):
    if (checkEmpty(stack)):
        return "stack is empty"
    return stack.pop()

stack = createStack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))

print("\npopped item: " + pop(stack))
print("stack after popping an element: " + str(stack))
