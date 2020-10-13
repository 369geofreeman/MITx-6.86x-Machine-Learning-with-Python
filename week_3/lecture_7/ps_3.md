# Problem Set Four



## Collaborative Filtering with Matrix Factorization



### Matrix Factorization Practice


We now use collaborative filtering to solve the movie recommender system problem.

As we saw in the previous problem, we ended up with an unsatisfactory and trivial solution of  𝑋  by minimizing the objective alone:

𝐽(𝑋)=∑𝑎,𝑖∈𝐷(𝑌𝑎𝑖−𝑋𝑎𝑖)22+𝜆2∑(𝑎,𝑖)𝑋2𝑎𝑖. 
 
In the collaborative filtering approach, we impose an additional constraint on  𝑋 :

𝑋=𝑈𝑉𝑇 
 
for some  𝑛×𝑑  matrix  𝑈  and  𝑑×𝑚  matrix  𝑉𝑇 . The number  𝑑  is the rank of the matrix  𝑋 .

Suppose

𝑋=⎡⎣⎢⎢321642321⎤⎦⎥⎥, 
 
then what is the minimum possible  𝑑 ?

Answer = 1


### Intuition on the Vector Factors

Assume we have a 3 by 2 matrix  𝑋  i.e. we have 3 users and 2 movies. Also,  𝑋  is given by

 	 𝑋 	 = 	 ⎡⎣⎢⎢⎢User 1's rating on movie 1User 2's rating on movie 1User 3's rating on movie 1User 1's rating on movie 2User 2's rating on movie 2User 3's rating on movie 2⎤⎦⎥⎥⎥ 	 = 	 𝑈𝑉𝑇 	 	 
for some  3×𝑑  matrix  𝑈  and  𝑑×2  matrix  𝑉𝑇 .

Now which of the following is true about  𝑈  and  𝑉𝑇 ? (Choose all those apply. )

Answer = The first row of  𝑈  represents information on user 1's rating tendency

Answer = The first column of  𝑉𝑇  represents information on movie 1


