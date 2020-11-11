# Similarity Measures-Cost functions




## The Need to Define Costs



Note that it is possible to have multiple clustering results given the same set of feature vectors. For example, in the following picture, we can have two scenarios of clustering outputs given the same set of feature vectors.

	  	
Output 1	  	Output 2
What is a good method for deciding which clustering output is more preferable?


Answer = Define a measure of homogeneity inside cluster assignments and compare the measure of each scenario 



## Choosing the Right Similarity Measure


Now, let's think about the Google News example the professor has mentioned in the beginning of the lecture. We want to measure the similarity between two Google News articles.

In the feature space, each article is represented as with the bag-of-words approach. For example, if "I", "love", "you", "more", "than", "Kevin" are the list of all unique vocabulary mentioned in all articles, the article "I love you" is represented as a vector  [1,1,1,0,0,0]  while another article "you love Kevin more than I" is represented as a vector  [1,1,1,1,1,1] . Note that each entry of vector is a binary indicator whether given word exists in an article or not.

You assume that the length of an article does not tell any useful information about the article, and hence choose a similarity measure that does not depend on the length of the article.

Which of the following similarity measure could be the one you chose?


Answer = Cosine distance



## Diameter


Recall from the above video that the diameter of a cluster is the measure of how far the two farthest points in a cluster are located.

Choose whether the following statement is True or False: “Adding a point to a cluster either increases the diameter of the cluster or the diameter stays the same."


Answer = True

## Possible Ways to Define Costs

Remember from the lecture above that the total cost of clustering output is defined as the sum of the cost inside each cluster. In other words,

Cost(𝐶1,...,𝐶𝐾)=∑𝑗=1𝐾Cost(𝐶𝑗) 
 
Note that the cost  Cost(𝐶𝑗)  is supposed to measure "how homogeneous" the assigned data are inside the  𝑗 th cluster  𝐶𝑗 . Which of the following are valid ways to define  𝐶𝑜𝑠𝑡 ? Select all those apply.


Answwer = The diameter of a cluster

Answer = The average distance between points inside a cluster

Answer = The sum of distance between the representative and all points inside a cluster


## Calculating Costs


As in the picture below, the set of feature vectors is given by

𝑆𝑛={𝑥1,...,𝑥5} 
 
and the number of clusters  𝐾=2 .  𝑆𝑛  is clustered such that

 	 1,2,3 	 ∈𝐶1whose representative is 𝑧1 	 	 
 	 4,5 	 ∈𝐶2whose representative is 𝑧2 	 	 

If the coordinates of points are given by

 	 	 𝑥1=(−1,2),𝑥2=(−2,1),𝑥3=(−1,0),𝑧1=(−1,1) 	 	 
 	 	 𝑥4=(2,1),𝑥5=(3,2),𝑧2=(2,2) 	 	 
The cost of a clustering output is given by the sum of the squared euclidean distance of all points in a cluster with the representative for each of its clusters, i.e.

Cost(𝐶1,...,𝐶𝐾)=∑𝑗=1𝐾Cost(𝐶𝑗)=∑𝑗=1𝐾∑𝑖∈𝐶𝑗‖𝑥𝑖−𝑧𝑗‖2 
 
What is  Cost(𝐶1) ?

Cost(𝐶1)= 3 

Now, What is  Cost(𝐶2) ?

Cost(𝐶2)= 2


Finally, what is the cost of this clustering output?

Cost(𝐶1,𝐶2)= 5



