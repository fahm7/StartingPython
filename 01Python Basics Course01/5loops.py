i= 5
print (type(i))  
print('________________________WHILE LOOP1_________________________')
i = 1
while i < 6:
  print(i)
  i += 1

print('________________________WHILE LOOP2 PASS_________________________')

while i>0:
	print (i)
	i=i-1
	pass
print("Done!!")
print (i)

print('________________________WHILE LOOP3_________________________')

#while True:
#	line = raw_input("enter some thing, or \'stop\' to stop the process  ")
#	if line=='stop':
#		break

#print (line)
#print("Done!!")

print('________________________WHILE LOOP4  CONTINUE_________________________')

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


print('________________________FOR LOOP1 FOR_________________________')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

print('________________________FOR LOOP2 CONTINUE_________________________')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


for x in range(6):
  print(x)

print('________________________FOR LOOP3 RANGE_________________________')

''' The range() function defaults to increment the sequence by 1, however it is possible to specify
 the increment value by adding a third parameter: range(2, 30, 3):
'''
for x in range(2, 30, 3):
  print(x)

print('________________________FOR NESTED LOOP4 NESTED FOR _________________________')
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)