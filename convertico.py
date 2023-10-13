from PIL import Image
filen = r'C:\Users\Hiurytg.000\Desktop\TH_SQL\Calculadora-TH-SQL\images\th_ico.png'
img = Image.open(filen)
img.save('th_ico.ico',format = 'ICO', sizes=[(32,32)])