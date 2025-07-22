#include <iostream>
#include <typeinfo>
#include <vector>
#include "../../Learn C++/LinkedList.h"

using namespace std;
// ## defined in header file ##
//  * Definition for singly-linked list.
// struct ListNode {
//     int val;
//     ListNode* next;

//     // constructor ==> struct/class 이름과 동일해야 하며, 반환 타입을 지정하지 않음.
//     // initializer list ==> 멤버 변수를 객체가 생성되자마자 초기화하는 데 사용됨.
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode* next) : val(x), next(next) {}
// };
//////////////////////////////////////////////////////////////////
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0, head);
        ListNode *res = &dummy;

        // 1. Place n ahead beforehand
        for (int i=0; i<n; ++i) {
            head = head->next;
        }
        // cout << head->val << endl; ==> 3

        // 2. move two pointers parallel
        // → Finds the (n-1)th node from the end (nth node should be removed)
        while (head) {
            head = head->next;
            res = res->next;
        }
        // cout << res->val << endl; ==> 3
        
        // 3. (n-1)th node → (n+1)th node.
        res->next = res->next->next;
    
    return dummy.next;
    };
};
//////////////////////////////////////////////////////////////////
int main() {
    // 1 → 2 → 3 → 4 → 5
    // 1 → 2 → 3 → → → 5
    ListNode* head = new ListNode(1);
    ListNode* node2 = new ListNode(2);
    ListNode* node3 = new ListNode(3);
    ListNode* node4 = new ListNode(4);
    ListNode* node5 = new ListNode(5);

    head->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;

    Solution solution;
    LinkedList linkedList;
    ListNode* node = solution.removeNthFromEnd(head, 2);

    cout << "result Linked List: ";
    linkedList.printList(node);

    return 0;
}