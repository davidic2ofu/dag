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
		edge = tuple([int(x.strip(',')) for x in a.split()])
		edges.add(edge)
	return edges


def bellman_ford(vertices, edges):
	dist = {}
	prev = {}
	for v in vertices:
		dist[v] = 999999
		prev[v] = None
	# print('vertices in bf:', dist, prev, edges)
	# s = vertices[random.randint(0, len(vertices) - 1)]
	s = 1
	dist[s] = 0
	is_cyclic = False
	for i in range(len(vertices) - 1):
		for e in edges:
			u, v = e[0], e[1]
			if dist[v] > dist[u] + 1:   # subtract 1 to get longest path (add for shortest)

# need better test for back edges, maybe dfs in separate function
				if dist[v] < 999999: # and dist[u] == 999999: 
					# need to test for back edges

				# 	path_from_u = set(find_path(prev, u))
				# 	path_from_v = set(find_path(prev, v))
				# 	print('PATHS: ', path_from_u, path_from_v)
				# 	common_vertices = path_from_v.intersection(path_from_u)
				# 	if len(common_vertices) > 0:

						is_cyclic = True
				dist[v] = dist[u] + 1
				prev[v] = u
	print('distances: {}\nprevious: {}\n'.format(dist, prev))
	return dist, prev, is_cyclic


def get_linear_ordering(vertices, edges):
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
	def _find_path(val):
		return [val] if val == 1 else [val] + _find_path(prev[val])
	return _find_path(len(prev))  # assumes last vertex is the highest num in v list


if __name__ == '__main__':
	print(instructions)
	vertices = get_vertices()
	edges = get_edges()
	dist, prev, is_cyclic = bellman_ford(vertices, edges)
	print(vertices, edges)
	if is_cyclic:
		print("NO... Graph is cyclic, therefore not a DAG")
		exit()
	linear_ordering = get_linear_ordering(vertices, edges)
	print('linear ordering: ', linear_ordering)
	path = find_path(prev)
	print(path)

