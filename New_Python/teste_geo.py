from osgeo import gdal, osr, ogr
import numpy
import os
import datetime

dire = '//172.23.5.17/Imagens/sar/Terra_do_Meio_Oeste_2006/sar_tm_02_w_geral_retif_cut_mat.tif'
dataset = gdal.Open(dire, gdal.GA_ReadOnly)

print("Driver: {}/{}".format(dataset.GetDriver().ShortName, dataset.GetDriver().LongName))
print("Projecao: {}".format(dataset.GetProjection()))
geotransform = dataset.GetGeoTransform()

print("Tamanho do pixel = ({}, {})".format(geotransform[1], geotransform[5]))

band = dataset.GetRasterBand(1)
print("Tipo de banda={}".format(gdal.GetDataTypeName(band.DataType)))

if band.GetOverviewCount() > 0:
    print("Banda tem {} overviews".format(band.GetOverviewCount()))

if band.GetRasterColorTable():
    print("Band has a color table with {} entries".format(band.GetRasterColorTable().GetCount()))

bands = dataset.RasterCount

print "Numero de bandas: " + str(bands)

ulx, xres, xskew, uly, yskew, yres  = dataset.GetGeoTransform()
lrx = ulx + (dataset.RasterXSize * xres)
lry = uly + (dataset.RasterYSize * yres)

print("Coordenadas {} {} {} {}".format(ulx, lry, uly, lrx))
