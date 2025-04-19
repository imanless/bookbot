def num_words(text):
  text_list = text.split()
  count = len(text_list)
  return count

def num_chars(text):
  text_lowered = text.lower()
  char_dict = {}
  for items in text_lowered:
    char_dict[items] = 0
  for items in text_lowered:
    char_dict[items] += 1
  return char_dict


def sorted_count_list(charactersdict):
  sorted_list = []
  for items in charactersdict:
    char_dict = {}
    char_dict["character"] = items
    char_dict["count"] = charactersdict[items]
    sorted_list.append(char_dict)

  def count(e):
    return e["count"]
  sorted_list.sort(reverse=True, key=count) 
  return sorted_list