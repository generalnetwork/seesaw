'''Consider telephone book database of N clients. Make use of a hash table
implementation to quickly look up client's telephone number. Make use of two
collision handling techniques and compare them using number of comparisons
required to find a set of telephone numbers'''


n = int(input("Enter the number of records : "))
hashTable = [-1]*n

#FUNCTION FOR LINEAR PROBING
def linearProbing(val, name, phone) :
    temp = [(name, phone)]
    while hashTable[val] != -1 :
       val = (val + 1) % n   
    hashTable[val] = temp
    displayHashTable()
#FUNCTION FOR SEPARATE CHAINING
def separateChaining(val, name, phone) :
    hashTable[val].append((name, phone))
    displayHashTable()
   
def insertValue(name, phone) :
    val = phone % n
    if hashTable[val] == -1 :
        hashTable[val] = [(name, phone)]
    else :
        print("\n***** Collision Occurred ******")
        choice = int(input('1.Linear Probing\n2.Separate Chaining\n'))
        if choice == 1 :
            linearProbing(val, name, phone)
        else :
            separateChaining(val, name, phone)
           

def displayHashTable() :
    for i in range(n) :
        print(str(i) + " -> " + str(hashTable[i]))
       
def searchNum(phone) :
    for i in range(10) :
        for name, num in hashTable[i] :
            if(num == phone) :
                print(f'Element Found! : {name}')
                return
    print("Not found")

for i in range(n) :
    name = input("Enter the name : ")
    phone = int(input("Enter the phone number : "))
    insertValue(name, phone)
   
print('\nHash Table\n')
displayHashTable()




#-----------------MENU--------------------
flag =1
while flag==1:
    print("menu")
    print ('''DO YOU WANT TO SEARCH AN ELEMENT??
             1) Yes
             2) Nope
 ''')
 
    no=int(input("choose option number"))
    if no == 1:
       insEle = int(input("enter total num u wanna search : ")) 
       for i in range(insEle) :
           phone = int(input("Enter the phone number to be searched : "))
           searchNum(phone)

       v=input("Do you wish to continue??(y/n)")
       if v=='y':
           flag=1
       elif v=='n':
          flag=0
          break
       else :
           print("INVALID OPTION")
    elif no== 2:
        break
    else :
       print("option not available")
       flag =0
