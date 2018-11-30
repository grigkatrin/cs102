from api import get_friends
import time
import igraph
from igraph import Graph, plot
import numpy as np
 
def get_network(users_ids, as_edgelist=True):
    t = 0
    friend_list = get_friends(users_ids, 'bdate')
    edges = []
    matrix = [[0] * len(friend_list)] * len(friend_list)

    for user_1 in range(len(friend_list)):
        friends = get_friends(friend_list[user_1]['id'], 'bdate')
        t += 1
        for user_2 in range(user_1 + 1, len(friend_list)):
            if friend_list[user_2] in friends:
                matrix[user_2][user_1] = 1
                matrix[user_1][user_2] = 1
                if as_edgelist:
                    edges.append((user_1, user_2))
        if t == 3:
            time.sleep(1)
            t = 0

    if as_edgelist:
        return edges
    return matrix


def plot_graph(user_id):
    friends = get_friends(user_id, 'bdate')
    edges = get_network(user_id)
    vertices = [(i['first_name']+' '+i['last_name']) for i in friends]

    graf = Graph(vertex_attrs={"label": vertices}, edges=edges, directed=False)

    N = len(vertices)
    visual_style = {}
    visual_style["layout"] = graf.layout_fruchterman_reingold(
        maxiter=1000,
        area=N ** 3,
        repulserad=N ** 3)

    plot(graf, **visual_style)
    graf.simplify(multiple=True, loops=True)

    communities = graf.community_edge_betweenness(directed=False)
    clusters = communities.as_clustering()
    print(clusters)

    pal = igraph.drawing.colors.ClusterColoringPalette(len(clusters))
    graf.vs['color'] = pal.get_many(clusters.membership)


if __name__ == '__main__':
    plot_graph(1253731)