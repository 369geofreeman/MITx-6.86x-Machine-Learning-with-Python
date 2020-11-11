#  Clustering Definition


## Partition Definition


A partition of a set is a grouping of the set's elements into non-empty subsets, in such a way that every element is included in one and only one of the subsets. In other words,  𝐶1,𝐶2,...,𝐶𝐾  is a partition of  {1,2,...,𝑛}  if and only if

𝐶1∪𝐶2∪...∪𝐶𝐾={1,2,...,𝑛} 
 
and

𝐶𝑖∩𝐶𝑗=∅for any 𝑖≠𝑗 in {1,...,𝑘}  
 
(Union of all  𝐶𝑗 's is the original set and the intersection of any  𝐶𝑖  and  𝐶𝑗  is an empty set.)

For example,

{3},{1},{2}, 
 
{2,1},{3}, 
 
{2,3,1} 
 
are all partitions of the set  {1,2,3} .

Now, which of the following is a partition of  {1,2,...,10} ? Select all those apply.


Answer = {1,2,3},{4},{5,6,7,8,9,10}

Answer = {1},{2},{3},{4},{5},{6},{7},{8},{9},{10}

Answer = {1,2,3,4,5,6,7,8,9,10}



## Clustering Definition: The Input


Remember that classification takes the training set

𝑆𝑛={(𝑥(𝑖),𝑦(𝑖))|𝑖=1,...,𝑛} 
 
and the number of classes as input. (where  𝑥(𝑖)  is the feature vector and  𝑦(𝑖)  is the label). (In other words, these were given so that we can find a classifier that will best classify the test set into the given number of classes.)

Remember in the lecture above that now we are discussing clustering, which has a different setting and a different goal from classification. Which of the following are the inputs (givens) of clustering? Select all those apply.

Answer = Set of feature vectors  𝑆𝑛={𝑥(𝑖)|𝑖=1,...,𝑛}

Answer = The number of clusters  𝐾




## Clustering Definition: The Output


In the last problem, you have figured out the clustering input. Which of the following are outputs of the clustering? Or in other words , which of the following are determined by the clustering algorithm? (More details of the algorithm will be on the next page.)

(Select all those apply.)



Answer =  A partition of indices  {1,...,𝑛}  into  𝐾  sets,  𝐶1,...,𝐶𝐾

Answer = "Representatives" in each of the  𝐾  partition sets, given as  𝑧1,...,𝑧𝐾



