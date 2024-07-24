# 1st program
print(9 ** 0.5 * 5)


# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)


# 3rd program
num1 = 1234
num2 = 5678

middle_num1 = (num1 // 10) % 100
middle_num2 = (num2 // 10) % 100

result = middle_num1 + middle_num2

print(result)


# 4th program
float_num1 = 13.42
float_num2 = 42.13

int_num1 = int(float_num1)
int_num2 = int(float_num2)

fraction_part1 = round((float_num1 - int_num1) * 100)
fraction_part2 = round((float_num2 - int_num2) * 100)
print(int_num1 == fraction_part2 or int_num2 == fraction_part1)


