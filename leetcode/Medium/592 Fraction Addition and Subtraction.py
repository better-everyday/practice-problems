"""
--- Description ---

Given a string expression representing an expression of fraction addition and subtraction, 
return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, 
change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.
"""

import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        def separate_fractions(expression, num, denom):
            number = ""
            for item in expression + "+":
                if item == '/':
                    num.append(number)
                    number = ""
                    continue
                elif item == '-' or item == '+':
                    denom.append(number)
                    number = ""
                number += item

        numerators = []
        denominators = []

        separate_fractions(expression, numerators, denominators)
        denominators = list(filter(None, denominators))

        denom_prod = 1
        for num in denominators:
            denom_prod *= int(num)

        new_numerators = []
        for i, num in enumerate(numerators):
            number = num
            if num[0] == '+':
                number = num[1:]
            factor = denom_prod / int(denominators[i])
            new_numerators.append(factor * int(number))

        reducible_numerator = sum(new_numerators)

        # Reduce numerator and denominator using gcd
        gcd = math.gcd(int(reducible_numerator), denom_prod)
        
        final_num = int(reducible_numerator / gcd)
        final_denom = int(denom_prod / gcd)

        return str(final_num) + "/" + str(final_denom)

"""
--- Submission ---

Runtime: 28 ms, 93.02%
Memory: 16.54 MB, 59.69%
"""