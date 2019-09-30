'''
    This code work only on the first brackets sequence.
    for example:-
        input:-
            2
            ()()()
            (()(
        output:-
            ()()() is balanced.
            ()()() is not balanced.
'''

#Complixity:-  O(len(input_sequence))->O(n)
def is_balanced(input_sequence):
    left_brackets = []

    for ch in input_sequence:
        if ch == '(':
            left_brackets.append(ch)
        if ch == ')':
            if not left_brackets:
                return False
            left_brackets.pop()

    return not left_brackets

#This test method for the is_balanced().
def test_is_balanced():
    assert True == is_balanced('()()()')
    assert True == is_balanced('(())')
    assert False == is_balanced(')(')
    assert False == is_balanced('(()()(')

if __name__ == "__main__":
    for _ in range(int(input())):
        input_sequence = input()

        if is_balanced(input_sequence):
            print(input_sequence, "is balanced")
        else:
            print(input_sequence, "is not balanced")
