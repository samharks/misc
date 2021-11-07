import hashlib,hmac
import string

#554324

'''

key = "This is a dummy key!"
for i in range(0,53):
    m = i * '\x61'
    m = m + key
    hmac_input = 'ClientCmd|554324|'+ m
    h2 = hmac.new(str.encode(key),b'',hashlib.sha256)
    h2.update(str.encode(hmac_input))
    s = "554324;"+m+";"+h2.hexdigest()
    print(s)
'''

#556d8b2868d8451f5facb4abee2402c415f3a7ca1e8caae53a98789ef3563c23


characters = []

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaThis is a dummy key!
'''
key = "This is a dummy key!"
newkey = key[1:20]
print(len(key))

for c in string.printable[0:95]:
    hmac_key = newkey + c
    m = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + key
    hmac_input = 'ClientCmd|554324|'+ m
    h2 = hmac.new(str.encode(hmac_key),b'',hashlib.sha256)
    h2.update(str.encode(hmac_input))
    s = "554324;"+m+";"+h2.hexdigest()
    print(s)
    print('key: ',hmac_key, len(hmac_key), hmac_input)

print('------')

print(str.encode(key))
'''
m = 30 * "a"
#key = '\0'
hmac_input = 'ClientCmd|554324|'+ m
characters = ['ä','Ä', 'ö', 'Ö', 'å','Å', '\\', '`','´','|', '\0']


for c in string.printable[0:95]:
    hmac_key = c + 'LZB4S1zV1acCFvZ8DaE'
    h2 = hmac.new(str.encode(hmac_key),b'',hashlib.sha256)
    h2.update(str.encode(hmac_input))
    s = "554324;"+m+";"+h2.hexdigest()
    print(s)
    print('hmac_key: ', hmac_key)

for c in characters:
    hmac_key = c + 'LZB4S1zV1acCFvZ8DaE'
    h2 = hmac.new(str.encode(hmac_key),b'',hashlib.sha256)
    h2.update(str.encode(hmac_input))
    s = "554324;"+m+";"+h2.hexdigest()
    print(s)
    print('hmac_key: ', hmac_key)

