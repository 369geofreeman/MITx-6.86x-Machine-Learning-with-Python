# K-means and K-medoids


Assume we have a 2D dataset consisting of  (0,−6),(4,4),(0,0),(−5,2) . We wish to do k-means and k-medoids clustering with  𝑘=2 . We initialize the cluster centers with  (−5,2),(0,−6) .

For this small dataset, in choosing between two equally valid exemplars for a cluster in k-medoids, choose them with priority in the order given above (i.e. all other things being equal, you would choose  (0,−6)  as a center over  (−5,2) ).

For the following scenarios, give the clusters and cluster centers after the algorithm converges. Enter the coordinate of each cluster center as a square-bracketed list (e.g. [0, 0]); enter each cluster's members in a similar format, separated by semicolons (e.g. [1, 2]; [3, 4]).


## Clustering 1

K-medoids algorithm with  𝑙1  norm.

Answer = Cluster 1 Center: [4, 4]

Answer = Cluster 1 Members: [4, 4]; [0,0]; [-5,2]

Answer = Cluster 2 Center: [0, -6]

Answer = Cluster 2 Members: [0, -6]


## Clustering 2

K-medoids algorithm with  𝑙2  norm.

Answer = [-1/3,2]

Answer = Cluster 1 Members: [4,4] ; [0,0]; [-5,2] 

Answer = Cluster 2 Center: [0,-6]

Answer = Cluster 2 Members: [0,-6]


## Clustering 3

K-means algorithm with  𝑙2  norm


Answer = Cluster 1 Center: [-0.5, 3]

Answer = Cluster 1 Members: [4,4]; [-5,2]

Answer = Cluster 2 Center: [0, -3] 

Answer = Cluster 2 Members: [0,-6]; [0,0]


