from PIL import Image
import sys
P = {'K':(26,28,44),'S':(244,196,156),'s':(200,138,106),'H':(139,74,43),'h':(90,46,26),
     'A':(167,176,192),'a':(86,108,134),'L':(220,228,236),'C':(177,62,83),'c':(122,37,55),
     'B':(93,58,26),'G':(255,205,117),'W':(232,238,245),'w':(148,163,184),'M':(100,110,125),'V':(120,80,200),'v':(190,160,255)}
N=32
def base():
    g=[[None]*N for _ in range(N)]
    def r(x0,y0,x1,y1,c):
        for y in range(y0,y1+1):
            for x in range(x0,x1+1): g[y][x]=c
    r(10,13,20,25,'C'); r(10,23,20,25,'c')                 # cape
    r(11,4,19,8,'H'); r(10,5,20,9,'H'); r(10,9,10,11,'h'); r(20,9,20,11,'h')  # hair
    r(11,8,19,12,'S'); r(11,12,19,12,'s')                  # face
    r(11,8,13,8,'H'); r(16,8,19,8,'H'); r(12,4,18,4,'h')
    g[10][13]='K'; g[10][17]='K'
    r(14,13,16,13,'s')                                     # neck
    r(11,14,19,20,'A'); r(18,14,19,20,'a'); r(13,15,14,17,'L')  # torso
    r(11,20,19,20,'B'); g[20][15]='G'                      # belt
    r(12,21,14,25,'a'); r(16,21,18,25,'a'); r(12,21,12,25,'A'); r(16,21,16,25,'A')  # legs
    r(11,26,14,27,'B'); r(16,26,19,27,'B')                 # boots
    r(9,14,10,19,'a'); r(9,20,10,20,'S')                   # left arm
    r(20,14,21,17,'A'); r(21,18,22,19,'S')                 # right arm
    return g,r
def longsword(g,r):
    r(22,4,23,16,'W'); r(23,4,23,16,'w'); g[3][22]='W'
    r(20,17,25,17,'G'); r(22,18,23,20,'B'); r(22,21,23,21,'G')
def rapier(g,r):
    r(23,2,23,16,'W'); r(21,17,25,17,'G'); r(21,16,21,16,'G'); r(25,16,25,16,'G')
    r(22,18,23,20,'B'); g[21][22]='G'
def greatsword(g,r):
    r(22,0,24,15,'W'); r(24,0,24,15,'w'); g[0][22]=None; g[0][24]=None
    r(19,16,27,16,'G'); r(22,17,24,21,'B'); r(22,22,24,22,'G')
def mace(g,r):
    r(22,10,23,22,'B'); r(20,5,25,9,'M'); r(21,4,24,10,'M'); r(24,5,25,9,'w')
    for (x,y) in [(19,7),(26,7),(22,3),(23,3),(22,11)]: g[y][x]='w'
def magicsword(g,r):
    longsword(g,r); r(22,6,23,14,'v'); r(23,6,23,14,'V'); g[17][20]='V'; g[17][25]='V'
def outline(g):
    o=[row[:] for row in g]
    for y in range(N):
        for x in range(N):
            if g[y][x] is None and any(0<=y+dy<N and 0<=x+dx<N and g[y+dy][x+dx] not in (None,'K')
                                     for dx,dy in ((1,0),(-1,0),(0,1),(0,-1))):
                o[y][x]='K'
    return o
variants=[longsword,rapier,greatsword,mace,magicsword]
S=8; img=Image.new('RGBA',(N*S*len(variants)+ (len(variants)+1)*16, N*S+32),(40,44,60,255))
for i,v in enumerate(variants):
    g,r=base(); v(g,r); g=outline(g)
    for y in range(N):
        for x in range(N):
            if g[y][x]:
                ox=16+i*(N*S+16)+x*S; oy=16+y*S
                for yy in range(S):
                    for xx in range(S): img.putpixel((ox+xx,oy+yy),P[g[y][x]]+(255,))
img.save(sys.argv[1])
