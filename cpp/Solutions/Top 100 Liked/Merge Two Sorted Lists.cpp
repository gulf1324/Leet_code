#include <iostream>
#include <typeinfo>
#include <vector>

using namespace std;

//  * Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;

    // constructor ==> struct/class 이름과 동일해야 하며, 반환 타입을 지정하지 않음.
    // initializer list ==> 멤버 변수를 객체가 생성되자마자 초기화하는 데 사용됨.
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy; //dummy 라는 객체 생성
        ListNode* tail = &dummy; //tail ==> dummy객체 주소를 가리키는 pointer

        while (list1 != nullptr && list2 != nullptr) {
            // object.member ==> access to object's member directly.
            // pointer->member ==> access to object's member via pointer.
            if (list1->val < list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }

        // 남은 리스트 중 하나를 연결
        if (list1 != nullptr) {
            tail->next = list1;
        } else {
            tail->next = list2;
        }

        // dummy의 다음이 실제 head
        return dummy.next;
    }
};
//////////////////////////////////////////////////////////////////
void printList(ListNode* head) {
    while (head != nullptr) {
        cout << head->val;
        if (head->next) cout << " -> ";
        head = head->next;
    }
    cout << endl;
}

// 리스트 메모리 해제 함수
void deleteList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

int main() {
    // 1 -> 3 -> 5
    ListNode* list1 = new ListNode(1, new ListNode(3, new ListNode(5)));

    // 2 -> 4 -> 6
    ListNode* list2 = new ListNode(2, new ListNode(4, new ListNode(6)));

    Solution solution;
    ListNode* merged = solution.mergeTwoLists(list1, list2);

    cout << "Merged list: ";
    printList(merged);
    deleteList(merged);

    return 0;
}