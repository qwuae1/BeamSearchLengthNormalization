class StringDouble:
    string = ""

    score = 0.0

    def __init__(self, a, b):
        self.string = a
        self.score = b

    def __eq__(self, other):
        if isinstance(other, StringDouble):
            return self.string == other.string
        return self.string == other

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score


