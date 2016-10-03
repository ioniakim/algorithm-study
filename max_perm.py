#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finding a Maximum Permutation
Eight persons with very particular tastes have bought tickets to movies. Some of them are happy with their seats, but most of them are not, adn after standing in line, they're getting a bit grumpy. Let's say each of them has favorite seat, and you want to fidn a way to let them switch seats to make as many people as possible happy with the result. However, because they are all rather grumpy, all of them refuse to move to another seat if they can't get their favorite.
"""

def max_perm(M):
    n = len(M)                      # How many elements?
    A = set(range(n))               # A = {0, 1, ... , n-1}
    count = [0 for _ in range(n)]    # C[i] == 0 for i in A
    for i in M:                     # All that are pointed to
        count[i] +=1                # Increment point count

    Q = [i for i in A if count[i] == 0] # Useless elements
    while Q:                            # While useless elts. left
        i = Q.pop()                     # Get one
        A.remove(i)                     # Remove it
        j = M[i]                        # Who's it pointing to?
        count[j] -= 1                   # Decrement point count
        if count[j] == 0:               # Is j useless?
            Q.append(j)                 # Then deal with it next

    return A                            # Return useful elts.


def main():
    M = [2, 2, 0, 5, 3, 5, 7, 4]
    print(max_perm(M))

if __name__ == '__main__':
    main()