class coordinates:
    def __init__(self, str_rep=None, **kwargs):
        if str_rep is None:
            self.x = kwargs["x"]
            self.y = kwargs["y"]
            self.z = kwargs["z"]
        else:
            self.x, self.y, self.z = map(int, str_rep.split(","))

    def __add__(self, other):
        return coordinates(x=self.x + other.x,y=self.y + other.y,z=self.z + other.z)

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

class Beacon:
    pass
    

class Scanner:
    def __init__(self, id_number):
        self.id_number = id_number
        self.beacons = []

    def __add__(self, beacon):
        self.beacons.append(beacon)

class OceanMapper():
    def __init__(self):
        pass

    def parse(self, f):
        for l in f.readlines():
            l = l.strip()

    def show_answer_p1(self):
        pass


def main():
    c1 = coordinates("-689,845,-530")
    print(c1)

    c2 = coordinates(x=-689,y=845,z=-530)
    print(c2+c1)

if __name__ == "__main__":
    main()