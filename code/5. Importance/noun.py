import nltk

qry = "who is Mahatma Gandhi"
tokens = nltk.tokenize.word_tokenize(qry)
pos = nltk.pos_tag(tokens)
sentt = nltk.ne_chunk(pos, binary = False)
print sentt
person = []
for subtree in sentt.subtrees(filter=lambda t: t.node == 'PERSON'):
    for leave in subtree.leaves():
        person.append(leave)
print "person=", person