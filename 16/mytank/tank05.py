"""
v1.0
    完成类的创建
    实现游戏窗口的加载
"""

import pygame
from pygame.sprite import Sprite
import sys
import time
import random
import numpy
import math
import matplotlib.pyplot as plt

# 窗口宽度
WINDOW_WIDTH = 810
# 窗口高度
WINDOW_HEIGHT = 510

COLOR_WHITE = pygame.color.Color('white')
COLOR_GREEN = pygame.color.Color('#000000')


# 定义一个精灵类
class BaseItem(Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

# 坦克父类
class BaseTank(BaseItem):
    # 定义类属性，所有坦克对象高和宽都是一样
    width = 30
    height = 30

    def __init__(self, left, top):
        self.direction = 'U'  # 坦克的方向默认向上
        # 存放图片的字典
        self.images = {
            'U': pygame.image.load('tank_img/p1tankU.gif'),
            'D': pygame.image.load('tank_img/p1tankD.gif'),
            'L': pygame.image.load('tank_img/p1tankL.gif'),
            'R': pygame.image.load('tank_img/p1tankR.gif')
        }
        self.image = self.images[self.direction]  # 坦克的图片由方向决定
        self.speed = 4  # 坦克的速度
        self.rect = self.image.get_rect()
        # 设置放置的位置
        self.rect.left = left
        self.rect.top = top
        self.stop = True  # 坦克是否停止
        self.live = True  # 决定坦克是否消灭了
        self.hg = 100
        self.n=0
        # 保持原来的位置
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    # 敌方坦克的移动
    def move(self):
        # 保持原来的状态
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
        # 判断坦克的移动方向
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < WINDOW_HEIGHT:
                self.rect.top += self.speed
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left+self.rect.height < WINDOW_WIDTH:
                self.rect.left += self.speed




     #我方坦克移动
    def moveM(self):
        # 保持原来的状态
        self.oldLeft= self.rect.left
        self.oldTop = self.rect.top
        # 判断坦克的移动方向
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < WINDOW_HEIGHT:
                self.rect.top += self.speed
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < WINDOW_WIDTH:
                self.rect.left += self.speed



    # 加载坦克
    def displayTank(self):
        self.image = self.images[self.direction]
        MainGame.window.blit(self.image, self.rect) #绘制图像到窗口

    # 撞墙处理
    def hitWall(self):
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(wall, self):      #判断精灵类重叠
                self.stay()

        for wallx in MainGame.wallListx:
            if pygame.sprite.collide_rect(wallx, self):
                self.stay()
        for wally in MainGame.wallListy:
            if pygame.sprite.collide_rect(wally, self):
                self.stay()
        for wallz in MainGame.wallListz:
            if pygame.sprite.collide_rect(wallz, self):
                self.stay()

        for jcqa in MainGame.jcq1List:
            if pygame.sprite.collide_rect(jcqa, self):
                if MainGame.o == 0:  #惩罚
                    self.stay()
                if MainGame.o == 1:  #加弹
                    MainGame.my_tank.n = 1   #n为一,开始打
                if MainGame.o == 2:  #加血
                    if MainGame.my_tank.hg <= 99:
                        MainGame.my_tank.hg += 0.5
                    else:
                        MainGame.my_tank.hg = 100

        for jcqb in MainGame.jcq2List:
            if pygame.sprite.collide_rect(jcqb, self):
                if MainGame.i == 0:  # 惩罚
                        self.stay()
                if MainGame.i == 1:  # 加弹
                        MainGame.my_tank.n = 1  # n为一,开始打
                if MainGame.i == 2:  # 加血
                    if MainGame.my_tank.hg <= 99:
                        MainGame.my_tank.hg += 0.5
                    else:
                        MainGame.my_tank.hg = 100

        for jcqc in MainGame.jcq3List:
            if pygame.sprite.collide_rect(jcqc, self):
                if MainGame.u == 0:  # 惩罚
                    self.stay()
                if MainGame.u == 1:  # 加弹
                    MainGame.my_tank.n = 1  # n为一,开始打
                if MainGame.u == 2:
                    if MainGame.my_tank.hg <= 99:
                        MainGame.my_tank.hg += 0.5
                    else:
                        MainGame.my_tank.hg = 100

        for jcqd in MainGame.jcq11List:
         for enemyTank in MainGame.EnemyTankList:
            if pygame.sprite.collide_rect(jcqd, self):
                if MainGame.o == 0:  # 惩罚
                    self.stay()
                if MainGame.o == 1:  # 加弹
                    enemyTank.h = 1  # n为一,开始打
                if MainGame.o == 2:  # 加血
                    if enemyTank.hg <= 99:
                        enemyTank.hg += 0.5
                    else:
                        enemyTank.hg = 100
            else:
               enemyTank.n = 0
        for jcqe in MainGame.jcq22List:
         for enemyTank in MainGame.EnemyTankList:
            if pygame.sprite.collide_rect(jcqe, self):
                    if MainGame.i == 0:  # 惩罚
                        self.stay()
                    if MainGame.i == 1:  # 加弹
                        enemyTank.h = 1  # n为一,开始打
                    if MainGame.i == 2:  # 加血
                        if enemyTank.hg <= 99:
                            enemyTank.hg += 0.5
                        else:
                            enemyTank.hg = 100

            else:
                enemyTank.n = 0
        for jcqf in MainGame.jcq33List:
         for enemyTank in MainGame.EnemyTankList:
            if pygame.sprite.collide_rect(jcqf, self):
                    if MainGame.u == 0:  # 惩罚
                            self.stay()
                    if MainGame.u == 1:  # 加弹
                        enemyTank.h = 1  # n为一,开始打
                    if MainGame.u == 2:  # 加血
                        if enemyTank.hg <= 99:
                            enemyTank.hg += 0.5
                        else:
                            enemyTank.hg = 100

            else:
                enemyTank.n = 0
    # 处理位置不变
    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop


# 我方坦克
class HeroTank(BaseTank):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.kx=20


    def myTank_hit_enemyTank(self):
        for enemyTank in MainGame.EnemyTankList:
            if pygame.sprite.collide_rect(enemyTank, self):
                self.stay()

    def shotM(self):
        if MainGame.my_tank.n == 2 :
                  num = 1
                  if num < 4:
                   return Bullet(self)
# 敌方坦克
class EnemyTank(BaseTank):
    def __init__(self, left, top, speed):
        super(EnemyTank, self).__init__(left, top)
        self.images = {
            'U': pygame.image.load('tank_img/enemy1U.gif'),
            'D': pygame.image.load('tank_img/enemy1D.gif'),
            'L': pygame.image.load('tank_img/enemy1L.gif'),
            'R': pygame.image.load('tank_img/enemy1R.gif')
        }

        self.direction = self.RandomDirection()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.step = 60
        self.enemy_flag = False
        self.hg=100
        self.h=0
        self.kx2=20

    # 坦克出生随机方向
    def RandomDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        else:
            return 'R'

    # 坦克随机移动
    def randomMove(self):
        if self.step < 0:
            self.direction = self.RandomDirection()
            self.step = 60
        else:
            self.move()
            self.step -= 1

    # 坦克射击
    def shot(self):
       for enemyTank in MainGame.EnemyTankList:
        if enemyTank.h==1:
         num = random.randint(1, 100)
         if num < 4:
             return Bullet(self)

    # 敌方坦克碰撞我方坦克
    def enemyTank_hit_MyTank(self):
        for enemy in MainGame.EnemyTankList:
            if MainGame.my_tank and MainGame.my_tank.live:
                if pygame.sprite.collide_rect(MainGame.my_tank, enemy):
                    self.stay()


# 子弹类
class Bullet(BaseItem):
    def __init__(self, tank):
        self.image = pygame.image.load('tank_img/QQ图片20191203224638.jpg')
        self.direction = tank.direction
        self.rect = self.image.get_rect()
        # 根据坦克方向，生成子弹位置
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.width / 2

        # 子弹的速度
        self.speed = 9
        # 子弹状态
        self.live = True

    # 加载子弹
    def displayBullet(self):
        MainGame.window.blit(self.image, self.rect)

    # 子弹的移动
    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < WINDOW_WIDTH:
                self.rect.left += self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < WINDOW_HEIGHT:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        self.speed -= 0.02
        if self.speed < 8:
         self.live = False


    # 我方子弹击中敌方坦克
    def myBullet_hit_enemy(self):
        for enemytank in MainGame.EnemyTankList:
            if pygame.sprite.collide_rect(enemytank, self):
                self.live = False
                MainGame.kb = 1
                if enemytank.hg <= 0:
                    enemytank.live = False

                    # 创建爆炸对象
                    explode = Explode(enemytank)
                    MainGame.explodeList.append(explode)
                    print('we win')
                else:
                    enemytank.hg -= 5
                    enemytank.kx2-= 1

    # 敌方坦克击中我方坦克
    def enemyBullet_hit_myTank(self):
        if MainGame.my_tank and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(MainGame.my_tank, self):
                 self.live = False
                 MainGame.kb=-10
                 if MainGame.my_tank.hg <= 0:
                      MainGame.my_tank.live = False

                      # 创建爆炸对象
                      explode = Explode(MainGame.my_tank)
                      MainGame.explodeList.append(explode)
                      print('we lose')
                 else:
                     MainGame.my_tank.hg -= 5
                     MainGame.my_tank.kx -= 1

    # 射击墙壁
    def wall_bullet(self):
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(wall, self):
                wall.hg -= 1
                self.live = False
                if wall.hg <= 0:
                    wall.live = False
        for wallx in MainGame.wallListx:
            if pygame.sprite.collide_rect(wallx, self):
                wallx.hg -= 1
                self.live = False
                if wallx.hg <= 0:
                    wallx.live = False
        for wally in MainGame.wallListy:
            if pygame.sprite.collide_rect(wally, self):
                wally.hg -= 1
                self.live = False
                if wally.hg <= 0:
                    wally.live = False
        for wallz in MainGame.wallListz:
            if pygame.sprite.collide_rect(wallz, self):
                wallz.hg -= 1
                self.live = False
                if wallz.hg <= 0:
                    wallz.live = False


# 墙壁类
class Wall:
    def __init__(self, left, top):
        self.image = pygame.image.load('tank_img/walls(1).gif')

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.live = True
        self.hg = 100000000000000
    def displayWall(self):
        if self.live:
             MainGame.window.blit(self.image, self.rect)

class Wallx:
    def __init__(self, leftx, topx):
          self.image = pygame.image.load('tank_img/walls.gif')
          self.rect = self.image.get_rect()
          self.rect.left = leftx
          self.rect.top = topx
          self.live = True
          self.hg = 100000000000000

    def displayWallx(self):
        if self.live:
              MainGame.window.blit(self.image, self.rect)

class Wally:
    def __init__(self, lefty, topy):
        self.image = pygame.image.load('tank_img/wall.gif')
        self.rect = self.image.get_rect()
        self.rect.left = lefty
        self.rect.top = topy
        self.live = True
        self.hg = 100000000000000

    def displayWally(self):
        if self.live:
              MainGame.window.blit(self.image, self.rect)

class Wallz:
    def __init__(self, leftz, topz):
        self.image = pygame.image.load('tank_img/wall(1).gif')
        self.rect = self.image.get_rect()
        self.rect.left = leftz
        self.rect.top = topz
        self.live = True
        self.hg = 100000000000000

    def displayWallz(self):
        if self.live:
            MainGame.window.blit(self.image, self.rect)

#加成，惩罚区
class jcq1:
    def __init__(self, lefta, topa):
        self.images = {
            0:pygame.image.load('tank_img/jcq1.gif'),
            1:pygame.image.load('tank_img/jcq2.gif'),
            2:pygame.image.load('tank_img/jcq3.gif')
        }
        self.image=self.images[MainGame.o]
        self.rect = self.image.get_rect()
        self.rect.left = lefta
        self.rect.top = topa
        self.live = True
        self.hg = 100000000000000

    def displayjcq1(self):
        if self.live:
            MainGame.window.blit(self.image, self.rect)

class jcq2:
    def __init__(self, leftb, topb):
        self.images = {
            0: pygame.image.load('tank_img/jcq1.gif'),
            1: pygame.image.load('tank_img/jcq2.gif'),
            2: pygame.image.load('tank_img/jcq3.gif')
        }
        self.image = self.images[MainGame.i]
        self.rect = self.image.get_rect()
        self.rect.left = leftb
        self.rect.top = topb
        self.live = True
        self.hg = 100000000000000

    def displayjcq2(self):
        if self.live:
            MainGame.window.blit(self.image, self.rect)

class jcq3:
    def __init__(self, leftc, topc):
        self.images = {
            0: pygame.image.load('tank_img/jcq1.gif'),
            1: pygame.image.load('tank_img/jcq2.gif'),
            2: pygame.image.load('tank_img/jcq3.gif')
        }
        self.image = self.images[MainGame.u]
        self.rect = self.image.get_rect()
        self.rect.left = leftc
        self.rect.top = topc
        self.live = True
        self.hg = 100000000000000

    def displayjcq3(self):
        if self.live:
            MainGame.window.blit(self.image, self.rect)

class jcq11:
    def __init__(self, leftz, topz):
        self.images = {
            0: pygame.image.load('tank_img/jcq11.gif'),
            1: pygame.image.load('tank_img/jcq22.gif'),
            2: pygame.image.load('tank_img/jcq33.gif')
        }
        self.image = self.images[MainGame.o]
        self.rect = self.image.get_rect()
        self.rect.left = leftz
        self.rect.top = topz
        self.live = True
        self.hg = 100000000000000

    def displayjcq11(self):
        if self.live:
            MainGame.window.blit(self.image, self.rect)

class jcq22:
    def __init__(self, leftz, topz):
        self.images = {
            0: pygame.image.load('tank_img/jcq11.gif'),
            1: pygame.image.load('tank_img/jcq22.gif'),
            2: pygame.image.load('tank_img/jcq33.gif')
        }
        self.image = self.images[MainGame.i]
        self.rect = self.image.get_rect()
        self.rect.left = leftz
        self.rect.top = topz
        self.live = True
        self.hg = 100000000000000

    def displayjcq22(self):
        if self.live:
            MainGame.window.blit(self.image, self.rect)

class jcq33:
    def __init__(self, leftz, topz):
        self.images = {
            0: pygame.image.load('tank_img/jcq11.gif'),
            1: pygame.image.load('tank_img/jcq22.gif'),
            2: pygame.image.load('tank_img/jcq33.gif')
        }
        self.image = self.images[MainGame.u]
        self.rect = self.image.get_rect()
        self.rect.left = leftz
        self.rect.top = topz
        self.live = True
        self.hg = 100000000000000

    def displayjcq33(self):
        if self.live:
            MainGame.window.blit(self.image, self.rect)
#血条
class xue:
    def __init__(self, leftl, topl):
        self.images = {
            1: pygame.image.load('tank_img/M1.jpg'),
            2: pygame.image.load('tank_img/M2.jpg'),
            3: pygame.image.load('tank_img/M3.jpg'),
            4: pygame.image.load('tank_img/M4.jpg'),
            5: pygame.image.load('tank_img/M5.jpg'),
            6: pygame.image.load('tank_img/M6.jpg'),
            7: pygame.image.load('tank_img/M7.jpg'),
            8: pygame.image.load('tank_img/M8.jpg'),
            9: pygame.image.load('tank_img/M9.jpg'),
            10: pygame.image.load('tank_img/M10.jpg'),
            11: pygame.image.load('tank_img/M11.jpg'),
            12: pygame.image.load('tank_img/M12.jpg'),
            13: pygame.image.load('tank_img/M13.jpg'),
            14: pygame.image.load('tank_img/M14.jpg'),
            15: pygame.image.load('tank_img/M15.jpg'),
            16: pygame.image.load('tank_img/M16.jpg'),
            17: pygame.image.load('tank_img/M17.jpg'),
            18: pygame.image.load('tank_img/M18.jpg'),
            19: pygame.image.load('tank_img/M19.jpg'),
            20: pygame.image.load('tank_img/M20.jpg')
        }
        self.image = self.images[MainGame.my_tank.kx]
        self.rect = self.image.get_rect()
        self.live =True
        self.rect.left = leftl
        self.rect.top = topl
        self.hg = 100000000000000

    def displayxl(self):
        if self.live and MainGame.my_tank.hg>0:
            self.image = self.images[MainGame.my_tank.kx]
            MainGame.window.blit(self.image, self.rect)
        else:
            game = MainGame()
            game.start_game()
class xue2:
    def __init__(self, leftl, topl):
        self.images = {
                        1: pygame.image.load('tank_img/M1.jpg'),
                        2: pygame.image.load('tank_img/M2.jpg'),
                        3: pygame.image.load('tank_img/M3.jpg'),
                        4: pygame.image.load('tank_img/M4.jpg'),
                        5: pygame.image.load('tank_img/M5.jpg'),
                        6: pygame.image.load('tank_img/M6.jpg'),
                        7: pygame.image.load('tank_img/M7.jpg'),
                        8: pygame.image.load('tank_img/M8.jpg'),
                        9: pygame.image.load('tank_img/M9.jpg'),
                        10: pygame.image.load('tank_img/M10.jpg'),
                        11: pygame.image.load('tank_img/M11.jpg'),
                        12: pygame.image.load('tank_img/M12.jpg'),
                        13: pygame.image.load('tank_img/M13.jpg'),
                        14: pygame.image.load('tank_img/M14.jpg'),
                        15: pygame.image.load('tank_img/M15.jpg'),
                        16: pygame.image.load('tank_img/M16.jpg'),
                        17: pygame.image.load('tank_img/M17.jpg'),
                        18: pygame.image.load('tank_img/M18.jpg'),
                        19: pygame.image.load('tank_img/M19.jpg'),
                        20: pygame.image.load('tank_img/M20.jpg')
                    }
        for enemytank in MainGame.EnemyTankList:
         self.image = self.images[enemytank.kx2]
        self.rect = self.image.get_rect()
        self.live = True
        self.rect.left = leftl
        self.rect.top = topl
        self.hg = 100000000000000

    def displayxl2(self):
     for enemytank in MainGame.EnemyTankList:
        if self.live and enemytank.hg>0:
             self.image = self.images[enemytank.kx2]
             MainGame.window.blit(self.image, self.rect)
        else:
            game = MainGame()
            game.start_game()



 # 爆炸类
class Explode:
    def __init__(self, tank):
        # 爆炸的位置由坦克决定
        self.rect = tank.rect
        self.images = [
            pygame.image.load('tank_img/blast0.gif'),
            pygame.image.load('tank_img/blast1.gif'),
            pygame.image.load('tank_img/blast2.gif'),
            pygame.image.load('tank_img/blast3.gif'),
            pygame.image.load('tank_img/blast4.gif'),
            pygame.image.load('tank_img/blast5.gif'),
            pygame.image.load('tank_img/blast6.gif'),
            pygame.image.load('tank_img/blast7.gif')
        ]
        self.step = 0
        self.image = self.images[self.step]
        self.live = True

    # 加载爆炸类
    def displayExplode(self):
        if self.step < len(self.images):
            self.image = self.images[self.step]
            self.step += 1
            MainGame.window.blit(self.image, self.rect)
        else:
            self.live = False
            self.step = 0




# 游戏类
class MainGame:
    # 类属性
    window = None
    my_tank = None

    # 敌方坦克初始化
    EnemyTankList = []
    EnemyTankCount = 1
    # 存储我方子弹列表
    myBulleList = []
    # 存储敌方子弹的列表
    EnemyBulletList = []
    en=[0,0] #敌方存储位置信息
    en1=0
    en2=0
    my=[0,0] #我方存储位置信息
    h=[0,0]  #定义一个矩阵，用于下面运算矩阵
    k=0     #存储矩阵运算用于jl运算
    jl=0   #距离
    wdsr=[0,0,0,0]   #存储我的操作
    explodeList = [] # 创建爆炸对象列表
    screen_image = [] #存储屏幕每次刷新的图片
    list1=[] #存储敌我双方位置和距离的列表
    kb=0 #打败或被打败返回值
    z=bool(0) #游戏是否结束的参数布尔型
    con=bool(1)
    # 创建墙壁列表
    wallList = []
    wallListx=[]
    wallListy=[]
    wallListz=[]
    #创建奖惩区
    jcq1List=[]
    jcq2List=[]
    jcq3List=[]
    jcq11List=[]
    jcq22List=[]
    jcq33List=[]
    xlList=[]
    xlList2=[]
    i=1
    u=2
    o=0
    # 游戏开始方法
    def start_game(self):
        # 初始化展示模块
        pygame.display.init()
        # 调用创建窗口的方法
        self.creat_window()
        # 设置游戏窗口标题
        pygame.display.set_caption('坦克大战')
        # 初始化我方坦克
        self.createMyTank()
        # 初始化敌方坦克
        self.creatEnemyTank()
        # 初始化墙壁
        self.creatWall()
        #传出游戏是否结束，我方输赢
        self.gameover()
        if MainGame.con==True:
            while True:
                self.fresh()

        # 程序持续进行
    def fresh(self):
            # 更改背景颜色
            MainGame.window.fill(COLOR_GREEN)
            # 背景音乐
            MainGame.kb=0
            if (MainGame.my_tank.live == False) or (MainGame.EnemyTankList == []):
                if MainGame.EnemyTankList == []:
                    MainGame.kb=1
                elif MainGame.my_tank.live == False:
                    MainGame.kb=-10
                game = MainGame()
                game.start_game()
            # 获取事件
            self.getEvent()
            # 调用我方坦克进行显示
            if MainGame.my_tank and MainGame.my_tank.live:
                MainGame.my_tank.displayTank()
                MainGame.my=[MainGame.my_tank.rect.left+15,MainGame.my_tank.rect.top+15]
                if not MainGame.my_tank.stop:
                    MainGame.my_tank.moveM()
                    MainGame.my_tank.hitWall()
                    MainGame.my_tank.myTank_hit_enemyTank()
                myBullet = MainGame.my_tank.shotM()
                if myBullet:
                    MainGame.myBulleList.append(myBullet)
            else:
                del MainGame.my_tank
                MainGame.my_tank = None


            # 加载我方子弹
            self.biltMyBullet()
            # 显示敌方坦克
            self.biltEnemyTank()
            #反馈参数信息
            self.step()
            #反馈输入和图像
            self.mej()
            #反馈游戏是否结束
            self.gameover()
            # 显示敌方子弹
            self.biltEnemyBullet()
            # 显示墙壁
            self.blitWall()
            self.blitWallx()
            self.blitWally()
            self.blitWallz()
            #显示奖惩区
            self.blitjcq1()
            self.blitjcq2()
            self.blitjcq3()
            self.blitjcq11()
            self.blitjcq22()
            self.blitjcq33()
            # 显示爆炸效果
            self.blitExplode()
            # 参数输入使坦克运动的函数
            self.xuel()
            self.xuel2()


            # 窗口持续刷新
            pygame.display.update()
            time.sleep(0.001)
            screen_image = pygame.surfarray.array3d(pygame.display.get_surface())
            MainGame.z=True
            MainGame.con=False
    # 创建游戏窗口方法：
    def creat_window(self):
        if not MainGame.window:
            # 创建窗口
            MainGame.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        return MainGame.window

    # 创建我方坦克
    def createMyTank(self):
        MainGame.my_tank = HeroTank(30,30 )
        music = Music('tank_img/start.wav')
        music.play()


    # 创建墙壁
    def creatWall(self):



            wallx= Wall(left=150, top=243)
            wally=Wall(left=580,top=243)
            wallz = Wallx(leftx=360,topx=100)
            walla = Wallx(leftx=360,topx=385)
            wallb = Wallx(leftx=0,topx=100)
            wallc = Wallx(leftx=710, topx=385)
            walld = Wally(lefty=635, topy=0)
            walle = Wally(lefty=150, topy=410)
            wallk = Wallz(leftz=389,topz=235)
            jcqa = jcq1(lefta=23,topa=150)
            jcqb = jcq2(leftb=163,topb=292)
            jcqc = jcq3(leftc=383,topc=435)
            jcqd = jcq11(leftz=733,topz=312)
            jcqe = jcq22(leftz=593,topz=169)
            jcqf = jcq33(leftz=383,topz=27)
            xl1 =  xue(leftl=5,topl=300)
            xl2 =  xue2(leftl=795,topl=10)
            MainGame.jcq1List.append(jcqa)
            MainGame.jcq2List.append(jcqb)
            MainGame.jcq3List.append(jcqc)
            MainGame.jcq11List.append(jcqd)
            MainGame.jcq22List.append(jcqe)
            MainGame.jcq33List.append(jcqf)
            MainGame.wallList.append(wallx)
            MainGame.wallList.append(wally)
            MainGame.wallListx.append(wallz)
            MainGame.wallListx.append(walla)
            MainGame.wallListx.append(wallb)
            MainGame.wallListx.append(wallc)
            MainGame.wallListy.append(walld)
            MainGame.wallListy.append(walle)
            MainGame.wallListz.append(wallk)
            MainGame.xlList.append(xl1)
            MainGame.xlList2.append(xl2)
    # 显示墙壁
    def blitWall(self):
        for b in MainGame.wallList:
            if b.live:
             b.displayWall()
            else:
             MainGame.wallList.remove(b)

    def blitWallx(self):
        for a in MainGame.wallListx:
            if a.live:
             a.displayWallx()
            else:
             MainGame.wallListx.remove(a)

    def blitWally(self):
        for n in MainGame.wallListy:
            if n.live:
             n.displayWally()
            else:
             MainGame.wallListy.remove(n)

    def blitWallz(self):
        for n in MainGame.wallListz:
            if n.live:
             n.displayWallz()
            else:
             MainGame.wallListz.remove(n)

    def blitjcq1(self):
        for b in MainGame.jcq1List:
            if b.live:
                b.displayjcq1()
            else:
                MainGame.jcq1List.remove(b)

    def blitjcq2(self):
        for b in MainGame.jcq2List:
            if b.live:
                b.displayjcq2()
            else:
                MainGame.jcq2List.remove(b)

    def blitjcq3(self):
        for b in MainGame.jcq3List:
            if b.live:
                b.displayjcq3()
            else:
                MainGame.jcq3List.remove(b)

    def blitjcq11(self):
        for b in MainGame.jcq11List:
            if b.live:
                b.displayjcq11()
            else:
                MainGame.jcq11List.remove(b)

    def blitjcq22(self):
        for b in MainGame.jcq22List:
            if b.live:
                b.displayjcq22()
            else:
                MainGame.jcq22List.remove(b)

    def blitjcq33(self):
        for b in MainGame.jcq33List:
            if b.live:
                b.displayjcq33()
            else:
                MainGame.jcq33List.remove(b)

    def xuel(self):
        for b in MainGame.xlList:
            if b.live:
                if 0 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 5:
                            MainGame.my_tank.kx = 1
                            b.image = [1]
                elif 5 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 10:
                            MainGame.my_tank.kx = 2
                            b.image= [2]
                elif 10 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 15:
                            MainGame.my_tank.kx = 3
                            b.image = [3]
                elif 15 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 20:
                            MainGame.my_tank.kx = 4
                            b.image = [4]
                elif 20 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 25:
                            MainGame.my_tank.kx = 5
                            b.image = [5]
                elif 25 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 30:
                            MainGame.my_tank.kx = 6
                            b.image = [6]
                elif 30 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 35:
                            MainGame.my_tank.kx = 7
                            b.image = [7]
                elif 35 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 40:
                            MainGame.my_tank.kx = 8
                            b.image = [8]
                elif 40 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 45:
                            MainGame.my_tank.kx = 9
                            b.image = [9]
                elif 45 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 50:
                            MainGame.my_tank.kx = 10
                            b.image = [10]
                elif 50 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 55:
                            MainGame.my_tank.kx = 11
                            b.image = [11]
                elif 55 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 60:
                            MainGame.my_tank.kx = 12
                            b.image = [12]
                elif 60 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 65:
                            MainGame.my_tank.kx = 13
                            b.image = [13]
                elif 65 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 70:
                            MainGame.my_tank.kx = 14
                            b.image = [14]
                elif 70 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 75:
                            MainGame.my_tank.kx = 15
                            b.image = [15]
                elif 75 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 80:
                            MainGame.my_tank.kx = 16
                            b.image = [16]
                elif 80 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 85:
                            MainGame.my_tank.kx = 17
                            b.image = [17]
                elif 85 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 90:
                            MainGame.my_tank.kx = 18
                            b.image = [18]
                elif 90 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 95:
                            MainGame.my_tank.kx = 19
                            b.image = [19]
                elif 95 < MainGame.my_tank.hg and MainGame.my_tank.hg <= 100:
                            MainGame.my_tank.kx = 20
                            b.image = [20]
                b.displayxl()

            else:
                MainGame.xlList.remove(b)

    def xuel2(self):
        for b in MainGame.xlList2:
                if b.live:
                    for EnemyTank in MainGame.EnemyTankList:
                            if 0 <EnemyTank.hg  and EnemyTank.hg <= 5:
                                EnemyTank.kx2 = 1
                                b.image = [1]
                            elif 5 < EnemyTank.hg and EnemyTank.hg <= 10:
                                EnemyTank.kx2 = 2
                                b.image = [2]
                            elif 10 < EnemyTank.hg and EnemyTank.hg <= 15:
                                EnemyTank.kx2 = 3
                                b.image = [3]
                            elif 15 < EnemyTank.hg and EnemyTank.hg <= 20:
                                EnemyTank.kx2 = 4
                                b.image = [4]
                            elif 20 < EnemyTank.hg and EnemyTank.hg <= 25:
                                EnemyTank.kx2 = 5
                                b.image = [5]
                            elif 25 < EnemyTank.hg and EnemyTank.hg <= 30:
                                EnemyTank.kx2 = 6
                                b.image = [6]
                            elif EnemyTank.hg and EnemyTank.hg <= 35:
                                EnemyTank.kx2 = 7
                                b.image = [7]
                            elif 35 < EnemyTank.hg and EnemyTank.hg <= 40:
                                EnemyTank.kx2 = 8
                                b.image = [8]
                            elif 40 < EnemyTank.hg and EnemyTank.hg <= 45:
                                EnemyTank.kx2 = 9
                                b.image = [9]
                            elif 45 < EnemyTank.hg and EnemyTank.hg <= 50:
                                EnemyTank.kx2 = 10
                                b.image = [10]
                            elif 50 < EnemyTank.hg and EnemyTank.hg <= 55:
                                EnemyTank.kx2 = 11
                                b.image = [11]
                            elif 55 < EnemyTank.hg and EnemyTank.hg <= 60:
                                EnemyTank.kx2 = 12
                                b.image = [12]
                            elif 60 < EnemyTank.hg and EnemyTank.hg <= 65:
                                EnemyTank.kx2 = 13
                                b.image = [13]
                            elif 65 < EnemyTank.hg and EnemyTank.hg <= 70:
                                EnemyTank.kx2 = 14
                                b.image = [14]
                            elif 70 < EnemyTank.hg and EnemyTank.hg <= 75:
                                EnemyTank.kx2 = 15
                                b.image = [15]
                            elif 75 < EnemyTank.hg and EnemyTank.hg <= 80:
                                EnemyTank.kx2 = 16
                                b.image = [16]
                            elif 80 < EnemyTank.hg and EnemyTank.hg <= 85:
                                EnemyTank.kx2 = 17
                                b.image = [17]
                            elif 85 < EnemyTank.hg and EnemyTank.hg <= 90:
                                EnemyTank.kx2 = 18
                                b.image = [18]
                            elif 90 < EnemyTank.hg and EnemyTank.hg <= 95:
                                EnemyTank.kx2 = 19
                                b.image = [19]
                            elif 95 < EnemyTank.hg and EnemyTank.hg <= 100:
                                EnemyTank.kx2 = 20
                                b.image = [20]
                            b.displayxl2()
                else:
                    MainGame.xlList2.remove(b)

                            # 加载我方子弹
    def biltMyBullet(self):
        for bullet in MainGame.myBulleList:
            if bullet.live:
                bullet.displayBullet()
                bullet.move()
                bullet.myBullet_hit_enemy()
                bullet.wall_bullet()
            else:
                MainGame.myBulleList.remove(bullet)


    # 创建敌方坦克
    def creatEnemyTank(self):
            MainGame.EnemyTankList=[]
            top = 170
            left = 620
            speed = random.randint(1,4)
            enemy = EnemyTank(left, top, speed)
            MainGame.EnemyTankList.append(enemy)

    def mej(self):
             print(MainGame.screen_image)
             return MainGame.screen_image

   # 我方坦克，敌方坦克，距离
    def step(self):
            list1=[MainGame.my, MainGame.en, MainGame.jl]

            print('我方坦克坐标:', MainGame.my_tank.rect.left + 15, MainGame.my_tank.rect.top + 15, '敌方坦克坐标:',\
                   MainGame.en1,MainGame.en2, '距离:', MainGame.jl,'我方血量',MainGame.my_tank.hg)

    def gameover(self):
        print(MainGame.z,MainGame.kb)
        return MainGame.z
    # 循环遍历显示敌方坦克
    def biltEnemyTank(self):
        for enemytank in MainGame.EnemyTankList:
            if enemytank.live:
                enemytank.displayTank()
                EnemyBullet = enemytank.shot()
                enemytank.randomMove()
                enemytank.hitWall()
                enemytank.enemyTank_hit_MyTank()
                MainGame.en=[enemytank.rect.left+15,enemytank.rect.top+15]    #中心坐标
                MainGame.en1=enemytank.rect.left+15
                MainGame.en2=enemytank.rect.top+15
                MainGame.h=numpy.array(MainGame.en) - numpy.array(MainGame.my)
                MainGame.k = numpy.matmul(MainGame.h, numpy.reshape(MainGame.h, (2, 1)))
                MainGame.jl = math.sqrt(MainGame.k)
                MainGame.jl = int(MainGame.jl)
                print('我方坦克坐标:',MainGame.my_tank.rect.left+15,MainGame.my_tank.rect.top+15,'敌方坦克坐标:',enemytank.rect.left+15,enemytank.rect.top+15,'距离:',MainGame.jl)

                # 存储敌方子弹
                if EnemyBullet:
                    MainGame.EnemyBulletList.append(EnemyBullet)
            else:
                MainGame.EnemyTankList=[]


    # 加载敌方子弹
    def biltEnemyBullet(self):
        for bullet in MainGame.EnemyBulletList:
            if bullet.live:
                bullet.displayBullet()
                bullet.move()
                bullet.enemyBullet_hit_myTank()
                bullet.wall_bullet()

            else:
                MainGame.EnemyBulletList.remove(bullet)

    # 加载爆炸效果
    def blitExplode(self):
        for explode in MainGame.explodeList:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.explodeList.remove(explode)

                # 获取游戏中的所有事件

    def getEvent(self):
            # 获取游戏中的事件列表
        even_list = pygame.event.get()
        for e in even_list:
            # 点击窗口的叉号实现游戏结束
         if e.type == pygame.QUIT:
                    sys.exit()

         if e.type == pygame.KEYDOWN:
                if MainGame.my_tank and MainGame.my_tank.live:
                    if e.key == pygame.K_DOWN or e.key == pygame.K_s:
                        MainGame.my_tank.direction = 'D'
                        MainGame.my_tank.stop = False
                        MainGame.wdsr=[1,0,0,0]
                        print("按下向下的键，向下移动",MainGame.wdsr)
                    elif e.key == pygame.K_UP or e.key == pygame.K_w:
                        MainGame.my_tank.direction = 'U'
                        MainGame.my_tank.stop = False
                        MainGame.wdsr = [0,1,0,0]
                        print("按下向上的键，向上移动",MainGame.wdsr)
                    elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        MainGame.my_tank.direction = 'L'
                        MainGame.my_tank.stop = False
                        MainGame.wdsr=[0,0,1,0]
                        print("按下向左的键，向左移动",MainGame.wdsr)
                    elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        MainGame.my_tank.direction = 'R'
                        MainGame.my_tank.stop = False
                        MainGame.wdsr = [0,0,0,1]
                        print("按下向右的键，向右移动",MainGame.wdsr)
                    elif e.key == pygame.K_SPACE:
                     if len(MainGame.myBulleList) < 3:
                        myBullet = Bullet(MainGame.my_tank)
                        MainGame.myBulleList.append(myBullet)
                    if e.key == pygame.K_j:
                        MainGame.o=1
                        for jcqa in MainGame.jcq1List:
                                jcqa.image=jcqa.images[1]
                        for jcqa in MainGame.jcq11List:
                                jcqa.image=jcqa.images[1]
                        MainGame.i=0
                        for jcqa in MainGame.jcq2List:
                                jcqa.image = jcqa.images[0]
                        for jcqa in MainGame.jcq22List:
                                jcqa.image = jcqa.images[0]
                        MainGame.u=2
                        for jcqa in MainGame.jcq3List:
                                jcqa.image = jcqa.images[2]
                        for jcqa in MainGame.jcq33List:
                                jcqa.image = jcqa.images[2]
                    elif e.key == pygame.K_k:
                        MainGame.o = 0
                        for jcqa in MainGame.jcq1List:
                            jcqa.image = jcqa.images[0]
                        for jcqa in MainGame.jcq11List:
                            jcqa.image = jcqa.images[0]
                        MainGame.i = 2
                        for jcqa in MainGame.jcq2List:
                            jcqa.image = jcqa.images[2]
                        for jcqa in MainGame.jcq22List:
                            jcqa.image = jcqa.images[2]
                        MainGame.u = 1
                        for jcqa in MainGame.jcq3List:
                            jcqa.image = jcqa.images[1]
                        for jcqa in MainGame.jcq33List:
                            jcqa.image = jcqa.images[1]
                    elif e.key == pygame.K_l:
                        MainGame.o = 2
                        for jcqa in MainGame.jcq1List:
                            jcqa.image = jcqa.images[2]
                        for jcqa in MainGame.jcq11List:
                            jcqa.image = jcqa.images[2]
                        MainGame.i = 1
                        for jcqa in MainGame.jcq2List:
                            jcqa.image = jcqa.images[1]
                        for jcqa in MainGame.jcq22List:
                            jcqa.image = jcqa.images[1]
                        MainGame.u = 0
                        for jcqa in MainGame.jcq3List:
                            jcqa.image = jcqa.images[0]
                        for jcqa in MainGame.jcq33List:
                            jcqa.image = jcqa.images[0]




         elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or e.key == pygame.K_DOWN or e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                        or e.key == pygame.K_w or e.key == pygame.K_s or e.key == pygame.K_a or e.key == pygame.K_d:
                    if MainGame.my_tank and MainGame.my_tank.live:
                        MainGame.my_tank.stop = True


    def steps(self,action):
        if (not MainGame.gameover()):
         if action=='up':
            MainGame.my_tank.direction = 'U'
            MainGame.my_tank.stop = False
            MainGame.wdsr = [0, 1, 0, 0]
         elif action=='down':
            MainGame.my_tank.direction = 'D'
            MainGame.my_tank.stop = False
            MainGame.wdsr = [1, 0, 0, 0]
         elif action=='left':
            MainGame.my_tank.direction = 'L'
            MainGame.my_tank.stop = False
            MainGame.wdsr = [0, 0, 1, 0]
         elif action=='right':
            MainGame.my_tank.direction = 'R'
            MainGame.my_tank.stop = False
            MainGame.wdsr = [0, 0, 0, 1]
            print("按下向右的键，向右移动", MainGame.wdsr)
         else:
            MainGame.my_tank.stop = True
        MainGame.con=True
        return [MainGame.my_tank.rect.left+15,MainGame.my_tank.rect.top+15, MainGame.en1,MainGame.en2, MainGame.jl], MainGame.z, MainGame.kb

def destory():
        sys.exit()




class Music:
    def __init__(self,filename):
        self.filename = filename
        # 初始化音乐混合器
        pygame.mixer.init()
        pygame.mixer.music.load(filename)

    def play(self):
        pygame.mixer.music.play()


if __name__ == '__main__':
    game=MainGame()
    game.start_game()

