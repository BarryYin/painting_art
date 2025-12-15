#!/usr/bin/env python
#coding:utf-8
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont

 

class postMaker(object):
	def __init__(self, backImg, font):
		self.backImg = backImg
		self.font = font
		self.post = None

	def create(self, userIcon, userName, qrImg, textColor):
		"""
		@userIcon: 用户头像URL
		@userName： 用户昵称
		@qrImg: 用户二维码URL
		@textColor: 文字颜色，{R，G，B}
		"""
		try:
			backImg = Image.open(self.backImg)
			#userIcon = Image.open(userIcon)
			font = ImageFont.truetype(self.font, 90)


			#userIcon.thumbnail((88,88))
			#backImg.paste(userIcon, (316,242))
			# 确保userName是字符串
			userName = str(userName)

			draw = ImageDraw.Draw(backImg)
			draw.ink = textColor.get('R',0) + textColor.get('G',0) * 256 + textColor.get('B',0)*256*256
			#textWidth,textHeight = font.getsize(userName)
			# 使用getbbox获取文本尺寸
			textWidth, textHeight = font.getbbox(userName)[2:]
			draw.text([450-textWidth/2, 1590], userName, font=font)

			qrImg = Image.open(qrImg)
			qrImg.thumbnail((650,650))
			backImg.paste(qrImg,(1800,2500))

			self.post = backImg
			backImg.save("testPost3.jpg", "jpeg")
		except Exception as e:
			print(repr(e))

if __name__=='__main__':
	# user= r"小猪猪快飞",
	# backImg = r"10001.jpg"
	# font = r"msyhl.ttc"
	# pMaker = postMaker(backImg=backImg, font= font)
	# userIcon = r'testIcon.jpg'
	# qrImg = r'333.png'
	# pMaker.create(
	# 	userIcon=userIcon,
	# 	userName=user,
	# 	qrImg=qrImg,
	# 	textColor={'R':0,'G':0,'B':0})
	print('ok')


