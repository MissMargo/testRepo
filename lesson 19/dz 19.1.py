import networkx as nx
import matplotlib.pyplot as plt


edgelist = [['Zinkiv', 'Hadiach', 45], ['Hadiach', 'Lebedyn', 60], ['Lebedyn', 'Hadiach', 60],
            ['Hadiach', 'Myrhorod', 61], ['Myrhorod', 'Hadiach', 61], ['Hadiach', 'Zavodske', 67],
            ['Zavodske', 'Hadiach', 67], ['Hadiach', 'Romny', 71], ['Romny', 'Hadiach', 71],
            ['Hadiach', 'Lokhvytsia', 81], ['Lokhvytsia', 'Hadiach', 81], ['Hadiach', 'Vorozhba', 94],
            ['Vorozhba', 'Hadiach', 94], ['Hadiach', 'Bilopillia', 94], ['Bilopillia', 'Hadiach', 94],
            ['Hadiach', 'Buryn', 94], ['Buryn', 'Hadiach', 94], ['Kremenets', 'Pochaiv', 26],
            ['Pochaiv', 'Kremenets', 26]]


g = nx.Graph()
for edge in edgelist:
    g.add_edge(edge[0], edge[1], weight = edge[2])


pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Graph Generation")
plt.show()




