import random

upper_letters = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' ,
 				 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 
 				 'W' , 'X' , 'Y' , 'Z']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                 'w', 'x', 'y', 'z',]

all_letters = [upper_letters, lower_letters]

def getRandomCode(q):
	code = ''
	for i in range(q):
		letters = random.choice(all_letters)
		code += random.choice(letters)

	return code



	
