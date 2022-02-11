import numpy as np #diyerek numpy yerine np yazarsın
import matplotlib.pyplot as mt

maasList= np.random.normal(400,500,1000)
np.mean(maasList)#ortalama laır

mt.hist(maasList,50)
mt.show



#numpy dizileri arrray#
benimLisf=[232,32,4,4]
np.array(benimLisf)


matrixList = [[10,20,30],[20,30,40]]
np.array(matrixList)

#numy arange#
list(range(0,10))
np.arange(0,10,2) #2 şer atlar
#ikiside rastgele list olş 

#zeros#
np.zeros(5) #5 tane sıfır yazar

np.ones(5) # 5 1 yazar

#linspace#

np.linspace(0,20,5)

np.random.randint(1,10,5) # 1 ilie 10 arası 5 dene rast deger döndür


