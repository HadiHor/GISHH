'''
Created on May 18, 2009
** 3D development 
@author: Hadi
'''
from scripting import *

# get a CityEngine instance
ce = CE()


def writeCGAlib():
    # open the cga file to be written
    cga = "/*Asset Library Loader : Generated by asset_lib.py*/\n version \"2012.1\"\n\n"
    
    # write start rule
    cga += "Lot -->  Geometries Textures"
    
    
    # write rule showing geometries
    cga += "\n\nGeometries --> "
    
    # get all .obj files from asset directory, and call their loader
    for obj in ce.getObjectsFrom("/", ce.isFile, ce.withName("/Tutorial_10*/assets/*.obj")):    
        # and write 
        cga += "\n\t t(2,0,0)  Geometry(\""+obj+"\")"
        print obj
    
    
    # write rule showing jpg textures
    cga += "\n\nTextures --> \n\ts(1,0,0) set(scope.tz,0) set(scope.ty,3) i(\"facades/xy-plane.obj\")"    
    
    # get all .jpg files from asset directory, and call their loader
    for jpg in ce.getObjectsFrom("/", ce.isFile, ce.withName("/Tutorial_10*/assets/*.jpg")):
        cga += "\n\tt(2,0,0)  Texture(\""+jpg+"\")"
        
    
    
    #write geometry loader rule
    cga += "\n\n Geometry(asset) --> s(1,0,0) i(asset) set(scope.ty,0) set(scope.tz,0)"
    
    #write texture loader rule
    cga += "\n\n Texture(asset) --> set(material.colormap, asset)"
    
    
    cgafile = ce.toFSPath("rules/asset_lib2.cga")
    CGA = open(cgafile, "w")
    CGA.write(cga)
    CGA.close()
    print "written file "+cgafile
        

def assignAndGenerateLib():
    object = ce.getObjectsFrom(ce.scene, ce.withName("'Lot2'"))
    ce.refreshWorkspace()
    ce.setRuleFile(object, "asset_lib2.cga")
    ce.generateModels(object)
    
if __name__ == '__main__':
    writeCGAlib()
    assignAndGenerateLib() 

