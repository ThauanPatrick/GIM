import os, glob
from osgeo import gdal, osr, ogr
import numpy
import os
import datetime
from .db import imagens

diretorio_principal = '//172.23.5.17/'
diretorio = 'Imagens/'

from django.shortcuts import render

def listar(diretorio_principal, diretorio):

    global name_file

    if os.path.isdir(diretorio_principal + diretorio):

        os.chdir(diretorio_principal + diretorio)

        for arquivo in glob.glob("*"):

            if os.path.isdir(diretorio_principal + diretorio + arquivo):

                listar(diretorio_principal, diretorio + arquivo + '/')

            else:

                name_file = arquivo.split('.')

                if name_file[-1] == 'tif':

                    gdal_analise(diretorio_principal + diretorio + arquivo)

    else:
        print 'arquivo: ' + diretorio_principal + diretorio

listar(diretorio_principal, diretorio)


def gdalanalise(diretorio):

    dataset = gdal.Open(diretorio, gdal.GA_ReadOnly)

    tipo = dataset.GetDriver().LongName)

    projecao = dataset.GetProjection()

    geotransform = dataset.GetGeoTransform()

    tamanho_pixel = geotransform[1]

    band = dataset.GetRasterBand(1)

    tipo_banda = gdal.GetDataTypeName(band.DataType)

    if band.GetOverviewCount() > 0:
        band_overview = band.GetOverviewCount()

    if band.GetRasterColorTable():
        band_color = band.GetRasterColorTable().GetCount()

    numero_banda = dataset.RasterCount

    ulx, xres, xskew, uly, yskew, yres = dataset.GetGeoTransform()
    lrx = ulx + (dataset.RasterXSize * xres)
    lry = uly + (dataset.RasterYSize * yres)

    superior_x =

    return render(request, 'home.html')