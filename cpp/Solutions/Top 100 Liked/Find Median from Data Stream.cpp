#include <iostream>
#include <typeinfo>
#include <vector>
#include <queue>
using namespace std;

/**
 * std::priority_queue<Type, Container, Comparator>
 */
class MedianFinder {
private:
    // Max heap - top() is the largest
    priority_queue<int> lowHalf;
    //default
    // ==> priority_queue<int, vector<int>, less<int>>

    // Min heap - top() is the smallest
    priority_queue<int, vector<int>, greater<int>> highHalf; 
public:
    MedianFinder() {}
    
    void addNum(int num) {
        if (lowHalf.empty() || num <= lowHalf.top()) {
            lowHalf.push(num);  // goes to max-heap
        } else {
            highHalf.push(num); // goes to min-heap
        }

        // Balance the heaps: max difference in size = 1
        if (lowHalf.size() > highHalf.size() + 1) {
            highHalf.push(lowHalf.top());
            lowHalf.pop();
        } else if (highHalf.size() > lowHalf.size()) {
            lowHalf.push(highHalf.top());
            highHalf.pop();
        }
    }
    
    double findMedian() {
        if (lowHalf.size() == highHalf.size()) {
            return (lowHalf.top() + highHalf.top()) / 2.0;
        } else {
            return lowHalf.top();  // max-heap has more elements
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
//////////////////////////////////////////////////////////////////
int main() {
    MedianFinder* solution = new MedianFinder();
    solution->addNum(1);
    solution->addNum(2);
    double result = solution->findMedian();
    cout << result << endl; // 1.5
    solution->addNum(3);
    double result2 = solution->findMedian();
    cout << result2 << endl; // 2

    delete solution;

    return 0;
}


/**
Stack
void foo() {
    MedianFinder mf;
    mf.addNum(1);
    cout << mf.findMedian() << endl;  // fine
} // mf is destroyed here

Heap
void foo() {
    MedianFinder* mf = new MedianFinder();
    mf->addNum(1);
    cout << mf->findMedian() << endl;
    delete mf; // must clean up
}
*/