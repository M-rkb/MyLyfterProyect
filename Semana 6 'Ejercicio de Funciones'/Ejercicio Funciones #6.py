def orderstrings():
    f_string= "apple-shave-kitchen-help "
    new_list= f_string.split('-')
    new_list.sort()
    f_string_two= " ".join(new_list)
    return f_string_two


print(orderstrings())





