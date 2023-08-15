#remove linked list element

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Solution:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def printLL(self):
        if self.head is None:
            print("Linked list is not available!!")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.ref
            print()
    def removeElements(self, head:Node, val: int):
        dummy = Node(0)
        dummy.ref = head
        prev, curr = dummy, head

        while curr:
            nxt = curr.ref

            if curr.data == val:
                prev.ref = nxt
            else:
                prev = curr

            curr = nxt

        return dummy.ref

ll1 = Solution()
ll1.append(12)
ll1.append(66)
ll1.append(64)
ll1.append(66)
ll1.append(12)
ll1.append(15)
ll1.append(12)
ll1.printLL()
new_head = ll1.removeElements(ll1.head, 12)  # Corrected function call
ll1.head = new_head
ll1.printLL()