import requests
import re
response = requests.get("http://quote.stockstar.com/stock/ranklist_a_3_1_1.html",)
# print(response.text)
res = re.findall(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">(\D*?)</a>', response.text)
# for i in res:
#     print(i[0])
#     print(i[1])
# res = re.findall(r"<a href='//stock.quote.stockstar.com/002496.shtml'>002496</a>", response.text)

# res1= re.findall(r"<a.*?stock.quote.stockstar.com/(.*?).shtml.*?></a>", response.text)
print(res)
