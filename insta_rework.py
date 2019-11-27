class person():
    def __init__(self, name):
        self.name = name
        self.words = []
        self.likes = 0
        self.messages = 0
    def __str__(self):
        return self.name + ": Words: " + str(self.get_count()) + " Messages: " + str(self.messages) + " Likes: " + str(self.likes)

    def add_word(self, word):
        self.words.append(word)
        
    def add_like(self):
        self.likes +=1
        
    def add_message(self):
        self.messages +=1
        
    def get_name(self):
        return self.name
    
    def get_count(self):
        return len(self.words)

    def get_likes(self):
        return self.likes
              
    def get_messages(self):
        return self.messages

    def get_word_len(self):
        total = 0
        for word in self.words:
            total += len(word)
        return total/len(self.words)

    def get_message_len(self):
        return len(self.words)/self.messages

    def get_most_common(self):
        dic = {}
        for word in self.words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        lis = []
        for word in dic:
            lis.append((dic[word], word))
        lis.sort(reverse=True)
        return lis[0][1]

tags = ["sammysharp1", "emilie_casey", "Paurecio", "Alyssa.agnos", "Haaris.khannn", "Itscameronrozek", "A.y.z_123", "Abby.fishh", "Kkatiedalton", "Comer_chris2", "Kzcheng1", "Nick.innis8",
          "Elizabethshamoun", "Johnyboii101", "Realhenryh", "Harvey_wang_", "Ev_k03", "Jack_vest_", "Connor_mchugh12",  "K_bagchi", "Uju.kim", "Evan._.liu", "joey_rubas", "Williamtongit",
          "Orrsoarsororesormore", "Cooperholmberg", "paige_lafferty", "Eileensmithh", "Morgan.sokol", "Paige_kolbe", "Abby.christman", "arja_500", "kassidyxy", "zoe.k918", "daniel.wu042",
        "ryanmadson01", "maxicat713", "alnass.ramy", "prem_chandraracecar"]
for num in range(len(tags)):
    tags[num] = tags[num].lower()

people = {}
dic = {}
for tag in tags:
    people[tag] = person(tag)
    
file = open("doc.txt", "r")
prev = 0
last = "joey_rubas"
current = "joey_rubas"
total = 0
for line in file:
    for word in line.strip().split():
        word = word.lower()
        if word in people:
            current = word
            if prev and word != last:
                people[last].add_like()
                
            elif word != last: 
                people[word].add_message()
                last = word
                prev = 1
        else:
            total +=1
            prev = 0
            people[current].add_word(word)
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
lis = []
for person in people:
    lis.append(people[person])

print("\n\nSummary")
lis.sort(key = lambda x: x.get_count(), reverse=True)
for person in lis:
    print(person)


print("\n\nWords Leaderboard")
lis.sort(key = lambda x: x.get_count(), reverse=True)
for num in range(len(lis)):
    print(num, ".", lis[num].get_name(), ":",  lis[num].get_count())

print("\n\nMessages Leaderboard")
lis.sort(key = lambda x: x.get_messages(), reverse=True)
for num in range(len(lis)):
    print(num, ".", lis[num].get_name(), ":",  lis[num].get_messages())

print("\n\nLikes Leaderboard")
lis.sort(key = lambda x: x.get_likes(), reverse=True)
for num in range(len(lis)):
    print(num, ".", lis[num].get_name(), ":",  lis[num].get_likes())

print("\n\nWord Length Leaderboard")
lis.sort(key = lambda x: x.get_word_len(), reverse=True)
for num in range(len(lis)):
    print(num, ".", lis[num].get_name(), ":",  lis[num].get_word_len())

print("\n\nMessage Length Leaderboard")
lis.sort(key = lambda x: x.get_message_len(), reverse=True)
for num in range(len(lis)):
    print(num, ".", lis[num].get_name(), ":",  lis[num].get_message_len())
        
print("\n\nMost Common Word by Person")
for num in range(len(lis)):
    print(lis[num].get_name(), ":",  lis[num].get_most_common())

print("\n\nMost common words")

list1 = []
for word in dic:
    list1.append((dic[word], word))
list1.sort()
list1.reverse()
for word in list1[:35]:
    print(word[1], ":", word[0], " times")

    
