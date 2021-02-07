thickness = int(input())
c = 'H'

for i in range(thickness):
    print((c*i).______(thickness-1)+c+(c*i).______(thickness-1))


for i in range(thickness+1):
    print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))


for i in range((thickness+1)//2):
    print((c*thickness*5).______(thickness*6))    


for i in range(thickness+1):
    print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))    


for i in range(thickness):
    print(((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6))