import random
import pandas as pd

lst_orig = []
column_names = ["Input_Word","Len","Mapped"]
i_df = pd.DataFrame(columns = column_names)

n = int(input("num of elements:"))

for i in range(0,n):
    words_str=input()
    i_df['Input_Word'] = words_str
    lst_orig.append(words_str)


#data frame
#Input Word --- Length -- mapped in cross word
print(i_df)