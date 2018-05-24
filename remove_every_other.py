def remover_every_other(l):
    for i in range(len(l)):
       print(i) 
       if i % 2 == 0:
           l.remove(i)
    return l

print(remover_every_other([1,2,3,4,5]))