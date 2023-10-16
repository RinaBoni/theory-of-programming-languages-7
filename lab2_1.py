import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Добавляем состояния
G.add_node("H", shape="circle", color="blue")
G.add_node("S", shape="circle", color="blue")
G.add_node("P", shape="circle", color="blue")
G.add_node("N", shape="circle", color="blue")

# Добавляем переходы
G.add_edge('H', 'N', label="0, 1")
G.add_edge('N', 'N', label="0, 1")
G.add_edge('N', 'P', label=".")
G.add_edge('S', 'S', label="0, 1")
G.add_edge('P', 'S', label="0, 1")

# nx.draw_spring(G, with_labels=True)


pos = nx.spring_layout(G, seed=42)  # Define layout
nx.draw_networkx(G, pos, with_labels=True, node_size=50, node_color="skyblue", font_size=5, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()



# import networkx as nx
# import matplotlib.pyplot as plt

# G.add_weighted_edges_from([('H', 'N', '0, 1'), ('N', 'N', '0, 1'), ('N', 'P', '.'), ('S', 'S', '0, 1'), ('P', 'S', '0, 1')])
# print(G.edges())
# nx.draw_spring(G, with_labels=True)
# plt.show()