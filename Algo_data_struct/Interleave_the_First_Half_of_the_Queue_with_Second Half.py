from collections import deque


class Solution:
    """
        Vous recevez une file d'attente Q de N entiers de longueur paire, réorganisez les éléments en entrelaçant
        la première moitié de la file d'attente avec la seconde moitié de la file d'attente.
        Expected Time Complexity: O(N) → car elle parcourt chaque élément de la file une seule fois.
        Expected Auxiliary Space: O(N) → car elle utilise une nouvelle liste pour stocker les éléments réarrangés.
    """

    def rearrangeQueue(self, n, q):
        """
        Sépare la 'queue' en deux moitiés égales et insère un élément sur deux dans la nouvelle queue
        :param n: Taille de la queue
        :param q: Queue
        :return: la queue réarrangée
        """
        interleaved_queue = deque()
        mid = n // 2

        # Crée deux queues pour les deux moitiés
        first_half = deque(q[:mid])
        second_half = deque(q[mid:])

        # Intercaler les éléments des deux moitiés
        while first_half and second_half:
            interleaved_queue.append(first_half.popleft())
            interleaved_queue.append(second_half.popleft())

        # Retourne la nouvelle 'queue (liste)' réarrangée
        return list(interleaved_queue)


N = 4
Q = [2, 4, 3, 1]
print("Before :", Q)
solution = Solution()
Q = solution.rearrangeQueue(N, Q)
print("After :", Q)

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