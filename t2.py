import sys
year=int(sys.argv[1])

is_leap_year=((year%100!=0) and  (year%4==0)) or (year%400==0)

print (is_leap_year)
