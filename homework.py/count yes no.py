items = ["Yes", "Yes", "Yes", "No", "Yes",
         "Yes", "Yes", "Yes", "Yes", "No",
         "Yes", "No", "Yes", "No", "No",
         "Yes", "Yes", "Yes", "Yes", "Yes",
         "No", "No", "Yes", "Yes", "No",
         "Yes", "Yes", "Yes", "No"]

def count_items(item_list):
    count_yes = item_list.count("Yes")
    count_no = item_list.count("No")
    return count_yes, count_no

yes_count, no_count = count_items(items)
print("Yes occurs:", yes_count, "times")
print("No occurs:", no_count, "times")
