import re
s1 = "hello\nworld"
print(s1)
# 在字符串开头
res = re.match("He", s1, flags=re.I)
print(res.group())
# 扫描整个字符串,返回第一个匹配
res = re.search("o", s1)
print(res.span(), type(res))
# 是否完全匹配
res = re.fullmatch("hello", s1)
print(res, type(res))
# 返回列表
res = re.findall("l", s1)
print(res)
# 分割返回列表
res = re.split("o", s1)
print(res, type(res))
# 替代
res = re.sub("hello", "hi", s1)
print(res)
# 迭代器
res = re.finditer("l", s1)
print(res, type(res))
for i in res:
    print(i.span())

s2 = "abcde\nabcre"
res = re.findall("^abc", s2, re.M)
print(res)
res = re.findall("e$", s2, re.M)
print(res)

s3 = "aaa \n aaa"
res = re.findall(".", s3, re.S)
print(res)
res = re.findall(".", s3, re.M)
print(res)

res = re.findall("[0123].abc", " 0cabc 2abc 33abc 26abc")
print(res)
res = re.findall("\d.abc", " 0cabc 2abc 33abc 26abc")
print(res)
res = re.findall("\D.abc", " 0cabc 2abc '3abc p6abc")
print(res)
res = re.findall("\s.abc", " 0cabc 2abc 33abc 26abc")
print(res)
res = re.findall("\S.abc", " 0cabc 2abc 33abc 26abc")
print(res)
res = re.findall("\w\d", "aaa1 aex5 afafg _12324")
print(res)

res = re.findall(r"\bhello\b", "hello world hello zhengzhou sayhellok")
print(res)
res = re.findall("\bhello\b", "hello world hello zhengzhou sayhellok")
print(res)
res = re.findall(r"\Bhello\B", "hello world hello zhengzhou sayhellok")
print(res)

print(r"hello \n world")

res = re.match(r"\d{9}[@][q]{2}.com", "982882262@qq.com")
print(res.group())

res = re.findall(r"[0-9]*@[q]{2}.com", "9882882262@qq.com  55@.com")
print(res)

res = re.findall("[0-9]*?", "123 456")
print(res)

res = re.findall("a*?", "aaaaaaaaaaa")
print(res)

retsult = re.match(".*?@.*?.com", "496575233@qq.com")
print(retsult.group())

retsult = re.match("(.*?)@(.*?)(.com)", "496575233@qq.com")
print(retsult.group(), retsult.group(1), retsult.group(2), retsult.group(3))

result = re.match(r"(hello).*?\1", "hello world hello china")
print(result.group(), result.group(1))


res = re.match("(?P<hname>hello).*?(?P=hname)", "hello world hello china")
print(res.group(), res.group('hname'))

print(r"<a href='//stock.quote.stockstar.com/[0-9]{6}.shtml'>(.*?)</a>")