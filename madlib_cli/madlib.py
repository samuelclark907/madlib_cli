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



questions = re.findall('{([^}]*)}', template)

# print(questions)
# print(stripped)

def parse_template(string):
    stripped_words = re.findall('{([^}]*)}', string)
    stripped_txt = re.sub('{([^}]*)}',"{}",string)
    return stripped_txt, tuple(stripped_words)

# parse_template()

def read_template(path):
    with open(path) as message:
        openmessage = message.readlines()[0]
        print(openmessage)
        return openmessage






def wordanswers():
    for q in questions:
        # print(questions[q])
        user_input = input(f"{q}\n>>>>")
        answers.append(user_input)
        



# print(answers)
def print_answers():
    template1 = template
    for word in answers:
        template1 = re.sub("{([^}]*)}",word, template1, count = 1)
    print(template1)
    with open('madlib_cli/madlibdone.txt', 'w') as f2:
        f2.write(template1)
    
# print(answers)

if __name__ == '__main__':
    read_template('madlib_cli/madlib.txt')
    wordanswers()
    print_answers()




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

