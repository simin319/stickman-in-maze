from OpenGL.GL import *
from OpenGL.GLUT import *
import keyboard
import numpy as np

# line.draw(x1, y1, x2, y2, dx, dy)
class line:

    @staticmethod
    def draw(x1, y1, x2, y2, dx1, dy1):
        dx = x2 - x1
        dy = y2 - y1
        zone = line.find_zone(dx, dy)
        px1, py1 = line.convert_to_zone0(zone, x1, y1)
        px2, py2 = line.convert_to_zone0(zone, x2, y2)
        line.midpointline(px1, py1, px2, py2, zone, dx1, dy1)

    @staticmethod
    def find_zone(dx, dy):
        if abs(dx) <= abs(dy):
            if dx >= 0 and dy >= 0:
                return 1
            elif dx <= 0 and dy >= 0:
                return 2
            elif dx >= 0 and dy <= 0:
                return 6
            elif dx <= 0 and dy <= 0:
                return 5
        else:
            if dx >= 0 and dy >= 0:
                return 0
            elif dx <= 0 and dy >= 0:
                return 3
            elif dx >= 0 and dy <= 0:
                return 7
            elif dx <= 0 and dy <= 0:
                return 4

    @staticmethod
    def convert_to_zone0(z, x, y):
        match z:
            case 0:
                return x, y
            case 1:
                return y, x
            case 2:
                return y, -x
            case 3:
                return -x, y
            case 4:
                return -x, -y
            case 5:
                return -y, -x
            case 6:
                return -y, x
            case 7:
                return x, -y

    @staticmethod
    def convert_original(z, x, y):
        match z:
            case 0:
                return x, y
            case 1:
                return y, x
            case 2:
                return -y, x
            case 3:
                return -x, y
            case 4:
                return -x, -y
            case 5:
                return -y, -x
            case 6:
                return y, -x
            case 7:
                return x, -y

    @staticmethod
    def midpointline(x1, y1, x2, y2, z, dx1, dy1):
        dx = x2 - x1
        dy = y2 - y1

        d = (2 * dy) - dx
        e = 2 * dy
        ne = 2 * (dy - dx)

        x = x1
        y = y1
        while x < x2:
            px, py = line.convert_original(z, x, y)
            line.translation(px, py, dx1, dy1)
            if d < 0:
                x += 1
                d += e
            else:
                x += 1
                y += 1
                d += ne

    @staticmethod
    def translation(x, y, dx1, dy1):
        dx = dx1
        dy = dy1
        t = np.array([[1, 0, dx],
                      [0, 1, dy],
                      [0, 0, 1]])
        v1 = np.array([[x],
                       [y],
                       [1]])
        v11 = np.matmul(t, v1)
        x1, y1 = v11[0][0], v11[1][0]
        line.draw_points(x1, y1)

    @staticmethod
    def draw_points(x, y):
        glPointSize(3)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

# fat_line.draw(x1, y1, x2, y2, dx, dy)
class fat_line:

    @staticmethod
    def draw(x1, y1, x2, y2, dx1, dy1):
        dx = x2 - x1
        dy = y2 - y1
        zone = fat_line.find_zone(dx, dy)
        px1, py1 = fat_line.convert_to_zone0(zone, x1, y1)
        px2, py2 = fat_line.convert_to_zone0(zone, x2, y2)
        fat_line.midpointline(px1, py1, px2, py2, zone, dx1, dy1)

    @staticmethod
    def find_zone(dx, dy):
        if abs(dx) <= abs(dy):
            if dx >= 0 and dy >= 0:
                return 1
            elif dx <= 0 and dy >= 0:
                return 2
            elif dx >= 0 and dy <= 0:
                return 6
            elif dx <= 0 and dy <= 0:
                return 5
        else:
            if dx >= 0 and dy >= 0:
                return 0
            elif dx <= 0 and dy >= 0:
                return 3
            elif dx >= 0 and dy <= 0:
                return 7
            elif dx <= 0 and dy <= 0:
                return 4

    @staticmethod
    def convert_to_zone0(z, x, y):
        match z:
            case 0:
                return x, y
            case 1:
                return y, x
            case 2:
                return y, -x
            case 3:
                return -x, y
            case 4:
                return -x, -y
            case 5:
                return -y, -x
            case 6:
                return -y, x
            case 7:
                return x, -y

    @staticmethod
    def convert_original(z, x, y):
        match z:
            case 0:
                return x, y
            case 1:
                return y, x
            case 2:
                return -y, x
            case 3:
                return -x, y
            case 4:
                return -x, -y
            case 5:
                return -y, -x
            case 6:
                return y, -x
            case 7:
                return x, -y

    @staticmethod
    def midpointline(x1, y1, x2, y2, z, dx1, dy1):
        dx = x2 - x1
        dy = y2 - y1

        d = (2 * dy) - dx
        e = 2 * dy
        ne = 2 * (dy - dx)

        x = x1
        y = y1
        while x < x2:
            px, py = fat_line.convert_original(z, x, y)
            fat_line.translation(px, py, dx1, dy1)
            if d < 0:
                x += 1
                d += e
            else:
                x += 1
                y += 1
                d += ne

    @staticmethod
    def translation(x, y, dx1, dy1):
        dx = dx1
        dy = dy1
        t = np.array([[1, 0, dx],
                      [0, 1, dy],
                      [0, 0, 1]])
        v1 = np.array([[x],
                       [y],
                       [1]])
        v11 = np.matmul(t, v1)
        x1, y1 = v11[0][0], v11[1][0]
        fat_line.draw_points(x1, y1)

    @staticmethod
    def draw_points(x, y):
        glPointSize(23)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

