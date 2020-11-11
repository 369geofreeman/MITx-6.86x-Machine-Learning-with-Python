# Determining the Number of Clusters



## Image Quantization Example


Remember that in our the first clustering lecture, the professor discussed how clustering can be used in image quantization. In short, by clustering many different colors into a few clusters, we can save(compress) the number of bits used to denote different colors.

The picture below is a general trend between the number of clusters  𝐾  and the total cost of clustering.


We expect the clustering cost to decrease as we increase the number of clusters  𝐾 .As mentioned in the lecture, the case of  𝐾=𝑛  is when every point is its own cluster.

In the context of image quantization, what is the problem with every point being its own cluster?


Answer = There is no compression at all


## Supervised Elements of Unsupervised Learning


Remember that clustering is an example of unsupervised learning. However, unlike its name suggests, there are some elements that we can "supervise" in clustering. In other words, there are some parts clustering that needs to be determined or "tuned" by us, depending on the application. Which of the following are elements of clustering that we can and should tune, depending on the application?




Ansswer = Number of clusters 𝐾

Answer = The cost measure for distance between  𝑥(𝑖)∈𝐶𝑗  and  𝑧𝑗  ( dist(𝑥(𝑖),𝑧𝑗))
