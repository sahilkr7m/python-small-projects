import random
print("This is dice simulator\n")
z ="y"
while z =="y"or z=="Y":

  x=random.randint(1,6)

  if x==1:
    print("--------")
    print("[       ]\n")
    print("[   0   ]\n")
    print("[       ]\n")
    print("--------\n")
  elif x==2:
    print("--------")
    print("[   0   ]\n")
    print("[       ]\n")
    print("[   0   ]\n")
    print("--------\n")
  elif x==3:
    print("--------")
    print("[   0   ]\n")
    print("[   0   ]\n")
    print("[   0   ]\n")
    print("--------\n")
  elif x==4:
    print("--------")
    print("[ 0    0 ]\n")
    print("[        ]\n")
    print("[ 0    0 ]\n")
    print("--------\n")
  elif x==5:
    print("--------")
    print("[ 0    0 ]\n")
    print("[    0   ]\n")
    print("[ 0    0 ]\n")
    print("--------\n")
  elif x==6:
    print("--------")
    print("[ 0    0 ]\n")
    print("[ 0    0 ]\n")
    print("[ 0    0 ]\n")
    print("--------\n")
  z=input("To continue enter Y")
