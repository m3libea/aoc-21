#!/usr/bin/env python3

class TrieNode:
    def __init__(self):
        self.children = [ None ] * 2
        self.isLeaf = False
        self.total = 0

class Trie:
    def __init__(self, lines):
        self.root = TrieNode()
        self.add_lines(lines)
        
    def insert(self, number) -> None:
        current = self.root 
        for bit in number:
            current.total += 1
            if not current.children[bit]:
                current.children[bit] = TrieNode()
            current = current.children[bit]            
        current.isLeaf = True

    def add_lines(self, lines):
        for number in lines:
            self.insert(number)