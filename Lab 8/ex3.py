#Pseudo to work off of
Kruskal(weighted connected undirected graph ):
    tree = null;
    edges = sequence of all edges of graph sorted by weight;
    for (i = 1; i ≤ |E| and |tree| < |V|–1; i++)
            if ei from edges does not form a cycle with edges in tree
            add ei to tree;