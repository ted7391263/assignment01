class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.getNext()

        temp = Node(item)
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

    def index(self, item):
        item = Node(item)
        current = self.head
        count = 0
        while current:
            if item.getData() == current.getData():
                return count
            current = current.getNext()
            count += 1
        return None

    def pop(self, pos=None):

        if pos is None:
            current_node = self.head
            previous_node = None
            while current_node.getNext() is not None:
                previous_node = current_node
                current_node = current_node.getNext()
            data = current_node.getData()
            previous_node.setNext(current_node.getNext())
            return data
        else:
            current_node = self.head
            previous_node = None
            current_pos = 0
            while current_pos != pos:
                previous_node = current_node
                current_node = current_node.getNext()
                current_pos = current_pos + 1
            data = current_node.getData()
            previous_node.setNext(current_node.getNext())
            return data



    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            cont = 0
            next = self.head
            while pos - 1 != cont:
                next = next.next
                cont += 1
            new_item = Node(item)
            new_item.next = next.next
            next.next = new_item
if __name__ == "__main__":
    mylist = UnorderedList()
    print(mylist.isEmpty())
    mylist.add(8957)
    mylist.add('Ted')
    mylist.add(1357)
    print(mylist.size())
    mylist.append(5555)
    print(mylist.search(5555))
    print(mylist.size())
    mylist.remove(1357)
    print(mylist.size())
    print(mylist.index(5555))
    mylist.insert(2, 44)
    print(mylist.index(44))
    mylist.pop()
    print(mylist.search(5555))
    mylist.pop(1)
    print(mylist.search(8957))


