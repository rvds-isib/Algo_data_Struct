"""Étant donné le pointeur/référence vers l'en-tête de la liste chaînée, la tâche consiste à trier la liste chaînée
donnée à l'aide de Merge Sort.
Remarque : Si la longueur de la liste chaînée est impaire, le nœud supplémentaire doit figurer dans la première liste
lors de la division.
Expected Time Complexity: O(N*Log(N)) - car il y a log(N) niveaux de division et chaque niveau de division a un coût
total de fusion de O(N).
Expected Auxiliary Space: O(N) - à cause des sous listes
"""


class Node:
    def __init__(self, data):
        """
        Initialise un nouveau nœud avec la donnée fournie et un pointeur vers le nœud suivant.
        """
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        """
        Initialise une nouvelle liste chaînée avec son pointeur "head".
        """
        self.head = None

    def append(self, new_value):
        """
        Crée la fonction pour ajouter une nouvelle valeur à la fin de la liste chaînée.
        :param new_value: La valeur à ajouter à la liste.
        :return:
        """
        # Crée un nouveau nœud avec la data fournie
        new_node = Node(new_value)

        # Si la liste est vide, initialise la tête avec le nouveau nœud
        if self.head is None:
            self.head = new_node
            return

        # Parcourt les nœuds pour arriver au dernier
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        # Ajoute la nouvelle valeur à la fin de la liste
        curr_node.next = new_node

    def sortedMerge(self, a, b):
        """
        Permet de trier et fusionner deux listes chaînées en une seule liste chaînée triée.
        :param a: première sous liste
        :param b: deuxième sous liste
        :return: la linked liste triée
        """
        result = None
        # Si une liste est vide rien à fusionner
        if a is None:
            return b
        if b is None:
            return a
        # Choisit le plus petit élément et le fusionne récursivement
        if a.data <= b.data:
            # result pointe vers a
            result = a
            # Récursivité pour trouver les élements suivants
            result.next = self.sortedMerge(a.next, b)
        else:
            # result pointe vers b
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, h):
        """
        Trie la liste chaînée en utilisant le tri fusion.
        :param h: tête de la liste chaine
        :return: la liste chainée triée
        """
        # Cas de base si la liste est vide ou a un seul élément
        if h is None or h.next is None:
            return h

        # Obtenir le milieu de la liste
        middle = self.getMiddle(h)
        # Obtenir l'élément suivant
        next_middle = middle.next

        # Divise la liste en deux parties en rompant la reference au milieu
        middle.next = None

        # Applique mergeSort sur la partie gauche
        left = self.mergeSort(h)

        # Applique mergeSort sur la partie droite
        right = self.mergeSort(next_middle)

        # Fusionne les listes triées gauche et droite
        sortedlist = self.sortedMerge(left, right)

        return sortedlist

    def getMiddle(self, head):
        """
        Trouve le nœud du milieu de la liste chaînée.
        :param head: la tête de la liste chainée
        :return: Le pointeur de l'élément au milieu
        """

        if head is None:
            return head

        slow = head
        fast = head

        # Parcourt la liste avec deux pointeurs
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow


# Créer la liste chaînée
llist = Solution()
llist.append(15)
llist.append(10)
llist.append(5)
llist.append(20)

# Trier la liste chaînée
sorted_list_head = llist.mergeSort(llist.head)

# Afficher la liste triée
current = sorted_list_head
while current:
    print(current.data, end=" ")
    current = current.next
