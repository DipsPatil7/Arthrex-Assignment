import unittest
from collections import deque

# Data setup
candidates = {
    'A': ['B', 'C', 'J'],
    'D': ['E', 'F', 'G'],
    'H': ['I', 'K', 'V'],
    'J': ['V'],
    'K': ['L', 'M', 'N', 'A'],
    'O': ['P', 'V', 'U'],
    'Q': ['S', 'T', 'D'],
    'U': ['H', 'J'],
    'V': ['W', 'X', 'Y', 'Z']
}

def gather_friends(start):
    contacted, queue = set([start]), deque([start])
    result = []

    while queue:
        person = queue.popleft()
        result.append(person)
        for friend in candidates.get(person, []):
            if friend not in contacted:
                contacted.add(friend)
                queue.append(friend)
    
    return result

def find_person(target):
    return next((person for person, friends in candidates.items() if target in friends), target)

# Unit tests
class TestGatherFriends(unittest.TestCase):
    def test_gather_friends_1(self):
        start_person = 'A'
        expected_result = ['A', 'B', 'C', 'J', 'V', 'W', 'X', 'Y', 'Z']
        self.assertEqual(gather_friends(start_person), expected_result)

    def test_gather_friends_2(self):
        start_person = 'D' 
        expected_result = ['D', 'E', 'F', 'G']
        self.assertEqual(gather_friends(start_person), expected_result)

    
    def test_gather_friends_4(self):
        start_person = 'Q' 
        expected_result = ['Q', 'S', 'T', 'D', 'E', 'F', 'G']
        self.assertEqual(gather_friends(start_person), expected_result)

    def test_find_person_1(self):
        target = 'A'
        expected_result = 'K' 
        self.assertEqual(find_person(target), expected_result)

   

    def test_find_person_3(self):
        target = 'O'
        expected_result = 'O'  # Since O is not in any friends list
        self.assertEqual(find_person(target), expected_result)

if __name__ == '__main__':
    unittest.main()
