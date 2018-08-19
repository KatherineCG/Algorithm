from __future__ import division


class Solution():
    def SortQuestions(self, questions):
        if not questions:
            return
        dictquestion = {}
        for ch in questions:
            if ch[0].islower() and len(ch[0]) <= 100:
                ch[1] = int(ch[1])
                ch[2] = int(ch[2])
                if ch[1] >= 1 and ch[1] <= 1000 and ch[2] >= 0 and ch[2] <= ch[1]:
                    rate = ch[2] / ch[1]
                    if rate <= 0.3:
                        diff = 5
                    elif rate > 0.3 and rate <= 0.6:
                        diff = 4
                    else:
                        diff = 3
                    dictquestion[ch[0]] = repr(diff)
        sorted(dictquestion.keys())
        return dictquestion


test = Solution()
n = input()
array = ''
questions = []
dictquestion = {}
for i in range(n):
    array = raw_input()
    array = array.split(' ')
    questions.append(array)
dictquestion = test.SortQuestions(questions)
for key in dictquestion:
    print key + ' ' + dictquestion[key]
