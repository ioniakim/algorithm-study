#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#

def walk(G, s, S=set()):
    '''Walking through a connected component of a graph represented using adjacency sets
    G: graph, s: start node, S: why needed?
    => P is return value. But it is hard to get the traveral path from s.
    '''
    P = dict()      # Predecessor
    Q = set()       # Queue => using set as Queue
    P[s] = None
    Q.add(s)

    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v] = u

    return P

def components(G):
    '''Return connected components
    '''
    comp = []
    seen = set()
    for u in G:
        if u in seen: continue

        c = walk(G, u)
        comp.append(c)
        seen.update(c)

    return comp


def main():
    ''' Code test
    '''
    G = {'a': set('bc'), 'b':set('ac'), 'c':set('ab'), 'd':set(), 'e':set('gh'), 'f':set('g'), 'g':set('ef'), 'h':set('e')}

    print(components(G))

if __name__ == '__main__':
    main()