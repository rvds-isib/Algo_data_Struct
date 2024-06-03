from queue import SimpleQueue


class Solution:
    def rearrangeQueue(self, n, q):
        interleaved_queue = SimpleQueue()

        # Créer deux files pour les deux moitiés
        first_half = SimpleQueue()
        second_half = SimpleQueue()

        # Remplir les deux moitiés de la file d'attente
        for _ in range(n // 2):
            second_half.put(q.pop())
        for _ in range(n // 2):
            first_half.put(q.pop())

        # Intercaler les éléments des deux moitiés
        while not first_half.empty() and not second_half.empty():
            interleaved_queue.put(second_half.get())
            interleaved_queue.put(first_half.get())

        return interleaved_queue


# Exemple d'utilisation
N = 4
Q = [2, 4, 3, 1]
print("Before:", Q)
solution = Solution()
result = solution.rearrangeQueue(N, Q)

# Stocker les éléments de la file d'attente dans une liste
reversed_queue = []
while not result.empty():
    reversed_queue.append(result.get())

# Imprimer les éléments de la liste dans le sens inverse
print("After rearrangement (reversed):", end=" ")
for i in range(len(reversed_queue) - 1, -1, -1):
    print(reversed_queue[i], end=" ")

"""
Output:
{2,3,4,1}
Explanation:
After the mentioned rearrangement of the first half
and second half, our final queue will be {2,3,4,1}.
"""

"""
NOTE : sur geek4geeks q est considéré comme une liste.
#init
Q = deque([2, 4, 3, 1])
#function
    for i in range(mid):
        first_half.append(q.popleft())
    
    for i in range(mid):
        second_half.append(q.popleft())
"""
