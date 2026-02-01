ans=['1','2','2','3']
print(''.join(ans))
#outpout 1223


numbers=[1,2,3,4]
a_even=[val for val in numbers if val%2==0]
print(a_even)
#output [2,4]


a_even=[print(val) for val in numbers if val%2==0]
print(a_even)
#output
#2
#4
#[None, None]

a=10
b=1 if a%2==0 else 2





