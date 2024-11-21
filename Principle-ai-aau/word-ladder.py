#!/usr/bin/python3 

from collections import deque, defaultdict

def word_ladder(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    # Create a graph of intermediate patterns
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
    wordList.append(beginWord)
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            neighbors[pattern].append(word)

    # BFS setup
    visited = set([ beginWord])
    queue = deque([(beginWord, 1)])  # (current_word, transformation_steps)

    while queue:
        current_word, steps = queue.popleft()
        
        # Explore neighbors
        for i in range(len(current_word)):
            pattern = current_word[:i] + "*" + current_word[i+1:]
            for neighbor in neighbors[pattern]:
                if neighbor == endWord:
                    return steps + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
    
    return 0  # No valid transformation sequence found

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(word_ladder(beginWord, endWord, wordList))

# w = "tom"
# for i in range(len(w)):
#     print(f"{w[:i]}*{w[i+1:]}")