#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

FONT_SIZE = 40
FONT = "jhenghei.ttf"
FONT_PADDING = 4

font = ImageFont.truetype(FONT, FONT_SIZE)
img = Image.new('RGB', (FONT_SIZE + FONT_PADDING, FONT_SIZE + FONT_PADDING), (255, 255, 255))
char = ImageDraw.Draw(img)
char.text((0, -FONT_PADDING), u"懂", fill=(255, 0, 0), font = font)
img.save("test.png")