# circle.draw(x, y, radius, dx, dy)
class circle:

    @staticmethod
    def draw(x0, y0, radius, dx, dy):
        d = 1 - radius
        x = 0
        y = radius
        circle.eightway(x, y, x0, y0, dx, dy)
        while x < y:
            if d >= 0:
                d = d + 2 * x - 2 * y + 5
                x = x + 1
                y = y - 1
            else:
                d = d + 2 * x + 3
                x = x + 1
            circle.eightway(x, y, x0, y0, dx, dy)

    @staticmethod
    def eightway(x, y, x0, y0, dx, dy):
        circle.translation(x + x0, y + y0, dx, dy)
        circle.translation(y + x0, x + y0, dx, dy)
        circle.translation(y + x0, -x + y0, dx, dy)
        circle.translation(x + x0, -y + y0, dx, dy)
        circle.translation(-x + x0, -y + y0, dx, dy)
        circle.translation(-y + x0, -x + y0, dx, dy)
        circle.translation(-y + x0, x + y0, dx, dy)
        circle.translation(-x + x0, y + y0, dx, dy)


    @staticmethod
    def draw_points(x, y):
        glPointSize(3)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

    @staticmethod
    def translation(x, y, dx, dy):
        dx = dx
        dy = dy
        t = np.array([[1, 0, dx],
                      [0, 1, dy],
                      [0, 0, 1]])
        v1 = np.array([[x],
                       [y],
                       [1]])
        v11 = np.matmul(t, v1)
        x1, y1 = v11[0][0], v11[1][0]
        circle.draw_points(x1, y1)

def maze_map():
    glColor3f(255, 255, 0)
    fat_line.draw(575, 450, 870, 450, 0, 0)
    fat_line.draw(575, 450, 575, 250, 0, 0)
    fat_line.draw(575, 250, 870, 250, 0, 0)
    fat_line.draw(870, 840, 870, 250, 0, 0)
    fat_line.draw(870, 840, 575, 840, 0, 0)
    fat_line.draw(575, 840, 575, 600, 0, 0)
    fat_line.draw(735, 600, 575, 600, 0, 0)
    fat_line.draw(735, 840, 735, 600, 0, 0)
    fat_line.draw(310, 600, 575, 600, 0, 0)
    fat_line.draw(460, 840, 460, 600, 0, 0)
    fat_line.draw(460, 840, 110, 840, 0, 0)
    fat_line.draw(310, 840, 310, 250, 0, 0)
    fat_line.draw(460, 250, 310, 250, 0, 0)
    fat_line.draw(460, 450, 460, 250, 0, 0)
    fat_line.draw(310, 450, 460, 450, 0, 0)
    fat_line.draw(110, 840, 110, 600, 0, 0)
    fat_line.draw(200, 600, 110, 600, 0, 0)
    fat_line.draw(200, 600, 200, 1000, 0, 0)
    fat_line.draw(0, 450, 200, 450, 0, 0)
    fat_line.draw(200, 250, 200, 450, 0, 0)
    fat_line.draw(110, 250, 200, 250, 0, 0)
    fat_line.draw(110, 450, 110, 250, 0, 0)
    fat_line.draw(870, 110, 870, 0, 0, 0)
    fat_line.draw(0, 110, 870, 110, 0, 0)
    fat_line.draw(988, 0, 988, 1000, 0, 0)
    fat_line.draw(200, 990, 1000, 990, 0, 0)
    ###################################
    ###########  goal ################
    glColor3f(0.0, 0.5, 1.0)  #baby Blue
    line.draw(70, 985, 115, 950, 0, 0)
    line.draw(25, 950, 115, 950, 0, 0)
    line.draw(70, 985, 25, 950, 0, 0)
    line.draw(40, 950, 100, 950, 0, 0)
    line.draw(100, 950, 100, 885, 0, 0)
    line.draw(100, 885, 40, 885, 0, 0)
    line.draw(40, 885, 40, 950, 0, 0)

