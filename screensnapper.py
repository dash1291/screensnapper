#!/usr/bin/env python
import re
import urllib2

from BeautifulSoup import BeautifulSoup
import gtk.gdk
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

# Capture the screen image and storing into a png file
w = gtk.gdk.get_default_root_window()
sz = w.get_size()
pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
if (pb != None):
    pb.save("ss.png","png")

# POST form image upload to picpaste.com
register_openers()
data, headers = multipart_encode({'upload': open("ss.png"), 'addprivacy': '1'})
request = urllib2.Request('http://picpaste.com/upload.php', data, headers)
response = urllib2.urlopen(request)

# Parse response from picpaste.com to extract the picture url
bs = BeautifulSoup(response.read())
s1 = bs.find(text=re.compile('Picture URL:')).parent
url = s1.findNextSiblings('td')[0].find('a').string
print url
