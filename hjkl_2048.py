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

            view = numpy.rot90(board, "hjlk".index(scr.getkey()))

            moved = False
            for line in view:
                r = [*line[line!=0], *[0]*4]
                for i in range(3):
                    if r[i] == r[i+1] != 0:
                        r[i:i+2] = [r[i]+1]
                moved |= (line != r[:4]).any()
                line[:] = r[:4]

        scr.addstr("END")
        scr.getkey()

    finally:
        curses.endwin()

