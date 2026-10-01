def prime_number(n,prime=0):
      for i in range(1, n + 1):
            if n % i == 0:
                  prime += 1

      if prime == 2:
            print("Prime Number")

      else:
            print("Not a Prime Number")

      return prime

n=int(input("Enter Number :"))
prime_number(n)
