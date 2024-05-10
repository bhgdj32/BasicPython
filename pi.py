s = "How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard."
m = s.replace(",","")
n = m.replace(".","")
a = n.split()
p = list(map(len,a))
k = ''.join(map(str,p))
print(k)
