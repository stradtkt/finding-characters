def createNewList(lists, char):
  newList = []
  for i in lists:
    if i.find(char) == -1:
      continue
    else:
      newList.append(i)
  print(newList)
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
createNewList(word_list, char)

#newList = ['hello', 'world']