import networkx as nx
import preprocessing as p
import time
import timeit

def calc_util(items, values):
    utility = 0
    for i in items:
        utility += values[i]
    return utility


def get_sources_and_sinks(G):
    sources = []
    sinks = []
    for x in G.nodes():
        if G.in_degree(x) == 0:
            sources.append(x)
        if G.out_degree(x) == 0:
            sinks.append(x)
    return sources, sinks


def generate_graph(current_allo, values):
    Gpi = nx.DiGraph()
    Gpi.add_nodes_from(current_allo.keys())
    edges = []
    for j in current_allo:
        for k in current_allo:
            if calc_util(current_allo[j], values[j]) < calc_util(current_allo[k], values[j]):
                edges.append((j, k))
    Gpi.add_edges_from(edges)
    return Gpi


def update(an_allo, cycle):
    output = an_allo.copy()
    for i in range(len(cycle)):
        if i == len(cycle) - 1:
            output[cycle[i]] = an_allo[cycle[0]]
        else:
            output[cycle[i]] = an_allo[cycle[i + 1]]
    return output


def allocation(items, values):
    agents = values.keys()
    allo = {x: [] for x in agents}
    graph = generate_graph(allo, values)
    for o in items:
        sources, sinks = get_sources_and_sinks(graph)
        nplus = [x for x in agents if values[x][o] >= 0]
        if nplus:
            subgraph = graph.subgraph(nplus)
            sources, sinks = get_sources_and_sinks(subgraph)
            agent = sources[0]
            agent_items = allo[agent]
            agent_items.append(o)
            allo[agent] = agent_items
        else:
            agent = sinks[0]
            agent_items = allo[agent]
            agent_items.append(o)
            allo[agent] = agent_items
        # print(allo)
        graph = generate_graph(allo, values)
        cycles = sorted(nx.simple_cycles(graph), key=lambda ele: len(ele), reverse=True)
        # print(cycles)
        while cycles:
            allo = update(allo, cycles[0])
            # print(allo)
            graph = generate_graph(allo, values)
            cycles = sorted(nx.simple_cycles(graph), key=lambda ele: len(ele), reverse=True)
    # nx.draw(graph)
    # plt.show()
    return allo


items = ["makeup", "book", "toy"]

evals = {"Drew": {"toy": 2, "book": 8, "makeup": -2},
         "Allison": {"toy": 7, "book": 4, "makeup": 5},
         "Kasey": {"toy": -2, "book": -8, "makeup": 10}}

# print(allocation(items, evals))

# example = {"Drew": ["makeup"], "Allison": ["book"], "Kasey": ["toy"]}
#
# G = generate_graph(example, evals)
#
# print(G.nodes)
# print(G.edges)
# test_cycles = sorted(nx.simple_cycles(G), key=lambda ele: len(ele), reverse=True)
#
# print(test_cycles)

