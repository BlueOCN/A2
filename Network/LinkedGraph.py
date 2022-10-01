from pythonds3.graphs import Graph, Vertex


def build_graph(path):
    d = {}
    g = Graph()
    wfile = open(path, 'r')     # Network\vocabulary.txt
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g

G = build_graph("Network\\vocabulary.txt")
G.bfs(G.get_vertex("FOOL"))