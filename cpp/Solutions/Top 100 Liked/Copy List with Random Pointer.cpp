#include <iostream>
#include <typeinfo>
#include <vector>
#include <unordered_map>
using namespace std;


// 노드 클래스 정의: 값, next 포인터, random 포인터를 포함
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};
////////////////////////////////////////////////////////////////////////////////////////////////////////
class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*>nodeMap;
        // Key: Node* (원본 리스트의 노드를 가리키는 포인터)
        // Value: Node* (복사된 리스트의 노드를 가리키는 포인터)
        Node* curr = head;
        
        // copy all Nodes(pointer) with mapping
        while(curr){
            nodeMap[curr] = new Node(curr->val); // new ==> returns pointer
            curr = curr->next;
        }

        curr = head;
        while(curr){
            Node* newHead = nodeMap[curr];
            if(curr->next){
                newHead->next = nodeMap[curr->next];
            }
            if(curr->random){
                newHead->random = nodeMap[curr->random];
            }
            curr = curr->next;
        }
        return nodeMap[head];
    }
};
////////////////////////////////////////////////////////////////////////////////////////////////////////
// 연결 리스트를 출력하는 함수 (디버깅용)
void printList(Node* head) {
    Node* curr = head;
    while (curr) {
        std::cout << "Node val: " << curr->val;
        if (curr->random) {
            std::cout << ", random points to: " << curr->random->val;
        } else {
            std::cout << ", random points to: null";
        }
        std::cout << std::endl;
        curr = curr->next;
    }
}
Node* createList(const std::vector<std::vector<int>>& input) {
    if (input.empty()) return nullptr;
    
    // 노드 생성
    std::vector<Node*> nodes;
    for (const auto& node : input) {
        nodes.push_back(new Node(node[0]));
    }
    
    // next와 random 포인터 설정
    for (size_t i = 0; i < input.size(); ++i) {
        if (i < input.size() - 1) {
            nodes[i]->next = nodes[i + 1];
        }
        if (input[i][1] != -1) { // -1은 null을 의미
            nodes[i]->random = nodes[input[i][1]];
        }
    }
    
    return nodes[0];
}
////////////////////////////////////////////////////////////////////////////////////////////////////////
int main() {
    // ex): [[7,null],[13,0],[11,4],[10,2],[1,0]]
    std::vector<std::vector<int>> input = {{7, -1}, {13, 0}, {11, 4}, {10, 2}, {1, 0}};
    
    Node* head = createList(input);
    std::cout << "Original List:" << std::endl;
    printList(head);
    
    // 복사된 리스트 출력
    Solution solution;
    Node* copiedHead = solution.copyRandomList(head);
    std::cout << "\nCopied List:" << std::endl;
    printList(copiedHead);

    Node* curr = head;
    while (curr) {
        Node* temp = curr;
        curr = curr->next;
        delete temp;
    }
    
    curr = copiedHead;
    while (curr) {
        Node* temp = curr;
        curr = curr->next;
        delete temp;
    }
    
    return 0;
}