from common_functions import solve

DAY = 7

MAX_SIZE_WANTED = 100000
total_sizes = 0


def solver(data: str) -> str:
    # initializing
    global root
    root = Node("/", None)
    curr_dir = root
    for line in data.splitlines():
        components = line.split()
        # will ignore "ls" command
        if components[0] == "$" and components[1] == "cd":
            curr_dir = change_dir(curr_dir, components[2])
        elif components[0] != "$":
            add_info(curr_dir, components)

    # finding answer
    dfs(root)

    return total_sizes


def change_dir(curr_dir, result_dir):
    if result_dir == "/":
        return root
    elif result_dir == "..":
        return curr_dir.parent
    else:
        return curr_dir.children[result_dir]


def add_info(directory, components):
    if components[0] == "dir":
        directory.children[components[1]] = Node(components[1], directory)
    else:
        directory.file_sizes += int(components[0])


def dfs(node):
    global total_sizes
    size = node.file_sizes
    for child in node.children.values():
        size += dfs(child)
    if size <= MAX_SIZE_WANTED:
        total_sizes += size
    return size


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}
        self.file_sizes = 0


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
