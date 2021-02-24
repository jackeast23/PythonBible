words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the' , 'lazy', 'dog']
answer = [[w.upper(), w.lower(), len(w)] for w in words]

print(answer)