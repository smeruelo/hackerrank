# Problem: Delete Middle Node
# Implement an algorithm to delete a node in the middle (i.e., any node but the
# first and last node, not necessarily the exact middle) of a singly linked
# list, given only access to that node.
# EXAMPLE
# lnput:the node c from the linked lista->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

from mutable_singly_linked_list import MSinglyLinkedList


# O(n)
def delete_middle_node(lst, node):
    # node exists and it's not either the 1st one or the last one
    current_node = lst.head
    while current_node.nxt != node:
        current_node = current_node.nxt
    current_node.nxt = current_node.nxt.nxt

    return lst

def nth_node(lst, n):
    if n <= 0 or n >= lst.length() - 1:
        raise Exception('Not a valid middle index')

    count = 0
    current_node = lst.head
    while count < n:
        count += 1
        current_node = current_node.nxt

    return current_node


if __name__ == '__main__':
    l = MSinglyLinkedList().push(0).push(7).push(3).push(2).push(7).push(1).push(0)
    node = nth_node(l, 3)
    delete_middle_node(l, node)
    print(l)
