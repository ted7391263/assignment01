class Stack:
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


def htmlChecker(htmltagString):
    s = Stack()
    balanced = True
    index = 0
    opens = ['<html>', '<title>', '<body>', '<head>','<h1>']  # html open tags
    closers = ['</html>', '</title>', '</body>', '</head>','</h1>'] # html close tags
    while index < len(htmltagString) and balanced:
        htmlTag = htmltagString[index]
        if htmlTag in opens:
            s.push(htmlTag)
        elif htmlTag in closers:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,htmlTag):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = ['<html>','<title>','<body>','<head>','<h1>']
    closers = ['</html>','</title>','</body>','</head>','</h1>']
    return opens.index(open) == closers.index(close)

htmlCheck = ['<html>','<head>','<title>','</title>','</head>','<body>','<h1>','</h1>','</body>','</html>']
htmlChecktest = ['<html>','<head>','<title>','</title>','</head>','<body>','<h1>','</h1>','</body>']
print(htmlChecker(htmlCheck))
print(htmlChecker(htmlChecktest))

