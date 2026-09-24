# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        returnPointer = l1
        head = l1
        carry = None

        while l1 is not None or l2 is not None:
            if l1 and l2:
                vals = l1.val + l2.val
                if carry:
                    vals += carry
                    carry = None

                if vals // 10 == 0:
                    returnPointer.val = vals
                    carry = None
                else:
                    returnPointer.val = vals % 10
                    carry = 1
                if l1.next is not None:
                    if l2.next is not None:
                        returnPointer = returnPointer.next
                        l2 = l2.next
                    else:
                        l2 = None
                    l1 = l1.next
                else:
                    l1 = None
                    l2 = l2.next
            # Base case taken care of 
            # here, we need to move both l1 forward, l2 forward, returnPointer forward
            # so in essence returnPointer actually corresponds to the current Node.
            # However, what happens when one of the branches dies? Say l1?
                # Then returnPointer needs to sit at the last viable node
            # So returnPointer only moves foward when both nodes move forward.
            # otherwise it only moves forward after appending a new node 
            else:
                if l1:
                    if carry is None:
                        returnPointer.next = l1
                        break
                    else:
                        if l1.val == 9:
                            l1.val = 0
                            returnPointer = l1
                            l1 = l1.next
                        else:
                            l1.val += 1
                            returnPointer.next = l1
                            carry = None
                            break
                else:
                    if carry is None:
                        returnPointer.next = l2
                        break
                    else:
                        if l2.val == 9:
                            l2.val = 0
                            returnPointer.next = l2
                            returnPointer = l2
                            l2 = l2.next
                        else:
                            l2.val += 1
                            returnPointer.next = l2
                            carry = None
                            break
        if carry is not None:
            returnPointer.next = ListNode(1)              

        return head

# Consider a few cases

    # Both pointers exist
        # No carry
            # Add the values. Mod by 10. If not 0, insert the remainder by dividing by 10
            # and set carry to 1
        # Carry
            # Same thing. Add the values Carry logic
        # If there is no carry, set carry to None (will be useful later)
    # If only one pointer exists
        # Then you can't just append the rest. You still need to iterate over the thing
            # That is, until carry == None
            # Otherwise propogate the carry
        # Note that if we break out of the while loop, we need 
        # to append a new Node if carry is not None