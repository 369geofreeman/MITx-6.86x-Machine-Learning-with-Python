# Q-value Iteration


The derivation of the Q-value iteration update rule from the equation above is similar to the derivation of the value iteration update rule.

First, recall the Bellman equations:

 	 𝑉∗(𝑠) 	 = 	 max𝑎𝑄∗(𝑠,𝑎) 	 	 
 	 𝑄∗(𝑠,𝑎) 	 = 	 ∑𝑠′𝑇(𝑠,𝑎,𝑠′)(𝑅(𝑠,𝑎,𝑠′)+𝛾𝑉∗(𝑠′)). 	 	 
Plugging first equation into the second, we get:

 	 𝑄∗(𝑠,𝑎) 	 = 	 ∑𝑠′𝑇(𝑠,𝑎,𝑠′)(𝑅(𝑠,𝑎,𝑠′)+𝛾max𝑎′𝑄∗(𝑠′,𝑎′)). 	 	 
Now, let  𝑄∗𝑘(𝑠,𝑎)  be the expected rewards from state  𝑠  followed by action  𝑎 , and then acting optimally for  𝑘  steps afterwards. (Hence,  𝑉∗𝑘(𝑠)=max𝑎𝑄∗𝑘(𝑠,𝑎) .)


## Q-Value Iteration Update Rule


Referring to the equations above, what should the Q-value iteration update rule be?

Answer = 𝑄∗𝑘+1(𝑠,𝑎)=∑𝑠′𝑇(𝑠,𝑎,𝑠′)(𝑅(𝑠,𝑎,𝑠′)+𝛾max𝑎′𝑄∗𝑘(𝑠′,𝑎′))



