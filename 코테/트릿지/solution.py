"""
Q1. Write a function called find_bigrams that takes a sentence or paragraph of strings and returns a list of all bigrams.

Example:

Input:

sentence =
Have free hours and love children?
Drive kids to school, soccer practice
and other activities.
Output:

 [('have', 'free'),
 ('free', 'hours'),
 ('hours', 'and'),
 ('and', 'love'),
 ('love', 'children?'),
 ('children?', 'drive'),
 ('drive', 'kids'),
 ('kids', 'to'),
 ('to', 'school,'),
 ('school,', 'soccer'),
 ('soccer', 'practice'),
 ('practice', 'and'),
 ('and', 'other'),
 ('other', 'activities.')]
"""


def find_bigrams(sentence):
     string = sentence.lower().split(" ")
     length = len(string)
     answer = []
     for i in range(length-1):
          answer.append(tuple([string[i],string[i+1]]))
     return answer


if __name__ == "__main__":
     sentence = "Have free hours and love children? Drive kids to school, soccer practice and other activities."

     answer = find_bigrams(sentence)
     for a in answer:
      print(a)




