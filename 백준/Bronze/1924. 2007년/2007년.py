JAN = 31
FEB = 28
MAR = 31
APR = 30
MAY = 31
JUN = 30
JUL = 31
AUG = 31
SEP = 30
OCT = 31
NOV = 30
DEC = 31    
MONTHS = [JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]
WEEKS = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

s = input().split(" ")

sum = 0

for i in range(int(s[0]) - 1):
    sum += MONTHS[i]
sum += int(s[1])

print(WEEKS[sum % 7])