class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(start):
    first = None
    prev = None
    while start:
        first = start
        start = start.next
        first.next = prev
        prev = first
    return first

def insert(start, n):
    q = Node(n)

    p = start
    prev = None

    while p != None:
        prev = p
        p = p.next

    if prev == None:
        return q

    prev.next = q
    return start


def printall(start):
    while start != None:
        print(start.value,end=" ")
        start = start.next
    print("")

z1=insert(None,2)
z1=insert(z1,3)
z1=insert(z1,4)
z1=insert(z1,5)
z1=insert(z1,6)

printall(z1)
z1 = reverse(z1)
printall(z1)

