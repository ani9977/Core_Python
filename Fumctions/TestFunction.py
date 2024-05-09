def sum(a,b):

    "it adds  two numbers"

    print('a',a,'b',b)

    c=a+b

    return c

print(sum(6,10))

def changeList(List):
    list.append(6)
    print(list)
    return

list=[1,2,3,4,5]
print(list)
changeList(list)
print(list)

def sumnum( a, *varg ):
   t = a
   for n in varg:
      t+=n
   return t;

total = sumnum(1,2,3,4,5)
print('Total', total)

def my_function(x):
  return 5 * x

print(my_function(2))
print(my_function(5))
print(my_function(9))


def my_function(fname):
  print(fname + " Gupta")

my_function("John")
my_function("Amy")
my_function("Linus")

print("Output show passing value as a parameter : ")
def my_function(food):
 for x in food:
   print(x)
fruits = ["Ram", "Shyam", "Jerry"]

