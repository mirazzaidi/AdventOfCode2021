from __future__ import annotations
from typing import List, Dict
from dataclasses import dataclass
from utils.utils import get_lines_from_file

@dataclass
class Cave:
    name: str
    connections: List[Cave]


all_paths = []
def dfs(node: Cave, path: str):
    path += node.name
    if node.name == 'end':
        all_paths.append(path)
        return
    path += ','
    
    connections: List[Cave] = [cave for cave in node.connections if cave.name !='start']
    for con in connections:
        if con == 'start':
            continue

        if con.name.islower() and con.name in path.split(','):
            continue

        dfs(con, path)


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
        if not end:
            if cave_a.name == 'end':
                end = cave_a
            elif cave_b.name == 'end':
                end = cave_b
    
    paths = ''
    dfs(start, paths)
    print("Answer is ", len(all_paths))






    









