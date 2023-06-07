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
lines_to_read = [15, 32, 49, 66, 83, 100, 117, 134, 151, 169]  # Specify the line numbers you want to read here

exp_path = ['./des_perf/', './vga_lcd/']
strname = ['des_perf_2queue_pftask_only', 'vga_lcd_2queue_pftask_only']
index = 0
for path in exp_path:
    file_path2 = path + '2_queue_pftask_only_log_t2_p2.txt'
    file_path3 = path + '2_queue_pftask_only_log_t3_p3.txt'
    file_path4 = path + '2_queue_pftask_only_log_t4_p4.txt'
    file_path5 = path + '2_queue_pftask_only_log_t5_p5.txt'
    file_path6 = path + '2_queue_pftask_only_log_t6_p6.txt'
    file_path7 = path + '2_queue_pftask_only_log_t7_p7.txt'
    file_path8 = path + '2_queue_pftask_only_log_t8_p8.txt'
    file_path9 = path + '2_queue_pftask_only_log_t9_p9.txt'
    file_path10 = path + '2_queue_pftask_only_log_t10_p10.txt'
    file_path11 = path + '2_queue_pftask_only_log_t11_p11.txt'
    file_path12 = path + '2_queue_pftask_only_log_t12_p12.txt'
    file_path13 = path + '2_queue_pftask_only_log_t13_p13.txt'
    file_path14 = path + '2_queue_pftask_only_log_t14_p14.txt'
    file_path15 = path + '2_queue_pftask_only_log_t15_p15.txt'
    file_path16 = path + '2_queue_pftask_only_log_t16_p16.txt'
    file_path17 = path + '2_queue_pftask_only_log_t17_p17.txt'
    file_path18 = path + '2_queue_pftask_only_log_t18_p18.txt'
    file_path19 = path + '2_queue_pftask_only_log_t19_p19.txt'
    file_path20 = path + '2_queue_pftask_only_log_t20_p20.txt'

    results2 = read_numbers_from_file(file_path2, lines_to_read)
    results3 = read_numbers_from_file(file_path3, lines_to_read)
    results4 = read_numbers_from_file(file_path4, lines_to_read)
    results5 = read_numbers_from_file(file_path5, lines_to_read)
    results6 = read_numbers_from_file(file_path6, lines_to_read)
    results7 = read_numbers_from_file(file_path7, lines_to_read)
    results8 = read_numbers_from_file(file_path8, lines_to_read)
    results9 = read_numbers_from_file(file_path9, lines_to_read)
    results10 = read_numbers_from_file(file_path10, lines_to_read)
    results11 = read_numbers_from_file(file_path11, lines_to_read)
    results12 = read_numbers_from_file(file_path12, lines_to_read)
    results13 = read_numbers_from_file(file_path13, lines_to_read)
    results14 = read_numbers_from_file(file_path14, lines_to_read)
    results15 = read_numbers_from_file(file_path15, lines_to_read)
    results16 = read_numbers_from_file(file_path16, lines_to_read)
    results17 = read_numbers_from_file(file_path17, lines_to_read)
    results18 = read_numbers_from_file(file_path18, lines_to_read)
    results19 = read_numbers_from_file(file_path19, lines_to_read)
    results20 = read_numbers_from_file(file_path20, lines_to_read)

    print("y_"+strname[index], end = " = [",)
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
    index += 1;
