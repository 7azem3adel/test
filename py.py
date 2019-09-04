

# # i = 1 

# # while i <=10:
# #     print(i)
# #     i += 1

# # print ('done')
# secretWord = "hazem"
# guess = ""
# guessLimit = 1
# print("enter the secret word")
# while guess != secretWord and guessLimit < 4:
#     guessLimit += 1
#     guess = input("enter guess: ")
    

# if guess != secretWord and guessLimit == 4:        
#     print('out of guesses')
# else :
#     print("correct!!")

# variable = open("test1.txt", "a")

# variable.write(input("enter the new line : "))
# variable.close()
flag = 1
openMusic = open("music.csv","r")
openMusic2 = open("music2.csv","r")
total = len(openMusic.readlines())
openMusic.seek(0)
for line,line2 in zip(openMusic.readlines(),openMusic2.readlines()):
    if line2 == line:
        flag += 1
print(str(int(flag/total*100)) + "%")
openMusic.close()
openMusic2.close()