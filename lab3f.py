#!/usr/bin/env python3

my_list = [1, 2, 3, 4]

def add_item_to_list(list_name):

    last_item = list_name[-1]

    list_name.append(last_item + 1)
    list_name.append(last_item + 2)

def remove_items_from_list(list_name, items):

    for item in items:
        if item in list_name:
            list_name.remove(item)
