
# Mapa de pendientes,sombras y orientación
from arcpy.sa import*
dem= arcpy.sa.Raster(r'C:\Desktop\DEM_HUAURA\DEM.tif')
slope = arcpy.sa.Slope(dem)
aspect = arcpy.sa.Aspect(dem)
hillshade = arcpy.sa.Hillshade(dem) 

#Listar campos de un Feature Class
import arcpy
import arcpy
featureClass = r"C:\Desktop\ZEE\AYACUCHO.gdb\DATOS"
listacampos = arcpy.ListFields(featureClass)
for campo in listacampos:
...     print (field.name)

#Sentencias de Python para trabajar en la calculadora de campos
1.capitalize(): Nos devuelve un texto con la primera letra en mayúsculas.
2• .lower(): Nos devuelve todo el texto en  letra en minúscula.
3• .upper(): Nos devuelve todo el texto en letra en mayúscula.
4• .replace('-', ':'): Nos devuelve una cadena de caracteres en la cual reemplaza la 
el signo guien  “a” por la diagonal “b”.
5.split('#')[0]

#Rellenar campo automáticamente en base a criterios
def rellenar(campo):
    if campo =="I":
        return 'Nivel 1'
    elif campo == "II":
        return 'Nivel 2'
    else:
        'Nivel 3'