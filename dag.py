

instructions = '''

Programming Assignment 2:
Directed Acyclic Graphs

This program takes as input a directed graph and outputs
- 'YES' or 'NO' depending on whether the graph is a DAG

and in the case it is a DAG...
- a linear ordering of the DAG
- the length of the longest path in the DAG starting from vertex 1

INPUTS
======
- A positive integer n, the number of vertices in the graph:
   the names of the vertices will be 1, 2, 3, ..., n.
- The next few lines will contain the edges of the graph as
   i, j 
  where 1 <= i <=n and 1 <= j <= n and i != j.

  Example of valid input:
    5
    1, 2
    3, 4
    3, 1

'''


def get_num_vertices():
	return int(input('\nEnter number of vertices: '))


def get_edges():
	edges = []
	while True:
		a = input('\nEnter value of edge: ')
		if not a:
			break
		edge = tuple([x.strip(',') for x in a.split()])
		edges.append(edge)
	return edges


if __name__ == '__main__':
	print(instructions)
	num_vertices = get_num_vertices()
	edges = get_edges()
