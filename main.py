graph = {
    'S': ['A', 'B'],
    'A': ['B', 'C', 'G'],
    'B': ['C'],
    'C': ['G'],
    'G': []
}
def bfs(graph, start, goal):
    visitedNode = []
    queue = [[start]]
    while queue:
        graphPath = queue.pop(0)
        node = graphPath[-1]
        if node in visitedNode:
            continue
        visitedNode.append(node)
        if node == goal:
            return graphPath
        else:
            nearbyNode = graph.get(node, [])
        for secNode in nearbyNode:
            newGraphPath = graphPath.copy()
            newGraphPath.append(secNode)
            queue.append(newGraphPath)

def dfs(graph, start, goal):
    visitedNode = []
    stack = [[start]]
    while stack:
        graphPath = stack.pop()
        node = graphPath[-1]
        if node in visitedNode:
            continue
        visitedNode.append(node)
        if node == goal:
            return graphPath
        else:
            nearbyNode = graph.get(node, [])
        for secNode in nearbyNode:
            newGraphPath = graphPath.copy()
            newGraphPath.append(secNode)
            stack.append(newGraphPath)

SolutionPathBFS = bfs(graph, 'S', 'G')
print('Solution Path For BFS is ', SolutionPathBFS)

SolutionPathDFS = dfs(graph, 'S', 'G')
print('Solution Path For DFS is ', SolutionPathDFS)