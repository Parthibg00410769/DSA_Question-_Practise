#Reverse Linked List (leetcode 206)
#YouTube link: https://www.youtube.com/watch?v=G0_I-ZF0S38&list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB&index=2

#checkout the notes of two methods below in the OneNote
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

    def reverseListIterative(self, head):
        prev, curr = None, head

        while curr is not None:
            nxt = curr.ref
            curr.ref = prev
            prev = curr
            curr = nxt

        return prev
    def reverseLRecursive(self, head):
        if head is None:
            return None
        newHead = head
        if head.ref is not None:
            newHead = self.reverseLRecursive(head.ref)
            head.ref.ref = head

        head.ref = None
        return newHead


ll1 = Solution()
ll1.append(12)
ll1.append(66)
ll1.append(64)
ll1.printLL()
reversed_head = ll1.reverseLRecursive(ll1.head)
ll1.head = reversed_head  # Update the head to the reversed list's head
ll1.printLL()