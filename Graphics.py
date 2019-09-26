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

def add_rectangle(x,y,w,h,s,axs,n):
   verts = [
      (x, y),  # left, bottom
      (x, y+h),  # left, top
      (x+w, y+h),  # right, top
      (x+w, y),  # right, bottom
      (0., 0.),  # ignored
   ]
   path = Path(verts, codes)
   patch = patches.PathPatch(path, facecolor='orange',lw=2)
   if n>1:
      axs[s].add_patch(patch)
   else:
      axs.add_patch(patch)

def set_draws(n_planchas,W,H,array):
   """
   Se manda el numero de planchas con
   las dimensiones deseadas y el arreglo
   de rectangulos a dibujar.
   La funcion dibujara los rectangulos en sus
   planchas
   """
   if n_planchas > 1:
      fig, axs = plt.subplots(1,n_planchas)

      for i in range(len(axs)):
         axs[i].set_xlim(-1,W)
         axs[i].set_ylim(-1,H)
   else: 
      fig, axs = plt.subplots()
      axs.set_xlim(-1,W)
      axs.set_ylim(-1,H)
       

   for i in range(len(array)):
      x=array[i].x
      y=array[i].y
      w=array[i].w
      h=array[i].h
      s=array[i].sheet-1
      add_rectangle(x,y,w,h,s,axs,n_planchas)

def draw():
   plt.show()