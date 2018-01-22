import os, glob
from osgeo import gdal, osr, ogr
import numpy
import os
import datetime
from models import imagens
from django.shortcuts import render

diretorio_principal = '//172.23.5.17/'
diretorio = 'Imagens/'

def home(request):

    def gdal_analise(diretorio, arquivo):

        dataset = gdal.Open(diretorio + arquivo, gdal.GA_ReadOnly)

#        tipo = dataset.GetDriver().LongName()

        projecao = dataset.GetProjection()

        geotransform = dataset.GetGeoTransform()

        band = dataset.GetRasterBand(1)

        tipo_banda = gdal.GetDataTypeName(band.DataType)

        if band.GetOverviewCount() > 0:
            band_overview = band.GetOverviewCount()

        if band.GetRasterColorTable():
            band_color = band.GetRasterColorTable().GetCount()

        numero_banda = int(dataset.RasterCount)

        ulx, xres, xskew, uly, yskew, yres = dataset.GetGeoTransform()
        lrx = ulx + (dataset.RasterXSize * xres)
        lry = uly + (dataset.RasterYSize * yres)

        superior_x = int(ulx)
        superior_y = int(uly)
        inferior_x = int(lrx)
        inferior_y = int(lry)

        i = imagens(banda = numero_banda, superior_x = superior_x,
                    superior_y = superior_y, inferior_x = inferior_x, inferior_y = inferior_y,
                    tipo_banda = tipo_banda, projecao = projecao,
                    caminho = diretorio, nome = arquivo)
        i.save()


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

                        gdal_analise(diretorio_principal + diretorio, arquivo)

        else:
            print 'arquivo: ' + diretorio_principal + diretorio

    listar(diretorio_principal, diretorio)

    return render(request, 'home.html')
