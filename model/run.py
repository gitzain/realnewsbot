from collections import defaultdict
import re

execfile("extract.py")
# execfile("remove_stopwords.py")
execfile("stem.py")
execfile("compare.py")
execfile("summarize.py")

# tag/categorize
# remove opionions
# calculate importance


STOPWORDS = ['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your']

def remove_stop_words(wordlist, stopwords=STOPWORDS):
    marked = ""
    for t in wordlist.split():
        if t.lower() not in stopwords:
            marked = marked + t + " "
    return marked



text1 = "Liverpool qualified for the knock-out stages of the Europa League after a 2-1 victory over Bordeaux at Anfield on Thursday night. Having fallen behind to Henri Saivet's well-placed strike from an indirect free-kick inside the area on 33 minutes, a James Milner penalty five minutes later and Christian Bentekes powerful strike put Liverpool ahead at the break.The Reds had chances to add to their lead early in the second half but were unable to take them."

text2 = "Liverpool reached the last 32 of the Europa League with one game to spare after coming from behind to beat Bordeaux and go top of Group B. Henri Saivet fired Bordeaux ahead from 16 yards after keeper Simon Mignolet conceded a needless free-kick for holding on to the ball for 20 seconds - the maximum time allowed is six. Liverpool levelled through James Milner's penalty after Christian Benteke was fouled by Ludovic Sane. Bentekes fine finish secured victory. The Belgium striker beat keeper Cedric Carrasso from 16 yards with a sublime shot on the turn after controlling Nathaniel Clyne's cross."

text3 = "Labour leader Jeremy Corbyn has written to his MPs saying he cannot back UK air strikes in Syria - prompting a warning of shadow cabinet resignations. Mr Corbyn rejected David Cameron's claim that targeting so-called Islamic State there would make Britain safer. His intervention - which puts him at odds with a number of his MPs - was criticised by a shadow cabinet member.The frontbencher said there would be resignations if Mr Corbyn ordered the shadow cabinet to back his stance.Labour is divided on whether to support Mr Cameron's call for air strikes, with about half of the shadow cabinet believed to back intervention."

text4 = "A convicted software pirate has been handed an unusual punishment. The man, named only as Jakub F, will be spared having to pay hefty damages - as long as a film denouncing piracy he was made to produce gets 200,000 views. He came to the out-of-court settlement with a host of firms whose software he pirated after being convicted by a Czech court. In return, they agreed not to sue him. The 30-year-old was also given a three-year suspended sentence. The criminal court decided that any financial penalty would have to be decided either in civil proceedings or out of court. The firms, which included Microsoft, HBO Europe, Sony Music and Twentieth Century Fox, estimated that the financial damage amounted to thousands of pounds, with Microsoft alone valuing its losses at 5.7m Czech Crowns (148,000)."

text5 = "An experimental drone fitted with sensors is being deployed to monitor gases rising from rubbish dumps. The unmanned aircraft is being flown above Britain's 200 landfill sites to study a major source of UK emissions. The latest estimate is that unwanted food produces 21 million tonnes of greenhouse gas in the UK every year. Although the number of landfill sites is being reduced, the emissions from decomposing matter are set to last for decades. The drone project is being run by the University of Manchester and the Environment Agency (EA). According to Doug Wilson, the EA's Director of Scientific & Evidence Services, the research is driven by the need to find an easy way to monitor a long-term problem. "

text6 = "Liverpool striker Daniel Sturridge has suffered a new injury setback after a foot problem in training ruled him out against Bordeaux in the Europa League. The 26-year-old was hoping to make a return on Thursday from a knee injury which has kept him out since 4 October. However, the England international has been sent for a scan after complaining of discomfort in a foot.'I don't know too much about the situation,' said Liverpool manager Jurgen Klopp. Speaking after Liverpool's 2-1 win over Bordeaux secured the Reds a place in the last 32, Klopp added: 'It wasn't a situation I saw because we trained in two groups - the starting line-up and the other players.'"

text7 = "Liverpool wrecked Manchester City's hopes of returning to the top of the Premier League and delivered more evidence of vast improvement under new manager Jurgen Klopp with an emphatic victory at The Etihad.Klopp's side tore City apart with a dazzling first-half performance, which saw them take a 3-0 lead through Eliaquim Mangala's early own goal and cool finishes from Philippe Coutinho and Roberto Firmino. Play media Jump media playerMedia player helpOut of media player. Press enter to return or tab to continue. Liverpool boss Klopp says win feels perfect Sergio Aguero gave City faint hope when he pulled a goal back on half time but City were undermined by shambolic defending as they failed to cope with the absence of injured captain Vincent Kompany. Liverpool, however, never looked like conceding their advantage and Martin Skrtel's thunderous late fourth confirmed their superiority as they added this fine away win to their recent victory at champions Chelsea."


text1and2 = "Liverpool qualified for the knock-out stages of the Europa League after a 2-1 victory over Bordeaux at Anfield on Thursday night. Having fallen behind to Henri Saivet's well-placed strike from an indirect free-kick inside the area on 33 minutes, a James Milner penalty five minutes later and Christian Bentekes powerful strike put Liverpool ahead at the break.The Reds had chances to add to their lead early in the second half but were unable to take them. Liverpool reached the last 32 of the Europa League with one game to spare after coming from behind to beat Bordeaux and go top of Group B. Henri Saivet fired Bordeaux ahead from 16 yards after keeper Simon Mignolet conceded a needless free-kick for holding on to the ball for 20 seconds - the maximum time allowed is six. Liverpool levelled through James Milner's penalty after Christian Benteke was fouled by Ludovic Sane. Bentekes fine finish secured victory.The Belgium striker beat keeper Cedric Carrasso from 16 yards with a sublime shot on the turn after controlling Nathaniel Clyne's cross."



def get_word_frequency_hash(text):
	word_frequency_hash = defaultdict(float)
	for text in text.split():
	    word_frequency_hash[text] += 1
	return word_frequency_hash

def get_word_average_hash(word_frequency_hash, word_in_doc):
	word_average_hash = word_frequency_hash
	for key,value in word_average_hash.iteritems():
		word_average_hash[key] = word_average_hash[key] / word_in_doc
	return word_frequency_hash




# print stem("testing")
# print extract("http://www.bbc.co.uk/news/uk-politics-34915218")
print "No stemming:"
print compare(text4, text2)
print ""
print "Stemming:"
stemmed_text1 = get_stemmed_string(text4)
stemmed_text2 = get_stemmed_string(text2)
print compare(stemmed_text1, stemmed_text2)

print ""
print ""
print "Stemming with stopwords removed:"
a = remove_stop_words(text1)
b = remove_stop_words(text7)

stemmed_texta = get_stemmed_string(a)
stemmed_textb = get_stemmed_string(b)

print compare(stemmed_texta, stemmed_textb)





print summarize("",text2)