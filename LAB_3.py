import re

pattern1=re.compile(r'^(\d\d\d)-(\d\d\d-\d\d\d\d)$')
text1='123-456-7890'
print("Text-1: ",text1)
match1=pattern1.search(text1)
print("group0 match: ",match1.group(0))
print("group1 match: ",match1.group(1))
print("group2 match: ",match1.group(2))

pattern2=re.compile(r'https?://\S+')
text2='http://google.com is a google website and https://google.com is even more secure version'
link=pattern2.findall(text2)
print(link)

pattern4=re.compile(r'^\d{1,3}(,\d{3})*$')
text4=['42','42,535','42,5353','5,345,567']