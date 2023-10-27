num = int(input("enter the year your wish :"))
if (num % 4 == 0):
  if (num % 100 == 0):
    if (num % 400 == 0):
      print("%d is a leap year " % num)
    else:
      print("%d is not leap year" % num)
  else:
    print("%d is not a leap year " % num)
else:
  print("%d is not leap year" % num)