#include <iostream>
#include <typeinfo>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        vector<int> inDegree(numCourses, 0);
        
        // 2. 그래프와 진입 차수 초기화
        for (const auto& pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]); 
            inDegree[pre[0]]++; 
        }
        // graph = {{1},{2},{3}}
        // inDegree = {0, 1, 1, 1}

        
        // 3. 진입 차수가 0인(선행 과목이 없는) 코스를 큐에 추가
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                q.push(i);
            }
        }
        // q = {0}
        
        // 4. BFS로 위상 정렬 수행
        int count = 0; // 처리한 코스 수
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            count++; // 코스 하나 처리
            
            // 현재 코스의 후속 코스들 처리
            for (int next : graph[curr]) {
                inDegree[next]--; // 진입 차수 감소
                if (inDegree[next] == 0) {
                    q.push(next); // 진입 차수가 0이 되면 큐에 추가
                }
            }
        }
        
        // 5. 모든 코스를 처리했는지 확인
        return count == numCourses;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;

    int numCourses = 4;
    vector<vector<int>> prerequisites = {{1, 0}, {2, 1}, {3, 2}};
    // 0 → 1 → 2 → 3
    // true
    
    bool result = solution.canFinish(numCourses, prerequisites);

    cout << result << endl;

    return 0;
}