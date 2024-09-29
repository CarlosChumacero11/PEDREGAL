import os
import cloudinary

import cloudinary.uploader 
from cloudinary.utils import cloudinary_url

# Configuracion de cloudinary
cloudinary.config(
    cloud_name = "ddheiqd5o",
    api_key="673638328592327",
    api_secret="z2-4i4oq0xL_t0PTM1xON_6UB0I",
    secure=True
)

ruta_imagenes="D:/5000orig"

archivos = os.listdir(ruta_imagenes)


def subirImagenaCloudinaryaCarpetaPedregal(imagen, idPublic):
    resultado_subida = cloudinary.uploader.upload(imagen,
                                      public_id=idPublic,
                                      folder="FolderP")
    return resultado_subida["secure_url"]

def subirImagenes():
    for imagen in archivos:
        imagen_separada = imagen.split(".")
        if imagen_separada[-1] == "tif" :
            nombreImagen = imagen_separada[0]
            ruta_imagen = ruta_imagenes+"/"+imagen
            imagen_segura = subirImagenaCloudinaryaCarpetaPedregal(ruta_imagen, nombreImagen)
            print(imagen_segura)
            


subirImagenes()