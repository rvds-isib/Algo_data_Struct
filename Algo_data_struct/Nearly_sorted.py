from heapq import heapify, heappop, heappush


class Solution:
    """
    Étant donné un tableau de n éléments, où chaque élément est à au plus k distance de sa position cible,
    vous devez trier le tableau de manière optimale. Complexité temporelle attendue : O(nlogk) car l'algorithme
    utilise un tas pour trier les k+1 premiers éléments, puis utilise une boucle pour ajouter les éléments restants
    Espace auxiliaire attendu : O(n) : linéaire car l'algorithme n'utilise qu'un seul tas de taille k+1 pour trier
    les éléments, et aucun espace supplémentaire n'est requis à mesure que la taille du tableau augmente.
    """
    def nearlySorted(self, a, n, k):
        """
        Trier un Array, chaque élément est à une distance maximale k de sa vraie position

        :param a: array
        :param n: taille array
        :param k: distance max de sa vraie position
        :return: array trié
        """
        # crée un arbre de tris comptant les k+1 premiers éléments
        heap = a[:k + 1]
        heapify(heap)

        target_index = 0
        for remaining_elements_index in range(k + 1, n):
            # Remplace dans arr par le premier de heap
            a[target_index] = heappop(heap)
            # Rajoute un élément dans heap
            heappush(heap, a[remaining_elements_index])
            target_index += 1

        # Vider le heap -> se trie auto
        while heap:
            a[target_index] = heappop(heap)
            target_index += 1

        return a


A = [6, 5, 3, 2, 8, 10, 9]
N = 7
K = 3
solution = Solution()
result = solution.nearlySorted(A, N, K)
print(result)

"""
Output: 2 3 5 6 8 9 10
"""
