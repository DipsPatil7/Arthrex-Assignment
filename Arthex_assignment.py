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

# Example input
start_person = 'A'
start_person = find_person(start_person)
result = gather_friends(start_person)
print(result)
