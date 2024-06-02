class Solution:
    """
    Objectif : Classer un Stack (pile) de manière décroissante
    !!!! Propriété d'un stack : LIFO : LAST IN FIRST OUT //(FILO)
    Donc trier de manière croissante sera ensuite sortie dans le bon ordre

    Expected Time Complexity: O(N*N) [quadratique] en raison du parcours récursif complet de la pile à chaque niveau
    Expected Auxilliary Space: O(N) [linéaire] recursive n raison de l'utilisation de la récursivité, nécessitant une
    quantité d'espace proportionnelle à la taille de la pile.
    """

    def Sorted(self, s):
        """
        Récursivité : Retire un élement à la fois.
        Dès que la "liste" est vide appelle la fonction Insert
        :param s: stack
        :return:
        """
        if len(s) != 0:
            # Retirer le dernier élément
            temp = s.pop()
            self.Sorted(s)
            self.sortedInsert(s, temp)

    def sortedInsert(self, s, temp_element):
        """
        Récursivité : Insère élément dans le stack de manière croissante
        :param s: stack (taille variable)
        :param temp_element: élément à classer
        :return:
        """
        # Si élément + grand ajouter à la liste
        if len(s) == 0 or temp_element > s[-1]:
            s.append(temp_element)
            return
        # Sinon vider la liste jusqu'à sa bonne place
        else:
            temp = s.pop()
            self.sortedInsert(s, temp_element)
            s.append(temp)


stack = [3, 7, 1, 4, 2]
solution = Solution()
solution.Sorted(stack)

print("Sorted stack:", stack)

"""
Solution Alternative :
 
class Solution:
    def Sorted(self, s):
        return s.sort()
"""