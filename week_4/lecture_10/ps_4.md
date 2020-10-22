# Problem set 4


## Gating and LSTM


### Gating

Recall that the most simple, single-layered RNN can be written in equation as:

𝑠𝑡=tanh(𝑊𝑠,𝑠𝑠𝑡−1+𝑊𝑠,𝑥𝑥𝑡). 
 
Recognize that, in the above formulation,  𝑠𝑡  is always overwritten with the calculated result  tanh(𝑊𝑠,𝑠𝑠𝑡−1+𝑊𝑠,𝑥𝑥𝑡) .

Now, we introduce a gate vector  𝑔𝑡  of the same dimension as  𝑠𝑡 , which determines "how much information to overwrite in the next state." In equation, a single-layered gated RNN can be written as:

 	 𝑔𝑡 	 =sigmoid(𝑊𝑔,𝑠𝑠𝑡−1+𝑊𝑔,𝑥𝑥𝑡) 	 	 
 	 𝑠𝑡 	 =(1−𝑔𝑡)⨀𝑠𝑡−1+𝑔𝑡⨀tanh(𝑊𝑠,𝑠𝑠𝑡−1+𝑊𝑠,𝑥𝑥𝑡). 	 	 
where the sign  ⨀  denotes element-wise multiplication. Now, which of the following is true about the gate  𝑔𝑡 ?
(Choose all those apply.)

Answer = If the  𝑖 th element of  𝑔𝑡  is 0, the  𝑖 th element of  𝑠𝑡  and that of  𝑠𝑡−1  are equal

Answer = If  𝑔𝑡  is a vector whose elements are all 0,  𝑠𝑡  and  𝑠𝑡−1  are equal


### LSTM

Which of the following components of an LSTM represent the context or state? (Choose all that apply.)

Answer = ct

Answer = ht


### LSTM Calculations


Let all the neural network's weight matrices, the hidden state, and the memory cell be a scalar  1 . Let the new  𝑥 -value be  5 . Calculate the value of the new hidden state. Round sigmoid to  1  or  0 , and round  tanh  to  −1  or  1 .


Answer = 1
