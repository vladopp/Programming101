import re
import json


class Panda:

    def __init__(self, name, email, gender):
        self.__name = str(name)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise(ValueError)
        self.__email = email
        if gender != "male" and gender != "female":
            raise(ValueError)
        self.__gender = gender

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def isMale(self):
        if self.gender() == "male":
            return True
        return False

    def isFemale(self):
        if self.gender() == "female":
            return True
        return False

    def __str__(self):
        return self.name()

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if self.name() == other.name() and self.email() == other.email() and self.gender() == other.gender():
            return True
        return False

    def __hash__(self):
        return (hash(self.name()) + hash(self.email()) + hash(self.gender()))


class PandaSocialNetwork:

    def __init__(self):
        self.__dict = {}

    @property
    def pandas(self):
        return self.__dict

    @pandas.setter
    def pandas(self, value):
        self.__dict = value

    def has_panda(self, panda):
        if panda in self.__dict:
            return True
        return False

    def add_panda(self, newpanda):
        if self.has_panda(newpanda):
            raise(Exception)
        else:
            self.__dict[newpanda] = []

    def are_friends(self, panda1, panda2):
        if panda1 in self.__dict[panda2] and panda2 in self.__dict[panda1]:
            return True
        return False

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise(Exception)

        self.__dict[panda1].append(panda2)
        self.__dict[panda2].append(panda1)

    def friends_of(self, panda):
        if self.has_panda(panda):
            return self.__dict[panda]
        return False

    def connection_level(self, panda1, panda2):

        if panda1 == panda2:
            raise(ValueError)

        if not self.has_panda(panda1) or not self.has_panda(panda2):
            return False

        visited_count = self.bfs(panda1)
        if visited_count[panda2] != 0:
            return visited_count[panda2]
        return -1

    def bfs(self, panda1):
        visited_count = {}
        for panda in self.__dict.keys():
            visited_count[panda] = 0
        visited = [panda1]
        queue = [panda1]
        while queue != []:
            for friend in self.__dict[queue[0]]:
                if friend not in visited:
                    queue.append(friend)
                    visited.append(friend)
                    visited_count[friend] = visited_count[queue[0]] + 1
            queue.pop(0)
        return visited_count

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) > 0:
            return True
        return False

    def how_many_gender_in_network(self, level, panda, gender):
        summ = 0
        visited_count = self.bfs(panda)
        for obj in visited_count.keys():
            if visited_count[obj] != 0 and obj.gender() == gender and visited_count[obj] <= level:
                summ += 1
        return summ

    def save(self, filename):
        f = open(filename, 'w')
        json.dumps(self.__dict, f)

    def load(self, filename):
        f = open(filename, 'r')
        f = f.open()
        self.__dict == json.loads(f)
