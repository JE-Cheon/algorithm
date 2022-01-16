cr_word = input()
cr_alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in cr_alpha:
    cr_word = cr_word.replace(i,"*")

print(len(cr_word))