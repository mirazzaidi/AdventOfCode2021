from __future__ import annotations
from typing import List, Dict
from dataclasses import dataclass
from utils.utils import get_lines_from_file


@dataclass
class Cave:
    name: str
    connections: List[Cave]


all_paths = []


def dfs(node: Cave, path: str, one_small_cave_visited_twice=False):

    path += node.name

    if node.name == 'end':
        all_paths.append(path)
        # print (path)
        return
    path += ','

    for connected_cave in node.connections:
        if connected_cave.name == 'start':
            continue

        if connected_cave.name.islower():
            all_nodes = path.split(',')
            if connected_cave.name not in all_nodes:
                dfs(connected_cave, path, one_small_cave_visited_twice)
            elif all_nodes.count(connected_cave.name) < 2 and not one_small_cave_visited_twice:
                dfs(connected_cave, path, one_small_cave_visited_twice=True)
            else:
                continue
        else:
            dfs(connected_cave, path, one_small_cave_visited_twice)


if __name__ == "__main__":
    lines = get_lines_from_file('day-12/input')

    cave_list: Dict[str, Cave] = {}

    start = None
    end = None

    for line in lines:
        a, b = line.split('-')

        cave_a = cave_list.get(a)
        cave_b = cave_list.get(b)

        if not cave_a:
            cave_a = Cave(a, [])
        if not cave_b:
            cave_b = Cave(b, [])

        cave_list[a] = cave_a
        cave_list[b] = cave_b

        cave_a.connections.append(cave_b)
        cave_b.connections.append(cave_a)

        if not start:
            if cave_a.name == 'start':
                start = cave_a
            elif cave_b.name == 'start':
                start = cave_b

    paths = ''
    dfs(start, paths)

    print("Answer is ", len(all_paths))
