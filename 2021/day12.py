# Part 1
lines = text.splitlines()
pairs = [line.split('-') for line in lines]
neighbors = {}

for first, second in pairs:
    neighbors.setdefault(first, []).append(second)
    neighbors.setdefault(second, []).append(first)

def count():
    total = 0
    visited = set()
    def visit(node):
        nonlocal total
        visited.add(node)
        if node == 'end':
            total += 1
            visited.remove(node)
            return
        for neighbor in neighbors[node]:
            if neighbor.isupper():
                visit(neighbor)
            elif neighbor.islower() and neighbor not in visited:
                visit(neighbor)
        visited.discard(node)
    visit('start')
    return total

count()

# Part 2
def count():
    total = 0
    visited = {key: 0 for key in neighbors}
    def visit(node):
        nonlocal total
        visited[node] += 1
        if node == 'end':
            total += 1
            visited[node] -= 1
            return
        for neighbor in neighbors[node]:
            if neighbor == 'start':
                continue
            elif neighbor.isupper():
                visit(neighbor)
            elif neighbor.islower():
                if visited[neighbor] == 0:
                    visit(neighbor)
                elif all(visited[key] < 2 for key in visited if key.islower()):
                    visit(neighbor)
        visited[node] -= 1
    visit('start')
    return total

count()
