import string
charl=lambda:string.ascii_lowercase
charu=lambda:string.ascii_uppercase
lower=lambda c:charl()[(charl().index(c)+13)%26]
upper=lambda c:charu()[(charu().index(c)+13)%26]
apply=lambda c:[lower,upper][c.is_upper()](c)
rot13=lambda s:[apply(c)for c in s]
print(rot13('WnvzrEbbgZR'))
