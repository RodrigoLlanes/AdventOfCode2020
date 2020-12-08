inp = [line.rstrip().split(" ") for line in open("input.txt")]

accumulator = 0
index = 0
loop_jmp_index = 298  # Sol1 repeated jmp instruction index

while index < len(inp):
    op = inp[index][0]
    arg = int(inp[index][1])

    if index == loop_jmp_index:
        pass
    elif op == "nop":
        pass
    elif op == "acc":
        accumulator += arg
    elif op == "jmp":
        index += arg - 1

    index += 1

print(accumulator)
