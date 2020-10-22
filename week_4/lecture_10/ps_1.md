# Problem set one


### Introduction to Recurrent Neural Networks



### Encoding Sequences with Feed-Forward Neural Networks

We have a temporal dataset of USD/EURO conversion rate from late 2012 to early 2017. Our goal is to predict the value of USD/EURO at the next timestep of early 2017.

If we are trying to encode the data into feature vectors for a feed-forward neural network, which of the following is the most viable strategy?

Answer = slide a window of size 10 and use the most recent 10 points as a feature vector


### Context for Predicting Next Word

What is the issue with predicting the next word in the sentence using the previous three words as context?
(Choose all that apply.)


Answer = Some words might need more context to predict correct
Answer = Some words might need less context to predict, and additional words could be inefficient correct
Answer = Some words might be closely related to words far away in the sentence correct
