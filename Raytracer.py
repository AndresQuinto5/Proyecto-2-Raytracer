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

    EscritorioMAt = Material(texture = Texture('./Utils/madera22.bmp'))
    Mantel = Material(texture = Texture('./Utils/mantel.bmp'))
    GoldLampMaterial = Material(texture = Texture('./Utils/lamp.bmp'))

    DiscoBall = Material(texture = Texture('./Utils/discob.bmp'))

    speakers = Material(texture = Texture('./Utils/bass2.bmp'))
    MaterialPared = Material(texture = Texture('./Utils/pared.bmp'))


    width = 1920
    height = 1080
    r = Raytracer(width,height)
    r.glClearColor(0.2, 0.6, 0.8)
    r.glClear()

    r.envmap = Envmap('./Utils/dark.bmp')


    # Lights
    r.pointLights.append( PointLight(position = V3(-3, -1.225, -10), intensity = 0.25)) # util
    r.pointLights.append( PointLight(position = V3(-3, -1.225, -11), intensity = 0.07)) # Window Efect
    r.ambientLight = AmbientLight(strength = 0.35)

    # Desk
    r.scene.append( AABB(V3(0, -3, -10), V3(10, 0.1, 5) , EscritorioMAt, 'box' ) )
    r.scene.append( AABB(V3(0, -2.9, -10), V3(9, 0.08, 4) , Mantel, 'box' ) )
    r.scene.append( AABB(V3(-5, -5.45, -10), V3(0.1, 5, 5) , EscritorioMAt, 'box' ) )
    r.scene.append( AABB(V3(5, -5.45, -10), V3(0.1, 5, 5) , EscritorioMAt, 'box' ) )

    # util
    r.scene.append( AABB(V3(-5.75, -1.75, -10), V3(1.5, 3.5, 1.25) , GoldLampMaterial, 'box' ) )
    r.scene.append( AABB(V3(-5.75, -1, -10), V3(2.75, 1.25, 1.25) , GoldLampMaterial, 'box' ) )
    r.scene.append( AABB(V3(-5, -1.2, -10), V3(1, 0.2, 1) , GoldLampMaterial, 'lamp' ) )
    
    # Ball
    r.scene.append( Sphere(V3( 0, 3.75, -10), 1, DiscoBall))

    #speakers
    r.scene.append( AABB(V3(3, -2, -10), V3(1, 0.85, 1.5) , speakers, 'box' ) )
    r.scene.append( AABB(V3(4, -2, -10), V3(1, 0.85, 1.5) , speakers, 'box' ) )
    r.scene.append( AABB(V3(3, -1.5, -10), V3(1, 0.85, 1.5) , speakers, 'box' ) )
    r.scene.append( AABB(V3(4, -1.5, -10), V3(1, 0.85, 1.5) , speakers, 'box' ) )
  
    # Room
    r.scene.append( AABB(V3(0,0,-12), V3(15,10,10), MaterialPared, 'room') )
    r.scene.append( AABB(V3(-5.58,0,-17), V3(3.75,10,0.2), MaterialPared, 'box') )
    r.scene.append( AABB(V3(5.58,0,-17), V3(3.75,10,0.2), MaterialPared, 'box') )
    r.scene.append( AABB(V3(0,-3.5,-17), V3(7.30,3,0.2), MaterialPared, 'box') )
    r.scene.append( AABB(V3(0,1.5,-17), V3(7.30,7,0.2), glass, 'box') ) # Window

    r.rtRender()

    r.glFinish('out.bmp')