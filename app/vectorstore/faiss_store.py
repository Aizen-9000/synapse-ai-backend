class FaissStore:
    def __init__(self):
        self.vectors = []

    def add(self, vector: list[float]):
        self.vectors.append(vector)

    def search(self, vector: list[float]):
        return self.vectors[:3]