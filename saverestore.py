import os
import sys
import re
#import shutil

selected_list = []
full_list = []
delete_list = []

def main():
    #print('Hello, Denis! Below is a list according to your search criteria! \n------------------\n')
    directory = "/var/www/html/cms/saverestore/"
    all_elements = os.listdir( directory ) # Список всех элиментов в папке!
    full_list = all_elements
    selection_criteria = re.compile("design_code_data_files*.*")  # Сортируем список согласно критерию «Regular expressions»
    selected_files = list(filter(selection_criteria.match, full_list)) #
    selected_list = selected_files

    #result=list(set(selected_list) & set(full_list)) # Создаст список совпадений
    #result=list(set(selected_list + full_list)) # Создаст список из уникальных элиментов.
    result=list(set(selected_list) ^ set(full_list)) # Создаст список элиментов которые соответсвуют критерию сортировки. 
    delete_list = result

    #print("List of all elements in selected folder - {}".format(all_elements), end='\n\n')
    #print("List which will delete: - {}".format(delete_list),end='\n\n')
    #print("." * 10)
    #print("list which will stay: - {}".format(selected_list))




    for file in delete_list: # Перебираеи весь список
        i = directory + file  # путь + имя файла
        if os.path.isfile(i): # Проверяем является ли элимент файлом
            os.remove(i) # Удалем!



if (__name__ == "__main__"):
    main();
