#import numpy & scipy
import numpy as np
np.set_printoptions(threshold=np.inf)
from scipy import optimize as op



# difine plants customers and logistic cost
#For this case, 2 plants [x1,x2] 3 customers [y1,y2,y3], 3 proudcts [c1,c2,c3]
x1y1c1=(0,None)
x1y2c1=(0,None)
x1y3c1=(0,None)
x2y1c1=(0,None)
x2y2c1=(0,None)
x2y3c1=(0,None)
x1y1c2=(0,None)
x1y2c2=(0,None)
x1y3c2=(0,None)
x2y1c2=(0,None)
x2y2c2=(0,None)
x2y3c2=(0,None)
x1y1c3=(0,None)
x1y2c3=(0,None)
x1y3c3=(0,None)
x2y1c3=(0,None)
x2y2c3=(0,None)
x2y3c3=(0,None)

#定义目标函数系数 c=[]*[x1~y3]
c=np.array([17,19,20,15,14,19,16,17,24,27,20,33,24,28,33,32,32,34])

#定义约束条件系数 A_ub for Formula B_ub for limits, <=
#A_ub=np.array([[1,1,1,0,0,0],[0,0,0,1,1,1],[1,0,0,1,0,0],[0,1,0,0,1,0],[0,0,1,0,0,1],[-1,0,0,-1,0,0],[0,-1,0,0,-1,0],[0,0,-1,0,0,-1]])
#B_ub=np.array([35,52,25,17,45,-25,-17,-45])
# Throughput [A_ub]*[all] < [B_ub]
A_ub=np.array([[1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],[0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1]])
B_ub=np.array([40,45])
# Requirements [A_eq]*[all] = [B_eq]
A_eq=np.array([[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1]])
B_eq=np.array([10,0,10,6,5,10,0,13,10])

#求解
res=op.linprog(c,A_ub,B_ub,A_eq,B_eq,bounds=(x1y1c1,x1y2c1,x1y3c1,x2y1c1,x2y2c1,x2y3c1,x1y1c2,x1y2c2,x1y3c2,x2y1c2,x2y2c2,x2y3c2,x1y1c3,x1y2c3,x1y3c3,x2y1c3,x2y2c3,x2y3c3),options={'disp': True})

print(res)
print(res.x)
print(res.fun)
