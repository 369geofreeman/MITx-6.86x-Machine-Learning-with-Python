# Problem Set Five


## Alternating Minimization


### Alternating Minimization Concept Question

As in the video above, we now want to find  𝑈  and  𝑉  that minimize our new objective

𝐽=∑(𝑎,𝑖)∈𝐷(𝑌𝑎𝑖−[𝑈𝑉𝑇]𝑎𝑖)22+𝜆2(∑𝑎,𝑘𝑈2𝑎𝑘+∑𝑖,𝑘𝑉2𝑖𝑘). 
 
To simplify the problem, we fix  𝑈  and solve for  𝑉 , then fix  𝑉  to be the result from the previous step and solve for  𝑈 , and repeat this alternate process until we find the solution.

Consider the case  𝑘=1 . The matrices  𝑈  and  𝑉  reduce to vectors  𝑢  and  𝑣,  such that  𝑢𝑎=𝑈𝑎1  and  𝑣𝑖=𝑉𝑖1 .

When  𝑣  is fixed, minimizing  𝐽  becomes equivalent to minimizing ...

Answer = ∑(𝑎,𝑖)∈𝐷(𝑌𝑎𝑖−𝑢𝑎𝑣𝑖)22+𝜆2∑𝑎(𝑢𝑎)2

Solution:

Regarding terms containing only  𝑉  as constants, minimizing  𝐽  is equivalent to minimizing

 	 ∑(𝑎,𝑖)∈𝐷(𝑌𝑎𝑖−𝑢𝑎𝑣𝑖)22+𝜆2∑𝑎(𝑢𝑎)2. 	 


### Fixing V and Finding U

Now, assume we have 2 users, 3 movies, and a 2 by 3 matrix  𝑌  given by

 	 𝑌=[128??5] 	 	 
Our goal is to find  𝑈  and  𝑉  such that  𝑋=𝑈𝑉𝑇  closely approximates the observed ratings in  𝑌 .

Assume we start by fixing  𝑉  to initial values of  [4,2,1]𝑇 . Find the optimal  2×1  vector  𝑈  in this case. (Express your answer in terms of  𝜆 ).

First element of  𝑈  is:

Answer =  20/(lambda+20)

The second element of  𝑈  is:

Answer = 13/(lambda+17)
