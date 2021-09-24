koloda = [2,3,4,5,6,7,8,9,10,11,12,13,14] * 4
igrok = [11,11,12,12,13,13,13,14,14,15,15,15,16,16,17,17,18,19,20,21]
import random
random.shuffle(koloda)
random.shuffle(igrok)
print('Поиграем в очко?')
count = 0

while True:
    choice = input('Будете брать карту? 1-Возьму/2-Хватит')
    if choice == '1':
        current = koloda.pop()
        print('Вам попалась карта достоинством %d' %current)
        count += current
        if count > 21:
            print('Извините, но вы проиграли')
            print('-------------------'*3)
            print('Игра начинается заново')
            count=0
        elif count == 21:
            print('Поздравляю, вы набрали 21!')
            print('-------------------'*3)
            print('Игра начинается заново')
            count=0
        
        else:
            print('У вас %d очков.' %count)
    elif choice == '2':
        edit = igrok.pop()
        print('У противника %s очков' %edit)
        if (int(edit))>=(int(count)):
            print('-------------------'*3)
            print('Вы проиграли.')
            print('-------------------'*3)
            print('Игра начинается заново')
            count=0
          
        else:
            print('-------------------'*3)
            print('ВЫ ВЫЙГРАЛИ!')
            print('-------------------'*3)
            print('Игра начинается заново')
            count=0
