# Homework part 4

A hyperplane in  𝑛  dimensions is a  𝑛−1  dimensional subspace. For instance, a hyperplane in  2 -dimensional space can be any line in that space and a hyperplane in  3 -dimensional space can be any plane in that space. A hyperplane separates a space into two sides.

In general, a hyperplane in  𝑛 -dimensional space can be written as  𝜃0+𝜃1𝑥1+𝜃2𝑥2+⋯+𝜃𝑛𝑥𝑛=0.  For example, a hyperplane in two dimensions, which is a line, can be expressed as  𝐴𝑥1+𝐵𝑥2+𝐶=0 .


Using this representation of a plane, we can define a plane given an  𝑛 -dimensional vector:  
```
	   ⎡𝜃1⎤
	𝜃= ⎥𝜃2⎥
	   ⎥ ⋮⎥
	   ⎣𝜃n⎦
```
and offset  𝜃0 . This vector and offset combination would define the plane  𝜃0+𝜃1𝑥1+𝜃2𝑥2+⋯+𝜃𝑛𝑥𝑛=0.  One feature of this representation is that the vector  𝜃  is normal to the plane.

# Number of Representations

## 1) 

Given a  𝑑 -dimensional vector  𝜃  and a scalar offset  𝜃0  which describe a hyperplane  P:𝜃⋅𝑥+𝜃0=0 . How many alternative descriptions  𝜃′  and  𝜃′0  are there for this plane P?

Answer = 

# Orthogonality Check

To check if a vector  𝑥  is orthogonal to a plane    characterized by  𝜃  and  𝜃0 , we check whether

𝑥=𝛼𝜃 for some 𝛼∈ℝ


# Perpendicular Distance to Plane

Given a point  𝑥  in  𝑛 -dimensional space and a hyperplane described by  𝜃  and  𝜃0,  find the signed distance between the hyperplane and  𝑥 . This is equal to the perpendicular distance between the hyperplane and  𝑥 , and is positive when  𝑥  is on the same side of the plane as  𝜃  points and negative when  𝑥  is on the opposite side.

(Enter theta_0 for the offset  𝜃0 .
Enter norm(theta) for the norm  ‖𝜃‖  of a vector  𝜃 .
Use * to denote the dot product of two vectors, e.g. enter v*w for the dot product  𝑣⋅𝑤  of the vectors  𝑣  and  𝑤 . )

Answer = 


# Orthogonal Projection onto Plane

Find an expression for the orthogonal projection of a point  𝑣  onto a plane    that is characterized by  𝜃  and  𝜃0 . Write your answer in terms of  𝑣 ,  𝜃  and  𝜃0 .

(Enter theta_0 for the offset  𝜃0 .
Enter norm(theta) for the norm  ‖𝜃‖  of a vector  𝜃 .
Use * to denote the dot product of two vectors, e.g. enter v*w for the dot product  𝑣⋅𝑤  of the vectors  𝑣  and  𝑤 . )

Answer = 


# Perpendicular Distance to Plane


Let  1  be the hyperplane consisting of the set of points  𝑥=[𝑥1𝑥2]  for which  3𝑥1+𝑥2−1=0 . (Note that this hyperplane is in fact a line, since it is 1-dimensional.)

What is the signed perpendicular distance of point  𝑎=[−1,−1]  from  1 ?

Answer = 

What is the signed perpendicular distance of the origin from  1 ?

Answer = 

What is the orthogonal projection of point  𝑎=[−1,−1]  onto  𝑝1 ?

First coordinate:

Second coordinate:










