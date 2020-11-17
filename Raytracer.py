from gl import *
from texture import Texture
from obj import ObjReader
from envmap import Envmap
from sphere import *

if __name__ == '__main__':
    brick = Material(diffuse = color(0.8, 0.25, 0.25 ), spec = 16)
    stone = Material(diffuse = color(0.4, 0.4, 0.4 ), spec = 32)
    mirror = Material(spec = 64, matType = REFLECTIVE)
    glass = Material(spec = 64, ior = 1.5, matType= TRANSPARENT) 

    deskMat = Material(texture = Texture('./Utils/wood2.bmp'))
    woodMat_4 = Material(texture = Texture('./Utils/wood4.bmp'))
    woodMat_4_1 = Material(texture = Texture('./Utils/wood4-1.bmp'))

    earthMat = Material(texture = Texture('./Utils/earthDay.bmp'))
    jupiterMat = Material(texture = Texture('./Utils/2k_jupiter.bmp'))
    moonMat = Material(texture = Texture('./Utils/2k_moon.bmp'))
    sunMat = Material(texture = Texture('./Utils/2k_sun.bmp'))

    bookMat = Material(texture = Texture('./Utils/book1-1.bmp'))
    concretewallMat = Material(texture = Texture('./Utils/concretewall.bmp'))
    bookMat_2 = Material(texture = Texture('./Utils/book2-1.bmp'))
    bookMat_3 = Material(texture = Texture('./Utils/book3.bmp'))
    bookMat_4 = Material(texture = Texture('./Utils/book4.bmp'))


    width = 1920
    height = 1080
    r = Raytracer(width,height)
    r.glClearColor(0.2, 0.6, 0.8)
    r.glClear()

    r.envmap = Envmap('./Utils/intothewoods.bmp')

    # Lights
    r.pointLights.append( PointLight(position = V3(-3, -1.225, -10), intensity = 0.25)) # Lamp
    r.pointLights.append( PointLight(position = V3(-3, -1.225, -11), intensity = 0.07)) # Window Efect
    r.ambientLight = AmbientLight(strength = 0.35)

    # Desk
    r.scene.append( AABB(V3(0, -3, -10), V3(10, 0.1, 5) , deskMat, 'box' ) )
    r.scene.append( AABB(V3(-5, -5.45, -10), V3(0.1, 5, 5) , deskMat, 'box' ) )
    r.scene.append( AABB(V3(5, -5.45, -10), V3(0.1, 5, 5) , deskMat, 'box' ) )

    # Lamp
    r.scene.append( AABB(V3(-4.75, -1.75, -10), V3(0.5, 2.5, 0.25) , woodMat_4, 'box' ) )
    r.scene.append( AABB(V3(-3.75, -1, -10), V3(1.75, 0.25, 0.25) , woodMat_4_1, 'box' ) )
    r.scene.append( AABB(V3(-3, -1.2, -10), V3(1, 0.2, 1) , woodMat_4_1, 'lamp' ) )


    # # Box of balls
    r.scene.append( AABB(V3(-3, -2.75, -10), V3(1.5, 1, 1) , glass, 'basket' ) )
    
    # # Balls
    r.scene.append( Sphere(V3( -3, -2.75, -10), 0.1, earthMat))
    r.scene.append( Sphere(V3( -3.25, -2.75, -9.80), 0.1, jupiterMat))
    r.scene.append( Sphere(V3( -2.75, -2.75, -9.80), 0.1, moonMat))
    r.scene.append( Sphere(V3( -3.25, -2.65, -9.90), 0.1, sunMat))

    # # Books
    r.scene.append( AABB(V3(3, -2, -10), V3(0.45, 1.75, 1.5) , bookMat, 'box' ) )
    r.scene.append( AABB(V3(3.5, -2, -10), V3(0.45, 1.75, 1.5) , bookMat_2, 'box' ) )
    r.scene.append( AABB(V3(4, -2, -10), V3(0.45, 1.75, 1.5) , bookMat_3, 'box' ) )
    r.scene.append( AABB(V3(4.5, -2, -10), V3(0.45, 1.75, 1.5) , bookMat_4, 'box' ) )

    # Room
    r.scene.append( AABB(V3(0,0,-12), V3(15,10,10), concretewallMat, 'room') )
    r.scene.append( AABB(V3(-5.58,0,-17), V3(3.75,10,0.2), concretewallMat, 'box') )
    r.scene.append( AABB(V3(5.58,0,-17), V3(3.75,10,0.2), concretewallMat, 'box') )
    r.scene.append( AABB(V3(0,-3.5,-17), V3(7.30,3,0.2), concretewallMat, 'box') )
    r.scene.append( AABB(V3(0,1.5,-17), V3(7.30,7,0.2), glass, 'box') ) # Window

    r.rtRender()

    r.glFinish('output.bmp')