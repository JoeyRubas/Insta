import statistics
people = ["sammysharp1", "emilie_casey", "Paurecio", "Alyssa.agnos", "Haaris.khannn", "Itscameronrozek", "A.y.z_123", "Abby.fishh", "Kkatiedalton", "Comer_chris2", "Kzcheng1", "Nick.innis8",
          "Elizabethshamoun", "Johnyboii101", "Realhenryh", "Harvey_wang_", "Ev_k03", "Jack_vest_", "Connor_mchugh12",  "K_bagchi", "Uju.kim", "Evan._.liu", "joey_rubas", "Williamtongit",
          "Orrsoarsororesormore", "Cooperholmberg", "paige_lafferty", "Eileensmithh", "Morgan.sokol", "Paige_kolbe", "Abby.christman", "arja_500", "kassidyxy", "zoe.k918", "daniel.wu042", "ryanmadson01", "maxicat713", "alnass.ramy", "prem_chandraracecar"]

import itertools
import operator

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]


words = {}
dict1 = {}
for num in range(len(people)):
    people[num] = people[num].lower()
    words[people[num]] = [0, 0, 0, "", [0], []]
person = people[0]
file = open("doc.txt", "r")
prev = 0
total = 0
recent_names = ["joey_rubas", "joey_rubas"]
for line in file:
    for word in line.strip().split():
        if word.lower() in people:
            person = word.lower()
            if word == recent_names[-1]:
                pass
            elif prev:
                words[recent_names[-1]][1] += 1
                words[person][4].append(0)
            else:
                words[word][2] +=1
                recent_names.append(person)
                prev = 1
                words[person][4].append(0)
            
        else:
            total +=1
            prev = 0
            words[person][0] += 1
            words[person][3] += word
            words[person][4][-1] += len(word)
            words[person][5].append(word)
            if word in dict1:
                dict1[word] += 1
            else:
                dict1[word] = 1
print(total)
final = []
for person in words:
    final.append((words[person], person))
final.sort()
final.reverse()

print("Everything leaderboard")
for person in final:
    if person[1] == "joey_rubas":
        print("The REAL winner: ", person[1], ": ", person[0][0], "words, ", person[0][2], "messages, ", person[0][1], "likes")
    else:
        print(final.index(person), ". ", person[1], ": ", person[0][0], "words, ", person[0][2], "messages, ", person[0][1], "likes")


print("Words Leaderboard")
for person in final:
    if person[1] == "joey_rubas":
        print("The REAL winner: ", person[1], ": ", person[0][0], "words")
    else:
        print(final.index(person), ". ", person[1], ": ", person[0][0], "words")

final = []
for person in words:
    final.append((words[person][1], person))
final.sort()
final.reverse()
              
print("Likes Leaderboard")
for person in final:
    print(final.index(person) + 1, ". ", person[1], ": ", person[0], "likes")


final = []
for person in words:
    final.append((len(words[person][3])/(words[person][0] if words[person][0] > 0 else 1) , person))
final.sort()
final.reverse()
              
print("Average word length Leaderboard")
for person in final:
    print(final.index(person) + 1, ". ", person[1], ": ", round(person[0], 3), "letters pers word")



final = []
for person in words:
   final.append((statistics.median(words[person][4]) , person))
final.sort()
final.reverse()
              
print("Median message length Leaderboard")
for person in final:
    print(final.index(person) + 1, ". ", person[1], ": ", person[0], "words pers message")

final = []
for person in words:
    final.append((person, words[person][5]))

for person in final:
    try:
        print(person[0], most_common(person[1]))
    except:
        pass



list1 = []
for word in dict1:
    list1.append((dict1[word], word))
list1.sort()
list1.reverse()
for word in list1[:35]:
    print(word[1], ":", word[0], " times")
