#!/usr/bin/python3
def search_repace(my_list, search, replace):
    def s_r_elm(elm):
        return (elm if elm != search else replace)
    return list(map(s_r_elm, my_list))
