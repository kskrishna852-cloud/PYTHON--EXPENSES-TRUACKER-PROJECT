# EXPENSES TRUACKER PROJECT

expensesList =[]#list of expenses in farm of dicitionry
print("wellcome to Enxpenses Tracker:")

while True:
    print("======MENU=====")
    print("1.Add Expenses")
    print("2.view all expenses")
    print("3 Total Expenses")
    print("4.Exit")
    choice=int(input("Places Enter Youer choice:"))

#1 Add expense
    if(choice==1):
        date=input("kis date par kharcha kiya tha? :")
        categary=input("what kind of expenses? (food , travel , makeap , books):")
        description=input("given a more diails:")
        amount=float(input("Enter the amount:"))

        expenses={
            "date":date,
           "categary":categary,
           "description":description,
           "amount":amount,

        }
        expensesList.append(expenses)
        print("\n DONE BRO. Epense is Added succesfully")

# 2.VIEW ALL EXPENSSES
    elif(choice==2):
        if(len(expensesList)==0):
            print("NO Expenses Added.Pleses go know and expenses many")
        else:
            print("=====thsis youer all Enpenses=====")
            count=1
            for eachExpenses in expensesList:
                print(f"expenses Number{count} -> {eachExpenses["date"]}, {eachExpenses[" categary"]}, {eachExpenses["description"]},{eachExpenses["amount"]}")
                count=count+1
# VIEW TOTAL SPENDING
    elif(choice==3):
        total=0
        for eachExpenses in expensesList:
            total= total + eachExpenses["amount"]
            print("\n Totalexpenses=",total)
#4 EXIT
    elif(choice==4):
        print("THANK YOU FOR VISIT IN OUER SYSTEM")
        break
    else:
       print("INVALID CHOICE .TRY AGAIN")