#pandas

"""
Pandas veri işleme ve analizi için python programlama 
dilinde yazılmış bir kütüphanedir.
Bu kütüphanede temel olarak zaman etiketli serilere ve
sayısal verileri işlemek için veri yapısı oluşturulur.
Ve veriler kolay bir şekilde işlenmiş olur. 

Pandas
-hızlı,güçlü ve esnek
-csv ve txt dosyalarının kolay bir şekilde okunur
-veri ekleme,çıkartma
"""

import pandas as pd

#dictionary
dictionary={"isim":["ali","veli","kenan","murat","ayse","hilal"],
            "yas":[15,16,17,33,45,66],
            "maas":[100,150,240,350,110,220]}
veri=pd.DataFrame(dictionary)
print(veri)
print(veri.head())
print(veri.columns) #verinin sütunları

#veri bilgisi
print(veri.info())

#istatistiksel özellikler
print(veri.describe())

#yaş sütunu
print(veri["yas"])

#sütun ekleme
veri["sehir"]=["Ankara","Istanbul","Konya","Izmir","Bursa","Antalya"]
print(veri)

#yaş sütunu 
print(veri.loc[:,"yas"])

#yaş sütunu ve 3 satır
print(veri.loc[:2,"yas"])

#yaş ve şehir  arası sütunu ve 3 satır
print(veri.loc[:2,"yas":"sehir"])

#satırları tersten yazdır
print(veri.loc[::-1,:])

#yaş ve sütunu iloc ile 
print(veri.iloc[:,1])

#ilk 3 satır yaş ve isim
print(veri.iloc[:3,[0,1]])


#filtreleme
dictionary={"isim":["ali","veli","kenan","murat","ayse","hilal"],
            "yas":[15,16,17,33,45,66],
            "sehir":["Ankara","Ankara","Bursa","Antalya","Bursa","Antalya"]
            }

veri=pd.DataFrame(dictionary)
print(veri)

#ilk olarak yaşa göre filtre yas>22
filtre1=veri.yas>22
filtrelenmis_veri=veri[filtre1]
print(filtrelenmis_veri)

#ortalama yaş
ortalama_yas=veri.yas.mean()
print(ortalama_yas)

veri["YAS_GRUBU"]=["Küçük" if ortalama_yas>i else "Büyük" for i in veri.yas]
print(veri)

#birleştirme
sozluk1={"isim":["ali","veli","kenan"],
         "yas":[15,16,17],
         "sehir":["Urfa","Antep","Diyarbakır"]}
veri1=pd.DataFrame(sozluk1)

sozluk2={"isim":["murat","ayse","elif"],
         "yas":[15,16,17],
         "sehir":["Urfa","Antep","siirt"]}
veri2=pd.DataFrame(sozluk2)

#dikey virleştirme
veri_dikey=pd.concat([veri1,veri2],axis=0)

#yatay birleştirme
veri_yatay=pd.concat([veri1,veri2],axis=1)















