#include <iostream>
#include <typeinfo>
#include <vector>
#include <queue>
#include "../../Learn C++/LinkedList.h"

using namespace std;

//////////////////////////////////////////////////////////////////
// 1. Generic comparator template
template <typename T>
struct GreaterByValue {
    bool operator()(T a, T b) const {
        return a->val > b->val;
    }
};


// 2. Comparator for this specific case
struct compare {
    bool operator()(ListNode* a, ListNode* b) {
        bool result = a->val > b->val;
        cout << a->val << " > " << b->val << "    : " << (result ? "true" : "false") << endl;
        return a->val > b->val; // min-heap
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // (X)
        // ==> comparator must be a type, not an expression
        // priority_queue<ListNode*, vector<ListNode*>, greater<ListNode->val>> minHeap; 
        
        // (O)
        // priority_queue<ListNode*, vector<ListNode*>, GreaterByValue<ListNode*>> minHeap;
        
        priority_queue<ListNode*, vector<ListNode*>, compare> minHeap;

        // Initialize the heap with the head of each list
        for (auto node : lists) {
            if (node)
                minHeap.push(node);
        }

        ListNode dummy(0);  // Dummy head
        ListNode* tail = &dummy;

        while (!minHeap.empty()) {
            ListNode* smallest = minHeap.top();
            minHeap.pop();

            tail->next = smallest;
            tail = tail->next;

            if (smallest->next) {
                cout << "push " << smallest->next->val << endl;
                minHeap.push(smallest->next);
                cout << "push end " << endl << endl;
            }
        }

        return dummy.next;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    // [
    //   1->4->5,
    //   1->3->4,
    //   2->6
    // ]
    // ==> 1->1->2->3->4->4->5->6
    ListNode* head1 = new ListNode(1);
    ListNode* head11 = new ListNode(4);
    ListNode* head12 = new ListNode(5);
    
    ListNode* head2 = new ListNode(1);
    ListNode* head21 = new ListNode(3);
    ListNode* head22 = new ListNode(4);

    ListNode* head3 = new ListNode(2);
    ListNode* head31 = new ListNode(6);


    head1->next = head11;
    head11->next = head12;
    
    head2->next = head21;
    head21->next = head22;

    head3->next = head31;

    vector<ListNode*> actual_lists = {head1, head2, head3};
    vector<ListNode*>& lists = actual_lists;

    Solution solution;
    ListNode* merged = solution.mergeKLists(lists);

    cout << "Merged list: ";
    LinkedList LinkedList;
    LinkedList.printList(merged);
    LinkedList.deleteList(merged);

    return 0;
}