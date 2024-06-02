
# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    """
    Given a singly linked list, sort the list (in ascending order) using insertion sort algorithm.
    Expected Time Complexity : O(n2) - dans le pire des cas, car pour chaque élément de la liste non triée,
    l'algorithme parcourt la liste triée pour trouver sa position d'insertion
    Expected Auxiliary Space : O(1) - car elle ne nécessite aucun espace supplémentaire proportionnel
    à la taille de l'entrée.
    """
    def insertionSort(self, head):
        """
        Trie une liste chaînée en utilisant l'algorithme de tri par insertion.
        :param head: tête de la liste chaine
        :return:
        """
        sorted_head = None
        # Pointe sur la liste
        current = head
        while current is not None:
            # Pointe sur les prochaines valeurs de la liste
            next_node = current.next

            if sorted_head is None or sorted_head.data >= current.data:
                # défini l'élément suivant
                current.next = sorted_head
                # pointe vers ma nvl liste
                sorted_head = current
            else:
                previous = sorted_head
                while previous.next is not None and previous.next.data < current.data:
                    previous = previous.next

                current.next = previous.next
                previous.next = current

            # les prochaines valeurs sont devenue la current
            current = next_node
        return sorted_head


"""
EXAMPLE:
Input : 
N = 7
Linked List=19->20->16->24->12->29->30 
Output : 
12 16 19 20 24 29 30 
Explanation : 
The resultant linked list is sorted.
"""