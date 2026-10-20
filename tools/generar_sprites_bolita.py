from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
src=Image.open('assets/file_00000000289881f5a0b01dd5ab44962b.png').convert('RGBA')
out=Path('assets/bolita');out.mkdir(parents=True,exist_ok=True)
# Recorte preciso: máscara poligonal que excluye todo el fondo cuadriculado.
cup=src.crop((17,24,207,213))
mask=Image.new('L',cup.size,0);d=ImageDraw.Draw(mask)
d.polygon([(37,22),(47,15),(75,12),(114,12),(146,18),(155,26),(180,149),(186,165),(178,176),(157,181),(38,181),(12,175),(4,165),(9,144)],fill=255)
mask=mask.filter(ImageFilter.GaussianBlur(.65))
cup.putalpha(mask)
cup.save(out/'cubilete.png',optimize=True)
# La bola se dibuja de forma independiente para evitar el fondo del atlas.
ball=Image.new('RGBA',(96,96));d=ImageDraw.Draw(ball)
d.ellipse((12,15,85,88),fill='#8b071a')
d.ellipse((15,13,82,79),fill='#ec1831')
d.ellipse((24,20,59,51),fill='#ff6467')
d.ellipse((30,22,46,37),fill='#fff2ec')
ball.save(out/'bolita.png',optimize=True)
# Mesa independiente: madera detallada y cuatro patas, sin cubiletes incrustados.
W,H=1000,410
table=Image.new('RGBA',(W,H));d=ImageDraw.Draw(table)
for x in (65,830):
 d.rounded_rectangle((x,230,x+108,399),radius=15,fill='#a65121',outline='#55230e',width=8)
 d.polygon([(x+18,250),(x+62,250),(x+40,382),(x+18,382)],fill='#dd8635')
d.rounded_rectangle((17,75,983,293),radius=25,fill='#8c421c',outline='#3f1c0c',width=9)
d.rounded_rectangle((25,22,975,249),radius=25,fill='#e99c48',outline='#49210f',width=9)
for y in (75,129,183):
 d.line((40,y,961,y),fill='#a95420',width=5)
 d.line((42,y+5,958,y+5),fill='#ffd084',width=3)
for y in range(43,220,18):
 for x in range(80,950,125):
  d.arc((x,y,x+100,y+13),0,130,fill='#c87b32',width=2)
for x in (70,930):
 for y in (51,212):
  d.ellipse((x-11,y-11,x+11,y+11),fill='#5b3424',outline='#24110b',width=3)
  d.line((x-5,y-2,x+5,y+2),fill='#d8d4cb',width=2)
table.save(out/'mesa.png',optimize=True)
print([(p.name,p.stat().st_size) for p in out.glob('*.png')])

# Regeneración automática de assets.
