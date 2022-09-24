class TrieNode:	
	def __init__(self):
		self.children = dict()
		self.isEndOfWord = False
		self.num = dict()

# root = None

def getNewTrieNode():
	
	pNode = TrieNode()
	return pNode

def insertWord(root,word):	
    # global root
    current = root
    s = ''
    for i in range(len(word)):
        s = word[i]
        if (s not in current.children):
            p = getNewTrieNode()
            current.children[s] = p
            current.num[s] = 1
        else:
            current.num[s] = current.num[s] + 1
        current = current.children[s]

    current.isEndOfWord = True

def countWords(root, prefix):			
	current = root
	s = ''
	wordCount = 0
	print(current,"check2")
	for i in range(len(prefix)):
		s = prefix[i]
		if (s not in current.children):
			wordCount = 0
			break
		wordCount += (current.num)[s]
		current = (current.children)[s]

	return wordCount

def sumPrefixScores(words):
    # global root
    root = None
    root = getNewTrieNode()
    print(root,"check")
    for word in words:
        insertWord(root,word)
    ans = []
    for word in words:
        ans.append(countWords(root, word))
        
    return ans


words = [ "abc","ab","bc","b"]
print(sumPrefixScores(words))