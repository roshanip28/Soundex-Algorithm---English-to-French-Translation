import sys
from fst import FST
from fsmutils import composewords

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    list26 = [2, 3, 4, 5, 6]
    list16 = [1, 2, 3, 4, 5, 6]
    list79 = [7, 8, 9]
    list19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list29 = [2, 3, 4, 5, 6, 7, 8, 9]


    f.add_state('1')
    f.add_state('2')
    f.add_state('3')
    f.add_state('4')
    f.add_state('5')
    f.add_state('6')
    f.add_state('7')
    f.add_state('8')
    f.add_state('9')
    f.add_state('10')
    f.add_state('11')
    f.add_state('12')
    f.add_state('13')
    f.add_state('14')
    f.add_state('15')
    f.add_state('16')
    f.add_state('17')
    f.add_state('18')
    f.add_state('19')
    f.add_state('20')
    f.add_state('21')


    f.initial_state = '1'

    f.set_final('2')
    f.set_final('4')
    f.set_final('7')
    f.set_final('8')
    f.set_final('9')
    f.set_final('10')
    f.set_final('12')
    f.set_final('14')
    f.set_final('15')
    f.set_final('19')
    f.set_final('21')

    element_z=[0]
    element_o=[1]


    for i in element_o:
        i=str(i)
        f.add_arc('1', '6', i, [kFRENCH_TRANS[int(i) * 10]])
        f.add_arc('18', '6', i, [kFRENCH_TRANS[int(i) * 10]])
        f.add_arc('1', '3', i, ())
        f.add_arc('18', '3', i, ())
        f.add_arc('11', '12',i, [kFRENCH_AND, kFRENCH_TRANS[int(i) + 10]])
        f.add_arc('13', '15', i, [kFRENCH_TRANS[20], kFRENCH_TRANS[int(i)]])
        f.add_arc('17', '21', i, [kFRENCH_TRANS[20], kFRENCH_TRANS[int(i) + 10]])
        f.add_arc('1', '18', i, [kFRENCH_TRANS[100]])
        f.add_arc('5', '8', i, [kFRENCH_AND, kFRENCH_TRANS[int(i)]])

    for i in element_z:
        i=str(i)
        f.add_arc('1', '10', i, [kFRENCH_TRANS[int(i)]])
        f.add_arc('11', '12', i, [kFRENCH_TRANS[int(i) + 10]])
        f.add_arc('18', '20', i, ())
        f.add_arc('6', '9', i, ())
        f.add_arc('20', '10', i, ())
        f.add_arc('13', '14', i, [kFRENCH_TRANS[20]])
        f.add_arc('17', '19', i, [kFRENCH_TRANS[20], kFRENCH_TRANS[10]])
        f.add_arc('1', '1', i, ())
        f.add_arc('5', '7', i, ())

    for i in list16:
        i=str(i)
        f.add_arc('3', '4', i, [kFRENCH_TRANS[int(i) + 10]])

    for i in list29:
        i=str(i)
        f.add_arc('13', '15',i, [kFRENCH_TRANS[20], kFRENCH_TRANS[int(i)]])
        f.add_arc('5', '8', i, [kFRENCH_TRANS[int(i)]])
        f.add_arc('1', '18', i, [kFRENCH_TRANS[int(i)], kFRENCH_TRANS[100]])

    for i in list26:
        i=str(i)
        f.add_arc('11', '12',i, [kFRENCH_TRANS[int(i) + 10]])
        f.add_arc('17', '21',i, [kFRENCH_TRANS[20], kFRENCH_TRANS[int(i) + 10]])
        f.add_arc('18', '5',i, [kFRENCH_TRANS[int(i) * 10]])
        f.add_arc('1', '5',i, [kFRENCH_TRANS[int(i) * 10]])


    for i in list19:
        i=str(i)
        f.add_arc('20', '2', i, [kFRENCH_TRANS[int(i)]])
        f.add_arc('1', '2', i, [kFRENCH_TRANS[int(i)]])


    for i in list79:
        i=str(i)
        f.add_arc('11', '12', i, [kFRENCH_TRANS[10], kFRENCH_TRANS[int(i)]])
        f.add_arc('6', '9',i, [kFRENCH_TRANS[int(i)]])
        f.add_arc('17', '21',i, [kFRENCH_TRANS[20], kFRENCH_TRANS[10], kFRENCH_TRANS[int(i)]])

    list7 = [7]
    list8 = [8]
    list9 = [9]
    y=int(60)
    x=int(4)

    for i in list7:
        i=str(i)
        f.add_arc('18', '11', i, [kFRENCH_TRANS[y]])
        f.add_arc('1', '11', i, [kFRENCH_TRANS[y]])

    for i in list8:
        i=str(i)
        f.add_arc('1', '13', i, [kFRENCH_TRANS[x]])
        f.add_arc('18', '13', i, [kFRENCH_TRANS[x]])

    for i in list9:
        i=str(i)
        f.add_arc('1', '17', i, [kFRENCH_TRANS[x]])
        f.add_arc('18', '17', i, [kFRENCH_TRANS[x]])

    return f
if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))
