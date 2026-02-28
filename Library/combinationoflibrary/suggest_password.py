import string
import random as r
x=' '.join(r.choices(string.ascii_uppercase+string.ascii_lowercase+string.punctuation+string.digits,k=12))
print(x)
