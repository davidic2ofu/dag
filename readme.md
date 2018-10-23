David Rosenberg
U00063482
COMP 7712 Algorithms
Programming Assignment 2
Submitted Oct 25, 2018



## Programming Assignment 2: Directed Acyclic Graphs

### To the grader:

Program written in Python 3.

To execute the program, please run the following, with Python 3.x installed:

`python3 dag.py`

This program takes as input a directed graph and outputs information about the graph.

### INPUTS

- A positive integer n, the number of vertices in the graph:
   the names of the vertices will be 1, 2, 3, ..., n.
- The next few lines will contain the edges of the graph as
   i, j 
  where _1 <= i <= n_ and _1 <= j <= n_ and _i != j_.

  Example of valid input:
    5
    1, 2
    3, 4
    3, 1

### OUTPUTS

- 'YES' or 'NO' depending on whether the graph is a DAG

and in the case it is a DAG...
- a linear ordering of the DAG
- the length of the longest path in the DAG starting from vertex 1

Thank you,
DR
