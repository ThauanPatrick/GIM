import os, glob
from osgeo import gdal, osr, ogr
import numpy
import os
from models import imagens
from django.shortcuts import render
import psycopg2

error = int(0)

def delete_table():
    con = psycopg2.connect(host='localhost', database='gim',
                           user='postgres', password='senha')
    cur = con.cursor()
    sql = "ALTER SEQUENCE public.core_imagens_id_seq RESTART WITH 1;"
    cur.execute(sql)
    sql = 'DELETE FROM public.core_imagens;'
    cur.execute(sql)
    con.commit()
    con.close()


diretorio_principal = '//172.23.5.17/Imagens/spot_sipam/'
diretorio = 'spot/'

def reset(request):

    delete_table()

    def gdal_analise(diretorio, arquivo):

        dataset = gdal.Open(diretorio + arquivo, gdal.GA_ReadOnly)

        try:
            tipo = dataset.GetDriver().LongName

        except AttributeError:

            try:
                tipo = dataset.GetDriver().ShortName
            except AttributeError:
                error += 1

        try:
            projecao = dataset.GetProjection()
        except AttributeError:
            error += 1

        try:
            global geotransform
            geotransform = dataset.GetGeoTransform()
        except AttributeError:
            error += 1

        try:
            tamanho_pixel = geotransform[1]

            band = dataset.GetRasterBand(1)

            tipo_banda = gdal.GetDataTypeName(band.DataType)

            numero_banda = int(dataset.RasterCount)

        except AttributeError:
            error += 1

        try:

            ulx, xres, xskew, uly, yskew, yres = dataset.GetGeoTransform()
            lrx = ulx + (dataset.RasterXSize * xres)
            lry = uly + (dataset.RasterYSize * yres)

            superior_x = int(ulx)
            superior_y = int(uly)
            inferior_x = int(lrx)
            inferior_y = int(lry)

        except AttributeError:
            error += 1


        i = imagens(banda = numero_banda, superior_x = superior_x,
                    superior_y = superior_y, inferior_x = inferior_x, inferior_y = inferior_y,
                    tipo_banda = tipo_banda, projecao = projecao,
                    caminho = diretorio, nome = arquivo, tamanho_pixel = tamanho_pixel, tipo_imagem = tipo)
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

                        try:

                            gdal_analise(diretorio_principal + diretorio, arquivo)

                        except UnicodeDecodeError:
                            global error
                            error += 1

        else:
            print 'arquivo: ' + diretorio_principal + diretorio

    listar(diretorio_principal, diretorio)

    return render(request, 'home.html')
