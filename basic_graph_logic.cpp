#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <list>

using namespace std;

template<typename T>
void walk(const map<T, set<T>> &graph, T s, map<T, T> &pred )
{
    queue<T> q;

    pred[s] = -1;
    q.push(s);

    while (!q.empty()){
        T u = q.back();
        q.pop();

        for (const auto& s : graph.at(u)){
            for (const auto&  v : s){
                if (pred.count(v) > 0) continue;
                q.push(v);
                pred[v] = u;
            }
        }
    }
}

template<typename T>
void component(const map<T, set<T>> &graph, list<map<T, T>> &comp)
{
    set<T> seen;

    for(auto& v : graph){
        if (seen.count(v.first) > 0) continue;

        map<T, T> c;
        walk(graph, v.first, c);
        comp.push_back(c);
        for (auto &u : c){
            seen.insert(u.first);
        }
    }
}
int main(int argc, char const *argv[])
{
    // map initialization
    map<char, set<char>> graph = {{'a', {'b', 'c'}}, {'b', {'a', 'c'}}, {'c', {'a', 'b'}}, {'d', {}}, {'e', {'g', 'h'}}, {'f', {}}, {'g', {'e', 'f'}}, {'h', {'e'}}};

    list<map<char, char>> comp;
    component(graph, comp);

    // cout << comp << endl;
    return 0;
}
