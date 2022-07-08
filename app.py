import random

length = int(input('Password Length > '))
symbols = ['0','1','2','3','4','5','6','7','8','9','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','I','P','A','S','D','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','!','@','#','$']

def create_password(characters , length):
    result = ''
    for i in characters:
        result += i
    output_1 = random.sample(result , length)
    output_2 = ''
    for symbols in output_1:
        output_2+=symbols
    print(output_2)

create_password(symbols , length)