def generate_testcode(agents, items):
    output = '''
utilities = [
        "Artichoke",
        "Arugula",
        "Asparagus",
        "Avocado",
        "Bamboo Shoots",
        "Bean Sprouts",
        "Beans",
        "Beet",
        "Belgian Endive",
        "Bell Pepper",
        "Bitter Melon/Bitter Gourd",
        "Bok Choy",
        "Broccoli",
        "Brussels Sprouts",
        "Burdock Root",
        "Cabbage",
        "Calabash",
        "Capers",
        "Carrot",
        "Cassava",
        "Cauliflower",
        "Celery",
        "Celery",
        "Celtuce",
        "Chayote",
        "Chinese Broccoli",
        "Corn/Maize",
        "Baby Corn",
        "Cucumber",
        "English Cucumber",
        "Gherkin",
        "Pickling Cucumbers",
        "Daikon Radish",
        "Edamame",
        "Eggplant/Aubergine",
        "Elephant Garlic",
        "Endive",
        "Curly/Frisee",
        "Escarole",
        "Fennel",
        "Fiddlehead",
        "Galangal",
        "Garlic",
        "Ginger",
        "Grape Leaves",
        "Green Beans/String Beans/Snap Beans",
        "Wax Beans",
        "Greens",
        "Amaranth Leaves/Chinese Spinach",
        "Beet Greens",
        "Collard Greens",
        "Dandelion Greens",
        "Kale",
        "Kohlrabi Greens",
        "Mustard Greens",
        "Rapini",
        "Spinach",
        "Swiss Chard",
        "Turnip Greens",
        "Hearts of Palm",
        "Horseradish",
        "Jerusalem Artichoke/Sunchokes",
        "Jícama",
        "Kale",
        "Curly",
        "Lacinato",
        "Ornamental",
        "Kohlrabi",
        "Leeks",
        "Lemongrass",
        "Lettuce",
        "Butterhead- Bibb",
        "Iceberg",
        "Leaf- Green Leaf",
        "Romaine",
        "Lotus Root",
        "Lotus Seed",
        "Mushrooms",
        "Napa Cabbage",
        "Nopales",
        "Okra",
        "Olive",
        "Onion",
        "Green Onions/Scallions",
        "Parsley",
        "Parsley Root",
        "Parsnip",
        "Peas",
        "green peas",
        "snow peas",
        "sugar snap peas",
        "Peppers",
        "Plantain",
        "Potato",
        "Pumpkin",
        "Purslane",
        "Radicchio",
        "Radish",
        "Rutabaga",
        "Sea Vegetables",
        "Shallots",
        "Spinach",
        "Squash",
        "Sweet Potato",
        "Swiss Chard",
        "Taro",
        "Tomatillo",
        "Tomato",
        "Turnip",
        "Water Chestnut",
        "Water Spinach",
        "Watercress",
        "Winter Melon",
        "Yams",
        "Zucchini"]
pre, val = p.final_preprocessing(''' + str(agents) + ',' + str(items) + ''',utilities)
thing = allocation(pre,val)'''
    return output


