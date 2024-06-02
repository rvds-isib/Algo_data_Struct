"""Étant donné le pointeur/référence vers la tête d'une liste doublement liée de n nœuds, la tâche consiste à trier
la liste doublement liée donnée en utilisant le tri par fusion dans un ordre non décroissant et non croissant. (ordre
se fait par le correcteur).

Complexité temporelle attendue : O(nlogn) car l'algorithme divise la liste de façon
récursive jusqu'à ce que chaque sous-liste ne contienne qu'un seul élément, puis fusionne ces sous-listes dans
l'ordre.
Complexité spatiale attendue : O(logn) parce que l'algorithme utilise la récursivité pour diviser la liste en
sous-listes jusqu'à ce que chaque sous-liste ne contienne qu'un seul élément, limitant ainsi l'espace mémoire
utilisé."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def sortDoubly(self, head):
        """
        Trie une liste doublement chaînée en utilisant le tri par fusion.
        :param head: tête de la liste doublement chaînée
        :return: nouvelle tête de la liste triée
        """
        # Cas de base : Si la liste est vide ou contient un seul nœud, elle est déjà triée
        if not head or not head.next:
            return head

        # Étape 1 : Diviser la liste en deux moitiés
        left, right = self.getMiddle(head)

        # Étape 2 : Trier récursivement les moitiés gauche et droite
        left = self.sortDoubly(left)
        right = self.sortDoubly(right)

        # Étape 3 : Fusionner les moitiés triées
        return self.merge(left, right)

    def getMiddle(self, head):
        """
        Divise la liste doublement chaînée en deux moitiés.
        :param head: tête de la liste doublement chaînée
        :return: têtes des deux moitiés
        """
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Diviser la liste en deux moitiés au point médian
        mid = slow.next
        slow.next = None
        if mid:
            mid.prev = None

        return head, mid

    def merge(self, left, right):
        """
        Fusionne deux listes doublement chaînées triées.
        :param left: tête de la première liste triée
        :param right: tête de la deuxième liste triée
        :return: tête de la liste fusionnée triée
        """
        # Création d'une nouvelle liste pour la fusion
        dummy = Node(0)  # Nœud
        current = dummy  # pointeur

        # Fusionner les deux listes tant qu'il y a des éléments dans les deux
        while left and right:
            if left.data < right.data:
                current.next = left
                left.prev = current
                left = left.next
            else:
                current.next = right
                right.prev = current
                right = right.next
            current = current.next

        # Ajouter les nœuds restants des listes gauche ou droite
        if left:
            current.next = left
            left.prev = current
        if right:
            current.next = right
            right.prev = current

        # Ajuster les pointeurs précédents de la liste fusionnée
        head = dummy.next
        if head:
            head.prev = None

        return head

    def printList(self, node):
        while node:
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == "__main__":
    # Creating the doubly linked list
    head = Node(7)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(5)
    head.next.next.prev = head.next
    head.next.next.next = Node(2)
    head.next.next.next.prev = head.next.next
    head.next.next.next.next = Node(6)
    head.next.next.next.next.prev = head.next.next.next
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.prev = head.next.next.next.next
    head.next.next.next.next.next.next = Node(1)
    head.next.next.next.next.next.next.prev = head.next.next.next.next.next
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.prev = head.next.next.next.next.next.next

    # Creating an object of Solution class
    obj = Solution()

    # Sorting the doubly linked list
    sorted_head = obj.sortDoubly(head)

    # Printing the sorted doubly linked list
    obj.printList(sorted_head)
