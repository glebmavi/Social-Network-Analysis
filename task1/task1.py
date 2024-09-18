import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph(nx.dense_gnm_random_graph(
    n=47,  # число вершин
    m=323,  # число ребер
    seed=34  # seed
))

nx.draw(graph)
plt.show()

density = nx.density(graph)
print(f"Плотность графа: {density:.3f}")

shortest_path_length = nx.shortest_path_length(graph, 3, 37)
print(f"Длина кратчайшего пути между вершинами 3 и 37: {shortest_path_length}")

largest_clique_size = max(len(clique) for clique in nx.find_cliques(graph))
print(f"Количество вершин в клике наибольшего размера: {largest_clique_size}")
