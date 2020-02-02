class ExtractGraph:
    # key is head word; value stores next word and corresponding probability.
    graph = {}

    sentences_add = "data\\assign1_sentences.txt"

    def __init__(self):
        # Extract the directed weighted graph, and save to [head_word][tail_word]:probability
        self.file = open(self.sentences_add, "r")
        for sentence in self.file:
            words = sentence.split()
            self.incrementCount(words)

        self.computeProbabilities()

    def getProb(self, head_word, tail_word):
        if head_word in self.graph and tail_word in self.graph[head_word]:
            return self.graph[head_word][tail_word]
        return 0.0

    def incrementCount(self, words):
        head_word = words[0]
        for tail_word in words[1:]:
            if head_word not in self.graph:
                self.graph[head_word] = {}
            if tail_word in self.graph[head_word]:
                self.graph[head_word][tail_word] += 1
            else:
                self.graph[head_word][tail_word] = 1
            head_word = tail_word

    def computeProbabilities(self):
        for head_word in self.graph.keys():
            total = 0
            for tail_word in self.graph[head_word].keys():
                total += self.graph[head_word][tail_word]
            for tail_word in self.graph[head_word].keys():
                self.graph[head_word][tail_word] = self.graph[head_word][tail_word] / total
