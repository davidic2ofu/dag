import random


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


def get_vertices():
	num_vertices = int(input('\nEnter number of vertices: '))
	return [x for x in range(1, num_vertices + 1)]


def get_edges():
	edges = set()
	while True:
		a = input('\nEnter value of edge: ')
		if not a:
			break
		edge = tuple(sorted([int(x.strip(',')) for x in a.split()]))
		edges.add(edge)
	return edges


def bellman_ford(vertices, edges):
	dist = {}
	prev = {}
	for v in vertices:
		dist[v] = 999999
		prev[v] = None
	print('vertices in bf:', dist, prev, edges)
	# s = vertices[random.randint(0, len(vertices) - 1)]
	s = 1
	dist[s] = 0
	for i in range(len(vertices) - 1):
		for e in edges:
			print('e', e[0], e[1])
			u, v = e[0], e[1]
			if dist[v] > dist[u] + 1 and dist[u] != 999999:
				dist[v] = dist[u] + 1
				prev[v] = u
	print('distances: {}\nprevious: {}\n'.format(dist, prev))


if __name__ == '__main__':
	print(instructions)
	vertices = get_vertices()
	edges = get_edges()
	bellman_ford(vertices, edges)

