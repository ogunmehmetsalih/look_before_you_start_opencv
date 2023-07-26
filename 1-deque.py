#deque
from collections import deque

dq=deque(maxlen=3)

dq.append(1)
print(dq)
dq.append(2) 
print(dq)
dq.append(3)
print(dq)
dq.append(4) # 1'i atıp 4 ü ekleyecek
print(dq)
#append - sağa ekleme 
#appendleft - sola ekleme

dq=deque(maxlen=3)
dq.append(1)
dq.appendleft(2) #sola ekleme işlemi
dq.appendleft(3)
print(dq)
dq.clear() #silme
print(dq)

#diğer metotları incele...