# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

      dummyHead=ListNode(0) #create a newresult_listNode, you need a dummy zero for the first self.next function
      result_ListNode=dummyHead #result_ListNode link after the dummy, you need 2 pointer (one dummy for the rest break dummyHead)
      carry=0 #create a carry, default 0

#input the ListNode value
      while l1 is not None or l2 is not None or carry!=0: 
    #OR since we still need to add when the length is different
    #carry !=0 because the last number can carry (in that situation, l1, l2 both None but still have carry)
        n1=l1.val if l1 is not None else 0 #in case l1 is shorter so break earlier, None value don't have .val
        n2=l2.val if l2 is not None else 0 #in case l2 is shorter 
        sum=n1+n2+carry
        result_next_val=sum%10
        carry=sum//10
        result_ListNode.next=ListNode(result_next_val)#+result)val in the ListNode
        result_ListNode=result_ListNode.next

        l1=l1.next if l1 is not None else None
        l2=l2.next if l2 is not None else None

      #break the dummyHead
      result=dummyHead.next #result e is different than result_listnode, cuz result_listnode has its pointer and linked with dummyHead
      dummyHead.next=None #break the linkenode
      return result




"""

def inputlistnode(list):
    head=ListNode(0)
    listnode1=head #Always a head cuz LinkNode is a special node, not list or array, you need a pointer to find the value
    for i in range(0,len(list)):
      listnode1.next=ListNode(list[i])
      listnode1=listnode1.next
    result1=head.next
    head.next=None
    return result1

def checkinput(listnode):
    input=[]
    while listnode is not None:
        input.append(listnode.val)
        listnode=listnode.next
    print(f"input is {input}")
    return input



l1_list=[9,9,9,9,9,9,9]
l1=inputlistnode(l1_list)
checkinput(l1)

l2_list=[9,9,9,9]
l2=inputlistnode(l2_list)
checkinput(l2)

#############################
#Solution is not static, create an instance
s=Solution()

result_listNode=s.addTwoNumbers(l1,l2)
checkinput(result_listNode)

"""
