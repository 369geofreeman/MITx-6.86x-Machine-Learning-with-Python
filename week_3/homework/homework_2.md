# Homework Two


### Feature Vectors Transformation

Consider a sequence of  𝑛 -dimensional data points,  𝑥(1),𝑥(2),... , and a sequence of  𝑚 -dimensional feature vectors,  𝑧(1),𝑧(2),... , extracted from the  𝑥 's by a linear transformation,  𝑧(𝑖)=𝐴𝑥(𝑖) . If  𝑚  is much smaller than  𝑛 , you might expect that it would be easier to learn in the lower dimensional feature space than in the original data space.


### 2. (a)

Suppose  𝑛=6 ,  𝑚=2 ,  𝑧1  is the average of the elements of  𝑥 , and  𝑧2  is the average of the first three elements of  𝑥  minus the average of fourth through sixth elements of  𝑥 . Determine  𝐴 .

Note: Enter  𝐴  in a list format:  [[𝐴11,...,𝐴16],[𝐴21,...,𝐴26]]


Answer = [[1/6,1/6,1/6,1/6,1/6,1/6], [1/3,1/3,1/3,-1/3,-1/3,-1/3]]


### 2. (b)

Using the same relationship between  𝑧  and  𝑥  as defined above, suppose  ℎ(𝑧)=𝑠𝑖𝑔𝑛(𝜃𝑧⋅𝑧)  is a classifier for the feature vectors, and  ℎ(𝑥)=𝑠𝑖𝑔𝑛(𝜃𝑥⋅𝑥)  is a classifier for the original data vectors. Given a  𝜃𝑧  that produces good classifications of the feature vectors, determine a  𝜃𝑥  that will identically classify the associated  𝑥 's.

Note: Use trans(...) for transpose operations, hea_z as  𝜃𝑧  and assume  𝐴  is a fixed matrix (enter this as A).

Note: Expects  𝜃𝑥  (an  [𝑛×1]  vector), not  𝜃⊤𝑥 .


Answer Thetsa_0 = trans(A)*theta_z

### 2. (c)

Given the same classifiers as in (b), if there is a  𝜃𝑥  that produces good classifications of the data vectors, will there always be a  𝜃𝑧  that will identically classify the associated  𝑧 's?

Note:  𝐴  is a fixed matrix.

Answer = No

### 3. (d)

Given the same classifiers as in (b), if there is a  𝜃𝑥  that produces good classifications of the data vectors, will there always be a  𝜃𝑧  that will identically classify the associated  𝑧 's?

Note: Now assume that you can change the  𝑚×𝑛  matrix  𝐴 .

Answer = Yes

### 2. (e)

If  𝑚<𝑛 , can we find a more accurate classifier by training in  𝑧 -space, as measured on the training data?

Answer = Yes

### 3. (f)

How about on unseen data?


Answer = Depends
