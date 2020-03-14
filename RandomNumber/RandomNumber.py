import random


class RandomNumberGenerator:

    def __init__(self, minx, maxx):
        self.minx = minx
        self.maxx = maxx

    def rand_wout_seed(self):
        val_int = random.randint(self.minx, self.maxx)
        val_float = random.uniform(self.minx, self.maxx)

        return val_int, val_float

    def rand_with_seed(self, seedval):
        random.seed(seedval)
        val_int = random.randint(self.minx, self.maxx)
        val_float = random.uniform(self.minx, self.maxx)

        return val_int, val_float

    def randlist_wout_seed(self, N):
        val_int = random.sample(range(self.minx, self.maxx), N)
        val_float = [random.uniform(self.minx, self.maxx) for i in range(N)]

        return val_int, val_float

    def randlist_with_seed(self, seedval, N):
        random.seed(seedval)
        val_int = random.sample(range(self.minx, self.maxx), N)
        val_float = [random.uniform(self.minx, self.maxx) for i in range(N)]

        return val_int, val_float

    def rand_one_from_list(self, seedval, N):
        list_int, list_float = self.randlist_with_seed(self, seedval, N)
        val_int = random.sample(list_int, 1)
        val_float = random.sample(list_float, 1)

        return val_int, val_float

    def rand_n_from_list(self, N, n):
        list_int, list_float = self.randlist_wout_seed(N)
        val_int = random.sample(list_int, n)
        val_float = random.sample(list_float, n)

        return val_int, val_float

