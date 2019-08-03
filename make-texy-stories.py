from PIL import Image, ImageDraw, ImageFont
 
#img = Image.new('RGB', (900, 1600), color = (0, 0, 0))
#fnt = ImageFont.truetype('C:\\Windows\\Fonts\\impact.ttf', 100)
#d = ImageDraw.Draw(img)
#d.text((30,150), "CARIOCA RIDER", font=fnt, fill=(255, 255, 255))
#img.save('stories/image-story-2.png')


image = Image.open('stories/background.jpg')
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('C:\\Windows\\Fonts\\Roboto-Bold.ttf', size=100)
(x, y) = (50, 50)

message = "BE STRONG"
color = 'rgb(0, 0, 0)' # black color

draw.text((x, y), message, fill=color, font=font)

image.save('stories/background_changed.jpg')
