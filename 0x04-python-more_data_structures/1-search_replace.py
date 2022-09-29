#!/usr/bin/python3
def search_repace(my_list, search, replace):
    #my_list = [1,2,3,4,5,4,3,2,89]
    #new_list = search_replace(my_list,56,23)#
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
