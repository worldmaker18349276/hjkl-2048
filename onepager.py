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
  vw = bd
  for _ in range("hjlk".index(scr.getkey())):
    vw = numpy.rot90(vw)
  mv = False
  for ln in vw:
    r = list(ln[ln!=0])
    i = 0
    while i < len(r)-1:
      if r[i] == r[i+1]:
        r[i:i+2] = [r[i]+1]
      i += 1
    r.extend([0]*(4-len(r)))
    if (ln != r).any(): mv = True
    ln[:] = r
