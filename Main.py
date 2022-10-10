from typing import List

def selectionSort(array, size) -> List[int]:
  for select in range(size):
    check = select
    for sort in range(select,size):
      if(array[sort]<array[select]):
        array[sort],array[select] = array[select],array[sort]
  return array

# Do not change the following code//
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
