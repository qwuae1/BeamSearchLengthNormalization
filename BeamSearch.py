import StringDouble
from math import *
from heapq import *


class BeamSearch:
    k_heap = []
    graph = {}

    def __init__(self, input_graph):
        self.graph = input_graph
        return

    def beamSearchV1(self, pre_words, beamK, maxToken):
        # Basic beam search.
        return self.beamSearchV2(pre_words, beamK, 0, maxToken)

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
        self.k_heap = []
        length = len(pre_words.split())
        heappush(self.k_heap, StringDouble.StringDouble(pre_words, 0))

        for i in range(length, maxToken):
            top_heap = []
            for sentence in self.k_heap:
                tail_word = sentence.string.split()[-1]

                # if reach end of a sentence
                if tail_word not in self.graph.graph:
                    BeamSearch.heap_add(top_heap, beamK, sentence)
                    continue
                else:
                    head_words = self.graph.graph[tail_word]

                for head_word in head_words[:min(len(head_words), beamK)]:
                    new_sentence = sentence.string + " " + head_word.string
                    new_score = ((pow(i, param_lambda) * sentence.score) + log(
                        head_word.score)) / pow(i + 1, param_lambda)
                    new_string_double = StringDouble.StringDouble(new_sentence, new_score)
                    BeamSearch.heap_add(top_heap, beamK, new_string_double)
            self.k_heap = top_heap

        return nlargest(1, self.k_heap)[0]

    @staticmethod
    def heap_add(top_heap, beamK, string_double):
        if len(top_heap) < beamK:
            heappush(top_heap, string_double)
        elif string_double > top_heap[0]:
            heapreplace(top_heap, string_double)