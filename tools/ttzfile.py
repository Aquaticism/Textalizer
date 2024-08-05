class TTZC:
    def __init__(self, char='', r=0, g=0, b=0):
        self.char = char
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return self.char + ("%03d%03d%03d" % (self.r, self.g, self.b))

    def __eq__(self, __value):
        return self.r == __value.r and self.g == __value.g and self.b == __value.b

    def __ne__(self, __value):
        return not (self.r == __value.r and self.g == __value.g and self.b == __value.b)


class Frame:
    def __init__(self, frame_id=0, grid=None):
        if grid is None:
            grid = []
        self.frame_id = frame_id
        self.grid = grid

    def __str__(self):
        arrstr = ""
        for line in self.grid:
            for c in line:
                arrstr += str(c)
        return f"{self.frame_id} {arrstr}"

    @staticmethod
    def from_string(string, width, height):
        grid = []
        frame_id = 0
        fid_str = ""
        while string[0] != ' ':
            fid_str += string[0]
            string = string[1:]
        string = string[1:]
        frame_id = int(fid_str)
        for i in range(height):
            grid.append([])
            for j in range(width):
                s = i * 10 * width + j * 10
                grid[j].append(TTZC(string[s], int(string[s + 1: s + 4]), int(string[s + 4: s + 7]), int(string[s + 7: s + 10])))
        return Frame(frame_id, grid)


class FrameSet:
    def __init__(self, frames=None):
        if frames is None:
            frames = []
        self.frames = frames

    def __getitem__(self, key):
        return self.frames[key]

    def __setitem__(self, key, value):
        self.frames[key] = value

    def __str__(self):
        arrstr = ""
        for frame in self.frames:
            arrstr += str(frame)
        return f"{arrstr}"

    @staticmethod
    def from_string(string, length, width, height):
        fs = width * height * 10
        for i in range(length):
            s = i * fs


class TTZ:
    def __init__(self, name='', width=0, height=0, fps=0.0, frame_count=0, length=0.0, frames=None):
        if frames is None:
            frames = FrameSet
        self.name = name
        self.width = width
        self.height = height
        self.fps = fps
        self.frame_count = frame_count
        self.length = length
        self.frames = frames

    @staticmethod
    def load_from_file(filepath):
        file = open(filepath, 'r')
        headers = file.readline().split(" ")
        ttz = TTZ(headers[0], int(headers[1]), int(headers[2]), float(headers[3]), float(headers[4]))
