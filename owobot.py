import sys
import time
from renderers import Eyes, KITT
from rgbmatrix import RGBMatrix, RGBMatrixOptions

if __name__ == "__main__":
    # See https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/bindings/python/samples/samplebase.py
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'regular'
    options.gpio_slowdown = 2
    options.disable_hardware_pulsing = True

    matrix = RGBMatrix(options = options)
    renderer = KITT(matrix)

    try:
        print("Press CTRL-C to stop")

        while True:
            renderer.draw()
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Done")
        sys.exit(0)