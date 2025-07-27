item_list = ['item', 5, 'foo', 3.14, True]
for i in item_list:
    if i=="item":
        item_list.remove(i)
    else:
        continue
    print(item_list)