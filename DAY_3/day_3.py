from collections import defaultdict
import copy

def part_1():
    output = ''
    debug = '_debug' if DEBUG_MODE else ''
    path_to_file = f'DAY_3/input{debug}.txt'

    tally = defaultdict(int)

    word_list = []

    with open(path_to_file, 'r') as f:
        for i, l in enumerate(f.readlines()):
            word_list.append(l.strip())
            for j, char in enumerate(l.strip()):
                tally[j] += 0  # Make sure the dict entry is created
                if char == '1':
                    tally[j] += 1


    gamma_rate = ""

    for _, v in tally.items():
        if v > (i / 2):
            gamma_rate += "1"
        else:
            gamma_rate += "0"


    epsilon_rate = ""
    for c in gamma_rate:
        if c == "1":
            epsilon_rate += "0"
        else:
            epsilon_rate += "1"

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))

    part_2(tally, word_list)
    # print(int(epsilon_rate, 2))




def part_2(tally, word_list):
    debug = '_debug' if DEBUG_MODE else ''
    path_to_file = f'DAY_3/input{debug}.txt'

    o2_gen_rating = copy.deepcopy(word_list)
    co2_scrub_rating = copy.deepcopy(word_list)

    total_items = len(o2_gen_rating)
    
    o2_number = co2_number = None


    idx = 0
    while not o2_number:
        n_ones = sum(int(w[idx]) for w in o2_gen_rating)
        
        filter_on = "0"
        if n_ones >= len(o2_gen_rating)/2:
            filter_on = "1"
            
        o2_gen_rating = list(filter(lambda s: s[idx] == filter_on, o2_gen_rating))             

        if len(o2_gen_rating) == 1:
            o2_number = int(o2_gen_rating[0], 2)

        idx += 1

    idx = 0
    while not co2_number:
        print(sorted(co2_scrub_rating))
        n_ones = sum(int(w[idx]) for w in co2_scrub_rating)
        
        filter_on = "1"
        if n_ones >= len(co2_scrub_rating)/2:
            filter_on = "0"
            
        co2_scrub_rating = list(filter(lambda s: s[idx] == filter_on, co2_scrub_rating))             

        if len(co2_scrub_rating) == 1:
            co2_number = int(co2_scrub_rating[0], 2)

        idx += 1


    print(o2_number, co2_number, o2_number*co2_number)

        



DEBUG_MODE = False

RUN_PART = part_1




if __name__ == "__main__":
    RUN_PART()



