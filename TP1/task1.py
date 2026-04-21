number_list={
  "0": "zero","1": "one","2": "two","3": "three","4": "four","5": "five","6": "six","7": "seven","8": "eight","9": "nine","10": "ten"
}
docs={
  "doc1": "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza.","doc2": "Five pizza were ready, but 3 bourak burned!","doc3": "We only had 8 chamiyya, no pizza, and one tea.","doc4": "Is 6 too much? I ate nine bourak lol."
}


def normalizing(txts):
    txt = txts.lower()
    p= "!?;,;/."
    for i in p:
        txt = txt.replace(i," ")
    tokans = txt.split()
    result = []
    for mot in tokans:
        if mot in number_list:
            result.append(number_list[mot])
        else:
            result.append(mot)
    return " ".join(result)

def run():
   print("after normalization:")
   for i, new_doc in docs.items():
      print("\t", i, ":", normalizing(new_doc))

run()