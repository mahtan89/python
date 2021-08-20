number_one = float(input('type number one :) \n'))
number_two = float(input('type number two :) \n'))
operator =  input('type a operator :) \n')
if operator ==  '+' :
    textone = f'The answer is {number_one + number_two}'
    print(textone)
elif operator ==  '-' :
    texttwo = f'The answer is {number_one - number_two}'
    print(texttwo)
elif operator ==  '*' :
    textthree = f'The answer is {number_one * number_two}'
    print(textthree)
elif operator ==  '/' :
    textfour = f'The answer is {number_one / number_two}'
    print(textfour)
elif operator ==  '**' :
    textfive = f'The answer is {number_one ** number_two}'
    print(textfive)
else :
    print('Sorry ! i dont now :(')
