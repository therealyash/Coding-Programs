"""
Write a program that defines two functions called create_sent1()
and create_sent2(). Both receive following 3 lists:
"""

subjects = ['He', 'She']
verbs = ['loves', 'hates']
objects = ['Tv Serials', 'Netflix']


def create_sen1(sub, verb, obj):
    lst = []
    for i in range(len(sub)):
        for j in range(len(verb)):
            for k in range(len(obj)):
                sent = sub[i] + ' ' + verb[j] + ' ' + obj[k] + "."
                print(sent)
                lst.append(sent)
    return lst

print(create_sen1(subjects, verbs, objects))










