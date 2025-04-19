dict_vo = {
  "i" : 20,
  " ": 34,
  "h":40
}
dict_list = []
for items in dict_vo:
  char_dict = {}
  char_dict["character"] = items
  char_dict["count"] = dict_vo[items]
  dict_list.append(char_dict)

def count(e):
  return e["count"]
dict_list.sort(reverse=True, key=count) 
print(dict_list)

count = 0
for items in dict_list:
  if dict_list[count]["character"].isalpha():
    print(f"{dict_list[count]['character']}: {dict_list[count]['count']}")
  count +=1