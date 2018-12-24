# coding: utf8
import datetime

f = open('words.txt','a+')#a+模式是为了避免第一次单词文件不存在时的报错
f.seek(0)
lines = f.readlines()
words = [line.split('      ')[0] for line in lines if lines.strip()]
#六个空格字符作为单词和时间的分割。words是一个列表。
#strip()方法是为了去除字符串前后多余的空白字符

while True:
    word = input('please enter the word you want to record(the enter key means exit):\n').strip()
    if not word:
        break
    if word in words:
        print('the word is already exist')
    else:
        words.append(word)
        t = datetime.date.today()
        line = word + '      ' + str(t) + '\n'
        lines.append(line)
        f.write(line)
        f.flush() #避免程序意外结束时，未保存的内容丢失
    print('it has recorded',len(words),'words/phrase\n')
f.close()        
