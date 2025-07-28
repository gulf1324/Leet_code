#include <iostream>
#include <typeinfo>
#include "../../Learn C++/LinkedList.h"
#include <unordered_map>
#include <list>
using namespace std;

// list 
// splice
// (int)cache.size()

class LRUCache {
private:
    int cap;
    // (key, value)를 저장, front가 가장 최근, back이 가장 오래된 것
    list<pair<int, int>> cache;
    
    // key -> list iterator
    unordered_map<int, list<pair<int, int>>::iterator> pos;

public:
    LRUCache(int capacity) : cap(capacity) {}

    // returns value(if exists) and move it to 'most recent'
    int get(int key) {
        
        // unordered_map.find() ==> iterator 반환
        //      iterator->first ==> key
        //      iterator->second ==> value
        
        // == unordered_map<int, list<pair<int, int>>::iterator>::iterator it = pos.find(key);
        auto it = pos.find(key);
        if (it == pos.end()) return -1;

        // 해당 노드를 가장 최근(front)으로 옮김
        // splice(목적지, source list, 옮길 원소(iterator))
        cache.splice(cache.begin(), cache, it->second);
        //      it->first 타입 (항상 const) == const int
        //      it->second 타입 == list<pair<int, int>>::iterator
        
        return it->second->second; // value
    }

    void put(int key, int value) {
        auto it = pos.find(key);

        // 존재하는 key 라면 value 갱신 후 front로 이동
        if (it != pos.end()) {
            it->second->second = value;
            cache.splice(cache.begin(), cache, it->second);
            return;
        }

        // 용량이 다 찼다면 back 제거
        if ((int)cache.size() == cap) {
            int k = cache.back().first;
            pos.erase(k);
            cache.pop_back();
        }

        // 새로운 key라면 front에 삽입
        cache.emplace_front(key, value);
        pos[key] = cache.begin();
    }

};
//////////////////////////////////////////////////////////////////
int main() {
    int capacity = 2;
    LRUCache* obj = new LRUCache(capacity);
    obj->put(1, 1);
    obj->put(2, 2);
    
    int result = obj->get(1); // 1
    cout << "get value: " << result << endl;
    
    obj->put(3, 3);
    
    result = obj->get(2); // -1
    cout << "get value: " << result << endl;
    
    obj->put(4, 4);
    
    result = obj->get(1); // -1
    cout << "get value: " << result << endl;
    result = obj->get(3); // 3
    cout << "get value: " << result << endl;
    result = obj->get(4); // 4
    cout << "get value: " << result << endl;


    return 0;
}