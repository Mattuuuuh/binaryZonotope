# Finding holes in binary zonotopes

holes/enumeration.py enumerates the vectors b in the hypercube enclosing the zonotope. If Ax=b is feasible for 0<=x<=1, it verifies whether it also is for x in {0, 1}.

|  Zonotope generators | Highest value of m verified |
| -------------------- | --------------------------- |
| Complete set         |             7               |
| At most 3 ones       |             7               |

# Generating facets of the complete binary zonotope

facets/fullfacets.py takes all families of size m-1 of binary vectors, computes their kernel. If it has dimension 1, it adds the normal and its opposite to the list. The normals are scaled to make integer, and the list is writting in facets[m]-full.

facets/generatingfacets.py takes the normals of facets[m-1]-full and generates normals in dimension m using the construction of facets/construction.pdf. It also adds opposites and permutations, and writes all normals in facets[m]-gen.

|  m  | Number of facets | Number of generated facets |
| --- | ---------------- | -------------------------- |
|  2  |        6         |             6              |
|  3  |        18        |             18             |
|  4  |        90        |             82             |
|  5  |       1250       |            900             |
|  6  |      57 750      |           26 216           |

# Number of vertices of the complete binary zonotope

|  m  | Number of vertices | 
| --- | ------------------ |
|  2  |          6         |
|  3  |          32        |
|  4  |         370        |
|  5  |      1 066 044     |
|  6  |     347 326 352    | 

Source: http://oeis.org/A034997
6, 32, 370, 11292, 1066044, 347326352
