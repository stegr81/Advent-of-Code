from collections import defaultdict

with open("Day7/20221207-AOC-Day7-Input.txt", "r") as f:
    structure = f.readlines()

#part 1

sizes = defaultdict(int)
directories = []
for line in structure:
    match line.split():
        case [_, _, "/"]:
            directories = []
        case [_, _, ".."]:
            directories.pop()
        case [_, _, x]:
            directories.append(x)
        case [a, _] if a.isnumeric():
            for i in range(len(directories)+1):
                path = "/" + "/".join(directories[:i])
                sizes[path] += int(a)

print(sum([x for x in sizes.values() if x<=100000]))

#part 2

available = 70000000 - sizes['/']
need = 30000000 - available
print(available)
print(need)
print(min([x for x in sizes.values() if x>=need]))




