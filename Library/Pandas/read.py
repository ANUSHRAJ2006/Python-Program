import pandas
x=pandas.read_csv(r'C:\Users\2006a\Downloads\archive\the_oscar_award.csv')
print(x)
x.loc[0,'year_film']=1928
print(x)
