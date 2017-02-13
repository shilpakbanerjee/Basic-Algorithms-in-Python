# Toying with linked lists

import sys, random

class singly_node:
    # node for a singly linked list

    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class singly_LinkedList(object):

    def __init__(self, root):
        self.root = root
        
    def append_list(self, new_node):
        if self.root == None:
            self.root = new_node

        temp_node = self.root
        while temp_node.next != None:
            temp_node = temp_node.next

        temp_node.next = new_node

    def delete_from_list(self, pos):
        p1 = self.root
        i = 0
        while (i < pos-1) and (p1 != None):
            p1 = p1.next
            i += 1
        if p1 == None:
            print("Cant delete: List not that long")
        else:
            p1.next = p1.next.next

    def print_list(self):
        p1 = self.root
        print(p1.key)
        while p1.next != None:
            print(p1.next.key)
            p1 = p1.next
        



if __name__=='__main__':

    input = list(map(int, sys.stdin.read().split()))
    n = input[0]
    data = input[1:]

    
    if n > 0:
        node = singly_node(data[0])
        LinkedList = singly_LinkedList(node)
        for i in range(n-1):
            node = singly_node(data[i+1])
            LinkedList.append_list(node)

    print('Linked List created!')

    LinkedList.print_list()

    print('deleting 2nd element:')
    LinkedList.delete_from_list(2)
    LinkedList.print_list()
    
    
            
        
        
