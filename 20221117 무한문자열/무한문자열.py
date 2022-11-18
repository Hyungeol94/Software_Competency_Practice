#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYP5JmsqcngDFATW

def compute():
    (a, b) = map(str, input().split(' '));

    first_string_length = len(a);
    second_string_length = len(b);

    new_a = a*second_string_length;
    new_b = b*first_string_length;

    if (new_a==new_b):
        return True;
    else:
        return False;


if __name__ == '__main__':
    n = int(input());
    for i in range(1, n+1):
        if (compute()):
            print('#'+str(i)+' yes');
        else:
            print('#' + str(i) + ' no');


