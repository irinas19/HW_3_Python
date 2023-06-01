#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
#В результирующем списке не должно быть дубликатов.
import collections
from collections import Counter
list_test = [1,2,3,6,4,3,3,5,4,3,2,1,8]
list_dup_1 = set([x for x in list_test if list_test.count(x) > 1])
list_dup_2 = [x for x,k in Counter(list_test).items() if k > 1]
print(list(list_dup_1))
print(list_dup_2)