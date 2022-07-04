# Finding holes in binary zonotopes

holes/enumeration.py enumerates the vectors b in the hypercube enclosing the zonotope. If Ax=b is feasible for 0<=x<=1, it verifies whether it also is for x in {0, 1}.

|  Zonotope generators | Highest value of m verified |
| -------------------- | --------------------------- |
| Complete set         |             7               |
| At most 3 ones       |             8               |

# Generating facets of the complete binary zonotope

facets/fullfacets.py takes all families of size m-1 of binary vectors, computes their kernel. If it has dimension 1, it adds the normal and its opposite to the list. The normals are scaled to make integer, and the list is writting in facets[m]-full.

facets/generatingfacets.py takes the normals of facets[m-1]-full and generates normals in dimension m using the construction of facets/construction.pdf. It also adds opposites and permutations, and writes all normals in facets[m]-gen.

|  m  | Number of facets | Number of generated facets |
| --- | ---------------- | -------------------------- |
|  2  |        6         |             6              |
|  3  |        18        |             18             |
|  4  |        90        |             82             |
|  5  |      1 250       |            900             |
|  6  |      57 750      |           26 216           |

facets/seymourfacets.py generates the facets from Seymour's algorithm for hyperplanes of matroids. It runs quadratically in the number of facets.

# Number of vertices of the complete binary zonotope

This table is for comparison with the number of facets. These values act like 2^(m²) asymptotically.

|  m  | Number of vertices | 
| --- | ------------------ |
|  2  |          6         |
|  3  |          32        |
|  4  |         370        |
|  5  |      1 066 044     |
|  6  |     347 326 352    | 

Source: http://oeis.org/A034997

# Plots

Logarithm base 2 of the number of vertices, facets of the complete binary zonotope in dimension m, in comparison with m² and m\*mlog(m) functions. 

![plot](https://github.com/Mattuuuuh/binaryZonotope/blob/main/plots/facetsandvertices.png?raw=true)
