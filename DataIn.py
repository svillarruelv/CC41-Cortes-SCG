#!/usr/bin/env python
# coding: utf-8

# In[259]:


get_ipython().run_line_magic('run', 'Rectangle.ipynb')


# In[260]:


def getline(line):
    return [str(n) for n in line.split(' ')]


# In[294]:


def set_var(array):
    sheet_w=int(array[0][0])
    sheet_h=int(array[0][1])
    n=int(array[1][0])
    rectangles = []
    for i in range(n):
        l=array[i+2][0]
        w=int(array[i+2][1])
        h=int(array[i+2][2])
        p=int(array[i+2][3])
        for j in range(p):
            rectangles.append(Rectangle(0,0,l+str(j+1),w,h))
    return sheet_w,sheet_h,n,rectangles


# In[295]:


def Read(path):
    file = open(path,"r")
    f1=file.readlines()
    t = []
    for line in f1:
        t.append(getline(line))
    return set_var(t)


# In[299]:





# In[ ]:




