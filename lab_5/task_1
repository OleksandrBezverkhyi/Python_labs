def arithmetic_mean_of_negative_elements(arr):
  sum_negative = 0
  count_negative = 0
  
  for i in range(len(arr)):
      if arr[i] < 0:
          sum_negative += arr[i]
          count_negative += 1
        
  if count_negative == 0:
      return 0 
    
  result = sum_negative / count_negative
  return result

n = int(input("Введіть розмір масиву: "))

while n <= 0:
  print("Розмір має бути більше 0")
  n = int(input("Введіть розмір масиву: "))

print("Введіть елементи масиву: ")
arr = [float(input("")) for i in range(n)]

result = arithmetic_mean_of_negative_elements(arr)
print(f"Середнє арифметичне від'ємних елементів становить: {result:.2f}")
