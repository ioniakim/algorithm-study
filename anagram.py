#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 문제
# * Anagram: 두 단어가 같은 letter로 (중복 포함) 구성되어 있음
#     + 예: anagram/managra, flow/wolf, nameless/salesman
# * 문제: n개의 단어가 주어져 있고, 단어들의 길이의 합은 W이다. 단어들 중에 anagram이 되는 쌍의 개수를 계산하라.
# * O(Wn) 시간
from counting_sort import counting_sort
from counting_sort import counting_sort2


def anagram_cs(word1, word2):
    ''' Anagram using Counting sort
    '''
    w1 = counting_sort2(word1, ord)
    w2 = counting_sort2(word2, ord)

    return w1 == w2

def anagram(word1, word2):
    '''두 개의 단어가 anagram이면겯 True, 아니면 False
    '''
    # 1. sort two words
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    # 2. check they are the same
    return word1_sorted == word2_sorted

def main():
    a = 'anagram'
    b = 'managra'

    print(anagram(a, b))
    print(anagram_cs(a, b))

if __name__ == '__main__':
    main()