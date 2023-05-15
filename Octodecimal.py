class Octodecimal:
    def __init__(self, num):
        self.num = num

    def convert_base(self, base):
        """
        Convert a number from base 18 to the specified base.
        """
        # Convert the input number to base 10
        base_10_num = int(self.num, 18)

        # Convert the base 10 number to the specified base
        if base == 2:
            return self.base_10_to_base_n(base_10_num, 2)
        elif base == 3:
            return self.base_10_to_base_n(base_10_num, 3)
        elif base == 4:
            return self.base_10_to_base_n(base_10_num, 4)
        elif base == 8:
            return self.base_10_to_base_n(base_10_num, 8)
        elif base == 10:
            return str(base_10_num)
        elif base == 12:
            if base_10_num == 0:
                return "0"
            base_12_digits = []
            while base_10_num > 0:
                digit = base_10_num % 12
                if digit < 10:
                    base_12_digits.append(str(digit))
                else:
                    base_12_digits.append(chr(ord('A') + digit - 10))
                base_10_num //= 12

            base_12_digits.reverse()
            base_12_num = ''.join(base_12_digits)
            return base_12_num

        elif base == 16:
            if base_10_num == 0:
                return "0"

            base_16_digits = []
            while base_10_num > 0:
                digit = base_10_num % 16
                if digit < 10:
                    base_16_digits.append(str(digit))
                else:
                    base_16_digits.append(chr(ord('A') + digit - 10))
                base_10_num //= 16

            base_16_digits.reverse()
            base_16_num = ''.join(base_16_digits)
            return base_16_num

        elif base == 18:
            return self.num        


        elif base == 20:
            if base_10_num == 0:
                return "0"

            base_20_digits = []
            while base_10_num > 0:
                digit = base_10_num % 20
                if digit < 10:
                    base_20_digits.append(str(digit))
                else:
                    base_20_digits.append(chr(ord('A') + digit - 10))
                base_10_num //= 20

            base_20_digits.reverse()
            base_20_num = ''.join(base_20_digits)
            return base_20_num

        else:
            return "Invalid base."

    def base_10_to_base_n(self, num, n):
        """
        Convert a base 10 number to the specified base (2 <= n <= 20).
        """
        if n < 2 or n > 20:
            return "Invalid base."

        digits = []
        while num > 0:
            digits.append(str(num % n))
            num //= n

        digits.reverse()
        return ''.join(digits)
    
