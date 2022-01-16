sum_array = []
num_list = []
num = 0
for number in range(1, 1000001):
    num_list = list(map(int, str(number)))
    for i in num_list:
        num = num + i
    sum_array.append(number + num)
    num = 0

# sum_array = 생성자
find_num = int(input())


if(sum_array.__contains__(find_num)):
    for i in range(1,1000001):
        tmp = sum_array[i];
        if(find_num == tmp):
            print(i + 1)
            break
        else:
            continue
else:
    print(0)