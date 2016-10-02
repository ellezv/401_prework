pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    pyglat = word[1:]+first+pyg
    print pyglat
else:
    print 'empty'
