from PIL import Image, ImageDraw, ImageFont

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
fonts = ['/Library/Fonts/Arial.ttf','/Library/Fonts/Times New Roman.ttf','/Library/Fonts/Comic Sans MS.ttf','/Library/Fonts/Courier New.ttf','/Library/Fonts/Verdana.ttf']
def create_image(text,fonts):
    for x in fonts:
        file_name = x.replace(' ','_').replace('/','_')
        file_name = file_name[1:-4]
        img = Image.new('RGB',(25,20), color=(0,0,0))
        fnt = ImageFont.truetype(x, 15)
        d = ImageDraw.Draw(img)
        d.text((0,0), text, font=fnt, fill=(255, 255, 255))
        img.save(file_name+'-'+text+'.jpeg')

for i in letters:
    create_image(i,fonts)

