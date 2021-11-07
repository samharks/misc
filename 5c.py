import requests,time

#r = requests.get('http://cdn1.vikaa.fi:52552/photos/0596fd37/6a18d5005f7ebca5ffff010b000033f6.png')

#           'http://cdn1.vikaa.fi:52552/photos/0596fd37/6a18d5005f7ebca5ffff010b000033f6.png
url_start = 'http://cdn1.vikaa.fi:52552/photos/0596fd37/6a18d5005f7'
url_midright = 'ffff010b000034'


#http://cdn1.vikaa.fi:52552/photos/0596fd37/6a18d5005f7eab31ffff010b00003364.png 404
#981945
url_ = ''
for j in range(981946,983208):
    url_midleft = f'{j:0>4x}'
    for i in range(0,256):
        u = url_start + url_midleft + url_midright
        url_ending = f'{i:0>2x}'
        url = u + url_ending + '.png'
        #time.sleep(0.001)
        r = requests.get(url)
        print(url, r.status_code)
        if r.status_code == 200:
            url_ = url
            break
    if url_ != '':
        break

'''
http://cdn1.vikaa.fi:52552/photos/0596fd37/6a18d5005f7efb63ffff010b00003470.png

http://cdn1.vikaa.fi:52552/photos/0596fd37/6a18d5005f7f00a8ffff010b0000347a.png
'''   