import StringDouble


class ExtractGraph:
    # key is head word; value stores next word and corresponding probability.
    counts = {}
    graph = {}
    sentences_add = "data\\assign1_sentences.txt"

    def __init__(self):
        # Extract the directed weighted graph, and save to [head_word][tail_word]:probability
        # open file and split into sentences to words and get probability
        self.file = open(self.sentences_add, "r")
        for sentence in self.file:
            words = sentence.split()
            self.countWords(words)

        self.getProbabilities()

    def getProb(self, head_word, tail_word):
        for word in self.graph[head_word]:
            if word == tail_word:
                return word.score
        return 0.0

    def countWords(self, words):
        head_word = words[0]
        for tail_word in words[1:]:
            if head_word not in self.counts:
                self.counts[head_word] = {tail_word: 0}
            if tail_word in self.counts[head_word]:
                self.counts[head_word][tail_word] += 1
            else:
                self.counts[head_word][tail_word] = 1
            head_word = tail_word

    def getProbabilities(self):
        for head_word in self.counts:
            total = 0
            temp = []
            # get total number of head - tail
            for tail_word in self.counts[head_word]:
                total += self.counts[head_word][tail_word]
            # get probability by dividing by total and append the result using StringDouble
            for tail_word in self.counts[head_word]:
                self.counts[head_word][tail_word] /= total
                temp.append(StringDouble.StringDouble(tail_word, self.counts[head_word][tail_word]))
            # sort in decreasing order to get max K probability
            temp.sort(key=lambda x: x.score, reverse=True)
            self.graph[head_word] = temp
