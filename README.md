# MITx-6.86x Machine Learning with Python


## Notes (cmd+f cheatsheet)

### Contents

* Formular searches
* key words
* Points and vectors
* Planes
* Loss Function
* Gradient Decent
* Chain Rule


## Formular Searches

* Sigmaa/Sumnation: summation 1, k=1..K, t=1..T
* 

## Key words

* **Points:** A data point
* **Vector:** A line from the origin to a data point
* **Origin:** The n 0's of any dimentional graph
* **Norm:** Using Euclidean distance the norm will be the √ of all of the vectors items.
* **Euclidean Distance:** The "ordinary" straight-line distance between two points
* **Dot Product:** How the vectors are arranged relative to each other
* **plane:** A slice through n dimensions. All the points that fit on the slice
* **hyperplane:** n-1 dimensions. A subspace whose dimension is one less than that of its ambient space. If a space is 3-dimensional then its hyperplanes are the 2-dimensional planes, while if the space is 2-dimensional, its hyperplanes are the 1-dimensional lines.



## Points and Vectors

* Data points will be written as [3,2,2]. The coordinates of the plotted data point
* A vector, x. The data points are all of it's coordinates
```
Vector:
     _
    |3|
x = |2|
    |2|
     -
```
* To get the index of a dimension, xi, we write it like this x1 which will = 3 in the above example.
* Adding vector together. The distance between 2 vectors (A, B), distance = (C) will be: A+C = B, C = B-A
* Vector size: Find the vector size using the norm (The √ of all of the vector items)
* Dot product: How the eliments are arranged relative to each other. We can find that by multiplying the relative data points:
```
The dot product (algerbraic):
     _          _        _
    |3|        |3|      |9|
x = |2| *  y = |3|  z = |6|   
    |2|        |4|      |8|
     -          -        -

When thinking about  𝑎  and  𝑏  as vectors in  𝑛 -dimensional space, we can also express the dot product as:
	𝑎⋅𝑏 = ‖𝑎‖‖𝑏‖cos𝛼
where  𝛼  is the angle formed between the vectors  𝑎  and  𝑏  in  𝑛 -dimensional Euclidean space. Here,  ‖𝑎‖  refers to the length, also known as norm, of  𝑎 :
	‖𝑎‖ = √𝑎2/1 + 𝑎2/2 + ...+𝑎2𝑛


Geometric version: x*y = |x|(norm) |y|(norm) * cosign (cos) of the angle between them
``` 


## Planes

<img src="img/Plane_1001.gif" alt="Neural Network" width="500"/>
<hr />

* A plane is a slice through n dimensions. 
* A typical use case for it will be to seperate data for classification (see the SVM algorithm or an example)

####  Defining a plane: 

* **A normal**: A vector in the plane in which all other points in this plane are perpendicular to this point. We will define this normal as Θ
* **An offset:** The distance from the origin to the plane. we will define this as X
```
Θ = normal 
X = offset
```

#### Find all of the points that fall on the plane:

* Take another point, defined as P. 
* P will only be on the plane if it is perpendicular to Θ

```
(P - X) * Θ = 0
(P * Θ) - (X*Θ) = 0
       |_______|
     P + Θ + Θo = 0

Any point that saitifies this linear relationship is on this plane
```



# Loss Function

* A way to determin how far away the model is from the data


# Gradient Distance

* Methodology for figuring out how to minimize the cost function by changing weight and bias terms throughout the network


# Chain Rule

* The chain rule is a formula to compute the derivative of a composite function





