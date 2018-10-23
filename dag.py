import random


instructions = '''

Programming Assignment 2:
DIRECTED ACYCLIC GRAPHS

This program takes as input a directed graph and outputs information about the graph.

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

OUTPUTS
=======
- 'YES' or 'NO' depending on whether the graph is a DAG

and in the case it is a DAG...

- a linear ordering of the DAG
- the length of the longest path in the DAG starting from vertex 1


'''


def get_vertices():
	'''
	Used for user input of vertices.
	'''
	num_vertices = int(input('\nEnter number of vertices: '))
	return [x for x in range(1, num_vertices + 1)]


def get_edges():
	'''
	Used for user input of edges.
	'''
	edges = set()
	while True:
		a = input('\nEnter value of edge: ')
		if not a:
			break
		edge = tuple([int(x.strip(',')) for x in a.split()])
		edges.add(edge)
	return edges


def bellman_ford(vertices, edges):
	'''
	Slight variation of Bellman Ford algorithm, subtracting edge weights instead of
	adding them.  In doing this, the longest path can be found, and if 'negative'
	cycles are found using the negative versions of the edge weights in the last
	loop, that means the graph is cyclic.
	'''
	dist = {}
	prev = {}
	for v in vertices:
		dist[v] = 999999
		prev[v] = None
	s = 1    # assumes starting vertex is vertex number 1
	dist[s] = 0
	is_cyclic = False
	for i in range(len(vertices) - 1):
		for e in edges:
			u, v = e[0], e[1]
			if dist[v] > dist[u] - 1:   # subtract 1 to get longest path (add for shortest)
				dist[v] = dist[u] - 1
				prev[v] = u
	# print('distances: {}\nprevious: {}\n'.format(dist, prev))
	for e in edges:
		u, v = e[0], e[1]
		if dist[v] > dist[u] - 1:
			is_cyclic = True

	return dist, prev, is_cyclic


def get_linear_ordering(vertices, edges):
	'''
	To get linear ordering, find vertex with minimum number of outgoing edges, add it
	to the list, remove it from the graph, then repeat (find a new vertex with the
	minimum number of outgoing edges and so forth) until all vertices have been removed
	from the graph. 
	'''
	vertex_list = vertices.copy()
	edge_list = edges.copy()
	linear_ordering = []
	while True:
		adjacency_index = { v: 0 for v in vertex_list }
		for (u, v) in edge_list:
			adjacency_index[v] += 1
		v_with_min_outgoing_edges = min(adjacency_index, key=adjacency_index.get)
		linear_ordering.append(v_with_min_outgoing_edges)
		vertex_list.remove(v_with_min_outgoing_edges)
		edges_to_remove = []
		for (u, v) in edge_list:
			if v_with_min_outgoing_edges in (u, v):
				edges_to_remove.append((u, v))
		for (u, v) in edges_to_remove:
			edge_list.remove((u, v))
		if not vertex_list:
			break
	return linear_ordering


def find_path(prev):
	'''
	Recursively finds the path using the prev dictionary returned from Bellman Ford
	'''
	def _find_path(val):
		return [val] if val == 1 else _find_path(prev[val]) + [val]
	return _find_path(len(prev))  # assumes destination vertex is the highest num in v list


if __name__ == '__main__':
	print(instructions)
	vertices = get_vertices()
	edges = get_edges()
	dist, prev, is_cyclic = bellman_ford(vertices, edges)
	# print(vertices, edges)
	if is_cyclic:
		print("\nNO ... (Graph is cyclic, therefore not a DAG)")
		exit()
	linear_ordering = get_linear_ordering(vertices, edges)
	print('\nLinear ordering: ', linear_ordering)
	path = find_path(prev)
	print('\nLongest path: {}'.format(path))
	print('\nLength of longest path: {}\n'.format(len(path)))

