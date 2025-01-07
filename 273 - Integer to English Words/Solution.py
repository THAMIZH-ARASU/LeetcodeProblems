class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        units = {
            1: "One", 2: "Two", 3: "Three",
            4: "Four", 5: "Five", 6: "Six",
            7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve",
            13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
            16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
            19: "Nineteen"
        }

        tens = {
            2: "Twenty", 3: "Thirty", 4: "Forty",
            5: "Fifty", 6: "Sixty", 7: "Seventy",
            8: "Eighty", 9: "Ninety"
        }

        def get_hundred(num):
            result = []
            if num >= 100:
                n = num //100
                result.append(units[n] + " Hundred")
                num = num % 100
            if num >= 20:
                n = num // 10
                result.append(tens[n])
                num = num % 10
            if num > 0:
                result.append(units[num])
            return " ".join(result)
        
        result =  []
        if num > 10**9:
            n = num // 10**9
            result.append(get_hundred(n) + " Billion")
            num = num % 10**9
        if num > 10**6:
            n = num // 10**6
            result.append(get_hundred(n) + " Million")
            num = num % 10**6
        if num > 10**3:
            n = num // 10**3
            result.append(get_hundred(n) + " Thousand")
            num = num % 10**3
        result.append(get_hundred(num))
        return " ".join(result).strip()
    
t = Solution()
print(t.numberToWords(1234567891))
print(t.numberToWords(123456789))
print(t.numberToWords(12345678)) 
print(t.numberToWords(1234567)) 