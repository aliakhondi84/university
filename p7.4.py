import sys
import stddraw


def draW_triangle(x0,y0,x1,y1,x2,y2):
    stddraw.line(x0,y0,x1,y1)
    stddraw.line(x1,y1,x2,y2)
    stddraw.line(x2,y2,x0,y0)
x0=float(sys.argv[1])
y0=float(sys.argv[2])
x1=float(sys.argv[3])
y1=float(sys.argv[4])
x2=float(sys.argv[5])
y2=float(sys.argv[6])
stddraw.setXscale(0,10)
stddraw.setYscale(0,10)
draW_triangle(x0,y0,x1,y1,x2,y2)
stddraw.show()
    
    