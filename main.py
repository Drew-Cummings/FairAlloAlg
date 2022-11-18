import networkx as nx


def calc_util(items, values):
    utility = 0
    for i in items:
        utility += values[i]
    return utility

def generate_graph(allo, values):
    Gpi = nx.DiGraph()
    Gpi.add_nodes_from(allo.keys())
    edges = []
    for j in allo:
        for k in allo:
            if calc_util(allo[j], values[j]) < calc_util(allo[k],values[j]):
                edges.append((j,k))
    Gpi.add_edges_from(edges)
    return Gpi

def update(graph):
    print(graph)


values = {"Drew": {"toy": 2, "book": 8, "makeup": -2},
          "Allison": {"toy": 7, "book": 3, "makeup": 5},
          "Kasey": {"toy": -2, "book": -8, "makeup": 10}}

dict = {"Drew": ["makeup"], "Allison": ["book"], "Kasey": ["toy"]}

G = generate_graph(dict, values)

print(G.nodes)
print(G.edges)


def allocation(items, values):
    people = values.keys()
    evaluations = [[1,-2,6],[-3,4,2]]
    allocation = {}
    G = nx.DiGraph()
    for o in items:
        nplus = []
        for i in people:
            if values[i][o] >= 0:
                nplus.append(i)
        graph = generate_graph(allocation, values)
        if nplus != []:
            person = graph.sources[0]
            person.allocate(o)
        else:
            person = graph.sinks[0]
            person.allocate(o)

        while nx.simple_cycles(G):
            allocation, G = update(G)
    return allocation




if __name__ == '__main__':
    print("hi")