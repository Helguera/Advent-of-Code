
input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open("2025/Day2/input.txt", "r") as f:
    input = f.read()


input_list = input.split(",")

result = 0
for item in input_list:
    for i in range(int(item.split("-")[0]), int(item.split("-")[1])+1):
        if len(str(i)) % 2 == 0:
            digits = int(len(str(i))/2)
            if str(i)[digits:] == str(i)[:digits]:
                result += int(i)

print(result)