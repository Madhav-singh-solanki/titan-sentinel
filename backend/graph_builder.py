import networkx as nx

G = nx.Graph()

G.add_edge("User","Device")

G.add_edge("Device","IP")

G.add_edge("User","Transaction")

G.add_edge("Transaction","Merchant")

print(G.nodes())
print(G.edges())
