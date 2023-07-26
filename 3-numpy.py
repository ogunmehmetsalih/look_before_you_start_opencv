"""
--Numpy
-matrisler için hesaplama kolaylığı sağlar
"""
import numpy as np

#1*15 boyutunda bir array dizi
dizi=np.array([1,2,3,4,5,6,7,8,9])
print(dizi)

print(dizi.shape) #array boyutu çıktı (15,) virgülden sonra boşluk olması 1 i ifade eder

dizi2=dizi.reshape(3,3)
print(dizi2)

print("şekil:",dizi2.shape)
print("Boy:",dizi2.size)
print("veri tipi",dizi2.dtype.name)
print("Boyut:",dizi2.ndim)

#2 boyutlu array ([[]])
dizi2D=np.array([[1,2,3,5],[4,5,6,1],[2,7,8,9]])
print(dizi2D)

#Sıfırlardan oluşan bir array
sifir_dizi=np.zeros((4,5))
print(sifir_dizi)

#Birlerden oluşan bir array 
bir_dizi=np.ones((7,8))
print(bir_dizi)

#Boş array tanımlama
bos_dizi=np.empty((4,5))
#aslında oluşan değerler boş değil sıfıra yakın olan değerlerdir
print(bos_dizi)

#arange(x den başla,y ye kadar dahil değil,z kadar artır)
dizi_aralik=np.arange(10,50,5)
print(dizi_aralik)

#linspace(x den başla,y de bitir,kaça böleyim)
dizi_bosluk=np.linspace(10,20,5)
print(dizi_bosluk)

#float array oluşturma
float_array=np.float32([[1,2],[3,4]])
print(float_array)


#matematiksel işlemler
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a-b)
print(a**2)

#dizi elemanlarını toplama
print(np.sum(a))
print(np.max(a))
print(np.median(a))
print(np.mean(a))


#rastgele sayı üretme [0,1] arasında sürekli üniform 3*3
rastgele_dizi=np.random.random((3,3))
print(rastgele_dizi)

#index
dizi=np.array([1,2,3,4,5,6,7])
print(dizi[0])

print(dizi[0:4])

print(dizi[::-1]) #tersine çevirme

array2D=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array2D)

#dizinin 1.satır ve 1.sütununda bulunan eleman 
print(array2D[1,1])

#1.sütun ve tüm satırlar 
print(array2D[:,1])

#satır 1,sütun 1,2,3
print(array2D[1,1:4])

#dizinin son satır tüm sütünları
print(array2D[-1,:])

#vektör haline getirme 
dizi2D=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

vektor=dizi2D.ravel()
print(vektor)

maxsimum_sayinin_indeksi=vektor.argmax()
print(maxsimum_sayinin_indeksi)




















