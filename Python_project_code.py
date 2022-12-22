import pwinput
print("Marketing and Sales System")
print('\n\t\t\tWelcome\t\t\t\n')
print("1.Login")
print("2.Exit")
choice=int(input("Enter your choice: "))
if choice==1:
    name=input("Enter the user name: ")
    passwd=pwinput.pwinput(prompt="Enter the password: ",mask="*")
    while name=='sophie' and passwd=='sophie123':
            print('1. Registry for Products Seller')#Akshaya
            print('2. Registry for Order Placement')#Sarayu
            print('3. Registry the Customer Details')#Ishpreet
            print('4. Registry for Cancelation of Order')#Dharshini
            print('5. Display the Products availability')#Akshaya
            print('6. Display the Datas about order placement')#Sarayu
            print('7. Display the Customer details')#Ishpreet
            print('8. Display the History of cancelation of order')#Dharshini
            print('9. Exit')
            choice=int(input('\nEnter your choice '))
            if choice==1:#Akshaya
                f=open('seller.txt','a')
                seller_name=input('Enter the product seller name:')
                product_type=input('Enter the product type:')
                product_brand=input('Enter the product brand:')
                product_available=input('Stocks available:')
                print("\n")
                f.write(seller_name)
                f.write("\t")
                f.write(product_type)
                f.write("\t")
                f.write(product_brand)
                f.write("\t")
                f.write(product_available)
                f.write("\n")
                f.close()  
            elif choice==2:#Sarayu
                f=open('customer.txt','a')
                customer_name=input('Enter the customer name:')
                product_name=input('Enter the product name:')
                demanding_quantity=input('Enter the quantity:')
                print("\n")
                f.write(customer_name)
                f.write("\t")
                f.write(product_name)
                f.write("\t")
                f.write(demanding_quantity)
                f.write("\n")
                f.close()  
            elif choice==3:#Ishpreet
                f=open('customerdetail.txt','a')
                customer_name=input('Enter the customer name:')
                mobile_number=input('Enter mobile number:')
                address=input('Enter your adress:')
                print("\n")
                f.write(customer_name)
                f.write("\t")
                f.write(mobile_number)
                f.write("\t")
                f.write(address)
                f.write("\n")
                f.close()
            elif choice==4:#Dharshini
                f=open('canceldetail.txt','a')
                customer_name=input('Enter the customer name:')
                order_number=input('Enter the order number:')
                products_contained=input('Enter the product contained in your order:')
                reason_cancelation=input('Enter the reason for cancelling the order:')
                confirm_cancel=input('Say YES to confirm cancellation:')
                print("\n")
                f.write(customer_name)
                f.write("\t")
                f.write(order_number)
                f.write("\t\t")
                f.write(products_contained)
                f.write("\t")
                f.write(reason_cancelation)
                f.write("\t")
                f.write(confirm_cancel)
                f.write("\n")
                f.close()
            elif choice==5:#Akshaya
                try:
                    f=open("seller.txt","r")
                    print("_______________________________________________________________________________________________")
                    print("_______________________________________________________________________________________________\n")
                    print("Seller\tProduct \tBrand\t\tAvailability\n")
                    print(f.read())
                    print("_______________________________________________________________________________________________")
                    print("_______________________________________________________________________________________________\n")
                    
                except:
                    print("\nSorry no text file with this name available\n")
            elif choice==6:#Sarayu
                try:
                    f=open("customer.txt","r")
                    print("_______________________________________________________________________________________________")
                    print("_______________________________________________________________________________________________\n")
                    print("Customer\tProduct\t\tAvailability\n")
                    print(f.read())
                    print("_______________________________________________________________________________________________")
                    print("_______________________________________________________________________________________________\n") 
                except:
                    print("\nSorry no text file with this name available\n")
            elif choice==7:#Ishpreet
                try:
                    f=open('customerdetail.txt','r')
                    print("_______________________________________________________________________________________________")
                    print("_______________________________________________________________________________________________\n")
                    print("Name  \tNumber  \tAddress\n")
                    print(f.read())
                    print("_______________________________________________________________________________________________")
                    print("_______________________________________________________________________________________________\n")
                except:
                    print("\nSorry no text file with this name available\n")
            elif choice==8:#Dharshini
                try:
                    f=open('canceldetail.txt','r')
                    print("_______________________________________________________________________________________________")
                    print("_______________________________________________________________________________________________\n")
                    print("Name \tOrder Number\tProducts\tReason\t\t\t\tConfirmation\n")
                    print(f.read())
                    print("_______________________________________________________________________________________________")
                    print("_______________________________________________________________________________________________\n")
                except:
                    print("\nSorry no text file with this name available\n")
            elif choice==9:
                print('Thank you for using the service')
                break