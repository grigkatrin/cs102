import jgraph
from api import get_friends
import time


def get_network(users_ids, as_edgelist=True):
    t = 0
    users_ids = get_friends(users_ids, 'bdate')
    edges = []
    matrix = [[0] * len(users_ids)] * len(users_ids)

    for user_1 in range(len(users_ids)):
        friends = get_friends(users_ids[user_1]['id'], 'bdate')
        t += 1
        for user_2 in range(user_1 + 1, len(users_ids)):
            if users_ids[user_2] in friends:
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

    graf = jgraph.Graph(vertex_attrs={"label": vertices}, edges=edges, directed=False)

    N = len(vertices)
    visual_style = {}
    visual_style["layout"] = g.layout_fruchterman_reingold(
        maxiter=1000,
        area=N ** 3,
        repulserad=N ** 3)

    jgraph.plot(graf, **visual_style)
    graf.simplify(multiple=True, loops=True)

    communities = graf.community_edge_betweenness(directed=False)
    clusters = communities.as_clustering()
    print(clusters)

    pal = jgraph.drawing.colors.ClusterColoringPalette(len(clusters))
    graf.vs['color'] = pal.get_many(clusters.membership)


if __name__ == '__main__':
    plot_graph(52918220)