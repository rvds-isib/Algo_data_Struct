from heapq import heapify, heappop, heappush


class Solution:
    """
    Étant donné un tableau Arr de N entiers positifs et un entier K, trouvez les K plus grands éléments du tableau.
    Les éléments de sortie doivent être imprimés par ordre décroissant.
    Expected Time Complexity: O(K+(N-K)*logK)
    Expected Auxiliary Space: O(K)
    """
    def kLargest(self, arr, n, k):
        """
        Trouver les k élements les plus grands de l'array.
        :param arr: Array
        :param n: Taille array
        :param k: Nombre d'éléments à trouver
        :return: Liste des k éléments trouvés dans l'ordre décroissant
        """
        heap = []
        heapify(heap)

        # Ajouter les éléments dans l'arbre de tris
        for i in range(n):
            heappush(heap, arr[i])
            # Si dépasse k, retire le min
            if len(heap) > k:
                heappop(heap)

        # Ajouter à une liste pour la reverse
        k_largest = []
        while len(heap) != 0:
            k_largest.append(heappop(heap))
        return k_largest[::-1]


N = 5
K = 2
Arr = [12, 5, 787, 1, 23]

solution = Solution()
largest_element = solution.kLargest(Arr, N, K)
print(largest_element)

""" 
    Output: 787 23
    Explication : 1er plus grand élément du le tableau est de 787 et le deuxième plus grand est de 23.
"""
