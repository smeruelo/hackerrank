#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-set-union/problem

if __name__ == '__main__':
    _ = raw_input(); english = set(raw_input().split())
    _ = raw_input(); french = set(raw_input().split())
    print len(english.union(french))
