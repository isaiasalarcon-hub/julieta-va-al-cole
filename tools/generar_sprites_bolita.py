from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
im=Image.open('assets/file_00000000289881f5a0b01dd5ab44962b.png').convert('RGB')
out=Path('assets/bolita')
out.mkdir(parents=True,exist_ok=True)
specs={
 'cubilete_frontal':((15,30,190,214),[(40,17),(55,10),(86,7),(119,7),(144,13),(155,20),(174,152),(175,166),(168,174),(148,180),(32,180),(10,172),(4,162),(8,147)]),
 'cubilete_inclinado':((380,18,562,214),[(13,44),(27,22),(54,10),(87,2),(105,4),(132,22),(171,141),(178,155),(169,171),(141,184),(76,195),(44,185),(26,168)]),
 'bolita':((40,420,113,493),[(35,2),(50,5),(62,15),(70,31),(69,47),(58,63),(44,70),(27,69),(11,58),(3,43),(4,27),(14,10)]),
 'mesa':((15,502,505,635),[(47,5),(448,5),(485,66),(488,90),(483,101),(466,104),(465,119),(456,128),(438,128),(436,104),(58,104),(57,124),(40,128),(26,126),(24,104),(5,103),(2,92),(4,74)]),
 'cartel_mirar':((557,637,886,742),[(25,4),(300,4),(322,17),(325,85),(311,99),(17,99),(4,85),(4,20)]),
 'cartel_pregunta':((900,638,1231,742),[(22,3),(310,3),(328,19),(329,86),(311,101),(18,101),(3,86),(3,20)]),
}
for name,(bbox,points) in specs.items():
    crop=im.crop(bbox).convert('RGBA')
    mask=Image.new('L',crop.size,0)
    ImageDraw.Draw(mask).polygon(points,fill=255)
    crop.putalpha(mask.filter(ImageFilter.GaussianBlur(.65)))
    crop.save(out/(name+'.png'),optimize=True)
# Compatibilidad con rutas existentes
for old,new in [('cubilete_frontal','cubilete'),('bolita','bolita'),('mesa','mesa')]:
    if old!=new:
        (out/(new+'.png')).write_bytes((out/(old+'.png')).read_bytes())
print('Sprites originales:',[(p.name,p.stat().st_size) for p in out.glob('*.png')])
