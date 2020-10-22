# problem set three

## Encoding with RNN


### Which is Which


As discussed in the lecture, the following is a typical structure of a single-layered recurrent neural network.


The structure above is often expressed like the following in terms of equations:

𝑠𝑡=tanh(𝑊𝑠,𝑠𝑠𝑡−1+𝑊𝑠,𝑥𝑥𝑡) 
 
Now, which element of the picture corresponds to  𝑠𝑡  in the equation above?


Answer = Above

Which element of the picture corresponds to  𝑥𝑡  in the equation above?

Answer = new Information

Which element of the picture corresponds to  𝑠𝑡−1  in the equation above?

Answer = context or state

Which of the following are "parameters" of the recurrent neural network?
(Choose all those apply.)

Answer =  𝑊 𝑠,𝑠
Answer =  𝑊 𝑠,𝑥

What is the role represented by  𝑊 𝑠,𝑥 ?

Answer = deciding what part of the previous information to keep

### Hidden State

For  𝑠  as defined in the lecture, where  𝑠0  is the null vector, take the sentence “Efforts and courage are not in vain". Which of the following contain(s) information about the phrase “Efforts and courage", i.e., the first three words in the sentence? (Choose all those apply.)

Answer = s3
Answer = s4
Answer = s5


### Encoding Sentences

Which of the following is true about encoding sentences with RNNs?
(Choose all those apply.)

Answer = input is received at each layer (per word), not just at the beginning as in a typical feed-forward network

Answer = the number of layers varies and depends on the length of the sentence

Answer = parameters of each layer are shared


