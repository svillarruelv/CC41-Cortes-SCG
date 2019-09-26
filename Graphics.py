import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from Rectangle import Rectangle 

codes = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,
]

fig, ax = plt.subplots()

def set_plancha(W,H):
   ax.set_xlim(-1, W)
   ax.set_ylim(-1, H)

def add_rectangle(x,y,w,h):

   verts = [
      (x, y),  # left, bottom
      (x, y+h),  # left, top
      (x+w, y+h),  # right, top
      (x+w, y),  # right, bottom
      (0., 0.),  # ignored
   ]
   path = Path(verts, codes)
   patch = patches.PathPatch(path, facecolor='orange',lw=2)
   ax.add_patch(patch)

def set_draws(W,H,array):
   set_plancha(W,H)
   for i in range(len(array)):
      x=array[i].x
      y=array[i].y
      w=array[i].w
      h=array[i].h
      add_rectangle(x,y,w,h)

def draw():
   plt.show()