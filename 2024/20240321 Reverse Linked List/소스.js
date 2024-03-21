/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  currentNode = head
  count = 1
  if (currentNode === null){
      return head
  }
  
  while (currentNode && currentNode.next!== null){
  count += 1
  currentNode = currentNode.next
 }

  top = head.next
  currentNode = head.next
  target = head
  head.next = null
  i = 1
  while (i!=count){
   top = currentNode.next
   currentNode.next = target
   target = currentNode
   currentNode = top
   i += 1
  }

  return target
};