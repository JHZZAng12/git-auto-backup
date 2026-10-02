from urllib import request 

target = request.urlopen("https://www.hanbit.co.kr/images/common/loho_hanbit.png")
output = target.read()
print(output)

file = open("output.png","wb")
file.write(output)
file.close()
