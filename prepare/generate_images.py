#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import codecs


image_size = 44
font_size = image_size - 2 
font_type = 'jhenghei.ttf'
font_padding = 2
save_dir = 'simp_jhenghei'

with codecs.open('simp_chars.txt', 'r', 'utf-8') as f:
	chars = f.readlines()

	for character in chars:
		font = ImageFont.truetype(font_type, font_size)
		img = Image.new('RGB', (font_size + font_padding, font_size + font_padding), (255, 255, 255))
		draw= ImageDraw.Draw(img)
		draw.text((0, -3 * font_padding), character, fill=(0, 0, 0), font = font)
		del draw
		img.save(save_dir + "/" + character + ".png")
