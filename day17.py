

class Probe:
    def __init__(self, start_vel_x, start_vel_y):
        self.target_x_min = 281
        self.target_x_max = 311
        self.target_y_min = -74
        self.target_y_max = -54
        self.vx = start_vel_x
        self.vy = start_vel_y
        self.x = 0
        self.y = 0
        self.max_height = 0

    def step(self):
        self.x += self.vx
        self.y += self.vy
        if self.vx > 0:
            self.vx += -1
        elif self.vx < 0:
            self.vx += 1
        self.vy += -1
        # print(str(self.x) + ", " + str(self.y))
        if self.y > self.max_height:
            self.max_height = self.y
        if self.target_y_max >= self.y >= self.target_y_min and self.target_x_max >= self.x >= self.target_x_min:
            return True
        elif self.y < self.target_y_min or abs(self.x) > abs(self.target_x_max) or \
                (self.vx < 0 and self.target_x_min > 0) or (self.vx > 0 and self.target_x_min < 0):
            return False
heights = {}
for i in range(0,1000):
    for j in range(-1000,1000):
        finished = False
        start_vx = i
        start_vy = j
        p = Probe(start_vx,start_vy)

        while not finished:
            result = p.step()
            if result == False:
                finished = True
            if result == True:
                heights[(start_vx,start_vy)] = p.max_height
                finished = True
print(heights)
print(list(heights.keys())[list(heights.values()).index(max(heights.values()))])
print(len(heights))