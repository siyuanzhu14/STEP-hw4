#depth first traversal
def dft(graph, start, visited=None):
    if visited is None:
        visited = []
    if start not in visited:
        visited += [start]
    for next in set(graph[start]) - set(visited):
        #vertices start points to and are not visited
        dft(graph, next, visited)
    return visited

#breadth first traversal
def bft(graph, start):
    visited = [start]
    q = []
    q.insert(0,start) #q is a queue, so the inserted vertex is in the first position
    while q:
        next = q.pop()
        for next in set(graph[next]) - set(visited):
            q.insert(0,next)
            visited += [next]
    return visited


#get if the graph is connected(each vertex can go to any other vertex)
def is_connected(graph, visited = None, start=None):
    if visited is None:
        visited = set()       
    vertices = list(graph.keys()) 
    if not start:
        start = vertices[0]
    visited.add(start)
    if len(visited) != len(vertices):
        for vertex in graph[start]:
            if vertex not in visited:
                if is_connected(graph,visited, vertex):
                    #check all the subgraphs linking with the vertex
                    return True
    else:
        return True
    return False


#retrun a path from start to end.
def find_path(graph, start, end, path=None, visited=None):
    if path == None:
        path = []
    path = path + [start]
    
    if visited == None:
        visited = []
    visited += [start]
    
    if start == end:
        return path
    if start not in graph:
        return None

    tempSet = set(graph[start])-set(visited)
    if end in tempSet:
        return path + [end]
    
    for vertex in tempSet:
        if vertex not in path:
            extended_path = find_path(graph,vertex, end, path, visited)
            if extended_path: 
                return extended_path
    return None


def find_isolated_vertices(graph):
    isolated = []
    for vertex in graph:
        if not graph[vertex]:
            isolated += [vertex]
    return isolated



with open('links.txt', 'r') as f:
    linksSet = [link.strip().split() for link in f.readlines()]
links = {}
tempKey = 0
for link in linksSet:
    if tempKey != link[0]:
        links.update({link[0]:[link[1]]})
    else:
        links[link[0]].append(link[1])
    tempKey = link[0]
#links is the dictionary showing all the vertices that a vertex points to

with open('nicknames.txt', 'r') as f:
    nicknames = dict(link.strip().split() for link in f.readlines())

#reverse the nicknames dictionary so that can search index from name
inv_nicknames = {name: index for index, name in nicknames.items()}

bft_list = bft(links,'0')
bft_list = [nicknames[index] for index in bft_list]
print('all the accounts in breadth first method:\n', bft_list, '\n')

dft_list = dft(links,'0')
bft_list = [nicknames[index] for index in dft_list]
print('all the accounts in depth first method:\n', bft_list, '\n')

#a path between jacob and craig(0)
path = [nicknames[index] for index in find_path(links, inv_nicknames['jacob'], inv_nicknames['craig'])]
print('A path from jacob to me(craig) is :\n', path,'\n')


connected = is_connected(links)
if not connected:
    print('The SNS network is not connected.', '\n')
else:
    print('The SNS network is connected.', '\n')

isolated = find_isolated_vertices(links)
if not isolated:
    print('No isolated account', '\n')
else:
    print('Isolatex accounts are', isolated, '\n')
