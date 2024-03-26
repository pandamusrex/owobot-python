# owobot-python

## Prerequisites
- Python 3.7 or newer

## Setup
- Create a virtual environment e.g. via https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment
- Shift Command P then Python: Create Environment
- Select venv (not conda)
- Select the latest python version (i.e. the one on /usr/bin/python3)
- Shift Command P then Python: Select Interpreter
- Selct the venv you just created

- Depends on the Python bindings added by https://github.com/hzeller/rpi-rgb-led-matrix/
- Follow the instructions here to build for Python 3: https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python

- You might want to try running the python samples from the library. To get the python samples to display properly, I needed to use the slowdown param, i.e.:

```
cd ~/Repos/rpi-rgb-led-matrix/bindings/python/samples
sudo ./runtext.py --led-cols=64 --led-rows=32 --led-slowdown-gpio=2
sudo ./rotating-block-generator.py --led-cols=64 --led-rows=32 --led-slowdown-gpio=2
```

- After installing and building the Python bindings for rpi-rgb-led-matrix, add a rgmatrix.pth file to your .venv/lib/python3.xx/site-packages folder with the path to the package, i.e.

```
/home/pi/Repos/rpi-rgb-led-matrix/bindings/python
```

- You may also need to install Pillow to avoid a missing reference to the obsolete PIL. To do so, in your venv type

```
ModuleNotFoundError: No module named 'PIL'
(.venv) pi@raspberrypi:~/Repos/pymatrix $ pip3 install Pillow
```

- Try running it, i.e.

```
(.venv) pi@raspberrypi:~/Repos/owobot-python $ /home/pi/Repos/owobot-python/.venv/bin/python /home/pi/Repos/owobot-python/owobot.py
```

- To avoid the "Can't set realtime thread priority" warning, do the following (replace 11 with your Python version)

```
sudo setcap 'cap_sys_nice=eip' /usr/bin/python3.xx
```
