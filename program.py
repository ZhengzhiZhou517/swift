class application:
    #create the Fabonacci
    def F(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        elif n>2:
            return self.F(n-1)+self.F(n-2)
    # check which condition is for the Fabonacci
    def check(self, n):
        x = self.F(n)
        #divisible by 15
        if x%15 == 0:
            print "FizzBuzz"
        #divisible by 3
        elif x%3 == 0:
            print "Buzz"
        ##divisible by 5
        elif x%5 == 0:
            print "Fizz"
        #prime
        elif self.primeCheck(n):
            print "BuzzFizz"
        else:
            print x
    #check if the Fabonacci is prime or not
    def primeCheck(self, n):
        x = self.F(n)
        result = True
        for i in range(2, x):
            if x%i == 0:
                result = False
        return result
x = application()
x.check(17)