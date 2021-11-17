from ursina import *
from ursina import vec3
from ursina import collider

# 참조 : Ursina 에서 model 중 cube 라는 model이 존재하지만 cube 라는 model은 color를 하나 밖에 못줌;;
# So 우리가 원하는 큐브 모양이 안됨ㅠ --> plane을 줘서 직접 만드는 거임 그럼 색상 다양하게 줄 수 있음
app = Ursina()

Entiti = Entity(enabled=False)# enabled -> 활성화 False 해야 겹치지 않음
#오른쪽 면 
cube_slice= Entity(
    parent=Entiti,# 종류???
    model='plane',# 모양
    origin_y=-.5,# size
    texture='white_cube',# 모양 텍스쳐
    color=color.white# 색깔
    )

#------큐브-조각-구성-코드------------------------------------
#어디를 보고 있는가 ? look_at  정육각형
# 1 화면 x y z
cube_slice.look_at(Vec3(1,0,0),'up')

# 2 화면 x y z 
cube_slice= Entity(parent=Entiti,model='plane',origin_y=-.5,texture='white_cube',color=color.red)
cube_slice.look_at(Vec3(-1,0,0),'up') 

# 3 화면 x y z
cube_slice= Entity(parent=Entiti,model='plane',origin_y=-.5,texture='white_cube',color=color.green)
cube_slice.look_at(Vec3(0,0,1),'up')

# 4 화면 x y z
cube_slice= Entity(parent=Entiti,model='plane',origin_y=-.5,texture='white_cube',color=color.yellow)
cube_slice.look_at(Vec3(0,0,-1),'up')

# top and bottom
cube_slice= Entity(parent=Entiti,model='plane',origin_y=-.5,texture='white_cube',color=color.blue)
cube_slice.look_at(Vec3(0,1,0),'up')# top
cube_slice= Entity(parent=Entiti,model='plane',origin_y=-.5,texture='white_cube',color=color.pink)
cube_slice.look_at(Vec3(0,-1,0),'up')# bottom

Entiti.combine()# 위에 부모를 Entiti로 잡아줬는데 이걸 다 묶어주는 역할 -> 큐브 조각 한개

cubelist=[]
for x in range(3):
    for y in range(3):
        for z in range(3):#duplicate = 복사 Vec3(xyz)-Vec3(111) 해줘서 전부 사용자가 돌릴 때 중앙에서 돌아가게끔 보이게 하는거
            e = duplicate(Entiti,position=Vec3(x,y,z)-Vec3(1,1,1),texture = "white_cube")
            cubelist.append(e)# append -> python list에서 추가해주는 함수

# 카메라(이게 있어야지 볼 수 있음 3차원)
EditorCamera()

# 충돌 객체
collider = Entity(model='cube',scale=3,collider=,box)
app.run()