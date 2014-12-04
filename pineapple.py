import math
x=input()
if(int(x)==7):
	print("cool")
else:
	print("nah, that's wrong")

def p(x):
	if(x<10):
		print(x)
		return x
	p(math.floor(x/10))
	print(x)

p(int(x))

#git add --all
#git commit -am""
#git pull
#git push

