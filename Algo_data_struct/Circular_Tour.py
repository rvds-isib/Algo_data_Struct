class Solution:
    """
    Suppose there is a circle. There are N petrol pumps on that circle.
    You will be given two sets of data.
    1. The amount of petrol that every petrol pump has.
    2. Distance from that petrol pump to the next petrol pump.
    Find a starting point where the truck can start to get through the complete circle without exhausting its petrol.
    Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.
    (The truck will stop at each petrol pump, and it has infinite capacity). If there exists multiple
    such starting points, then the function must return the first one out of those. (return -1 otherwise)

    Expected Time Complexity: O(N), car elle parcourt chaque station une seule fois (N est le nombre de stations-services)
    Expected Auxiliary Space : O(1), car la fonction utilise une quantité constante de mémoire
            indépendamment de la taille de l'entrée.

    Constraints:
    2 ≤ N ≤ 10000
    1 ≤ petrol, distance ≤ 1000
    """

    def tour(self, lis, n):
        """
        Fonction pour trouver le point de départ où le camion peut commencer à traverser
        le cercle complet sans épuiser son essence en cours de route.

        :param lis: Liste de tuples, chaque tuple contient la quantité de pétrole et la distance à la prochaine station.
            lis[][0]: Petrol
            lis[][1]: Distance
        :param n: Nombre de stations.
        :return: Indice du point de départ à partir duquel le camion peut compléter le tour,
            (-1 s'il n'y a pas de solution possible).
        """
        total_petrol = 0
        total_distance = 0
        start_index = 0
        current_petrol = 0

        if n == 1:
            return 0

        for i in range(n):
            petrol, distance = lis[i]
            total_petrol += petrol
            total_distance += distance
            current_petrol += petrol - distance

            # Si le carburant disponible devient négatif,
            # on met à jour l'indice de départ potentiel et on réinitialise le carburant disponible
            if current_petrol < 0:
                start_index = i + 1
                current_petrol = 0

        # Si le total du carburant disponible est inférieur ou égal au total de la distance,
        # il n'y a pas de solution possible.
        if total_petrol < total_distance:
            return -1
        else:
            return start_index


if __name__ == "__main__":
    solution = Solution()

    # Test 1
    lis1 = [(4, 6), (6, 5), (7, 3), (4, 5)]
    n1 = 4
    result1 = solution.tour(lis1, n1)
    print("Starting point for Test 1:", result1)  # Output: 1

    # Test 2
    lis2 = [(6, 40), (7, 50), (8, 60), (5000, 10)]
    n2 = 4
    result2 = solution.tour(lis2, n2)
    print("Starting point for Test 2:", result2)  # Output: 3

    # Test 3
    lis3 = [(2, 6), (4, 5), (6, 3), (2, 5)]
    n3 = 4
    result3 = solution.tour(lis3, n3)
    print("Starting point for Test 3:", result3)  # Output: -1

"""
Alternative :
class Solution:
    def tour(self, lis, n):
        if n == 1:
            return 0

        start = 0
        end = 1
        remaining_fuel = lis[start][0] - lis[start][1]

        while end != start or remaining_fuel < 0:
            while remaining_fuel < 0 and start != end:
                remaining_fuel -= (lis[start][0] - lis[start][1])
                start = (start + 1) % n
                if start == 0:
                    return -1

            remaining_fuel += (lis[end][0] - lis[end][1])
            end = (end + 1) % n

        return start
"""