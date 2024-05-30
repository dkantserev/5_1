 word=input()
l=len(word)
h=int(l/2)
left=word[:h:]
right=word[l-1:l-h-1:-1]
if left==right:
	print('yes')
else:
	print('no')	
