import re

print('Hello World!')


# questions = ['A large animal:', 'A small animal:', 'A Girls Name:', 'Adjective:', 'Plural Noun:']
answers = []

# message = """
#     *****************************************
#     Today we will be having fun with madlibs
#     *****************************************
#     Please input the required words.
#     *****************************************
#     """

with open('madlib_cli/madlib.txt') as ans:
    template = ans.readlines()[2]



questions = re.findall('{([^\}]*)}', template)
    


with open('madlib_cli/madlib.txt') as message:
    print(message.readlines()[0])



def wordanswers():
    for q in questions:
        # print(questions[q])
        user_input = input(f"{q}\n>>>>")
        answers.append(user_input)
        

wordanswers()

# print(answers)
for str in answers:
    template1 = re.sub("{([^\}]*)}",answers, template)
    
    
print(answers)
print(template1)


# def madlib():
#     with open('madlib_cli/madlib.txt') as ans:
#         template = ans.readlines()[2]
#         for i in answers:
#             for j in questions:
#                 replace()


# def writemadlib():
#     with open('madlib_cli/madlibdone.txt', 'w') as f2:
#     f2.write(madlib)

# print(answers)

# largeanimal = input("""A large animal
# """)

# smallanimal = input("""A small animal
# """)



# madlib = f"What are a {answers[0]} and backpacking {answers[1]} to do?Before you can help {answers[2]}, youll have to collect the {answers[3]} {answers[4]}" 
 
 


# print(madlib)

# with open('madlib_cli/madlibdone.txt', 'w') as f2:
#     f2.write(madlib)