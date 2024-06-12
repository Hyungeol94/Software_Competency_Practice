# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1

        head = None
        if list1.val <= list2.val:
            head = list1
        else:
            head = list2
    
        pointer1 = list1
        pointer2 = list2

        while pointer1 != None and pointer2 != None:
            #이 swap을 통해 pointer1.val <= pointer2.val이 보장됨
            if pointer2.val < pointer1.val:
                temp = pointer1
                pointer1 = pointer2
                pointer2 = temp
        
            temp1 = pointer1.next
            temp2 = pointer2.next

            if pointer1.next == None: 
                pointer1.next = pointer2
                pointer1 = None
                continue   

            #pointer2가 pointer1의 두 원소 사이에 들어갈 수 있는 경우
            #pointer1의 두 원소 사이에 들어갈 수 있는 모든 pointer2의 끝 인덱스까지 가야함

            if pointer2.val <= pointer1.next.val:    
                pointer1.next = pointer2
                while pointer2.next and pointer2.next.val <= temp1.val:
                    pointer2 = pointer2.next
                    temp2 = temp2.next
                pointer2.next = temp1

                #pointer를 한칸씩 당기기
                pointer1 = temp1
                pointer2 = temp2
            
            else:
                pointer1 = pointer1.next
            
        return head