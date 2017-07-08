# -*- coding: utf-8 -*-
#author:shaodonghang
#date:2017-1-12
import tartes
from tartes import ssa
import numpy as np
import codecs
from scipy import integrate
# x=312
# y=integrate.quad(x, 1, 3)
# print 'y=',y
resultfilepath="H:/2016-6-8/albedo.txt"
savefile=codecs.open(resultfilepath,"w","utf-8")
# ssa = 20      # in m^2/kg
density = 300 # in kg/m^3
# the result should be independent of the density for a semi-infinite medium
r_opt= 5.0059E-04
# in m  optical radius (m)4.15:4.14E-04 4.16:1.14E-03 4.17:3.12E-04 4.18:5.17E-04
# wavelength = 850e-9 # in m
solar_zenith_angle= np.loadtxt('H:/2016-6-8/solar_zenith_angle.txt')
nameList = ['645e-9','858e-9','469e-9','1240e-9','2130e-9']
for m in range(len(nameList)):
    waveleng=nameList[m]
    print waveleng
    wavelength =float(waveleng)
    # solar_zenith_angle= np.loadtxt('H:/2016-6-8/solar_zenith_angle.txt')
    # solar_zenith_angle= np.loadtxt('H:/2016-6-8/Solar_elevation_angle.txt')
    print 'solar_zenith_angle=',solar_zenith_angle
    # solar_zenith_angle1=np.arry(solar_zenith_angle1)
    # solar_zenith_angle=90-solar_zenith_angle1
    # solar_zenith_angle =68.02
    for i in range(len(solar_zenith_angle)):
        angle=solar_zenith_angle[i]
        albedo = tartes.albedo(wavelength,ssa(r_opt),density,dir_frac=0.7,theta_inc=angle)
        # albedo=[]
        # albedo=np.arry(albedo)
        print 'albedo=',albedo
        # print(albedo)
        savefile.writelines(str(albedo)+"\n")
        # np.savetxt('H:/2016-6-8/albedo.txt',str(albedo),fmt='%1.4e')
    # solar_zenith_angle.close()
print 'end'