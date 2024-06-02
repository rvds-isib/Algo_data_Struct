class Solution:
    """
    Étant donné un ensemble de n écrous de différentes tailles et n boulons de différentes tailles. Il existe une
    correspondance individuelle entre les écrous et les boulons. Vous devez faire correspondre efficacement les
    écrous et les boulons. La comparaison d’un écrou avec un autre écrou ou d’un boulon avec un autre boulon n’est
    pas autorisée. Cela signifie que l'écrou ne peut être comparé qu'au boulon et que le boulon ne peut être comparé
    qu'à l'écrou pour voir lequel est le plus grand/le plus petit. Les éléments doivent suivre l'ordre suivant : {!,
    #, $, %, &, *, @, ^, ? }
    Expected Time Complexity: O(n(logn)) car quicksort divise récursivement le tableau en
    sous-tableaux.
    Expected Auxiliary Space: O(log(n)) car il utilise une pile d'appels récursifs supplémentaire
    dont la hauteur maximale est log(n) pour un tableau de taille n.
    """
    def matchPairs(self, nuts, bolts, n):
        self.quickSort(nuts, bolts, 0, n - 1)

    def quickSort(self, nuts, bolts, index_low, index_high):
        if index_low < index_high:
            # Choisir le pivot
            pivot_index = self.partition(nuts, index_low, index_high, bolts[index_high])
            # Partitionner bolts autour du pivot
            self.partition(bolts, index_low, index_high, nuts[pivot_index])
            # Trier les sous-listes avant et après le pivot récursivement
            self.quickSort(nuts, bolts, index_low, pivot_index - 1)
            self.quickSort(nuts, bolts, pivot_index + 1, index_high)

    def partition(self, arr, index_low, index_high, pivot):
        left = index_low
        for i in range(index_low, index_high):
            if arr[i] == pivot:
                arr[i], arr[index_high] = arr[index_high], arr[i]
            if arr[i] < pivot:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        arr[left], arr[index_high] = arr[index_high], arr[left]
        # print(arr)
        return left


sol = Solution()
N = 5
Nuts = ["@", "%", "$", "#", "^"]
Bolts = ["%", "@", "#", "$", "^"]
sol.matchPairs(Nuts, Bolts, N)
print("Sorted nuts:", Nuts)
print("Sorted bolts:", Bolts)
