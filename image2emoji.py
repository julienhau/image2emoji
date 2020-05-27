#! python3

import requests
from bs4 import BeautifulSoup as soup
from PIL import Image
from io import BytesIO
import json
from pathlib import Path
import threading
import os


res = requests.get('https://www.webfx.com/tools/emoji-cheat-sheet/')
bs = soup(res.text, 'html.parser')

name = input('Move the image you want to convert in the same directory as the program, then write down the file name below (eg. Picture.jpg)\n')
p = Path.cwd()/name
stem = p.stem

f = open('coloremoji.json','r')
content = f.read()
emojidict = json.loads(content)

img = Image.open(p)
basewidth = int(input('Write down the pixel width you wish to obtain (minimum value recommended: 1200, maximum value: 2400)\nNote: the value should be a multiple of 200\n'))
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img = img.convert('RGB')
newImage = Image.new('RGBA',(basewidth,hsize),'black')


def first():
	global img, newImage, basewidth
	for x in range(0,basewidth//10,20):
		for y in range(0,img.size[1],20):
			r, g, b = img.getpixel((x,y))
			theList = [(r1-r)**2+(g1-g)**2+(b1-b)**2 for r1,g1,b1 in emojidict.values()]
			emojiIndex = theList.index(min(theList))+1
			emoji = bs.select(f'#e_{emojiIndex}')
			emojisrc = emoji[0].get('data-src')
			emojiimg = requests.get('https://www.webfx.com/tools/emoji-cheat-sheet/'+emojisrc)
			ImageFile = Image.open(BytesIO(emojiimg.content))
			ImageFile = ImageFile.resize((20,20),Image.ANTIALIAS)
			newImage.paste(ImageFile,(x,y))
			print(x,y)

def second():
	global img, newImage, basewidth
	for x in range(basewidth//10,basewidth//5,20):
		for y in range(0,img.size[1],20):
			r, g, b = img.getpixel((x,y))
			theList = [(r1-r)**2+(g1-g)**2+(b1-b)**2 for r1,g1,b1 in emojidict.values()]
			emojiIndex = theList.index(min(theList))+1
			emoji = bs.select(f'#e_{emojiIndex}')
			emojisrc = emoji[0].get('data-src')
			emojiimg = requests.get('https://www.webfx.com/tools/emoji-cheat-sheet/'+emojisrc)
			ImageFile = Image.open(BytesIO(emojiimg.content))
			ImageFile = ImageFile.resize((20,20),Image.ANTIALIAS)
			newImage.paste(ImageFile,(x,y))
			print(x,y)

def third():
	global img, newImage, basewidth
	for x in range(basewidth//5,(3*basewidth)//10,20):
		for y in range(0,img.size[1],20):
			r, g, b = img.getpixel((x,y))
			theList = [(r1-r)**2+(g1-g)**2+(b1-b)**2 for r1,g1,b1 in emojidict.values()]
			emojiIndex = theList.index(min(theList))+1
			emoji = bs.select(f'#e_{emojiIndex}')
			emojisrc = emoji[0].get('data-src')
			emojiimg = requests.get('https://www.webfx.com/tools/emoji-cheat-sheet/'+emojisrc)
			ImageFile = Image.open(BytesIO(emojiimg.content))
			ImageFile = ImageFile.resize((20,20),Image.ANTIALIAS)
			newImage.paste(ImageFile,(x,y))
			print(x,y)

def forth():
	global img, newImage, basewidth
	for x in range((3*basewidth)//10,(4*basewidth)//10,20):
		for y in range(0,img.size[1],20):
			r, g, b = img.getpixel((x,y))
			theList = [(r1-r)**2+(g1-g)**2+(b1-b)**2 for r1,g1,b1 in emojidict.values()]
			emojiIndex = theList.index(min(theList))+1
			emoji = bs.select(f'#e_{emojiIndex}')
			emojisrc = emoji[0].get('data-src')
			emojiimg = requests.get('https://www.webfx.com/tools/emoji-cheat-sheet/'+emojisrc)
			ImageFile = Image.open(BytesIO(emojiimg.content))
			ImageFile = ImageFile.resize((20,20),Image.ANTIALIAS)
			newImage.paste(ImageFile,(x,y))
			print(x,y)

def fifth():
	global img, newImage, basewidth
	for x in range((4*basewidth)//10,(5*basewidth)//10,20):
		for y in range(0,img.size[1],20):
			r, g, b = img.getpixel((x,y))
			theList = [(r1-r)**2+(g1-g)**2+(b1-b)**2 for r1,g1,b1 in emojidict.values()]
			emojiIndex = theList.index(min(theList))+1
			emoji = bs.select(f'#e_{emojiIndex}')
			emojisrc = emoji[0].get('data-src')
			emojiimg = requests.get('https://www.webfx.com/tools/emoji-cheat-sheet/'+emojisrc)
			ImageFile = Image.open(BytesIO(emojiimg.content))
			ImageFile = ImageFile.resize((20,20),Image.ANTIALIAS)
			newImage.paste(ImageFile,(x,y))
			print(x,y)

def sixth():
	global img, newImage, basewidth
	for x in range((5*basewidth)//10,(6*basewidth)//10,20):
		for y in range(0,img.size[1],20):
			r, g, b = img.getpixel((x,y))
			theList = [(r1-r)**2+(g1-g)**2+(b1-b)**2 for r1,g1,b1 in emojidict.values()]
			emojiIndex = theList.index(min(theList))+1
			emoji = bs.select(f'#e_{emojiIndex}')
			emojisrc = emoji[0].get('data-src')
			emojiimg = requests.get('https://www.webfx.com/tools/emoji-cheat-sheet/'+emojisrc)
			ImageFile = Image.open(BytesIO(emojiimg.content))
			ImageFile = ImageFile.resize((20,20),Image.ANTIALIAS)
			newImage.paste(ImageFile,(x,y))
			print(x,y)

def seventh():
	global img, newImage, basewidth
	for x in range((6*basewidth)//10,(7*basewidth)//10,20):
		for y in range(0,img.size[1],20):
			r, g, b = img.getpixel((x,y))
			theList = [(r1-r)**2+(g1-g)**2+(b1-b)**2 for r1,g1,b1 in emojidict.values()]
			emojiIndex = theList.index(min(theList))+1
			emoji = bs.select(f'#e_{emojiIndex}')
			emojisrc = emoji[0].get('data-src')
			emojiimg = requests.get('https://www.webfx.com/tools/emoji-cheat-sheet/'+emojisrc)
			ImageFile = Image.open(BytesIO(emojiimg.content))
			ImageFile = ImageFile.resize((20,20),Image.ANTIALIAS)
			newImage.paste(ImageFile,(x,y))
			print(x,y)

def eighth():
	global img, newImage, basewidth
	for x in range((7*basewidth)//10,(8*basewidth)//10,20):
		for y in range(0,img.size[1],20):
			r, g, b = img.getpixel((x,y))
			theList = [(r1-r)**2+(g1-g)**2+(b1-b)**2 for r1,g1,b1 in emojidict.values()]
			emojiIndex = theList.index(min(theList))+1
			emoji = bs.select(f'#e_{emojiIndex}')
			emojisrc = emoji[0].get('data-src')
			emojiimg = requests.get('https://www.webfx.com/tools/emoji-cheat-sheet/'+emojisrc)
			ImageFile = Image.open(BytesIO(emojiimg.content))
			ImageFile = ImageFile.resize((20,20),Image.ANTIALIAS)
			newImage.paste(ImageFile,(x,y))
			print(x,y)

def ninth():
	global img, newImage, basewidth
	for x in range((8*basewidth)//10,(9*basewidth)//10,20):
		for y in range(0,img.size[1],20):
			r, g, b = img.getpixel((x,y))
			theList = [(r1-r)**2+(g1-g)**2+(b1-b)**2 for r1,g1,b1 in emojidict.values()]
			emojiIndex = theList.index(min(theList))+1
			emoji = bs.select(f'#e_{emojiIndex}')
			emojisrc = emoji[0].get('data-src')
			emojiimg = requests.get('https://www.webfx.com/tools/emoji-cheat-sheet/'+emojisrc)
			ImageFile = Image.open(BytesIO(emojiimg.content))
			ImageFile = ImageFile.resize((20,20),Image.ANTIALIAS)
			newImage.paste(ImageFile,(x,y))
			print(x,y)

def tenth():
	global img, newImage, basewidth
	for x in range((9*basewidth)//10,basewidth,20):
		for y in range(0,img.size[1],20):
			r, g, b = img.getpixel((x,y))
			theList = [(r1-r)**2+(g1-g)**2+(b1-b)**2 for r1,g1,b1 in emojidict.values()]
			emojiIndex = theList.index(min(theList))+1
			emoji = bs.select(f'#e_{emojiIndex}')
			emojisrc = emoji[0].get('data-src')
			emojiimg = requests.get('https://www.webfx.com/tools/emoji-cheat-sheet/'+emojisrc)
			ImageFile = Image.open(BytesIO(emojiimg.content))
			ImageFile = ImageFile.resize((20,20),Image.ANTIALIAS)
			newImage.paste(ImageFile,(x,y))
			print(x,y)
threadObj1 = threading.Thread(target=second)
threadObj2 = threading.Thread(target=first)
threadObj3 = threading.Thread(target=third)
threadObj4 = threading.Thread(target=forth)
threadObj5 = threading.Thread(target=fifth)
threadObj6 = threading.Thread(target=sixth)
threadObj7 = threading.Thread(target=seventh)
threadObj8 = threading.Thread(target=eighth)
threadObj9 = threading.Thread(target=ninth)
threadObj10 = threading.Thread(target=tenth)

threadObj1.start()
threadObj2.start()
threadObj3.start()
threadObj4.start()
threadObj5.start()
threadObj6.start()
threadObj7.start()
threadObj8.start()
threadObj9.start()
threadObj10.start()


threadObj1.join()
threadObj2.join()
threadObj3.join()
threadObj4.join()
threadObj5.join()
threadObj6.join()
threadObj7.join()
threadObj8.join()
threadObj9.join()
threadObj10.join()

newImage.save('emojified'+stem+'.png')
