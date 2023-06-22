from collections import deque

def bfs(graph, from_person, search_person):

	if not from_person in graph: 
		return False

	# deque is doubly linked queue 
	search_queue = deque()
	search_queue += graph[from_person]

	searched = []
	length = 1
	
	while search_queue:
		person = search_queue.popleft()

		if not person in searched: 
			if person == search_person:
				return True

			searched.append(person)
			if person in graph:
				search_queue += graph[person]

	return False

graph = {}
graph["me"] = ["father", "mother", "sister", "wife"]
graph["father"] = ["grandfather", "grandmother", "aunty", "uncle"]
graph["mother"] = ["me", "father"]
graph["wife"] = ["father in law", "mother in law", "brother in law"]
graph["sister"] = ["niece"]

print(bfs(graph, 'me', 'niece'))

