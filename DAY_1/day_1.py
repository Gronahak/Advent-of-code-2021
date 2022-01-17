

def part_1():
    got_up = 0

    debug = "_debug" if DEBUG_MODE else ""
    path_to_file = f"DAY_1/input{debug}.txt"

    with open(path_to_file, "r") as f:
        previous = None
        for l in f.readlines():
            candidate = int(l.strip())
            if previous:
                if  candidate > previous:
                    got_up += 1
            previous = candidate

    print(got_up)




def part_2():
    got_up = 0

    debug = "_debug" if DEBUG_MODE else ""
    path_to_file = f"DAY_1/input{debug}.txt"

    last_four = [None, None, None, None]

    with open(path_to_file, "r") as f:
        for i, l in enumerate(f.readlines()):
            candidate = int(l.strip())
            last_four.insert(0, candidate)
            last_four = last_four[:4]
            # print(last_four)
            if all(last_four):
                # print(last_four, sum(last_four[-3:]), sum(last_four[:3]))
                if sum(last_four[:3]) > sum(last_four[-3:]):
                    got_up += 1

    print(got_up)



DEBUG_MODE = False

RUN_PART = part_2

if __name__ == "__main__":
    RUN_PART()