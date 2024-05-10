'''To create ADT that implements the "set" concept'''

setA = set()
noA = int(input("ENTER TOTAL NO. OF ELEMENTS IN SETA: "))
if (noA>10):
   print("no more than 10!")
else:
   for i in range(noA):
       addEle = input(f"enter element no. {i+1}: ")
       setA.add(addEle)
   print(setA)

setB = set()
noB = int(input("ENTER TOTAL NO. OF ELEMENTS IN SETB: "))
if (noB>10):
   print("no more than 10!")
else:
   for i in range(noB):
       addEle = input(f"enter element no. {i+1}: ")
       setB.add(addEle)
   print(setB)






#-----------------MENU--------------------
flag =1
while flag==1:
    print("menu")
    print ('''CHOOSE ONE OF THE SET OPERATIONS TO PERFORM
             1) Union
             2) Intersection
             3) Difference
             4) Symmetric Difference
             5) SubSet
             6) Insert Element
             7) Remove Element
             8) Size of a Set
             9) Find an element
 ''')
 
    no=int(input("choose option number"))
    if no == 1:
       print("Union of the two sets is: \n" , setA.union(setB))
       v=input("Do you wish to continue??(y/n)")
       if v=='y':
           flag=1
       elif v=='n':
          flag=0
          break
       else :
           print("INVALID OPTION")
    elif no== 2:
       print("Intersection of the two sets is: \n" , setA.intersection(setB))
       w=input("Do you wish to continue??(y/n)")
       if w=='y':
           flag=1
       elif w=='n':
           flag = 0
           break
       else :
           print("INVALID OPTION")
    elif no == 3 :
       print("Difference of the two sets A and B is: \n" , setA - setB)
       v=input("Do you wish to continue??(y/n)")
       if v=='y':
           flag=1
       elif v=='n':
           flag = 0
           break
       else :
           print("INVALID OPTION")
    elif no == 4 :
       print("Symmetric Difference of the two sets is: \n" , setA.symmetric_difference(setB))
       v=input("Do you wish to continue??(y/n)")
       if v=='y':
           flag==1
       elif v=='n':
           flag = 0
           break
       else :
           print("INVALID OPTION")
    elif no == 5 :
       checkSub = setB.issubset(setA)
       if(checkSub == 1):
            print("set B is a Subset of Set A")
       else:
            print("set B is not a Subset of Set A")
       v=input("Do you wish to continue??(y/n)")
       if v=='y':
           flag=1
       elif v=='n':
           flag = 0
           break
       else :
           print("INVALID OPTION")
    elif no == 6 :
       insEle = input("Enter element you want to insert: ")
       nameSet= int (input("enter which set you want to enter the element(1 or 2) : "))
       if(nameSet == 1):
            setA.add(insEle)
       elif(nameSet==2):
            setB.add(insEle)
       else:
            print("invalid choice")
       
       v=input("Do you wish to continue??(y/n)")
       if v=='y':
           flag=1
       elif v=='n':
           flag = 0
           break
       else :
           print("INVALID OPTION")
    elif no == 7 :
       insEle = input("Enter element you want to remove: ")
       nameSet= int (input("enter which set you want to enter the element(1 or 2) : "))
       if(nameSet == 1):
            setA.remove(insEle)
       elif(nameSet==2):
            setB.remove(insEle)
       else:
            print("invalid choice")
       print(f"2 sets after deleting are : \nSET A : {setA} \nSET B : {setB}")

       v=input("Do you wish to continue??(y/n)")
       if v=='y':
           flag=1
       elif v=='n':
           flag = 0
           break
       else :
           print("INVALID OPTION")
    elif no == 8 :
       print(f"size of the sets is : \nSET A : {len(setA)} \nSET B : {len(setB)} ")
       v=input("Do you wish to continue??(y/n)")
       if v=='y':
           flag=1
       elif v=='n':
           flag = 0
           break
       else :
           print("INVALID OPTION")
    elif no == 9 :
       check = input("enter element you want to find : ")
       nameSet= int (input("enter which set you want to find the element(1 or 2) : "))
       if(nameSet == 1):
            if check in setA:
                print("element found in setA")
            else :
                print("element not found")
       elif(nameSet==2):
            if check in setB:
                print("element found in setB")
            else :
                print("element not found")
       else:
            print("invalid choice")
       print(f"size of the sets is : \nSET A : {len(setA)} \nSET B : {len(setB)} ")
       v=input("Do you wish to continue??(y/n)")
       if v=='y':
           flag=1
       elif v=='n':
           flag = 0
           break
       else :
           print("INVALID OPTION")
    else :
       print("option not available")
       flag =0
