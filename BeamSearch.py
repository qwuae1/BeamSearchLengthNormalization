import heapq
import StringDouble
import ExtractGraph
from heapq import heappush, heapreplace

import math


class Node:
    tokens = []
    prob = 0.0

    def __init__(self, tokens, prob):
        self.tokens = tokens
        self.prob = prob

    def __lt__(self, other):
        if self.prob < other.prob:
            return True
        else:
            return False

class BeamSearch:

    graph = []

    def __init__(self, input_graph):
        self.graph = input_graph
        self.topK = []
        return

    def beamSearchV1(self, pre_words, beamK, maxToken):
        # Basic beam search.
        return self.beamSearchV2(pre_words, beamK, 0, maxToken)

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
    	# Beam search with sentence length normalization.
        # heappush(self.heap, StringDouble.StringDouble(pre_words, 1))
        for i in range(len(pre_words.split()), maxToken):
            # print(self.heap)
            self.search(10, beamK)
        return self.heap[-1]





        sentence = ""
        probability = 0.0
        # use a queue to do the BFS
        queue = [Node(pre_words.split(' '), 1.0)]
        while len(queue[0].tokens) < maxToken:
            while queue:
                current = queue.pop()
                if current.tokens[-1] in self.graph.graph:
                    for key in self.graph.graph[current.tokens[-1]]:
                        newNode = Node(current.tokens[:] + [key],
                                       current.prob * self.graph.graph[current.tokens[-1]][key])
                        if len(self.topK) < beamK:
                            heapq.heappush(self.topK, newNode)
                        else:
                            if newNode.prob > self.topK[0].prob:
                                heapq.heapreplace(self.topK, newNode)
            for node in self.topK:
                queue.append(node)
            self.topK = []

        for node in queue:
            if node.prob > probability:
                sentence = ' '.join(node.tokens)
                probability = node.prob
        # print(probability)
        probability = (math.log(probability)) / math.pow(len(sentence), param_lambda)
        return StringDouble.StringDouble(sentence, probability)
