#'' "How to super market bill Generation.we will see given the below. which condition we used once we observe it.otherwise we understand"''.
import math
from datetime import datetime
name = input("enter your name:")
def bill_cal():
    a=True
    total_price = 0
    list_item_price =[]
    while a:
        print('''
             1. list _of _items
             2.choose item
             3.exit
             ''')
        choice = int(input("enter your choice"))
        choices = [1,2,3]

        if choice in chioces:
            d={"dal":65,"oil":70,"mirchi":180,"paste":50,"shampo":50}
            if choice==1:
                c=1
                for i, j in d .items():
                    print("\t,c",".","i","Rs","j")
                    c+=1
            if choice ==2:
                q= True
            while q:
                print("press q to see main menu.")
                item = input("enter item:")
                if item in d.keys():
                    qnt = input("enter quantity",)
                    if qnt.isdigit():
                        qnt = int(qnt)
                        price = float(d[item]*qnt)
                        list_item_price.append =((item,qnt,price))
                        total_price+=price
                    else:
                        print("invaild input quantity..")
                elif item=="q":
                    q=false
                else:
                    print("item not present")
        if choice ==3:
            a = false            

    else:
        print("Invaild Input. Please enter a vaild input.")
    return total_price,"Thank you",'Please visit again.', list_item_price
    total_price,msg,item_price = bill_cal()
    if total_price !=0:
        print('\n')
        print('''
                JP stores p BTM,
                Banglore, 560076
        ''')
        print("customername":,name,"\t",'Date': datetime.now())    
        print(20*"==")
        #print('\n')    
        for j in item_price:
            print('Item:',j[0],'\tquantity',j[1],'price:',j[2])
        gst=total*0.01
        gst =math.cell(gst)
        print(18*'==')
        print('GST:Rs.',float(gst+total))
        print('Total Payable amount:Rs.', float(gst+total))
        print(18*'==')
    else:
        print("Hey,you not Brought anything...please Buy something you.")
        bill_cal()



 
