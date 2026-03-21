def my_sum(*args):
  total=0
  for num in args:
    total+=num
  return total

print(my_sum(1, 2, 3))        
print(my_sum(10))            
print(my_sum())              
print(my_sum(5, -5, 10,20))