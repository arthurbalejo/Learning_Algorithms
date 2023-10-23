#fatorial

def fat(x):
    if x == 1:
        return 1
    else:
        x = x * fat(x-1)
        return x
    
fatorial = 5
print (fat(fatorial))