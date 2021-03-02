from textblob import TextBlob 
import json
import os

class person():
    def __init__(self, name):
        self.name = name
        self.words = []
        self.messages = 0
        self.message_blocks = 0
        self.likes_given = 0
        self.sentiment = 0
        self.photos = 0
        self.likes_given = 0
        self.likes = 0
        self.video_calls = 0
    def __str__(self):
        return self.name + ": Words: " + str(self.get_count()) + " Messages: " + str(self.messages)

    def add_word(self, word):
        self.words.append(word)

    def add_message(self):
        self.messages += 1

    def add_message_block(self):
        self.message_blocks +=1
        
    def add_photo(self):
        self.photos += 1

    def add_like(self):
        self.likes += 1

    def add_like_given(self):
        self.likes_given += 1

    def add_video_call(self):
        self.video_calls += 1
        
    def get_name(self):
        return self.name
    
    def get_count(self):
        return len(self.words)
              
    def get_messages(self):
        return self.messages

    def get_message_blocks(self):
        return self.message_blocks

    def get_likes(self):
        return self.likes

    def get_likes_given(self):
        return self.likes_given
    
    def get_photos(self):
        return self.photos
    
    def get_word_len(self):
        total = 0
        for word in self.words:
            total += len(word)
        return total/(len(self.words)+1)

    def get_message_len(self):
        return len(self.words)/(self.messages + 1)

    def get_message_blocks_len(self):
        return len(self.words)/( self.message_blocks + 1)

    def get_video_calls(self):
        return self.video_calls

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
        try:
            return lis[0][1]
        except:
            return ""

    def get_word_sentiment(self):

        if self.sentiment:
            return self.sentiment
        else:
            su = 0
            total = 0
            for word in self.words:
                temp = TextBlob(word).sentiment.polarity
                if temp:
                    su += temp
                    total += 1
            try:
                self.sentiment = su/total
            except:
                pass
            return self.sentiment




    




lis = []
indicies = []
dic = {}



for user in ["Joey Rubas"]:
    print(user)
    lis.append(person(user))
    indicies.append(user)
    


new = 0
current = lis[0].get_name()
total = 0

directory_contents = os.listdir(".")

for item in ["folder name"]: #replace with directory_contents to do all folders
     if os.path.isdir(item):
        dataIn = json.load(open(item+"/message_1.json", "r"))
        for message in dataIn["messages"]:
            if message["sender_name"] != current:
                lis[indicies.index(current)].add_message_block()
                if not(message["sender_name"] in indicies):
                    #print("here", message["sender"])
                    lis.append(person(message["sender_name"]))
                    indicies.append( message["sender_name"])
                current = message["sender_name"]
            lis[indicies.index(current)].add_message()
            try:
                if "liked" in message["content"] or "Liked" in message["content"] or "Video call ended" in message["content"]:
                        message["content"] = ""
                if "Video call started" in message["content"]:
                        lis[indicies.index(current)].add_video_call()
                        message["content"] = ""
                for word in message["content"].strip().split():
                    fixed = word.replace("?", "").replace(".", "").replace("!", "")
                    lis[indicies.index(current)].add_word(fixed)
                    total += 1
                    if word in dic:
                        dic[fixed] += 1
                    else:
                        dic[fixed] = 1
            except Exception as e:
                lis[indicies.index(current)].add_photo()
            try:
                for like in message["reactions"]:
                    lis[indicies.index(current)].add_like()
                    lis[indicies.index(like["actor"])].add_like_given()
            except Exception as e:
                pass
                  
        



print("\n\nSummary")

words = 0
messages = 0
mbs = 0
photos = 0
likes = 0
for person in lis:
    words+= person.get_count()
    messages += person.get_messages()
    mbs += person.get_message_blocks()
    photos += person.get_photos()
    likes += person.get_likes()
print("Total Words:", words)
print("Total messages:", messages)               
print("Total Message Bloacks:", mbs)
print("Total Photos:", photos)
print("Total Likes:", likes)

print("\n\nWords Leaderboard")
lis.sort(key = lambda x: x.get_count(), reverse=True)
for num in range(len(lis)):
    print(num +1, ".", lis[num].get_name(), ":",  lis[num].get_count())

print("\n\nMessages Leaderboard")
lis.sort(key = lambda x: x.get_messages(), reverse=True)
for num in range(len(lis)):
    print(num +1, ".", lis[num].get_name(), ":",  lis[num].get_messages())
               
print("\n\nMessage Blocks Leaderboard")
lis.sort(key = lambda x: x.get_message_blocks(), reverse=True)
for num in range(len(lis)):
    print(num +1, ".", lis[num].get_name(), ":",  lis[num].get_message_blocks())

print("\n\nPhotos Leaderboard")
lis.sort(key = lambda x: x.get_photos(), reverse=True)
for num in range(len(lis)):
    print(num +1, ".", lis[num].get_name(), ":",  lis[num].get_photos())

print("\n\nLikes Leaderboard")
lis.sort(key = lambda x: x.get_likes(), reverse=True)
for num in range(len(lis)):
    print(num + 1, ".", lis[num].get_name(), ":",  lis[num].get_likes())

print("\n\nLikes Given Leaderboard")
lis.sort(key = lambda x: x.get_likes_given(), reverse=True)
for num in range(len(lis)):
    print(num +1, ".", lis[num].get_name(), ":",  lis[num].get_likes_given())

print("\n\nVideo Calls Leaderboard")
lis.sort(key = lambda x: x.get_video_calls(), reverse=True)
for num in range(len(lis)):
    print(num +1, ".", lis[num].get_name(), ":",  lis[num].get_video_calls())

print("\n\nNiceness Leaderboard")
lis.sort(key = lambda x: x.get_word_sentiment(), reverse=True)
for num in range(len(lis)):
    print(num + 1, ".", lis[num].get_name(), ":",  lis[num].get_word_sentiment())

print("\n\nMeanness Leaderboard")
lis.sort(key = lambda x: x.get_word_sentiment())
for num in range(len(lis)):
    print(num + 1, ".", lis[num].get_name(), ":",  lis[num].get_word_sentiment())

print("\n\nWord Length Leaderboard")
lis.sort(key = lambda x: x.get_word_len(), reverse=True)
for num in range(len(lis)):
    print(num + 1, ".", lis[num].get_name(), ":",  lis[num].get_word_len())

print("\n\nMessage Length Leaderboard")
lis.sort(key = lambda x: x.get_message_len(), reverse=True)
for num in range(len(lis)):
    print(num + 1, ".", lis[num].get_name(), ":",  lis[num].get_message_len())
               
print("\n\nMessage Block Length Leaderboard")
lis.sort(key = lambda x: x.get_message_blocks_len(), reverse=True)
for num in range(len(lis)):
    print(num + 1, ".", lis[num].get_name(), ":",  lis[num].get_message_blocks_len())

print("\n\nMost Common Word by Person")
for num in range(len(lis)):
    try:
        print(lis[num].get_name(), ":",  lis[num].get_most_common())
    except:
        pass

print("\n\nMost common words")

list1 = []
for word in dic:
    list1.append((dic[word], word))
list1.sort()
list1.reverse()
for word in list1[:35]:
    print(word[1], ":", word[0], " times")


