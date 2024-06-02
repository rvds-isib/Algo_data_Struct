import sys

sys.setrecursionlimit(10 ** 6)  # limite le nombre de niveaux de récursion


class Solution:
    """
    You are given a stack St. You have to reverse the stack using RECURSION.

    Expected Time Complexity: O(N^2)
    Expected Auxiliary Space: O(1)
    Cette approche a une complexité temporelle de O(N^2) car à chaque niveau de la récursion,
    tous les éléments de la pile doivent être retirés et réinsérés.
    La complexité spatiale auxiliaire est O(1) car seule une quantité constante de mémoire est utilisée
    pour chaque appel récursif.
    LAST IN FIRST OUT
    """

    def reverse(self, s):
        """
        Récursivité : Vider le stack et insérer les élements 1 par 1 en commençant par le dernier
        :param s: Le stack actuel
        :return:
        """
        if len(s) > 0:
            first = s.pop()
            self.reverse(s)
            self.insert_at_bottom(s, first)

    def insert_at_bottom(self, s, first):
        """
        Insère l'élément quand la "pile" est vide
        :param s: le stack actuel
        :param first: l'élément à placer
        :return:
        """
        if len(s) == 0:
            s.append(first)
        else:
            # retire élément jusqu'à liste vide
            last = s.pop()
            # insère FIRST
            self.insert_at_bottom(s, first)
            # insère l'élément "last"
            s.append(last)


St = [3, 2, 1, 7, 6]
solution = Solution()
solution.reverse(St)
print(St)

"""
Output:
{6,7,1,2,3}
Explanation:
Input stack after reversing will look like the stack in the output.
"""
