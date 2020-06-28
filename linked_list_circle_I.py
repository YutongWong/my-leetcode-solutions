#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
        
    def hasCycle1(self, head: ListNode) -> bool:
        seen = []
        cur = head
        while cur:
            print(cur.val)
            if cur in seen:
                return True
            seen.append(cur)
            cur = cur.next
        return False
    
    def hasCycle2(self, head: ListNode) -> bool:
        if not head:
            return False
        slow_pt = head
        fast_pt = head
        while fast_pt.next and fast_pt.next.next:
            slow_pt = slow_pt.next
            fast_pt = fast_pt.next.next
            if slow_pt == fast_pt:
                return True
        return False