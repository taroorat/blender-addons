import bpy
import os

def update(texcoat,tex_type,node):
    
    if (os.path.normpath(texcoat[tex_type][0]) != os.path.normpath(node.image.filepath)):
        tex_found = False

        for image in bpy.data.images:
            if (os.path.normpath(image.filepath) == os.path.normpath(texcoat[tex_type][0])):
                node.image = image
                tex_found = True
                break

        if (tex_found == False):
            node.image = bpy.data.images.load(texcoat[tex_type][0])
