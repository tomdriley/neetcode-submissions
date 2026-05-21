def digitsSquared(n: int) -> int:
    # Number guarenteed less than or equal to 1000
    thousands = n // 1000
    hundreds = (n % 1000) // 100
    tens = (n % 100) // 10
    ones = n % 10

    return (thousands * thousands) + (hundreds * hundreds) + (tens * tens) + (ones * ones)

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        x = n

        while(True):
            seen.add(x)
            
            x = digitsSquared(x)

            if (x == 1):
                return True
            
            if (x in seen):
                return False

        