if __name__ == '__main__':

    setup_code = '''
import networkx as nx
import preprocessing as p
from __main__ import allocation
    '''

    test_code_5_5 = (generate_testcode(5, 5))
    print(timeit.timeit(setup=setup_code, stmt=test_code_5_5, number=8))
    test_code_5_50 = (generate_testcode(5, 50))
    print(timeit.timeit(setup=setup_code, stmt=test_code_5_50, number=8))
    test_code_5_500 = (generate_testcode(5, 500))
    print(timeit.timeit(setup=setup_code, stmt=test_code_5_500, number=8))
    test_code_5_5000 = (generate_testcode(5, 5000))
    print(timeit.timeit(setup=setup_code, stmt=test_code_5_5000, number=8))

    test_code_50_5 = (generate_testcode(50, 5))
    print(timeit.timeit(setup=setup_code, stmt=test_code_50_5, number=8))
    test_code_500_5 = (generate_testcode(500, 5))
    print(timeit.timeit(setup=setup_code, stmt=test_code_500_5, number=8))
    test_code_5000_5 = (generate_testcode(5000, 5))
    print(timeit.timeit(setup=setup_code, stmt=test_code_5000_5, number=8))







    # utilities = [
    #     "Artichoke",
    #     "Arugula",
    #     "Asparagus",
    #     "Avocado",
    #     "Bamboo Shoots",
    #     "Bean Sprouts",
    #     "Beans",
    #     "Beet",
    #     "Belgian Endive",
    #     "Bell Pepper",
    #     "Bitter Melon/Bitter Gourd",
    #     "Bok Choy",
    #     "Broccoli",
    #     "Brussels Sprouts",
    #     "Burdock Root",
    #     "Cabbage",
    #     "Calabash",
    #     "Capers",
    #     "Carrot",
    #     "Cassava",
    #     "Cauliflower",
    #     "Celery",
    #     "Celery",
    #     "Celtuce",
    #     "Chayote",
    #     "Chinese Broccoli",
    #     "Corn/Maize",
    #     "Baby Corn",
    #     "Cucumber",
    #     "English Cucumber",
    #     "Gherkin",
    #     "Pickling Cucumbers",
    #     "Daikon Radish",
    #     "Edamame",
    #     "Eggplant/Aubergine",
    #     "Elephant Garlic",
    #     "Endive",
    #     "Curly/Frisee",
    #     "Escarole",
    #     "Fennel",
    #     "Fiddlehead",
    #     "Galangal",
    #     "Garlic",
    #     "Ginger",
    #     "Grape Leaves",
    #     "Green Beans/String Beans/Snap Beans",
    #     "Wax Beans",
    #     "Greens",
    #     "Amaranth Leaves/Chinese Spinach",
    #     "Beet Greens",
    #     "Collard Greens",
    #     "Dandelion Greens",
    #     "Kale",
    #     "Kohlrabi Greens",
    #     "Mustard Greens",
    #     "Rapini",
    #     "Spinach",
    #     "Swiss Chard",
    #     "Turnip Greens",
    #     "Hearts of Palm",
    #     "Horseradish",
    #     "Jerusalem Artichoke/Sunchokes",
    #     "Jícama",
    #     "Kale",
    #     "Curly",
    #     "Lacinato",
    #     "Ornamental",
    #     "Kohlrabi",
    #     "Leeks",
    #     "Lemongrass",
    #     "Lettuce",
    #     "Butterhead- Bibb",
    #     "Iceberg",
    #     "Leaf- Green Leaf",
    #     "Romaine",
    #     "Lotus Root",
    #     "Lotus Seed",
    #     "Mushrooms",
    #     "Napa Cabbage",
    #     "Nopales",
    #     "Okra",
    #     "Olive",
    #     "Onion",
    #     "Green Onions/Scallions",
    #     "Parsley",
    #     "Parsley Root",
    #     "Parsnip",
    #     "Peas",
    #     "green peas",
    #     "snow peas",
    #     "sugar snap peas",
    #     "Peppers",
    #     "Plantain",
    #     "Potato",
    #     "Pumpkin",
    #     "Purslane",
    #     "Radicchio",
    #     "Radish",
    #     "Rutabaga",
    #     "Sea Vegetables",
    #     "Shallots",
    #     "Spinach",
    #     "Squash",
    #     "Sweet Potato",
    #     "Swiss Chard",
    #     "Taro",
    #     "Tomatillo",
    #     "Tomato",
    #     "Turnip",
    #     "Water Chestnut",
    #     "Water Spinach",
    #     "Watercress",
    #     "Winter Melon",
    #     "Yams",
    #     "Zucchini"]
    #
    # print(len(utilities))
    # items = ["makeup", "book", "toy"]
    #
    # evals = {"Drew": {"toy": 2, "book": 8, "makeup": -2},
    #          "Allison": {"toy": 7, "book": 4, "makeup": 5},
    #          "Kasey": {"toy": -2, "book": -8, "makeup": 10}}
    # t0 = time.time()
    # pre, val = p.final_preprocessing(5,5,utilities)
    # thing = allocation(pre,val)
    # print(thing)
    # t1 = time.time()
    # print(t1-t0)
    #
    # t0 = time.time()
    # pre, val = p.final_preprocessing(5, 50, utilities)
    # thing = allocation(pre, val)
    # print(thing)
    # t1 = time.time()
    # print(t1 - t0)
    #
    # t0 = time.time()
    # pre, val = p.final_preprocessing(5, 500, utilities)
    # thing = allocation(pre, val)
    # print(thing)
    # t1 = time.time()
    # print(t1 - t0)
    #
    # t0 = time.time()
    # pre, val = p.final_preprocessing(5, 5000, utilities)
    # thing = allocation(pre, val)
    # print(thing)
    # t1 = time.time()
    # print(t1 - t0)
    #
    #
    #
