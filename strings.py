Str1="This is a string"
Str2='this is also a string'
Str3="""this is a string"""
Str4='''this is also a string'''
str5="This is a string with a 'single quote' inside"
str6='This is a string with a "double quote" inside'
str7='''This is a string with a "double quote" and a 'single quote' inside'''
str1="manthan"
str2="gupta"
str3=str1+" " +str2
print(str3)             #manthan gupta
print(str1,str2)        #manthan gupta
print(str1+str2)        #manthangupta
print(len(str2+str1))   #12
print(len(str3))        #13
print(str1[0])          #m
print(str1[1])          #a
print(str1[2])          #n
print(str1[3])          #t
print(str1[4])          #h
print(str1[5])          #a
print(str1[6])          #n
print(str1[-1])         #n
print(str1[-2])         #a
print(str1[-3])         #h
print(str1[-4])         #t
print(str1[-5])         #n
print(str1[-6])         #a
print(str1[-7])         #m
print(str1[0:3])        #man
print(str1[1:4])        #ant
print(str1[2:])         #nthan
print(str1[:3])         #man
print(str1[1:])         #anthan
print(str1[0:2])        #ma
print(str1[0:6])        #mantha
print(str1[0:len(str1)])        #manthan
print(str1.endswith('n')) # True
print(str1.endswith('a')) # False
print(str1.startswith('m')) # True
print(str1.startswith('a')) # False
print(str1.find('a'))    # 1
print(str1.find('z'))    # -1 (not found)
print(str1.index('a'))   # 1
#print(str1.index('z'))   # Raises ValueError (not found)
print(str1.count('a'))   # 2
