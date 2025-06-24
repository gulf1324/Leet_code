#include <iostream>
#include <typeinfo>
#include <vector>
#include "../../Learn C++/LinkedList.h"

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (!head || !head->next){
            return head;
        }

        // find the middle 
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // split 
        ListNode* secondHalf = slow->next;
        slow->next = nullptr;

        // recursively sort both halves
        ListNode* left = sortList(head);
        ListNode* right = sortList(secondHalf);

        // merge 
        return LinkedList::mergeTwoLists(left, right);

    }
};
//////////////////////////////////////////////////////////////////
// not solved as intended
#include <algorithm>
class Solution2 {
public:
    ListNode* sortList(ListNode* head) {
        std::vector<int> v;
        ListNode* temp = head;

        // append all node's value to a vector
        while(temp!= nullptr){
            v.push_back(temp->val);
            temp = temp->next;
        }

        //sort
        sort(v.begin(), v.end());
        
        // make a linked list again
        temp = head;
        for(int& item : v){
            temp->val = item;
            temp = temp->next;
        }
        return head;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    // -1, 5, 3, 4, 0
    ListNode* list1 = new ListNode(-1, new ListNode(5, new ListNode(3, new ListNode(4, new ListNode(0)))));
    Solution solution;
    ListNode* sorted = solution.sortList(list1);

    std::cout << "Sorted list: ";
    LinkedList LinkedList;
    LinkedList.printList(sorted);
    // >>> -1 -> 0 -> 3 -> 4 -> 5
    LinkedList.deleteList(sorted);

    return 0;
}