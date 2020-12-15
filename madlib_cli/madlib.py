import re

print('Hello World!')

answers = []


with open('madlib_cli/madlib.txt') as ans:
    template = ans.readlines()[2]


questions = re.findall('{([^}]*)}', template)


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

