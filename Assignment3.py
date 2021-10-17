from numpy import *
a = array([[1,1,0,1,1],
           [0,2,0,3,1],
           [0,1,1,1,1],
           [1,0,1,0,1],
           [0,1,1,1,0]])
p= a[2][2]
q= a[2][1]
q1=a[1][1]
q2 = a[1][3]
v=[1,0,3]
n4= a[2-1][2] or a[2][2-1] or a[2][2+1] or a[2+1][2] == q
nd=a[2-1][2-1] or a[2-1][2+1] or a[2+1][2+1] or a[2+1][2-1] == q1

n4p= a[2-1][2] or a[2][2-1] or a[2][2+1] or a[2+1][2] == q2
ndp=a[2-1][2-1] or a[2-1][2+1] or a[2+1][2+1] or a[2+1][2-1] == q2
n4q=a[1][3-1] or a[1-1][3] or a[1][3+1] or a[1+1][3]

if n4 and v.__contains__(q):
    print("Given Points are 4 adjacent")
if nd and v.__contains__(q1):
    print("Given Points are D adjacent")
if (n4p and v.__contains__(q2)) or (ndp and v.__contains__(q1) and (a[2-1][2] or a[2][2-1] or a[2][2+1] or a[2+1][2]).intersection(n4q)):
    print("Given Points are M adjacent")