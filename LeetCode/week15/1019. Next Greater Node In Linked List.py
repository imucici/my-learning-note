class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        temp = head
        l = []
        #transver linked list values to a list -> l
        while temp :
            l.append(temp.val)
            temp = temp.next
        # Take an empty stack
        stack = []
        #Take a res with all zeros
        res = [0]*len(l)
        
        #Traverse from reverse of list
        for i in range(len(l)-1, -1, -1):
            if len(stack)!=0:
                #Check until the top of stack is less than current item
                while len(stack)!=0 and stack[-1]<=l[i]:
                    stack.pop()
            
            #If the current item is not greater than top of stack, then its next greater is current Top of stack
            if len(stack)!=0:
                res[i] = stack[-1]
                
            #Finally append current item for future element checking
            stack.append(l[i])
            
        del stack
        return res
