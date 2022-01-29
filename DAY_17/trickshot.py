class TrickShot():
    def __init__(self, values=None):
        self.p0x = self.p0y = 0
        if values is None:
            values = [0]*4
        self.x_inf, self.x_sup, self.y_inf, self.y_sup = values


    def parse(self, f):
        for l in f.readlines():
            l = l.strip()
            l = l.replace("target area: ", "")
            x_range, y_range = l.split(', ')
            x_range = x_range.replace("x=", "")
            y_range = y_range.replace("y=", "")
            x_inf, x_sup = x_range.split("..")
            y_inf, y_sup = y_range.split("..")

            self.x_inf, self.x_sup, self.y_inf, self.y_sup = map(int, [x_inf, x_sup, y_inf, y_sup])
            break

    def compute_step(self, x, y, vx, vy):
        x += vx
        y += vy

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy -= 1

        return x, y, vx, vy

    def iterate_trajectory(self, p0x, p0y, v0x, v0y):
        pass
        if (self.x_inf <= p0x <= self.x_sup) and (self.y_inf <= p0y <= self.y_sup):
            return True
        if p0y < self.y_inf:
            return False
        if v0x == 0 and (p0x < self.x_inf or p0x > self.x_sup):
            return False

        return self.iterate_trajectory(*self.compute_step(p0x, p0y, v0x, v0y))
        

    def compute_likely_v0x(self):
        # for v0x in range(self.)
        pass

    def show_answer_p1(self):
        pass

    def show_answer_p2(self):
        count = 0
        for v0x in range(0, self.x_sup+1):
            for v0y in range(-260,260):
                if self.iterate_trajectory(0,0,v0x,v0y):
                    count += 1

        print(count)

if __name__ == "__main__":
    path_to_file = 'DAY_17/input_debug_part1.txt'

    x_inf = 20
    x_sup = 30
    y_inf = -10
    y_sup = -5

    ts = TrickShot([x_inf, x_sup, y_inf, y_sup])

    v0x = 6
    v0y = 9

    values = [ts.p0x, ts.p0y, v0x, v0y]

    print(ts.iterate_trajectory(*values))