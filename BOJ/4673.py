number_list = list(range(1,10000));
none_selfnumber_list = []

for i in number_list:
  none_selfnumber = sum(map(int, str(i))) + i
  if(none_selfnumber < 10000):     
    none_selfnumber_list.append(none_selfnumber);

selfnumber = list(set(number_list) - set(none_selfnumber_list));
selfnumber.sort();
for i in selfnumber:
  print(i)
