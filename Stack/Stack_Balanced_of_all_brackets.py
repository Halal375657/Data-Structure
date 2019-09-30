'''This code workable on the all brackets sequence.
    for example:-
        input:-
            2
            (}(
            [{()}]
        output:-
            ()()() is balanced.
            ()()() is not balanced.
'''
#Complixity O(len(str_input))->O(n)
def is_balanced(str_input):
    s = []
    for ch in str_input:
        if ch is '[' or ch is '{' or ch is '(':
            s.append(ch)
        if ch is ']' or ch is '}' or ch is ')':
            if not s:
                return False
            p = s.pop()
            if p is '(':
                p = ')'
            elif p is '{':
                p = '}'
            elif p is '[':
                p = ']'
            if ch is not p:
                return False
    return not s

def test_is_balanced():
    assert True == is_balanced('[{()}]')
    assert False == is_balanced('(}')


if __name__=="__main__":
    for _ in range(int(input())):
        str_input = input()
        if is_balanced(str_input):
            print(str_input," is balanced")
        else:
            print(str_input,"is not balanced")

