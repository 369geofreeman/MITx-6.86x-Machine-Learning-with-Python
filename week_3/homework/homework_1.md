# Homework One


## Collaborative Filtering, Kernels, Linear Regression


In this question, we will use the alternating projections algorithm for low-rank matrix factorization, which aims to minimize

𝐽(𝑈,𝑉)=12∑(𝑎,𝑖)∈𝐷(𝑌𝑎𝑖−[𝑈𝑉𝑇]𝑎𝑖)2Squared Error+𝜆2∑𝑎=1𝑛∑𝑗=1𝑘𝑈2𝑎𝑗+𝜆2∑𝑖=1𝑚∑𝑗=1𝑘𝑉2𝑖𝑗Regularization. 
 
In the following, we will call the first term the squared error term, and the two terms with  𝜆  the regularization terms.

Let  𝑌  be defined as

𝑌=⎡⎣⎢⎢⎢⎢5?4??2?37??6⎤⎦⎥⎥⎥⎥ 
 
𝐷  is defined as the set of indices  (𝑎,𝑖) , where  𝑌𝑎,𝑖  is not missing. In this problem, we let  𝑘=𝜆=1 . Additionally,  𝑈  and  𝑉  are initialized as  𝑈(0)=[6,0,3,6]𝑇 , and  𝑉(0)=[4,2,1]𝑇 .

### 1) a

Compute  𝑋(0) , the matrix of predicted rankings  𝑈𝑉𝑇  given the initial values for  𝑈(0)  and  𝑉(0) .

Answer = [[24, 12, 6], [0, 0, 0], [12, 6, 3], [24, 12, 6]]

### 2) b

Compute the squared error term, and the regularization terms in for the current estimate  𝑋 .

Enter the squared error term (including the factor  1/2 ):

Answer = 511/2

Enter the regularization term (the sum of all the regularization terms):

Answer = 51

### 3) c

Suppose  𝑉  is kept fixed. Run one step of the algorithm to find the new estimate  𝑈(1) .

Enter the  𝑈(1)  as a list of numbers,  [𝑈(1)1,𝑈(1)2,𝑈(1)3,𝑈(1)4] :

Answer = [27/18,4/5,16/17,12/6]
