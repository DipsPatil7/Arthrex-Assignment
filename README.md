**Problem Statement:**
Arthrex, a leading company, is looking to hire interns to bolster its workforce. To streamline the hiring process and maintain an active pipeline, Arthrex's recruiters need a systematic method for contacting potential candidates. Each intern contacted is asked to provide a list of their classmates, expanding the pool of potential candidates further. However, it's crucial to avoid contacting the same candidate multiple times and ensure that the recruiter exhausts the list of candidates and their classmates.

**Input:**
- Any character representing the person initially selected for the job.

**Output:**
- A list of all candidates contacted, including the initial selected person and their classmates.

**Problem Constraints:**
1. Each person is associated with a list of their classmates.
2. No candidate should be contacted more than once.
3. The contacting process continues until either a candidate is hired or the complete list of candidates along with their classmates is exhausted.

**Objective:**
To Develop an algorithm that efficiently gathers a list of all potential candidates contacted during the hiring process, adhering to the constraints mentioned above. The algorithm should start from the initially selected person and iteratively contact their classmates until the entire list of potential candidates is exhausted.

Solution :
The best-suited algorithm for this problem is Breadth-First Search (BFS). BFS is ideal because it explores all neighbors at the present depth level before moving on to nodes at the next depth level, ensuring that each candidate and their friends are contacted systematically without duplication.

Data Structure: Use a queue to manage the BFS process.
Set: Use a set to keep track of candidates who have already been contacted to avoid contacting the same candidate more than once.
Initialization: Start with the given candidate (selected for the job).
Process: While the queue is not empty, dequeue the front candidate, add their friends to the queue (if they haven't been contacted yet), and mark them as contacted.

Explanation
Data Setup: The candidates dictionary contains each candidate along with their friends.

Function gather_friends:
Initialize a set contacted with the start person to keep track of contacted candidates.
Use a deque queue initialized with the start person for BFS processing.
While the queue is not empty:
Dequeue the front candidate (person).
Add the person to the result list.
Iterate over the friends of the person from the candidates dictionary.
If a friend has not been contacted, add the friend to the contacted set and enqueue the friend.
Return the result list of all contacted candidates.



Function find_person:
Uses a generator expression with next to find the person who has the target as a friend, or returns the target itself if not found.

Main Execution:
Sets the starting person to 'M'.
Finds the correct starting person using find_starting_person.
Calls gather_candidates and prints the result.

Testing:
Testing Approach:
Each test case is written to verify a specific aspect of the functions under test.
The expected results are predetermined based on the provided dataset and the logic of the functions.
The unittest.TestCase class provides assertion methods like assertEqual() to compare the expected output with the actual output of the functions.
If all assertions pass without raising any exceptions, the test is considered successful.
The unittest.main() function runs the test suite, executing all test cases and reporting any failures or errors encountered.

Test Cases for find_person Function:

Test Case 1: Checks if the find_person function correctly identifies the person 'A' in a friend's list, returning the friend who has 'A' in their friends.
Test Case 2: Similar to Test Case 1 but tests for the case where the target person is not in any friend's list, ensuring the function returns the target person itself.

Test Cases for gather_friends Function:

Test Case 1: Tests the functionality of gather_friends starting from person 'A'. It asserts whether the function returns the correct list of contacts, including 'A' and all of 'A's friends and their friends' friends recursively until no new contacts are found.
Test Case 2: Similar to Test Case 1 but starts from person 'D'. It ensures that the function correctly gathers friends starting from a different person in the dataset.
Test Case 3: Tests the function starting from person 'Q', ensuring it handles scenarios where a person has no friends and returns only the initial person.
