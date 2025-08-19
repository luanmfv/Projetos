import sys
from pyboy import PyBoy

def main():
    if len(sys.argv) < 2:
        print("Uso: python jogar_gb.py caminho/para/rom.gb")
        sys.exit(1)

    rom = sys.argv[1]
    # window_type 'SDL2' abre janela; 'headless' seria sem janela
    pyboy = PyBoy(rom, window_type="SDL2", window_scale=3, sound=True)

    # Loop principal: tick() retorna True quando a janela fecha
    while not pyboy.tick():
        pass

    pyboy.stop()

if __name__ == "__main__":
    main()
