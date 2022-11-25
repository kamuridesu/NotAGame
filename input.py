import sys
import termios
import atexit
from select import select
WINDOWS = False
try:
    import msvcrt
    WINDOWS = True
except ImportError:
    WINDOWS=False


class Keyboard:
    def __init__(self) -> None:
        if not WINDOWS:
            self.fd: int = sys.stdin.fileno()
            self.new_term: list = termios.tcgetattr(self.fd)
            self.old_term: list = termios.tcgetattr(self.fd)

            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

            atexit.register(self.setNormalTerm)
    
    def setNormalTerm(self) -> None:
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)
    
    def getch(self) -> str:
        if not WINDOWS:
            key = sys.stdin.read(1)
            return key
        else:
            return msvcrt.getch()

    def getArrow(self):
        inp = sys.stdin.read(3)[2]
        vals = [65, 67, 66, 68]
        print(ord(inp))
        if ord(inp) in vals:
            return vals.index(ord(inp))
    
    def hit(self) -> tuple:
        if not WINDOWS:
            return select([sys.stdin], [], [], 0)[0] != []
        else:
            return msvcrt.kbhit()


def save(content) -> None:
    content = str(content)
    with open("file.txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    kb = Keyboard()
    print("esc to stop")
    while True:
        if kb.hit():
            c = kb.getch()
            #if ord(c) == 27:
            #    break
            #save(ord(c))
            print(ord(c))
