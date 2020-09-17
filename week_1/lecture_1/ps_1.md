# Problem set one



## Feature Vector Demystified 1



We have a movie recommending system that reads description of each movie and determines some important characteristics of the movie. In particular, it examines whether each of the criterion below is true for that movie:

Is it a comedy movie?

Is it an action movie?

Was the movie directed by Spielberg?

Do dinosaurs appear in the movie?

Is it a Disney film?

For example, when the recommending system reads descriptions of "Jurassic Park", the answers for the five questions above will be "no, yes, yes, yes, no." On the other hand if the recommending system reads descriptions of "High School Musical", the answers will be "no, no, no, no, yes"

The system converts "yes" into 1, "no" into 0, and makes a feature vector  𝑋  for each movie. So  𝑋𝐽𝑢𝑟𝑟𝑎𝑠𝑖𝑐𝑃𝑎𝑟𝑘  will be  [0,1,1,1,0] , while  𝑋𝐻𝑖𝑔ℎ𝑆𝑐ℎ𝑜𝑜𝑙𝑀𝑢𝑠𝑖𝑐𝑎𝑙  will be  [0,0,0,0,1] 

Question 1: Now we have a comedy movie that is not an action movie, that was not directed by Spielberg, that does not have dinosaurs in it, but was produced by Disney. What is this movie's feature vector?

Answer = [1, 0, 0, 0, 1]


## Feature Vector Demystified 2

Question 2: What is the dimension of the feature vector of this movie?

Answer = 5



## Training Set vs Test Set 1

The ultimate goal of our recommending system is to predict whether John will like this movie. Now suppose our movie recommending system knows whether John likes or dislikes the following movies:

|         | comedy | action | Spielberg | Dinosaur Appearance | Disney | Liked by John? |
|:-------:|:------:|:------:|:---------:|:-------------------:|:------:|:--------------:|
| movie 1 |    0   |    1   |     0     |          0          |    1   |        1       |
| movie 2 |    1   |    1   |     1     |          0          |    0   |       -1       |
| movie 3 |    0   |    1   |     0     |          1          |    1   |        1       |
| movie 4 |    1   |    1   |     0     |          1          |    0   |        1       |


(Like is denoted as  1  and dislike as  −1  in the above table) On the other hand, the movie recommender does not know whether John likes the following movies when building the model, but will know them after the model is built:

|         | comedy | action | Spielberg | Dinosaur Appearance | Disney | Liked by John? |
|:-------:|:------:|:------:|:---------:|:-------------------:|:------:|:--------------:|
| movie 5 |    1   |    0   |     0     |          0          |    0   | Don't know yet |
| movie 6 |    0   |    0   |     0     |          0          |    1   | Don't know yet |
| movie 7 |    0   |    0   |     0     |          1          |    1   | Don't know yet |


Assume that, when John evaluates movies, he only does so based on the five criteria.

Question 1: What is the label of movie 1, based on the fact that John likes the movie?

Answer 1


## Training Set vs Test Set 2

Question 2: What movies are in the training set? Select all those apply.

Answer = Movie 1, Movie 2, Movie 3, Movie 4


## Training Set vs Test Set 3

Question 3: What movies are in the test set? Select all those apply.

Answer = Movie 5, Movie 6, Movie 7





