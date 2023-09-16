# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


from pathlib import Path                            #Взять из готовой библиотеки конструктор Path

FILE_PATH = Path('phonebook.txt')
print(FILE_PATH)

#Функция добавления контактов
def open_contakt():
    with open(FILE_PATH, 'a', encoding='utf8') as file:  #открывает и закрывает файл, нумерует его и переводит буквы в цифры(шифрует) a- добавляет в конец файла.txt
        info = input('Введите данные: ')
        file.write(f'\n{info}')

# open_contakt()

#Функция вывода контактов
def show_contakt():
    with open(FILE_PATH, 'r', encoding='utf8') as file:  #открывает и закрывает файл, нумерует его и переводит буквы в цифры(шифрует) a- добавляет в конец файла.txt
        #print(file.readlines())                         #вывод в одну строку
        print(*[line for line in file])                  #Вывод с новой строки

# show_contakt()

#Функция поиска контактов
def find_contakt():
    list_1 = []
    serch = input('Найти: ').strip()
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        for contakt in file:
            if serch in contakt:
                list_1.append(contakt)          
        print(*[line for line in list_1])

# find_contakt()

#Удалить контакт
def delete_contact():
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        d = input('Введите имя или фамилию для удаления: ')
        lines = file.readlines()
        with open(FILE_PATH, 'w', encoding="utf8") as file:
            for contakt in lines:
                if d in contakt:
                    print('Строка удалена')
                else:
                    print(contakt)    
                    file.write(contakt)

# delete_contact()
            
#Объединение функций в одну
def choouse():
    flag = True
    while flag:
        print('1. Добавить контакт',
              '2. Ввести контакт',
              '3. Найти контакт',
              '4. Удалить контакт',
              '5. Выйти', sep = '\n')
        n = input('Выберите действие: ')
        match n:
            case '1':
                open_contakt()
            case '2':
                show_contakt()
            case '3':
                find_contakt()
            case '4':
                delete_contact()
            case '5':
                flag = False

choouse()

# def edit_contact():
#     arr_1 = []
#     with open(FILE_PATH, 'r', encoding='utf8') as file:
#         old_name = input('Введите имя или фамилию из справочника: ')
#         #lines = file.readlines()
#         with open(FILE_PATH, 'w', encoding="utf8") as file:
#             for contakt in file:
#                 if old_name in contakt:
#                     new_name = input('Введите новую запись: ')
#                     arr_1.replace(contakt, new_name)