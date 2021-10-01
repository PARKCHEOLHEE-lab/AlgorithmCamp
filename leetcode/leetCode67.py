class Solution:
    def addBinary(self, a: str, b: str) -> str:       
        def decimal_to_binary(target_num):
            if target_num == 0:
                return 0
            
            binary_list = []
            while target_num > 0:
                binary_list.insert(0, str(target_num%2))
                target_num = target_num//2
            return int(''.join(binary_list)) 
                
        def binary_to_decimal(target_num):
            decimal_num = 0
            power = 1
            while target_num > 0:
                decimal_num = decimal_num + (target_num % 10) * power
                target_num = target_num // 10
                power = power * 2
            return decimal_num
            
        add_decimal_num = binary_to_decimal(int(a)) + binary_to_decimal(int(b))
        return str(decimal_to_binary(add_decimal_num))