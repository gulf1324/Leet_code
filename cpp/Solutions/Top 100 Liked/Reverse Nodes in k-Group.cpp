#include <iostream>
#include <typeinfo>
#include <vector>
#include <queue>
#include "../../Learn C++/LinkedList.h"

using namespace std;

//////////////////////////////////////////////////////////////////
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* before = dummy;
        ListNode* after = head;
        ListNode* curr = nullptr;
        ListNode* prev = nullptr;
        ListNode* nxt = nullptr;
        
        while(true){
            
            // check if there are at least k nodes ahead to reverse
            ListNode* cursor = after;
            for(int i = 0; i < k; ++i){
                if(cursor == nullptr) {
                    return dummy->next;
                }
                cursor = cursor->next;
            }
            
            // reverse k nodes, linking them back to before (not to nullptr as normal reversal)
            curr = after;
            prev = before;
            for(int i = 0; i < k; ++i){
                nxt = curr->next;
                curr->next = prev;
                prev = curr;
                curr = nxt;
            }

            // set for next group
            after->next = curr;
            before->next = prev;    // in the first iteration only; before == dummy
            before = after;
            after = curr;
        }
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    // 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head1 = new ListNode(1);
    ListNode* head11 = new ListNode(2);
    ListNode* head12 = new ListNode(3);
    ListNode* head13 = new ListNode(4);
    ListNode* head14 = new ListNode(5);

    head1->next = head11;
    head11->next = head12;
    head12->next = head13;
    head13->next = head14;

    Solution solution;
    ListNode* merged = solution.reverseKGroup(head1, 2);
    // 2 -> 1 -> 4 -> 3 -> 5

    cout << "Reversed K-group list: ";
    LinkedList LinkedList;
    LinkedList.printList(merged);
    LinkedList.deleteList(merged);

    return 0;
}