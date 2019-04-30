# Say you have a list value like this:


# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space,
# with and inserted before the last item.
# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
# But your function should be able to work with any list value passed to it.

def format_list(list):
    new_str = ''
    for i in list:
        if i == list[-1]:
            new_str = new_str + 'and ' + str(i)
            break
        else:
            new_str = new_str + str(i) + ', '
    print(new_str)


format_list([1, 2, 3, 'four', 'five', 6, 7])
