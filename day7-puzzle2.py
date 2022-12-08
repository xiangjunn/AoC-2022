from common_functions import solve

DAY = 7

TOTAL_SPACE = 70_000_000
NEEDED_SPACE = 30_000_000


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

    # finding amount of space to be deleted
    global directories_space
    directories_space = []
    unused = TOTAL_SPACE - dfs(root)
    needs_deletion = NEEDED_SPACE - unused
    if needs_deletion < 0:
        return 0
    # sort and find the first directory with size > needs_deletion
    directories_space.sort()
    for dir_size in directories_space:
        if dir_size >= needs_deletion:
            return dir_size


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
    size = node.file_sizes
    for child in node.children.values():
        size += dfs(child)
    directories_space.append(size)
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
