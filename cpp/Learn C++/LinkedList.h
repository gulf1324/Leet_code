#ifndef LINKED_LIST
#define LINKED_LIST
#include <iostream>

struct ListNode {
    int val;
    ListNode* next;

    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class LinkedList {
public:
static
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
    
    void printList(ListNode* head) {
        while (head != nullptr) {
            std::cout << head->val;
            if (head->next) std::cout << " -> ";
            head = head->next;
        }
        std::cout << std::endl;
    }

    // 리스트 메모리 해제 함수
    void deleteList(ListNode* head) {
        while (head != nullptr) {
            ListNode* temp = head;
            head = head->next;
            delete temp;
        }
    }


};

#endif