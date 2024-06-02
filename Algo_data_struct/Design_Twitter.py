class Twitter:
    """
    Conception d'une version simplifiée de Twitter où les utilisateurs peuvent poster des tweets,
    follow/unfollow d'autres utilisateurs,
    et voir les 10 tweets les plus récents dans leur fil d'actualité.

    Constraints:
    1 <= no. of queries <= 1000
    1 <= userId, tweetId, followerId, followeeId <= 105
    """

    def __init__(self):
        """
        Liste de tuples pour stocker les tweets sous la forme (userId, tweetId)
        Dictionnaire pour stocker les relations de follow entre les utilisateurs
        """
        self.tweets = []
        self.following = {}

    def postTweet(self, userId: int, tweetId):
        """
        Publier un nouveau tweet.
        :param userId: Identifiant de l'utilisateur qui publie le tweet
        :param tweetId: Identifiant du tweet
        :return: None
        """
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int):
        """
        Récupérer les 10 identifiants de tweets les plus récents dans le fil d'actualité de l'utilisateur.
        Si le nombre total de tweets dans le fil d'actualité est inférieur à 10, retourner tous les tweets disponibles.
        Chaque tweet dans le fil d'actualité doit être publié par les utilisateurs que l'utilisateur suit ou par
        l'utilisateur lui-même.
        Les tweets doivent être ordonnés du plus récent au plus ancien.
        :param userId: Identifiant de l'utilisateur
        :return: Liste des identifiants de tweets les plus récents
        """
        newsFeed = []
        # index initialisé à la dernière position de la liste `self.tweets`
        i = len(self.tweets) - 1
        while i >= 0 and len(newsFeed) < 10:
            if userId in self.following and self.tweets[i][0] in self.following[userId]:
                newsFeed.append(self.tweets[i][1])
            elif self.tweets[i][0] == userId:
                newsFeed.append(self.tweets[i][1])
            i -= 1
        return newsFeed

    def follow(self, followerId: int, followeeId: int):
        """
        Permettre à un utilisateur de suivre un autre utilisateur.
        :param followerId: Identifiant de l'utilisateur qui suit
        :param followeeId: Identifiant de l'utilisateur suivi
        :return: None
        """
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int):
        """
        Permettre à un utilisateur de ne plus suivre un autre utilisateur.
        :param followerId: Identifiant de l'utilisateur qui ne suit plus
        :param followeeId: Identifiant de l'utilisateur qui est suivi
        :return: None
        """
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
