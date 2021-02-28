#
# Example file for working with loops
#

def func1():
  x = 0

  # define a while loop
  while(x < 10):
     print(x)
     x = x + 1 

  # define a for loop
  for i in range(5,10):
    print(i)

  # use a for loop over a collection
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i in days:
    print(i)
  
  # use the break and continue statements
  for i in range(1,10):
    if(i==8): 
      print("i is 8 so will brack.") 
      break
    elif(i == 6): 
      print("i is 6 so will continue.") 
      continue
    print(i)

  #using the enumerate() function to get index 
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i, d in enumerate(days):
    print(i,d)
  
func1()
