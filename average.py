def calc_average(numbers):
    total = 0.0
    count = 0
    for n in numbers:
        total += n
        count += 1
    return total / count

numbers = [2.5, -1.4, -7.2, -11.7, -13.5, -13.5, -14.9, -15.2, -14.0, -9.7, -2.6, 2.1]
average = calc_average(numbers)
print(average)
if (average >= 10):
		print("Multiple digits")
else:
		print("Single digit")

if(average < 0):
		print("Average value negative")

name = "Yoojin Ahn "
student_id = "104853318"
print(name + student_id)

id_last_digit = int(student_id[-1])
avg_last_digit = int(str(average)[-1])

if(avg_last_digit > id_last_digit):
    print("Larger than my last digit")
elif(avg_last_digit == id_last_digit):
    print("Equal to my last digit")
else:
    print("Smaller than my last digit")


