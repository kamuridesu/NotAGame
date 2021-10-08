import sys
import termios
import atexit
from select import select


class Keyboard:
    def __init__(self) -> None:
        self.fd = sys.stdin.fileno()
        self.new_term = termios.tcgetattr(self.fd)
        self.old_term = termios.tcgetattr(self.fd)

        self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

        atexit.register(self.setNormalTerm)
    
    def setNormalTerm(self):
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)
    
    def getch(self):
        key = sys.stdin.read(1)
        return key

    def getArrow(self):
        inp = sys.stdin.read(3)[2]
        vals = [65, 67, 66, 68]
        print(ord(inp))
        if ord(inp) in vals:
            return vals.index(ord(inp))
    
    def hit(self):
        return select([sys.stdin], [], [], 0)[0] != []



def save(content):
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
