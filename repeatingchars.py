def count_repeating_digits(num):
	count = 0
	str_num = str(num) 

	for i in range(len(str_num)):
		for j in range(i+1, len(str_num)):
			if str_num[i] == str_num[j]:
				count += 1
				break 
	return count


num = 99677

repeating_digits = count_repeating_digits(num)
print("Number of repeating digits:", repeating_digits)
