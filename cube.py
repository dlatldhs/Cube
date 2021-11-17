from ursina import *
from ursina import vec3

app = Ursina()

Entiti = Entity()
#오른쪽 면 
cube_slice= Entity(
    parent=Entiti,# 종류???
    model='plane',# 모양
    origin_y=-.5,# size
    texture='white_cube',# 모양 텍스쳐
    color=color.yellow# 색깔
    )

#------큐브-조각-구성-코드------------------------------------
#어디를 보고 있는가 ? look_at  정육각형
# 1 화면 x y z
cube_slice.look_at(Vec3(1,0,0),'up')

# 2 화면 x y z
cube_slice= Entity(parent=Entiti,model='plane',origin_y=-.5,texture='white_cube',color=color.yellow)
cube_slice.look_at(Vec3(-1,0,0),'up') 

# 3 화면 x y z
cube_slice.look_at(Vec3(0,0,1),'up')

# 4 화면 x y z
cube_slice.look_at(Vec3(0,0,-1),'up')

# top and bottom
cube_slice.look_at(Vec3(0,1,0),'up')# top
cube_slice.look_at(Vec3(0,-1,0),'up')# bottom

#카메라(이게 있어야지 볼 수 있음 3차원)
EditorCamera()

app.run()