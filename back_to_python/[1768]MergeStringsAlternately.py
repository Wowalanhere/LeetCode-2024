s1 = "abcdefg"
s2 = "abcdefghi"
result = []

p1 = 0
p2 = 0

while p1 < len(s1) and p2 < len(s2):
    result.append(s1[p1])
    result.append(s2[p2])
    p1+=1
    p2+=1

# trick here 
# 2 pointers and final concate the rest of those list
result.append(s1[p1:])
result.append(s2[p2:])

result_string = "".join(result)

print(result_string)