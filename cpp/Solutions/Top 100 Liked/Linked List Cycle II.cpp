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

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head;
        ListNode *fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow==fast) break;
        }

        if (!fast || !fast->next) return nullptr;

        fast = head;
        while (fast != slow) {
            fast = fast->next;
            slow = slow->next;
        }
        
        return slow;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    // 3 → 2 → 0 → 4 --┐
    //      ↑----------┘
    ListNode* head = new ListNode(3);
    ListNode* node2 = new ListNode(2);
    ListNode* node0 = new ListNode(0);
    ListNode* node4 = new ListNode(4);

    head->next = node2;
    node2->next = node0;
    node0->next = node4;
    node4->next = node2;

    Solution solution;
    ListNode* node = solution.detectCycle(head);

    cout << "Tail connects to node " << node->val << endl;

    return 0;
}