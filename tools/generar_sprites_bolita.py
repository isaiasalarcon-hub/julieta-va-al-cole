from PIL import Image
from pathlib import Path
import cv2
import numpy as np
src=Path('assets/file_00000000289881f5a0b01dd5ab44962b.png')
im=Image.open(src).convert('RGB')
print('Atlas:',im.size)
if im.size!=(1536,768):
    im=im.resize((1536,768),Image.Resampling.LANCZOS)
out=Path('assets/bolita');out.mkdir(exist_ok=True,parents=True)
# Los cuadros de fondo son grises, mientras los sprites originales son saturados.
# Se identifica el objeto mediante la mayor componente conexa y se amplía
# ligeramente la máscara para incluir el contorno negro, sin arrastrar el damero.
regions={
 'cubilete_frontal':(15,28,195,215),
 'cubilete_inclinado':(380,18,562,214),
 'bolita':(37,419,116,494),
 'mesa':(15,500,510,637),
 'cartel_mirar':(557,637,886,742),
 'cartel_pregunta':(900,638,1231,742)
}
for name,(x1,y1,x2,y2) in regions.items():
    rgb=np.array(im.crop((x1,y1,x2,y2)))
    hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV)
    saturated=(hsv[:,:,1]>55).astype(np.uint8)
    n,labels,stats,centroids=cv2.connectedComponentsWithStats(saturated,8)
    if n<2:raise ValueError('No se encontró sprite: '+name)
    idx=1+np.argmax(stats[1:,cv2.CC_STAT_AREA])
    mask=(labels==idx).astype(np.uint8)*255
    # Cerrar huecos interiores del objeto, preservar la forma exterior.
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    solid=np.zeros_like(mask)
    cv2.drawContours(solid,contours,-1,255,cv2.FILLED)
    solid=cv2.dilate(solid,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
    solid=cv2.GaussianBlur(solid,(3,3),.65)
    rgba=np.dstack((rgb,solid))
    ys,xs=np.where(solid>4)
    pad=2
    left=max(0,int(xs.min())-pad);right=min(rgb.shape[1],int(xs.max())+pad+1)
    top=max(0,int(ys.min())-pad);bottom=min(rgb.shape[0],int(ys.max())+pad+1)
    Image.fromarray(rgba[top:bottom,left:right]).save(out/(name+'.png'),optimize=True)
    print(name, 'sprite',right-left,bottom-top)
(out/'cubilete.png').write_bytes((out/'cubilete_frontal.png').read_bytes())

# Regenerar sprites originales limpios.
