# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# i = 0
# while my_list[i] >= 0 and i < len(my_list):
  #  if my_list[i] != 0:
   #   print(my_list[i])
   # i += 1

    # первый код (верхний) - вариант без операторов на продолжение и прекращение (более короткий и удобный)
    # нижний код - вариант №2 (с операторами)

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if my_list[i] < 0:
        break
    elif my_list[i] == 0:
        i += 1
        continue
    print(my_list[i])
    i += 1