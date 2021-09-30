import hashlib

'''
hexstr = hashPw("4Plub56z", "ea67b08fb5dd68e5")
obj = { "username": "student", "hashpw": "ac383ea2005194b614c9ebe6a1037f9a", "salt": "ea67b08fb5dd68e5" }

print("is the same: ",obj["hashpw"] == hexstr)
'''
data = [
    {"username": "aamu", "hashpw": "1f80b3a2a6682e6157d0afd9bb4d53cc", "salt":	"6cc291d349195274"},
    {"username": "abdullo","hashpw": "a007b8598b6dbb03a8f4521225dad466", "salt": "4f4c1e84f449eaef"},
    {"username": "aki","hashpw": "bab5d0882399a1278900ba6a124f0cc1", "salt": "56732bbfa92de084"},
    {"username": "amahle","hashpw": "f3a93f84256490b280be9a769c6d024e", "salt": "64258ee3176af2b3"},
    {"username": "anastasija","hashpw": "347ce2b2e1abffafdd9f1adccd30ad5b", "salt": "d144a974dd1feb1d"},
    {"username": "antonio","hashpw": "2fad198862f07c9d79bda30e8210872e", "salt": "934edd5572a13f25"},
    {"username": "asser","hashpw": "4c4ce0f5efa8624dfc727ce5e88e8bc5", "salt": "d7c44397c662554e"},
    {"username": "banele","hashpw": "c0b6dbc4facdb84bc9acf39002b9ad13", "salt": "3073c0a9f141634c"},
    {"username": "danila","hashpw": "7e93ec92ed6b9f6fb72037bd4d769d24", "salt": "9feaa244e05b9f40"},
    {"username": "eetu","hashpw": "03af847e9816797caafab473baf139d0", "salt": "e1396e40b2168137"},
    {"username": "elna","hashpw": "5e8e80f935212088f4985d845f4d4994", "salt": "1cc47b90ca1403db"},
    {"username": "fenna","hashpw": "9e6372b8c45cbeb950a4a46f61553a09", "salt": "5814ed2136890990"},
    {"username": "heimo","hashpw": "744efef078ef2f857ad895ca3eb1688f", "salt": "7498d4d1771dc760"},
    {"username": "henriikka","hashpw": "d609efb5d16b80e3c6dee95085dc557c", "salt": "a9e7359dbd28538c"},
    {"username": "henrik","hashpw": "bf7fccaf2df1c3f6f66661ff7d4fa2ee", "salt": "7138c0787a9e4c33"},
    {"username": "ibrahim","hashpw": "2b5e697f841d7bd3ee3a3bedd90a2e07", "salt": "fe4225e19c57488b"},
    {"username": "james","hashpw": "5dc44eb20a1fca332fd5eeb93d022231", "salt": "e564a9d6ef0c5c5c"},
    {"username": "janine","hashpw": "459d2d84a33f7fbc83bf516654df849f", "salt": "28331f55c31d03b0"},
    {"username": "leon","hashpw": "c2263a32632a4dffb3416fad34ee9ee2", "salt": "11f993ad560cf86d"},
    {"username": "mari","hashpw": "764ebf7b47ded35c4747d9480d8426b9", "salt": "1e846851118f92e0"},
    {"username": "miina","hashpw": "78bd87728141ee0de05df8d4b5b205ce", "salt": "10d661b4c93de755"},
    {"username": "miko","hashpw": "a84d205b2c96860465280dee035c4d6f", "salt": "ca00b9603fbe40ea"},
    {"username": "nathan","hashpw": "1abed8465e87f431b3c9ba9309c2ec6e", "salt": "9cbcd9b9b617f777"},
    {"username": "nikolai","hashpw": "c6708e70d7438b39d3eb83b02e0cbd65", "salt": "bb37c4980647c30e"},
    {"username": "nisanur","hashpw": "4941e16eb8478d272c31c4a3499c9acc", "salt": "9aecfb22ad129643"},
    {"username": "robo","hashpw": "1d3644a7478ad676c5933b9c48662ac1", "salt": "ea67b08fb5dd68e5"},
    {"username": "russia","hashpw": "1a4c67de96178f6455128f64b5fa03aa", "salt": "399482f657e0b705"},
    {"username": "sari","hashpw": "240eee1b1965b9e9793c9a5002fc75d3", "salt": "222a8330721a26f0"},
    {"username": "sem","hashpw": "3c7710a0f7af225a112ecdd6871dbe9a", "salt": "95551a6b911f82c8"},
    {"username": "siti","hashpw": "affb6fdfb6607f3afb2b297e0499e644", "salt": "df82efc703860ce1"},
    {"username": "taina","hashpw": "60c2af5832fc849ec3035968f2cacab1", "salt": "1ab0aeb7181a03c8"},
    {"username": "tuukka","hashpw": "601e878d06a7c98e17d0bc858e9200b5", "salt": "059bbf3c1dc660c9"},
]

f = open('test.txt','r')


constantString = "potPlantSalt"
def hashPw(password, salt):
    stringToHash = constantString + password + salt
    hfunc = hashlib.sha256()
    hfunc.update(str.encode(stringToHash))
    hexstr = hfunc.hexdigest()
    return hexstr[0:32]

'''
def extractWord(w):
    s = w[7:len(w)]
    ends = s.find('<')
    s = s[0:ends] + '\n'
    return s
'''

def main():
    print("hello world")

    for w in f:
        found = False
        for obj in data:
            hexstr = hashPw(w[0:len(w)-1], obj["salt"])
            if hexstr == obj["hashpw"]:
                print(obj["username"], "password is ", w)
                found = True
                break
        if not found:
            print(w[0:len(w)-1],"is not password")
        else:
            break


main()

f.close()



