#!/usr/bin/python3
from collections import deque, defaultdict
import json

def word_ladder(beginWord, endWord, wordList):
    
    # check required conditions
    if endWord not in wordList:
        return 0
    if beginWord is None or len(beginWord) == 0:
        return 0
    if endWord is None or len(endWord) == 0:
        return 0
    # prepare neighbors dictionary for patterns
    if beginWord not in wordList:
        wordList.append(beginWord)
    neighbors = defaultdict(list)
    #     neighbors = {
#     "*it": ["hit"],
#     "h*t": ["hit", "hot"],
#     "hi*": ["hit"],
#     "*ot": ["hot", "dot", "lot"],
#     "ho*": ["hot"],
#     "d*t": ["dot"],
#     "do*": ["dot", "dog"],
#     "*og": ["dog", "log", "cog"],
#     "d*g": ["dog"],
#     "l*t": ["lot"],
#     "lo*": ["lot", "log"],
#     "c*g": ["cog"],
#     "co*": ["cog"]
# }

    for word in wordList:
        for chr in range(len(word)):
            # find diffrent patterns for each word
            pattern = word[:chr] + '*' + word[chr + 1:]
            # add the patten as key to the neghbors dict to know where to go from that pattern
            neighbors[pattern].append(word)
    
    # print(json.dumps(neighbors, indent=4))
    # Preparation for Greadth First Search
    # now each words are counted as nodes
    
    steps = 1
    queue = deque([[beginWord, steps]])
    # hold information for visited words or in this case nodes
    visited = set([beginWord])
    
    while queue:
        # get the first item (node) form the queue
        current_word, steps = queue.popleft()
        # print(current_word) 
        for idx in range(len(current_word)):
            # get pattern to look in the neighbors dictonary
            pattern = current_word[:idx] + '*' + current_word[idx + 1:]
            # look possible paths for the pattern in neighbors
            for neighbor in neighbors[pattern]:
                if neighbor == endWord:
                        return steps + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append([neighbor, steps + 1])

    return 0
if __name__ == "__main__":
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # beginWord = "lead"
    # endWord = "gold"
    # wordList = ["load", "goad", "gold", "lode", "lade"]
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog"],
    print(word_ladder(beginWord, endWord, wordList))
    