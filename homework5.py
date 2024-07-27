immutable_var='apple',1,True
print(immutable_var)
#immutable_var[2]=2
# Ошибка! tuple невозможно изменить (только если внутри находится list, который уже можно изменять)
print(immutable_var)
mutable_list=[1,False,'book']
print(mutable_list)
mutable_list[1]=True
print(mutable_list)