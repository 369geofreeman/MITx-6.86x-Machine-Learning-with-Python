# Problem set two


## Collaborative Filtering: the Naive Approach


### Compute the Derivative of the Regression Objective

Recall that each user  𝑎  has a set of movies that (s)he has already rated. Let  𝑌  be a matrix with  𝑛  row and  𝑚  columns whose  (𝑎,𝑖)th  entry  𝑌𝑎𝑖  is the rating by user  𝑎  of movie  𝑖  if this rating has already been given, and blank if not. Our goal is to come up with a matrix  𝑋  that has no blank entries and whose  (𝑎,𝑖)th  entry  𝑋𝑎𝑖  is the prediction of the rating user  𝑎  will give to movie  𝑖 .

Let  𝐷  be the set of all  (𝑎,𝑖) 's for which a user rating  𝑌𝑎𝑖  exists, i.e.  (𝑎,𝑖)∈𝐷  if and only if the rating of user  𝑎  to movie  𝑖  exists.

A naive approach to solve this problem would be to minimize the following objective:

𝐽(𝑋)=∑𝑎,𝑖∈𝐷(𝑌𝑎𝑖−𝑋𝑎𝑖)22+𝜆2∑(𝑎,𝑖)𝑋2𝑎𝑖 
 
where the first term is the sum of the squared errors for entries with observed rating, and the second term is a regularization term roughly to prevent the predictions to become extremely large, and the parameter  𝜆  controls the balance between theses two terms.

Compute the derivative  ∂𝐽∂𝑋𝑎𝑖  of the objective function  𝐽(𝑋) . (Note that  𝐽(𝑋)  can be viewed as a function of the variables  𝑋𝑎𝑖 .)

(Type X_{ai} for matrix entries  𝑋𝑎𝑖 , Y_{ai} for matrix entries  𝑌𝑎𝑖  and "lambda" for  𝜆 . Note that  𝑋  and  𝑌  are capital letters to represent matrices.)

For (any fixed)  (𝑎,𝑖)∈𝐷 ,

Answer = X_{ai}-Y_{ai}+lambda*X_{ai}

For (any fixed)  (𝑎,𝑖)∉𝐷 :

Answer lambda * X_{ai}

Solution:

Derive the objective and remember to treat any entry in the matrix that is not the one that we are deriving by as a constant. Hence, the derivative of all components of the sum that are not  (𝑎,𝑖)  will be zero.

### Performance of the Naive Approach

Let us now check the quality of the solution when using this wrong approach. Recall the naive approach assumes independence between all entries of the matrix.

What value of the matrix  𝑋  will minimize the loss  𝐽(𝑋)=∑𝑎,𝑖∈𝐷(𝑌𝑎𝑖−𝑋𝑎𝑖)22+𝜆2∑(𝑎,𝑖)𝑋2𝑎𝑖 ? That is, for each  (𝑎,𝑖) , solve the following equation for  𝑋𝑎𝑖 :

 	 ∂𝐽∂𝑋𝑎𝑖=0. 	 	 
We will denote the argmin as  𝑋ˆ  and its components as  𝑋ˆ𝑎𝑖 .

For  (𝑎,𝑖)∈𝐷 :

Answer = Y_{ai}/(1+lambda)

For  (𝑎,𝑖)∉𝐷 :

Answer = 0





