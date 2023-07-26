#%%Matplotlib
"""
-görselleştirme-
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=np.array([1,2,3,4])
y=np.array([4,3,2,1])

plt.figure() #boş ekran 
plt.plot(x,y,color="red",alpha=0.7,label="line")

#parçacık eklemek için
plt.scatter(x,y,color="blue",alpha=0.8,label="scatter")
plt.title("Matplotlib")
plt.xlabel("x")
plt.ylabel("y")

#grafigi gridlere bölmek için
plt.grid(True)
plt.xticks([0,1,2,3,4,5])
plt.legend() #label ın görünmesi için
plt.show() #bunu yazmazsan bundan sonra yazacakların grafiğe dahil olur

# Birden fazla plot u tek bir figür içerisinde çizdirme

fig,axes=plt.subplot(2,1,figsize=(9,7))
fig.subplots_adjust(hspace=0.5)

x=[1,2,3,4,5,6,7,8,9,10]
y=[10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set.title("sub-1")
axes[0].set.ylabel("sub-1 y")
axes[0].set.xlabel("sub-1 x")

axes[1].scatter(y.x)
axes[1].set.title("sub-2")
axes[1].set.ylabel("sub-2 y")
axes[1].set.xlabel("sub-2 x")


#random resim
plt.figure()
img=np.random.random((50,50))
plt.imshow(img,cmap="gray") #0(siyah) -1(beyaz) ->0.5(gri)
plt.axis("off") #eksenleri kapatır
plt.show()


plt.figure()
img1=np.random.random((50,50))
plt.imshow(img1) 

plt.show()