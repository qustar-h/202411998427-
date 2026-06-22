import taichi as ti
from src.Work0.config import *
from src.Work0.physics import *

def main():
    initialize()
    gui = ti.GUI("N-Body Gravity Simulation", res=(WINDOW_WIDTH, WINDOW_HEIGHT))
    
    while gui.running:
        compute_forces()
        gui.clear(0x112233)
        gui.circles(pos.to_numpy(), color=0xffffff, radius=2)
        gui.show()

if __name__ == "__main__":
    main()
