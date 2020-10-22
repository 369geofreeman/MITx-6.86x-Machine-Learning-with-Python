# Problem set 4


## RNN Decoding


### Decoding with RNN


Now, we would like to decode a feature vector with RNN's. The picture below illustrates how a vector encoding of the English sentence "I have seen better lectures" is translated into a sentence of a foreign language.


Unlike in encoding, at each step, an output distribution  𝑝𝑡  is produced in a decoding RNN.


Now, which of the following is true about decoding RNN's?
(Choose all those apply.)


Answer = In the first image, the foreign word "Olen" in the above picture is a "sampled" result from a distribution the RNN produced



### Predictions


Suppose we are building an RNN model to translate images into sentences, as described in the lecture. Which of the following is only done in generating the predictions of sentences from a trained RNN given the test images but not in the training process?

Amswer = Feeding the sampled output as part of the input to the next time step
