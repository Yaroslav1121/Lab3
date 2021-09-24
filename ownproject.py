print('Санек: Привет Виталик даш денег на колу?')
print('Виталик: Сколько?')
while True:
    try:
        i = int(input('Санек: Всего-то '))
        if i < 30:
            print('Конечно дружище, держи')
        elif i >= 30:
             print('Виталик: Это слишком')
        break
    except ValueError:
                    print('Виталик: в гривнах говори')
input()
