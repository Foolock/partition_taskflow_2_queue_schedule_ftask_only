def read_numbers_from_file(filename, lines):
    numbers = []
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number in lines:
                parts = line.split(':')
                if len(parts) == 2:
                    number = parts[1].strip().rstrip('%')
                    try:
                        number = float(number)
                        numbers.append(number)
                    except ValueError:
                        print(f"Invalid number found on line {line_number}: {number}")
    results = 0
    for i in range(len(numbers)):
        results += numbers[i]
    return results / len(numbers)

# Usage example
runtime = [15, 31, 47, 63, 79, 95, 111, 127, 143, 159]  # Specify the line numbers you want to read here

path = './vga_lcd/'

file_path2 = path + 'log_t2_p2.txt'
file_path3 = path + 'log_t3_p3.txt'
file_path4 = path + 'log_t4_p4.txt'
file_path5 = path + 'log_t5_p5.txt'
file_path6 = path + 'log_t6_p6.txt'
file_path7 = path + 'log_t7_p7.txt'
file_path8 = path + 'log_t8_p8.txt'
file_path9 = path + 'log_t9_p9.txt'
file_path10 = path + 'log_t10_p10.txt' 
file_path11 = path + 'log_t11_p11.txt'
file_path12 = path + 'log_t12_p12.txt'
file_path13 = path + 'log_t13_p13.txt'
file_path14 = path + 'log_t14_p14.txt'
file_path15 = path + 'log_t15_p15.txt'
file_path16 = path + 'log_t16_p16.txt'
file_path17 = path + 'log_t17_p17.txt'
file_path18 = path + 'log_t18_p18.txt'
file_path19 = path + 'log_t19_p19.txt'
file_path20 = path + 'log_t20_p20.txt'

results2 = read_numbers_from_file(file_path2, runtime)
results3 = read_numbers_from_file(file_path3, runtime)
results4 = read_numbers_from_file(file_path4, runtime)
results5 = read_numbers_from_file(file_path5, runtime)
results6 = read_numbers_from_file(file_path6, runtime)
results7 = read_numbers_from_file(file_path7, runtime)
results8 = read_numbers_from_file(file_path8, runtime)
results9 = read_numbers_from_file(file_path9, runtime)
results10 = read_numbers_from_file(file_path10, runtime)
results11 = read_numbers_from_file(file_path11, runtime)
results12 = read_numbers_from_file(file_path12, runtime)
results13 = read_numbers_from_file(file_path13, runtime)
results14 = read_numbers_from_file(file_path14, runtime)
results15 = read_numbers_from_file(file_path15, runtime)
results16 = read_numbers_from_file(file_path16, runtime)
results17 = read_numbers_from_file(file_path17, runtime)
results18 = read_numbers_from_file(file_path18, runtime)
results19 = read_numbers_from_file(file_path19, runtime)
results20 = read_numbers_from_file(file_path20, runtime)

print("k2 = [", end = "")
print(results2, end = ",")
print(results3, end = ",")
print(results4, end = ",")
print(results5, end = ",")
print(results6, end = ",")
print(results7, end = ",")
print(results8, end = ",")
print(results9, end = ",")
print(results10, end = ",")
print(results11, end = ",")
print(results12, end = ",")
print(results13, end = ",")
print(results14, end = ",")
print(results15, end = ",")
print(results16, end = ",")
print(results17, end = ",")
print(results18, end = ",")
print(results19, end = ",")
print(results20, end = "")
print("]\n")
















