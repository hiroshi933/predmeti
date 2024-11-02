import random
try:
    syllabus = {
        'Элементы высшей математики': 2,
        'Архитектура аппаратных средств': 2,
        'Основы алгоритмизации и программирования': 3,
        'Основы графики и дизайна': 2,
        'Иностранный язык': 2,
        'Информационные технологии': 1,
        'Базы данных': 3,
        'Физкультура': 3
    }
    while True:
        print('Список возможных действий:')
        print('1 - Вывести "учебный план" на экран ')
        print('2 - Найти информацию по части названия предмета')
        print('3 - Добавить новый предмет в учебный план')
        print('4 - Удалить  предмет из учебного плана')
        print('5 - Изменить  количество часов по предмету')
        print('0 - Закончить работу')
        # запрашиваем у пользователя номер действия:
        user_choice=int(input("Выберите № действия: "))
        if(user_choice==1):
            print("Учебный план:")
            for subject in syllabus:
                hours = syllabus[subject]
                sum_hours=sum(syllabus.values())
                print(f"{subject}: {hours} ч.")
            print(f'Общее кол-во занятий по всем предметам: {sum_hours}')
        if(user_choice==2):
            user_input = input('Введиите предмет, чтобы вывести информацию о нем: ').upper()
            # print(syllabus.keys())
            flag=False
            for i in syllabus.keys():
                if user_input in i.upper():
                    print(f'Нашел в предмете {i}')
                    flag = True
            if(flag==False):
                print("Такого предмета нет, ознакомьтесь со списком!")
        if(user_choice == 3):
            input_original = input('Введите Новый предмет: ')
            input_hours = int(input('Введите кол-во часов: '))
            if input_original in syllabus:
                print("Такого предмета нет, ознакомьтесь со списком!")
            syllabus[input_original]=input_hours
            print(f'Предмет {input_original}  был добавлен в словарь')
            for subject in syllabus:
                hours = syllabus[subject]
                print(f"{subject}: {hours} ч.")
        if(user_choice == 4):
            del_item=input('Введите предмет, который вы хотите удалить: ').strip()
            del syllabus[del_item]
            for subject in syllabus:
                hours = syllabus[subject]
                print(f"{subject}: {hours} ч.")
        if(user_choice == 5):
            syllabus_item=input("Введите предмет, у которого нужно поменять часы: ")
            if syllabus_item not in syllabus:
                print("Такого предмета нет, ознакомьтесь со списком!")
            else:
                syllabus_hour = int(input("Введите кол-во часов: "))
                syllabus[syllabus_item]=syllabus_hour
                for subject in syllabus:
                    hours = syllabus[subject]
                    print(f"{subject}: {hours} ч.")
        if(user_choice == 0):
            print('До свидания! Хорошего дня :)')
            break
except ValueError as e:
    print("Некорректный ввод данных!")