
import numpy as np
import matplotlib.pyplot as plt
import math

def ball(xo,yo,mo):
	c=yo-mo*xo
	xn=(-mo*c*a*a+a*b*(a*a*mo*mo+b*b-c*c)**0.5)/(a*a*mo*mo+b*b)
	yn=(b*b*c+a*b*mo*(a*a*mo*mo+b*b-c*c)**0.5)/(a*a*mo*mo+b*b)
	if abs(xn-xo)<eps and abs(yn-yo)<eps :
		xn=(-mo*c*a*a-a*b*(a*a*mo*mo+b*b-c*c)**0.5)/(a*a*mo*mo+b*b)
		yn=(b*b*c-a*b*mo*(a*a*mo*mo+b*b-c*c)**0.5)/(a*a*mo*mo+b*b)
	
	try :
		d=yn/xn*(a*a)/(b*b)-xn/yn*(b*b)/(a*a)
		mn=(2.0+d*mo)/(-d+2.0*mo)
	except ZeroDivisionError:
		mn=-mo
	
	return xn,yn,mn


a=2.0   
b=1.5
x0=0.707106781  
y0=1.414213562
m0=3.0

x1=0.0       
y1=0.0
m1=0.0
eps=1.e-6
abs_succ=[]
ord_succ=[]
pentes_succ = []
ecarts_succ =[]
for i in range(1000):
    x1,y1,m1=ball(x0,y0,m0)
    pentes_succ.append(m1)
    abs_succ.append(x1)
    ord_succ.append(y1)
    ecarts_succ.append(((x1-x0)**2+(y1-y0)**2)**0.5)
    x0,y0,m0=x1,y1,m1
print ('done')

import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 

fig = plt.figure() 
ax = plt.axes(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5)) 
line, = ax.plot([], [], lw=2) 

# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	return line, 

# lists to store x and y axis points 
xdata, ydata = [], [] 

# animation function 
def animate(i): 

	x = abs_succ[i] 
	y = ord_succ[i]  
	
	# appending new points to x, y axes points list 
	xdata.append(x) 
	ydata.append(y) 
	line.set_data(xdata, ydata) 
	return line, 
	
# setting a title for the plot 
plt.title('phase graph') 

g = np.arange(-2, 2, 0.01)
h=[]
for i in range(len(g)):
    h.append(b*math.sqrt(1-g[i]**2/a**2))
plt.plot(g,h,color ='blue')    
plt.plot(g,np.negative(h),color ='blue')

# call the animator	 
anim = animation.FuncAnimation(fig, animate, init_func=init,  interval=500,frames=1000,  blit=True) 
plt.show()
