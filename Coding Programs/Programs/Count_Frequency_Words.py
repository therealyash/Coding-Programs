# Count Frequency of words

a = "Jela is a good dog"
b = "Pablo pees everywhere he goes!"
c = """It was 7 minutes after midnight. The dog was lying on the grass 
in the middle of the lawn in front of Mrs Shears’ house. Its eyes 
were closed. It looked as if it was running on its side, the way dogs 
run when they think they are chasing a cat in a dream. But the dog was 
not running or asleep. The dog was dead. There was a garden fork 
sticking out of the dog. The points of the fork must have gone all the 
way through the dog and into the ground because the fork had not fallen 
over. I decided that the dog was probably killed with the fork because I 
could not see any other wounds in the dog and I do not think you would 
stick a garden fork into a dog after it had died for some other reason, 
like cancer for example, or a road accident. But I could not be certain 
about this.

I went through Mrs Shears’ gate, closing it behind me. I walked onto her 
lawn and knelt beside the dog. I put my hand on the muzzle of the dog. 
It was still warm.

The dog was called Wellington. It belonged to Mrs Shears who was our friend. 
She lived on the opposite side of the road, two houses to the left.

Wellington was a poodle. Not one of the small poodles that have hairstyles 
but a big poodle. It had curly black fur, but when you got close you could 
see that the skin underneath the fur was a very pale yellow, like chicken.

I stroked Wellington and wondered who had killed him, and why."""


# print(c)


unintersting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

unintersting_words = " ".join(unintersting_words)
def remove_punctuation(s):
    punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    new_s = ""
    for char in c:
    	for r_word in unintersting_words:
    		if char not in punctuation and r_word not in c: 
    			new_s = new_s + char
    	
    return new_s

word_list = remove_punctuation(c).split()


def count_frequency(lst):
	# defining an empty dict
	word_cloud = {}
	for word in word_list:
		if word in word_cloud:
			word_cloud[word] += 1
		else:
			word_cloud[word] = 1

	return word_cloud


cloud = count_frequency(word_list)
#print(cloud)
print('Frequency in Tabular Form')
for word,freq in cloud.items():
	print(f'{word:15} : {freq:15d}')