def stick_man(dx, dy):
    glColor3f(0, 255, 255)
    circle.draw(935, 75, 15, dx, dy)
    line.draw(935, 60, 935, 35, dx, dy)
    line.draw(935, 50, 924, 37, dx, dy)
    line.draw(935, 50, 946, 37, dx, dy)
    line.draw(935, 35, 947, 11, dx, dy)
    line.draw(935, 35, 923, 11, dx, dy)

s, dx, dy = 0, 0, 0

def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, -50.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #########
    maze_map()
    maze_game()
    ###########
    glutSwapBuffers()

def maze_game():
    global s, dx, dy
    p = keyboard.read_key()
    if p=="enter" and s==0:
        dx, dy = 0, 0
    elif p=="w" and s==0:
        dx, dy = -4, 135
        s=1        # 0->1
    elif p=="a" and s==1:
        dx, dy = -148, 135
        s=21       # 1->21
    elif p=="d" and s==21:
        dx, dy = -4, 135
        s=1         # 1<-21
    elif p=="a" and s==21:
        dx, dy = -282, 135
        s=22     # 21->22
    elif p=="d" and s==22:
        dx, dy = -148, 135
        s=21      # 21<-22
    elif p=="a" and s==22:
        dx, dy = -418, 139
        s=2    #22->2
    elif p=="d" and s==2:
        dx, dy = -282, 135
        s=22    # 22<-2
    elif p=="a" and s==2:
        dx, dy = -551, 135
        s=31     # 2->31
    elif p=="d" and s==31:
        dx, dy = -418, 139
        s=2     # 2<-31
    elif p=="a" and s==31:
        dx, dy = -682, 138
        s=3   # 31->3
    elif p=="d" and s==3:
        dx, dy = -551, 135
        s=31    #31<-3
    elif p=="w" and s==3:
        dx, dy = -682, 311
        s=41    # 3->41
    elif p=="s" and s==41:
        dx, dy = -682, 138
        s=3       # 3<-41
    elif p=="w" and s==41:
        dx, dy = -685, 477
        s=4      # 41->4
    elif p=="s" and s==4:
        dx, dy = -682, 311
        s=41     # 41<-4
    elif p=="w" and s==4:
        dx, dy = -685, 616
        s=51     # 4->51
    elif p=="s" and s==51:
        dx, dy = -685, 477
        s=4      # 4<-51
    elif p=="w" and s==51:
        dx, dy = -684, 717
        s=5    # 51->5
    elif p=="s" and s==5:
        dx, dy = -685, 616
        s=51    # 51<-5
    elif p=="a" and s==4:
        dx, dy = -787, 477
        s=100     # 4->100
    elif p=="d" and s==100:
        dx, dy = -685, 477
        s=4     # 4<-100
    elif p=="a" and s==100:
        dx, dy = -879, 477
        s=200    # 100->200
    elif p=="d" and s==200:
        dx, dy = -787, 477
        s=100     # 100<-200
    elif p=="w" and s==200:
        dx, dy = -879, 620
        s=300     # 200->300
    elif p=="s" and s==300:
        dx, dy = -879, 477
        s=200     # 200<-300
    elif p=="w" and s==300:
        dx, dy = -879, 753
        s=400      # 300->400
    elif p=="s" and s==400:
        dx, dy = -879, 620
        s=300      # 300<-400
    elif p=="w" and s==400:
        dx, dy = -782, 887
        s=500                               ############ goal reached ############
    elif p=="a" and s==3:
        dx, dy = -779, 135
        s=61         # 3->61
    elif p=="d" and s==61:
        dx, dy = -682, 138
        s=3        # 3<-61
    elif p=="a" and s==61:
        dx, dy = -879, 135
        s=62    # 61->62
    elif p=="d" and s==62:
        dx, dy = -779, 135
        s=61     # 61<-62
    elif p=="w" and s==62:
        dx, dy = -879, 226
        s=63       # 62->63
    elif p=="s" and s==63:
        dx, dy = -879, 135
        s=62       # 62<-63
    elif p=="w" and s==63:
        dx, dy = -879, 315
        s=6        # 63->6
    elif p=="s" and s==6:
        dx, dy = -879, 226
        s=63        # 63<-6
    elif p=="w" and s==2:
        dx, dy = -418, 305
        s=71       # 2->71
    elif p=="s" and s==71:
        dx, dy = -418, 139
        s=2        # 2<-71
    elif p=="w" and s==71:
        dx, dy = -420, 478
        s=7         # 71->7
    elif p=="s" and s==7:
        dx, dy = -418, 305
        s=71       # 71<-7
    elif p=="a" and s==7:
        dx, dy = -494, 478
        s=81      # 7->81
    elif p=="d" and s==81:
        dx, dy = -420, 478
        s=7        # 7<-81
    elif p=="a" and s==81:
        dx, dy = -575, 474
        s=8      # 81->8
    elif p=="d" and s==8:
        dx, dy = -494, 478
        s= 81       # 81<-8
    elif p=="d" and s==7:
        dx, dy = -280, 478
        s=91       # 7->91
    elif p=="a" and s==91:
        dx, dy = -420,478
        s=7      # 7<-91
    elif p=="d" and s==91:
        dx, dy = -136, 478
        s=92       # 91->92
    elif p=="a" and s==92:
        dx, dy = -280, 478
        s=91       # 91<-92
    elif p=="w" and s==92:
        dx, dy = -135, 597
        s=93       # 92->93
    elif p=="s" and s==93:
        dx, dy = -136, 478
        s=92      # 92<-93
    elif p=="w" and s==93:
        dx, dy = -135, 700
        s=9       # 93->9
    elif p=="s" and s==9:
        dx, dy = -135, 597
        s=93      # 93<-9
    elif p=="w" and s==1:
        dx, dy = -4, 320
        s=101     # 1->101
    elif p=="s" and s==101:
        dx, dy = -4, 135
        s=1        # 1<-101
    elif p=="w" and s==101:
        dx, dy = -4, 512
        s=102      # 101->102
    elif p=="s" and s==102:
        dx, dy = -4,320
        s=101     # 101<-102
    elif p=="w" and s==102:
        dx, dy = -4, 699
        s=103      # 102->103
    elif p=="s" and s==103:
        dx, dy = -4, 512
        s=102       # 102<-103
    elif p=="w" and s==103:
        dx, dy = -4, 876
        s=104      # 103->104
    elif p=="s" and s==104:
        dx, dy = -4, 699
        s=103      # 103<-104
    elif p=="a" and s==104:
        dx, dy = -155, 875
        s=105       # 104->105
    elif p=="d" and s==105:
        dx, dy = -4, 876
        s=104      # 104<-105
    elif p=="a" and s==105:
        dx, dy = -295, 876
        s=106      # 105->106
    elif p=="d" and s==106:
        dx, dy = -155, 876
        s=105         # 105<-106
    elif p=="a" and s==106:
        dx, dy = -421, 876
        s=10          # 106->10
    elif p=="d" and s==10:
        dx, dy = -295, 876
        s=106       # 106<-10
    elif p=="s" and s==10:
        dx, dy = -419, 751
        s=111      # 10->111
    elif p=="w" and s==111:
        dx, dy = -421, 876
        s=10       # 10<-111
    elif p=="s" and s==111:
        dx, dy = -419, 640
        s=11       # 111->11
    elif p=="w" and s==11:
        dx, dy = -419, 751
        s=111      # 111<-11
    elif p=="a" and s==10:
        dx, dy = -555, 869
        s=121       # 10->121
    elif p=="d" and s==121:
        dx, dy = -421, 876
        s=10        # 10<-121
    elif p=="a" and s==121:
        dx, dy = -679, 869
        s=12       # 121->12
    elif p=="d" and s==12:
        dx, dy = -555, 869
        s=121       # 121<-12
    elif p=="x":
        glutLeaveMainLoop()
    else:
        dx, dy =dx, dy
    stick_man(dx, dy)

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(850, 850)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Press (Enter) to start, (X) to quit and (W/A/S/D) for control")
glutDisplayFunc(screen)
glutIdleFunc(screen)
glutMainLoop()