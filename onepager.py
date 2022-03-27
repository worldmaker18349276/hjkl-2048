# pip install hjkl-2048

import curses, random, numpy
scr = curses.initscr()
mv = True
bd = numpy.zeros((4,4),int)
while not bd.all():
    if mv:
        i = random.randint(0,15)
        if bd.flat[i] != 0: continue
        bd.flat[i] = 1 if random.random() < 0.7 else 2
    scr.addstr(0,0, str(bd))
    vw = numpy.rot90(bd, "hjlk".index(scr.getkey()))
    mv = False
    for ln in vw:
        r = [*ln[ln!=0],*[0]*4]
        for i in range(3):
            if r[i] == r[i+1] != 0:
                r[i:i+2] = [r[i]+1]
        mv |= (ln != r[:4]).any()
        ln[:] = r[:4]
