%matplotlib inline # If running in IPython Notebook, insert this as your first line. OS X Yosemite backend will not display node lables 

# Otherwise, starting below beginning with try: to import matplotlib and networkx to bring in our social graphing tools 

try:
    import matplotlib.pyplot as plt

except:
    raise 

import networkx as nx 

# Build an empty graph

G = nx.Graph()

# Add edges between nodes & edge weights 

G.add_edge('a', 'b', weight = 10.0)
G.add_edge('a', 'c', weight = 0.2)
G.add_edge('c', 'd', weight = 0.1)
G.add_edge('c', 'e', weight = 0.7)
G.add_edge('c', 'f', weight = 0.9)
G.add_edge('a', 'd', weight = 0.3)

# Create two variables, one for "large" edges and one for "small" edges, to graph positions between nodes & edges 

elarge = [(u,v) for (u, v, d) in G.edges(data = True) if d['weight'] > 0.5]
esmall = [(u,v) for (u, v, d) in G.edges(data = True) if d['weight'] <= 0.5]

pos = nx.spring_layout(G) # positions for all nodes

# Draw nodes 
nx.draw_networkx_nodes(G, pos, node_size = 700)

# Draw edges
nx.draw_networkx_edges(G, pos, edgelist = elarge, width = 6)
nx.draw_networkx_edges(G, pos, edgelist = esmall, 
                       width =6, alpha = 0.5, edge_color = 'b',
                       style = 'dashed')

# Add node labels 
nx.draw_networkx_labels(G, pos, font_size = 20, font_family = 'sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png 
plt.show() # display the graph 
