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
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy = ListNode(0, head);
        
        // 1. two pointers (actually 4 including second, npf)
        ListNode* prev = &dummy;
        ListNode* curr = head;

        while (curr && curr->next) {
            // npf - next pair first
            ListNode *second = curr->next;  
            ListNode *npf = curr->next->next;
            
            //  ex) 1 → 2
            // cout << npf << endl;
            //      ==> 1->next->next ==> nullptr
            //      ==> print nullptr
            //      ==> 0 
            
            // cout << npf->val << endl;
            //      ==> Error
            

            // 2. Set 3 pointers
            second->next = curr;
            curr->next = npf;
            prev->next = second;

            // 3. Update pointers
            prev = curr;
            curr = npf;
        }

        return dummy.next;
    }
};
//////////////////////////////////////////////////////////////////
// Not as described in the problem but simple
//   ==> simply swapping values and go on to the next pair
class Solution2 {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* cur = head;

        while (cur && cur->next) {
            std::swap(cur->val, cur->next->val);
            cur = cur->next->next;
        }
        return head;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    // 1 → 2 → 3 → 4 → 5
    ListNode* head = new ListNode(1);
    ListNode* node2 = new ListNode(2);
    ListNode* node3 = new ListNode(3);
    ListNode* node4 = new ListNode(4);

    head->next = node2;
    node2->next = node3;
    node3->next = node4;

    Solution solution;
    LinkedList linkedList;
    ListNode* node = solution.swapPairs(head);

    cout << "result Linked List: ";
    linkedList.printList(node);

    return 0;
}