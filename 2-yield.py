"""
fonksiyon_lambda=lambda x,y,z :x*y*z
sonuc=fonksiyon_lambda(2,3,4)
print(sonuc)
"""
#generator

generator=(x for x in range(1,4))
for i in generator:
    print(i)
    
"""
döngü içerisindeki her değer generate edildiğinde 
sonraki değere geçtiği zaman önceki değer unutuluyor.
"""


"""
fonksiyon eğer return olarak generator döndürecek ise 
return yerine yield kullanılır.
"""

def createGenerator():
    liste=range(1,4)
    for i in liste:
        yield i
        
newGenerator=createGenerator()
for i in newGenerator:
    print(i)
