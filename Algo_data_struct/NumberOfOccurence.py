import bisect


class Solution:
    """
    Utiliser la recherche binaire pour compter le nombre d'occurrences de x dans le tableau arr
    Expected Time Complexity: O(logN) - bisect utilise la recherche dichotomique (=méthode de la bissection)
    Expected Auxiliary Space: O(1) - espace mémoire constant
    """
    def count(self, arr, n, x):
        """
        Compte le nombre d'occurrences de x dans le tableau arr
        :param arr: Tableau trié
        :param n: Taille tableau
        :param x: élement dont on veut compter les occurrences
        :return: Nombre d'occurrences de x dans arr.
        """
        # Obtenir l'index de la première occurrence de x.
        low_index = bisect.bisect_left(arr, x)

        # Check si l'élément n'est pas présent → retourner 0
        if low_index == n or arr[low_index] != x:
            return 0

        # Obtenir l'index de la dernière (+1) occurrence de x.
        high_index = bisect.bisect_right(arr, x, low_index)

        return high_index - low_index


Arr = [1, 1, 2, 2, 2, 2, 3]
N = 7
X = 2

solution = Solution()
print(solution.count(Arr, N, X))
"""
Output: 4
"""
