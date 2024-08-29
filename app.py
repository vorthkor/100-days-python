import os

print("create py files")

for name in range(31,51):
    print(name)
    # os.system(f"rm day00{name}.py")
    os.system(f"code src/day0{name}.py")
    # f = open(f"src/day0{name}.py","+a")
    # f.write(f"# day {name}")
    # f.close()