from pathlib import Path

p1 = Path('files/abd.txt')
print(type(p1))

if not p1.exists():
    with open(p1, 'w') as file:
        file.write('Content 3')

print(p1.name)  # print filename
print(p1.stem)  # print file name without extension
print(p1.suffix)  # print file extension

p2 = Path('../files')
print(p2.iterdir())
for item in p2.iterdir():
    print(item)

print(list(p2.iterdir()))
