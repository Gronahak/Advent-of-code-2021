

def part_1():
    debug = "_debug" if DEBUG_MODE else ""
    path_to_file = f"DAY_2/input{debug}.txt"

    x = y = 0

    with open(path_to_file, "r") as f:
        for l in f.readlines():
            action, amount = l.strip().split()
            amount = int(amount)
            if action == "forward":
                x += amount
            if action == "up":
                y -= amount
            if action == "down":
                y += amount

    print(x*y)




def part_2():
    debug = "_debug" if DEBUG_MODE else ""
    path_to_file = f"DAY_2/input{debug}.txt"

    x = y = aim = 0

    with open(path_to_file, "r") as f:
        for l in f.readlines():
            action, amount = l.strip().split()
            amount = int(amount)
            if action == "forward":
                x += amount
                y -= amount*aim
            if action == "up":
                aim -= amount
            if action == "down":
                aim += amount

    print(-x*y)



DEBUG_MODE = False

RUN_PART = part_2

if __name__ == "__main__":
    RUN_PART()