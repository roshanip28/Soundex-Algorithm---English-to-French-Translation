from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """
    exceptions=['a','e','i','o','u','h','w','y','A','E','I','O','U','H','W','Y']
    repl_3=['b','f','p','v','B','F','P','V']
    repl_4=['c','g','j','k','q','s','x','z','C','G','J','K','Q','S','X','Z']
    repl_5=['d','t','D','T']
    repl_6=['l','L']
    repl_7=['m','n','M','N']
    repl_8=['r','R']

    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('1')
    f1.add_state('2')
    f1.add_state('3')
    f1.add_state('4')
    f1.add_state('5')
    f1.add_state('6')
    f1.add_state('7')
    f1.add_state('8')
    f1.initial_state = '1'

    # Set all the final states
    f1.set_final('2')
    f1.set_final('3')
    f1.set_final('4')
    f1.set_final('5')
    f1.set_final('6')
    f1.set_final('7')
    f1.set_final('8')


    # Add the rest of the arcs
    for letter in string.ascii_letters:

        if letter in exceptions:
            f1.add_arc('1', '2', (letter), (letter))
            for i in range(2,9):
                i=str(i)
                f1.add_arc(i,'2',(letter),())
        if letter in repl_3:
            f1.add_arc('1', '3', (letter), (letter))

            for i in range(2,9):
                i=str(i)
                if i == '3':
                    f1.add_arc('3','3',(letter),())
                else:
                    f1.add_arc(i,'3',(letter),('1'))

        if letter in repl_4:
            f1.add_arc('1', '4', (letter), (letter))

            for i in range(2,9):
                i=str(i)
                if i == '4':
                    f1.add_arc('4','4',(letter),())
                else:
                    f1.add_arc(i,'4',(letter),('2'))
        if letter in repl_5:
            f1.add_arc('1', '5', (letter), (letter))

            for i in range(2,9):
                i=str(i)
                if i == '5':
                    f1.add_arc('5','5',(letter),())
                else:
                    f1.add_arc(i,'5',(letter),('3'))
        if letter in repl_6:
            f1.add_arc('1', '6', (letter), (letter))

            for i in range(2,9):
                i=str(i)
                if i == '6':
                    f1.add_arc('6','6',(letter),())
                else:
                    f1.add_arc(i,'6',(letter),('4'))
        if letter in repl_7:
            f1.add_arc('1', '7', (letter), (letter))
            for i in range(2,9):
                i=str(i)
                if i == '7':
                    f1.add_arc('7','7',(letter),())
                else:
                    f1.add_arc(i,'7',(letter),('5'))
        if letter in repl_8:
            f1.add_arc('1', '8', (letter), (letter))

            for i in range(2,9):
                i=str(i)
                if i == '8':
                    f1.add_arc('8','8',(letter),())
                else:
                    f1.add_arc(i,'8',(letter),('6'))

    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    f2.add_state('5')


    f2.initial_state = '1'

    f2.set_final('2')
    f2.set_final('3')
    f2.set_final('4')
    f2.set_final('5')


    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '2', (letter), (letter))
    for n in range(10):
        for i in range(1,6):
            if i==5:
                f2.add_arc(str(i), str(i), (str(n)), ())
            elif i==1:
                f2.add_arc(str(i), str(i+2), (str(n)), (str(n)))
            else:
                f2.add_arc(str(i), str(i+1), (str(n)), (str(n)))


    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('2')
    f3.add_state('3')
    f3.add_state('4')
    f3.add_state('5')

    f3.initial_state = '1'
    f3.set_final('5')

    f3.add_arc('2', '3', (), ('0'))
    f3.add_arc('3', '4', (), ('0'))
    f3.add_arc('4', '5', (), ('0'))

    for letter in string.letters:
        f3.add_arc('1', '2', (letter), (letter))
    for number in xrange(10):
        f3.add_arc('1', '3', (str(number)), (str(number)))
        f3.add_arc('2', '3', (str(number)), (str(number)))
        f3.add_arc('3', '4', (str(number)), (str(number)))
        f3.add_arc('4', '5', (str(number)), (str(number)))
    
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1,f2,f3)))
