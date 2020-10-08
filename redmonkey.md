import matplotlib.pyplot as plt 

object=["python,"c++","java","perl","scale","lisp"]

x=range(len(object))

performance= [10,8,6,4,2,1]

plt.barh(x,performance,align="centre",color="blue")

plt.yaxis(x,object)
