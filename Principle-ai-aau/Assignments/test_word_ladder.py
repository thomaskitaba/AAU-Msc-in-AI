import unittest
from word_ladder import word_ladder  # import your function

class TestWordLadder(unittest.TestCase):
    def test_basic_case(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(word_ladder(beginWord, endWord, wordList), 5)

    def test_another_case(self):
        beginWord = "lead"
        endWord = "gold"
        wordList = ["load", "goad", "gold", "lode", "lade"]
        self.assertEqual(word_ladder(beginWord, endWord, wordList), 4)
    def test_endword_missing(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "kog"]
        self.assertEqual(word_ladder(beginWord, endWord, wordList), 0)
    def test_empty_beginword(self):
        beginWord = None
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(word_ladder(beginWord, endWord, wordList), 0)
    def test_empty_endword(self):
        beginWord = "hit"
        endWord = None
        wordList = ["load", "goad", "gold", "lode", "lade"]
        self.assertEqual(word_ladder(beginWord, endWord, wordList), 0)

if __name__ == "__main__":
    unittest.main()
