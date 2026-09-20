while True:
  a =int(input("enter the 1 number:"))
  b =int(input("entaer the 2 number:"))

  claculultionList=[]
  print("Wellcome To My Project")

  print("====MENU====")
  print("1.sum")
  print("2.subs")
  print("3.mul")
  print("4.div")
  print("5.exit")
  choice=int(input("Enter youer choice"))

#1 sum
   
  if(choice==1):
        sum=a+b
        print(sum)
        if(sum%2==0):
            print("value is even")
        else:
            print("number is odd")

#2 subs
  elif(choice==2):
        subs=a-b
        print(subs)
        if(subs%2==0):
            print("value is even")
        else:
            print("number is odd")

#3mul
  elif(choice==3):
        mul=a*b
        print(mul)
        if(mul%2==0):
          print("value is even")
        else:
          print("number is odd")

#4 div
  elif(choice==4):
        div=a/b
        print(div)
        if(div%2==0):
            print("value is even")
        else:
             print("number is odd")
               
#5eixt
  elif(choice==5):
        print("THANK YOU")
        break
  else:
        print("INVILID CHOICE, PLESES TRY AGAin")