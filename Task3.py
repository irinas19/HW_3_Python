#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть 
# один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

dict_thing = {'вещь_1':1, 'вещь_2':8,'вещь_3':9,'вещь_4':4.5,'вещь_5':1,'вещь_6':6,'вещь_7':7,'вещь_8':6,'вещь_9':1}
max_weight = 12

sorted_dict = sorted(dict_thing.items(), key=lambda x: x[1])
complect = []
# print(sorted_dict)
# print(len(sorted_dict))
weight_compl = 0
step = 0

while (weight_compl + sorted_dict[step][1] <= max_weight) and (step <= (len(sorted_dict) - 1)):
    # print(sorted_dict[step])
    step += 1
    weight_compl += sorted_dict[step][1]
    # print(weight_compl)
    complect.append(sorted_dict[step][0])
print(f'Масса вещей = {weight_compl}')
print(f'В рюкзаке будет: {", ".join(complect)} ')
