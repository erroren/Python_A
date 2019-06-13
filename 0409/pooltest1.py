from multiprocessing import Pool
import requests
list1 = ["https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=bc9be6a0336d55fbc3c672265d224f40/b3119313b07eca80ff34b3999f2397dda144839f.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=cb250cb54d166d223e77119476220945/cb8065380cd7912309031f0aa3345982b3b780e9.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=4ed4331a9aeef01f4b141cc5d0ff99e0/bba1cd11728b4710434977b2cdcec3fdfc03236e.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=97a7118d77310a55c224daf487444387/a8ec8a13632762d097922fc1aeec08fa513dc624.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=0ca80270bf3533faf3b6972e98d2fdca/0824ab18972bd407208a588375899e510fb3097a.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=b54a4692df00baa1bc2c43bb7711b9b1/faedab64034f78f0dd41118d77310a55b3191c01.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=0c3d18a206fa513d57aa68de0d6c554c/c75c10385343fbf22fa32b5dbe7eca8064388fc5.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=bc9be6a0336d55fbc3c672265d224f40/b3119313b07eca80ff34b3999f2397dda144839f.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=cb250cb54d166d223e77119476220945/cb8065380cd7912309031f0aa3345982b3b780e9.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=4ed4331a9aeef01f4b141cc5d0ff99e0/bba1cd11728b4710434977b2cdcec3fdfc03236e.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=97a7118d77310a55c224daf487444387/a8ec8a13632762d097922fc1aeec08fa513dc624.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=0ca80270bf3533faf3b6972e98d2fdca/0824ab18972bd407208a588375899e510fb3097a.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=b54a4692df00baa1bc2c43bb7711b9b1/faedab64034f78f0dd41118d77310a55b3191c01.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=0c3d18a206fa513d57aa68de0d6c554c/c75c10385343fbf22fa32b5dbe7eca8064388fc5.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=bc9be6a0336d55fbc3c672265d224f40/b3119313b07eca80ff34b3999f2397dda144839f.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=cb250cb54d166d223e77119476220945/cb8065380cd7912309031f0aa3345982b3b780e9.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=4ed4331a9aeef01f4b141cc5d0ff99e0/bba1cd11728b4710434977b2cdcec3fdfc03236e.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=97a7118d77310a55c224daf487444387/a8ec8a13632762d097922fc1aeec08fa513dc624.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=0ca80270bf3533faf3b6972e98d2fdca/0824ab18972bd407208a588375899e510fb3097a.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=b54a4692df00baa1bc2c43bb7711b9b1/faedab64034f78f0dd41118d77310a55b3191c01.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=0c3d18a206fa513d57aa68de0d6c554c/c75c10385343fbf22fa32b5dbe7eca8064388fc5.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=bc9be6a0336d55fbc3c672265d224f40/b3119313b07eca80ff34b3999f2397dda144839f.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=cb250cb54d166d223e77119476220945/cb8065380cd7912309031f0aa3345982b3b780e9.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=4ed4331a9aeef01f4b141cc5d0ff99e0/bba1cd11728b4710434977b2cdcec3fdfc03236e.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=97a7118d77310a55c224daf487444387/a8ec8a13632762d097922fc1aeec08fa513dc624.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=0ca80270bf3533faf3b6972e98d2fdca/0824ab18972bd407208a588375899e510fb3097a.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=b54a4692df00baa1bc2c43bb7711b9b1/faedab64034f78f0dd41118d77310a55b3191c01.jpg",
"https://imgsa.baidu.com/news/q%3D100/sign=0c3d18a206fa513d57aa68de0d6c554c/c75c10385343fbf22fa32b5dbe7eca8064388fc5.jpg"]


def save_data(list1,i):
    print(list1[i])
    # res = requests.get(list1[i])
    # print(res.content)
    # with open("./image/" +
    #           + ".jpg", "wb") as file1:
    #     file1.write(res.content)


def multiprocess():
    pool = Pool(5)
    for i in range(len(list1)):
        pool.apply_async(save_data, args=(list1, i))
    pool.close()
    pool.join()


if __name__ == '__main__':
    multiprocess()
