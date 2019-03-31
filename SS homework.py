height_input = int(input('Please, enter the triangle height: '))
width_input = int(input('Please, enter the triangle width: '))
symbol = '*'
i = 0
i2 = 1
if (height_input and width_input) >= 1:
    print('This is the first triangle:')
else:
    print('Triangle sides length should be positive and more than 0')

while i < height_input and i2 <= width_input:
    print(symbol * i2)
    i += 1
    i2 += 1

if height_input and width_input >= 1:
    print('This is the second one:')

i3 = height_input
i4 = width_input
while i3 > 0 and i4 > 0:
    if width_input >= height_input:
        print(symbol * i3)
        i3 -= 1
    elif width_input <= height_input:
        print(symbol * i4)
        i4 -= 1

if height_input and width_input >= 1:
    print('This is the third one:')

space_symbol = ' '
i5 = 1
i6 = 1
while i5 <= height_input and i5 <= width_input:
    if width_input >= height_input:
        print(space_symbol * (height_input - i5) + symbol * i6 + space_symbol * (height_input - i5))
        i5 += 1
        i6 += 2
    elif width_input <= height_input:
        print(space_symbol * (height_input - i5) + symbol * i6 + space_symbol * (height_input - i5))
        i5 += 1
        i6 += 2

if height_input and width_input >= 1:
    print('This is the fourth one:')

i7 = 1
i8 = 1
while i7 <= height_input and i7 <= width_input:
    if width_input and height_input != 0:
        print(space_symbol * (height_input - i8) + symbol * i7)
        i7 += 1
        i8 += 1
print('Thank you!')