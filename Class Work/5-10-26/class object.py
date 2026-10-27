# class Myclass:

#     def fun1(self,__a):
#         print(__a)
#         print("Method 1!!")
        
#     def fun2(self):
#         print("Method 2!!")

#     def fun3(self):
#         print("Method 3!!")

# obj=Myclass()
# obj.fun1(10)
# obj.fun2()
# obj.fun3()

class even:
    def even():
        if(n%2==0):
                print("Even Number")
        else:
                print("odd number")
    def prime():
         prime=0
         for i in range(1,n+1):
              if(n%i==0):
                   prime+=1
              if(prime==2):
                    print("Prime Number")
                    
              else:
                    print("Not Prime Number")
                    
    def fect():
          fact=1
          i=1
          while(i<=n):
                fact=fact*1
                i=i*1
          print(fact)
                          
n=int(input("Enter Number :"))
e=even
e.even()
e.prime()
e.fect()