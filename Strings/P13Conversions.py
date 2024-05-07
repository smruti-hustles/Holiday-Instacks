binary_string = '1010'
decimal_number = int(binary_string, 2)

decimal_number = 10
binary_string = bin(decimal_number)[2:]  # [2:] to remove the '0b' prefix

decimal_number = 10
octal_string = oct(decimal_number)[2:]  # [2:] to remove the '0o' prefix

octal_string = '12'
decimal_number = int(octal_string, 8)

hexadecimal_string = '1A'
decimal_number = int(hexadecimal_string, 16)

decimal_number = 26
hexadecimal_string = hex(decimal_number)[2:]  # [2:] to remove the '0x' prefix
