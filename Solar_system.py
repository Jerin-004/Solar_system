from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# import numpy as np

#def update():
    # global t
    # t = t + 1
    # angle = np.pi*40/180
    
    # radius = 1
    # n = 0
    # pd = 4
    # mercury.y = np.cos(pd*t+angle*n)*radius
    # mercury.z = np.sin(pd*t+angle*n)*radius    

    # radius = 1.4
    # n = 1
    # pd = 3
    # venus.y = np.cos(pd*t+angle*n)*radius
    # venus.z = np.sin(pd*t+angle*n)*radius
    # venus.x = venus.y*np.sin(angle*n)
    # venus.y = venus.y*np.cos(angle*n)

    # radius = 1.8
    # n = 2
    # pd = 2
    # earth.y = np.cos(pd*t+angle*n)*radius
    # earth.z = np.sin(pd*t+angle*n)*radius  
    # earth.x = earth.y*np.sin(angle*n)    
    # earth.y = earth.y*np.cos(angle*n)

    # radius = 2.2
    # n = 3
    # pd = 1
    # mars.y = np.cos(pd*t+angle*n)*radius
    # mars.z = np.sin(pd*t+angle*n)*radius
    # mars.x = mars.y*np.sin(angle*n)    
    # mars.y = mars.y*np.cos(angle*n)

    # radius = 2.6
    # n = 4
    # pd = 3
    # jupiter.y = np.cos(pd*t+angle*n)*radius
    # jupiter.z = np.sin(pd*t+angle*n)*radius
    # jupiter.x = jupiter.y*np.sin(angle*n)
    # jupiter.y = jupiter.y*np.cos(angle*n)
    
    # radius = 3
    # n = 5
    # pd = 5
    # saturn.y = np.cos(pd*t+angle*n)*radius
    # saturn.z = np.sin(pd*t+angle*n)*radius
    # saturn.x = saturn.y*np.sin(angle*n)        
    # saturn.y = saturn.y*np.cos(angle*n)

    # radius = 3.4
    # n = 6
    # pd = 2
    # uranus.y = np.cos(pd*t+angle*n)*radius
    # uranus.z = np.sin(pd*t+angle*n)*radius
    # uranus.x = uranus.y*np.sin(angle*n)
    # uranus.y = uranus.y*np.cos(angle*n)

    # radius = 3.8
    # n = 7
    # pd = 5
    # neptune.y = np.cos(pd*t+angle*n)*radius
    # neptune.z = np.sin(pd*t+angle*n)*radius 
    # neptune.x = neptune.y*np.sin(angle*n)
    # neptune.y = neptune.y*np.cos(angle*n)

    # radius = 4
    # n = 8
    # pd = 4
    # pluto.y = np.cos(pd*t+angle*n)*radius
    # pluto.z = np.sin(pd*t+angle*n)*radius
    # pluto.x = pluto.y*np.sin(angle*n)    
    # pluto.y = pluto.y*np.cos(angle*n)

app = Ursina()

def update():
    friend.look_at(player, 'back')
    friend.rotation_x = 0

    if held_keys['f']:                              
       camera.position += (0, time.dt, 0)        # move up    
    if held_keys['g']:                               
       camera.position -= (0, time.dt, 0)        # move down



sun = Entity(model='sun', scale=3,position = (7.5,3,10),)
mercury = Entity(model='mercury', scale=0.4,position = (7.5,3,11))
venus = Entity(model='venus', scale=0.6,position = (7.5,3,12))
earth = Entity(model='earth', scale=0.9,position = (7.5,3,14.5))
mars = Entity(model='mars', scale=1.1,position =(7.5,3,18.5))
jupiter = Entity(model='jupiter', scale=2,position =(7.5,3,21.3))
saturn = Entity(model='saturn', scale=2.5,position =(7.5,3,26.9))
uranus = Entity(model='uranus', scale=2,position =(7.5,3,26.4))
neptune = Entity(model='neptun', scale=1.2,position =(7.5,3,22))
pluto = Entity(model='pluto', scale=0.4,position =(7.5,3,23.9))
space_texture = load_texture = ('space.jpg')


window.exit_button.visible = True
window.fps_counter.enabled = False
window.title = 'Solar_system'


class Space(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            scale = 150,
            texture = space_texture,
            double_sided = True
        )

class Voxel(Button):
    def __init__(self, position=(0, 0, 0),):
        super().__init__(
            parent=scene,
            position=position,
            model='block',
            origin_y=0.5,
            color =color.rgba(0,0,200,126),
            scale=0.5)

class Friend(Entity):
    def __init__(self):
        super().__init__(
            model = 'friend',
            scale = 5.7,
            position = (0,1.1,12.5),
        )

for z in range(25):
    for x in range(15):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
player.gravity = 0.1
space = Space()
friend = Friend()
# t = -np.pi
app.run()