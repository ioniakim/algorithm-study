#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <limits>
#include <algorithm>

using namespace std;

struct Node {
    int parent;
    int distFromRoot;
    std::vector<int> edges;
    std::vector<int> edgeDists;

    Node()
     : parent(-1)
     , distFromRoot(0)
     , edges()
     , edgeDists(){
    }
};

int solve(std::vector<Node>& tree){

    stack<int> nodeStack;

    int root = tree.size() - 1;
    nodeStack.push(root);

    int maxDist = numeric_limits<int>::min();
    while(!nodeStack.empty()){
        int nodeIndex = nodeStack.top();
        nodeStack.pop();
        Node &node = tree[nodeIndex];

        if (node.edges.size() == 1){
            maxDist = max(maxDist, node.distFromRoot);
        }

        for (int i = 0 ; i < node.edges.size(); ++i){
            int neighborIndex = node.edges[i];
            if (node.parent == neighborIndex){
                continue;
            }

            Node &neighbor = tree[neighborIndex];
            neighbor.parent = nodeIndex;
            neighbor.distFromRoot = node.edgeDists[i] + node.distFromRoot;
            nodeStack.push(neighborIndex);
        }

    }

    return maxDist;
}

int main(){

    freopen("firework.dat", "r", stdin);

    int T;
    cin >> T;

    for(int t = 1 ; t <= T ; ++t){
        int n;
        cin >> n;
        std::vector<Node> tree(2*n);
        for (int i = 0 ; i < 2*n-1 ; ++i){
            int a, b, c;
            cin >> a >> b >> c;
            --a, --b;
            tree[a].edges.push_back(b);
            tree[a].edgeDists.push_back(c);
            tree[b].edges.push_back(a);
            tree[b].edgeDists.push_back(c);
        }

        cout << "#" << t << ' ' << solve(tree) << endl;
    }
}