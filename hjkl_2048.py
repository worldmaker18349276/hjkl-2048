import curses, random, numpy

def main():
    try:
        scr = curses.initscr()

        moved = True
        board = numpy.zeros((4,4),int)
        while not board.all():
            if moved:
                i = random.randint(0,15)
                if board.flat[i] != 0: continue
                board.flat[i] = 1 if random.random() < 0.7 else 2

            scr.addstr(0,0, str(board))

            view = board
            for _ in range("hjlk".index(scr.getkey())):
                view = numpy.rot90(view)

            moved = False
            for line in view:
                r = list(line[line!=0])
                i = 0
                while i < len(r)-1:
                    if r[i] == r[i+1]:
                        r[i:i+2] = [r[i]+1]
                    i += 1
                r.extend([0]*(4-len(r)))
                if (line != r).any():
                    moved = True
                line[:] = r

        scr.addstr("END")
        scr.getkey()

    finally:
        curses.endwin()

