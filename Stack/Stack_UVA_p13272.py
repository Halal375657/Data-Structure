'''
    ACM ICPC Dhaka regional problem of UVA.Problem no: p13272
    Sample input:-
        3
        )(
        (()}
        [{(())}]
    Sample output:-
        Case 1:
        0
        0
        Case 2:
        0
        2
        0
        0
        Case 3:
        8
        6
        4
        2
        0
        0
        0
        0
'''
'''
     Complixity of stack() function:-
         = O(n+(n-1)+(n-2)+(n-3)+.......(n-(n-1)) - 1
         = O( (n*(n+1)/2) )
         Also another factor of complexity in this code is when i used 'in' operator at 3rd line before of the last line to the stack method.
         if n is 6(I mean n is length of sub paramitter) than complixity is
         = (6+(6-1)+(6-2)+(6-3)+(6-4)+(6-5)) - 1
         = (6+5+4+3+2+1) - 1
         = (22 - 1)
         = 21
         I am proved that by complixity_count variable in this code.
         
'''
#I am here use an extra variable called complixity_count for find out code complixity
def stack(sub, complixity_count):
    count = 0
    s = []
    for ch in sub:
        complixity_count[0] += 1
        if '(' is ch or ch is '{' or ch is '[' or ch is '<':
            s.append(ch)
            count += 1
        if ')' is ch or ch is '}' or ch is ']' or ch is '>':
            if not s:
                return count
            last = s.pop()
            absulate = abs(ord(last) - ord(ch))
            if absulate == 2 or absulate == 1:
                count += 1
            else:
                s.append(last)

    if ')' in s or '(' in s or '{' in s or '}' in s or '[' in s or ']' in s or '>' in s or '<' in s:
        complixity_count[0] += len(s)
        return 0
    else:
        return count

if __name__ == "__main__":
    for test in range(1, int(input())+1):
        complixity_count = [0]
        string = input()
        print("Case %d:"%test)
        for i in range(len(string)):
            sub = string[i:]
            c = stack(sub, complixity_count)
            print(c)
        print("Complixity is", complixity_count[0])
        
