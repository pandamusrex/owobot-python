# A renderer for a talking car from the eighties

from .renderer_base import Renderer

class KITT(Renderer):
    def __init__(self, matrix):
        self.num_lamps = 8
        self.on_lamp_index = 0
        self.sweeping_right = True
        self.lamp_brightness = [0] * self.num_lamps
        self.matrix = matrix

    def draw(self):
        for i in range(0, self.num_lamps):
            self.lamp_brightness[i] = self.lamp_brightness[i] / 2

        self.lamp_brightness[self.on_lamp_index] = 255

        for i in range(0, self.num_lamps):
            r = self.lamp_brightness[i]
            for x in range(0, self.num_lamps):
                for y in range(0, self.num_lamps):
                    self.matrix.SetPixel(i * 8 + x, 12 + y, r, 0, 0)

        if self.sweeping_right:
            self.on_lamp_index += 1
        else:
            self.on_lamp_index -= 1

        if self.on_lamp_index > self.num_lamps - 1:
            self.sweeping_right = False
            self.on_lamp_index = self.num_lamps - 2
        
        if self.on_lamp_index < 0:
            self. sweeping_right = True
            self.on_lamp_index = 1
