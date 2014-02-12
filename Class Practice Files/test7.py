__author__ = 'bjones'
movies = ["Indiana Jones", "1975", "Brian Jones & Leo Dean", "Star Wars", "1980", "Steven Spielberg"]

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies)