from encodings import utf_8
from view import user_choiсe
from random import  randint
def search():
    while True:
        user_choiсe()
        n = int(input())
        if n ==1:
            with open('learners.txt', 'r', encoding = 'utf_8') as f:
                    for line in f.readlines():
                        print(line)
            input('\nНажмите enter')
        
        elif n == 2:
            answer = input('Введите фамилию ученика: ').title()
            with open('learners.txt', 'r', encoding='utf_8') as f:
                for line in f.readlines():
                    if answer in line:
                        a = line.split()
                        print(a[3])                        
                        input('\nНажмите enter')

        elif n == 3:
            with open('learners.txt','a+', encoding = 'utf_8') as file:
                
                new_contact = input('Введите данные через пробел (Фамилия и имя, год рождения, успеваемость) ')
                file.write(new_contact )
               
                file.close()
                input('\nНажмите enter')
            
  
        

        elif n == 4:
            print('До встречи')
            exit()