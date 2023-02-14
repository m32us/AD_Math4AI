a = [1, 2, 3, 4, 5]


def listed_binary(n):
    if n == 0:
        yield ""
    else:
        for bit in ('0', '1'):
            yield from (sbit+bit for sbit in listed_binary(n-1))


def masking(inp_set, str_bin):
    return map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(inp_set, str_bin)))


def ssp(inp_set, target):
    masks = list(listed_binary(len(inp_set)))
    for mask in masks:
        pick_set = list(masking(inp_set, mask))
        if sum(pick_set) == target:
            yield pick_set

# print(list(ssp(a, 7)))

def combination_of_n(inp_set, target):
    masks = list(listed_binary(len(inp_set)))
    for mask in masks:
        pick_set = list(masking(inp_set, mask))
        if len(pick_set) == target:
            yield pick_set

# print(list(combination_of_n(a, 4)))

def permutations():
    global running
    global characters
    global bitmask

    if len(running) == len(characters):
        print(''.join(str(running)))
    else:
        for i in range(len(characters)):
            if ((bitmask >> i) & 1) == 0:
                bitmask |= 1 << i
                running.append(characters[i])
                permutations()
                bitmask ^= 1 << i  # make the bit zero again.
                running.pop()

characters = list(a)
running = []
bitmask = 0
permutations()