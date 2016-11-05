#!/usr/bin/env python

import os
def contains_spaces(string):
    '''
    Returns true if a string has spaces, otherwise returns false
    '''
    for i in string:
        if i == " ":
            return True
    return False

def get_files_with_spaces(): 
    '''
    Returns a list of the files in the current directory with spaces
    '''
    files = os.listdir(os.getcwd())
    files_with_spaces = list(filter(lambda x: contains_spaces(x), files))
    return files_with_spaces

def despace(string):
    '''
    Removes the spaces from string and replaces them with an underscore
    params:
    string: a string that you want the spaces removes from
    '''
    str_list = list(string)
    for i in range(len(str_list)):
        if str_list[i] == " ":
            str_list[i] = "_"
    return "".join(str_list)

def main():
    for i in get_files_with_spaces():
        os.rename(i, despace(i))

if __name__== "__main__":
    main()
