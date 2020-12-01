# Bellman Equations



Recall from lecture the Bellman Equations are

 	 𝑉∗(𝑠) 	 = 	 max𝑎𝑄∗(𝑠,𝑎) 	 	 
 	 𝑄∗(𝑠,𝑎) 	 = 	 ∑𝑠′𝑇(𝑠,𝑎,𝑠′)(𝑅(𝑠,𝑎,𝑠′)+𝛾𝑉∗(𝑠′)) 	 	 
where

the value function  𝑉∗(𝑠)  is the expected reward from starting at state  𝑠  and acting optimally.

the Q-function  𝑄∗(𝑠,𝑎)  is the expected reward from starting at state  𝑠 , then acting with action  𝑎 , and acting optimally afterwards.


## Value Function in Terms of Q Function

Let us work through a numerical example to understand the Bellman equations.

Let there be  4  possible actions,  𝑎1,𝑎2,𝑎3,𝑎4,  from a given state  𝑠 , and let the  𝑄∗  values be as follows:

 	 𝑄∗(𝑠,𝑎1) 	 = 	 10 	 	 
 	 𝑄∗(𝑠,𝑎2) 	 = 	 −1 	 	 
 	 𝑄∗(𝑠,𝑎3) 	 = 	 0 	 	 
 	 𝑄∗(𝑠,𝑎4) 	 = 	 11. 	 	 
Enter the value of  𝑉∗(𝑠)  below:


Answer = 11


## Bellman Equation for Q Function

As above, let there be  4  possible actions,  𝑎1,𝑎2,𝑎3,𝑎4,  from a given state  𝑠  wth  𝑄∗  values given below:

 	 𝑄∗(𝑠,𝑎1) 	 = 	 10 	 	 
 	 𝑄∗(𝑠,𝑎2) 	 = 	 −1 	 	 
 	 𝑄∗(𝑠,𝑎3) 	 = 	 0 	 	 
 	 𝑄∗(𝑠,𝑎4) 	 = 	 11. 	 	 
Let  𝑠′  be a state that can be reached from  𝑠  by taking the action  𝑎1 . Let

 	 𝑇(𝑠,𝑎1,𝑠′) 	 = 	 1 	 	 
 	 𝑅(𝑠,𝑎1,𝑠′) 	 = 	 5 	 	 
 	 𝛾 	 = 	 0.5. 	 	 
Enter the value of  𝑉∗(𝑠′)  below:


Answer = 10



