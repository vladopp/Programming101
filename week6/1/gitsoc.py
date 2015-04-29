from graph import DirectedGraph
import requests


class Gitsoc:

    def __init__(self, user, level):
        self.graph = DirectedGraph()
        self.visited = set()
        self.visited.add(user)
        self.visiteddict = {user: 0}
        self.user = user
        if level > 0:
            self.fill_graph_for_user(user)
        self.level = level
        self.fill_graph()

    def fill_graph_for_user(self, user):
        followingobj = requests.get("https://api.github.com/users/{}/following?client_id=fbe8a26356c233a9fad4&client_secret=23fab8586c690d9212460e773efa69bd326d4acb".format(user))
        followersobj = requests.get("https://api.github.com/users/{}/followers?client_id=fbe8a26356c233a9fad4&client_secret=23fab8586c690d9212460e773efa69bd326d4acb".format(user))
        followinglist = followingobj.json()
        followerslist = followersobj.json()
        self.visited.add(user)
        for guru in followinglist:
            self.graph.add_edge(user, guru["login"])
            self.visiteddict[guru["login"]] = self.visiteddict[user]+1
        for sheep in followerslist:
            self.graph.add_edge(sheep["login"], user)
            self.visiteddict[sheep["login"]] = self.visiteddict[user]+1

    def fill_graph(self):
        for node in self.graph.graph.keys()[:]:
            if node not in self.visited and self.visiteddict[node] < self.level:
                self.fill_graph_for_user(node)

    def do_you_follow(self, user):
        if user in self.graph.graph[self.user]:
            return True
        return False

    def do_you_follow_indirectly(self, user):
        return self.graph.path_between(self.user, user)

    def does_he_she_follows(self, user):
        if self.user in self.graph.graph[user]:
            return True
        return False

    def does_he_she_follows_indirectly(self, user):
        return self.graph.path_between(user, self.user)

    def who_follows_you_back(self):
        result = []
        pass
