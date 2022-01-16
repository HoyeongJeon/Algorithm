from collections import deque

total = int(input())
que = deque([])
for i in range(total):
  que.insert(i, i + 1)
  print(que)

print("==============")
print(que)
while total != 1:
  que.popleft()
  print("front 팝 => ",que)
  que.append(que[0])
  print("front 아래로 옮기기 =>",que)
  que.popleft()
  print("front값 제거=>",que)
  total = total - 1


print(que[0])