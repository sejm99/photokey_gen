import gdstk
import sys, time
import numpy as np

PROCESS=[]
PRORITY=[]
LAYER_NO_1=[]
LAYER_NO_2=[]
GDS_NAME=[]
PAD_NO=[]
TYPE=[]
MAIN_X=[]
MAIN_Y=[]
global NAME_PAD_1830AN18BA
global NAME_PAD_1830BD15BA
global NAME_PAD_SJ
global NAME_PAD_709AHE35BA
NAME_PAD_1830AN18BA={'9':'10','11':'12','13':'14','15':'16','17':'18','19':'20','151':'152','187':'16','188':'18','190':'20'}
NAME_PAD_1830BD15BA={'9':'10','11':'12','13':'14','15':'16','17':'18','19':'20'}
NAME_PAD_709AHE35BA={'26':'27','28':'29','30':'31','32':'33','42':'43','62':'31','63':'33','64':'43'}
NAME_PAD_SJ={'9':'10'}

def get_arr():
    #input 파일 정보 가져오기
    with open('./fab1/vernier_input','r') as f:
        lines = f.readlines()
        for line in lines:
            line_st=line.strip()
            line_sp=line_st.split()
            if line_sp[0] == "PROCESS":
                PROCESS.append(line_sp[1])
            else:
                PRORITY.append(line_sp[0])
                GDS_NAME.append(line_sp[3])
                PAD_NO.append(line_sp[4])
                TYPE.append(line_sp[3].split('_')[1][-1])
                MAIN_X.append(line_sp[3].split('_')[2])
                if line_sp[3].split('_')[1][-1] == "2" or line_sp[3].split('_')[1][-1] == "3":
                    MAIN_Y.append("76")
                else:
                    if line_sp[3].split('_')[1][-1] == "5" and "SJ" in PROCESS[0] and line_sp[1] == "10" and line_sp[2] == "9":
                        MAIN_Y.append("48")
                    else:
                        MAIN_Y.append("44")

def Make_letter(input,layer_no,scale_x,scale_y):
    #알파벳 만들기
    x=float(scale_x)
    y=float(scale_y)
    if input == "A":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        rect3 = gdstk.rectangle((0.3*x,0),(0.7*x,0.4*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "B":
        points = [(0,0),(0,1*y),(0.9*x,1*y),(1*x,0.9*y),(1*x,0.6*y),(0.9*x,0.5*y),(1*x,0.4*y),(1*x,0.1*y),(0.9*x,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        rect2 = gdstk.rectangle((0.25*x,0.2*y),(0.75*x,0.4*y))
        rect3 = gdstk.rectangle((0.25*x,0.6*y),(0.75*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "C":
        points = [(0,0.2*y),(0,0.8*y),(0.2*x,1*y),(0.9*x,1*y),(1*x,0.9*y),(1*x,0.8*y),(0.9*x,0.7*y),(0.4*x,0.7*y),(0.3*x,0.6*y),(0.3*x,0.4*y),(0.4*x,0.3*y),(0.9*x,0.3*y),(1*x,0.2*y),(1*x,0.1*y),(0.9*x,0),(0.2*x,0),(0,0.2*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "D":
        points = [(0,0),(0,1*y),(0.8*x,1*y),(1*x,0.8*y),(1*x,0.2*y),(0.8*x,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        points = [(0.25*x,0.25*y),(0.25*x,0.75*y),(0.65*x,0.75*y),(0.75*x,0.65*y),(0.75*x,0.35*y),(0.65*x,0.25*y),(0.2*x,0.25*y)]
        rect2 = gdstk.Polygon(points)
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "E":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0.8*y),(0.3*x,0.8*y),(0.3*x,0.6*y),(1*x,0.6*y),(1*x,0.4*y),(0.3*x,0.4*y),(0.3*x,0.2*y),(1*x,0.2*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "F":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0.8*y),(0.3*x,0.8*y),(0.3*x,0.6*y),(1*x,0.6*y),(1*x,0.4*y),(0.3*x,0.4*y),(0.3*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "G":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0.8*y),(0.3*x,0.8*y),(0.3*x,0.2*y),(0.8*x,0.2*y),(0.8*x,0.4*y),(0.5*x,0.4*y),(0.5*x,0.6*y),(1*x,0.6*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "H":
        points = [(0,0),(0,1*y),(0.3*x,1*y),(0.3*x,0.65*y),(0.7*x,0.65*y),(0.7*x,1*y),(1*x,1*y),(1*x,0),(0.7*x,0),(0.7*x,0.35*y),(0.3*x,0.35*y),(0.3*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "I":
        points = [(0,0),(0,0.25*y),(0.35*x,0.25*y),(0.35*x,0.75*y),(0,0.75*y),(0,1*y),(1*x,1*y),(1*x,0.75*y),(0.65*x,0.75*y),(0.65*x,0.25*y),(1*x,0.25*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "J":
        points = [(0,0.8*y),(0,1*y),(1*x,1*y),(1*x,0.75*y),(0.9*x,0.75*y),(0.9*x,0.1*y),(0.8*x,0),(0.2*x,0),(0.1*x,0.1*y),(0.1*x,0.5*y),(0.35*x,0.5*y),(0.35*x,0.25*y),(0.65*x,0.25*y),(0.65*x,0.75*y),(0,0.75*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "K":
        points = [(0,0),(0,1*y),(0.3*x,1*y),(0.3*x,0.6*y),(0.7*x,1*y),(1*x,1*y),(0.9*x,0.9*y),(0.5*x,0.5*y),(0.9*x,0.1*y),(1*x,0),(0.7*x,0),(0.3*x,0.4*y),(0.3*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "L":
        points = [(0,0),(0,1*y),(0.35*x,1*y),(0.35*x,0.35*y),(1*x,0.35*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "M":
        points = [(0,0),(0,1*y),(0.25*x,1*y),(0.5*x,0.75*y),(0.75*x,1*y),(1*x,1*y),(1*x,0),(0.75*x,0),(0.75*x,0.65*y),(0.5*x,0.4*y),(0.25*x,0.65*y),(0.25*x,0.2*y),(0.25*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "N":
        points = [(0,0),(0,1*y),(0.25*x,1*y),(0.75*x,0.4*y),(0.75*x,1*y),(1*x,1*y),(1*x,0),(0.75*x,0),(0.25*x,0.6*y),(0.25*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "O":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.3*y),(0.7*x,0.7*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "P":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0.4*y),(0.3*x,0.4*y),(0.3*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.3*x,0.65*y),(0.75*x,0.75*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "Q":
        rect1 = gdstk.rectangle((0,0.1*y),(0.9*x,1*y))
        rect2 = gdstk.rectangle((0.25*x,0.35*y),(0.65*x,0.75*y))
        points = [(0.35*x,0.6*y),(0.6*x,0.6*y),(1*x,0.1*y),(1*x,0),(0.8*x,0),(0.35*x,0.6*y)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "R":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0.4*y),(0.3*x,0.4*y),(0.3*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        points = [(0.8*x,0),(0.3*x,0.4*y),(0.65*x,0.4*y),(1*x,0.1*y),(1*x,0),(0.8*x,0)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "S":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.25*y),(0.7*x,0.38*y))
        rect3 = gdstk.rectangle((0.3*x,0.63*y),(1*x,0.75*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "T":
        rect1 = gdstk.rectangle((0,0.7*y),(1*x,1*y))
        rect2 = gdstk.rectangle((0.35*x,0),(0.65*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "U":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.3*y),(0.7*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "V":
        points = [(0.4*x,0),(0,0.3*y),(0,1*y),(1*x,1*y),(1*x,0.3*y),(0.6*x,0),(0.4*x,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.3*x,0.4*y),(0.7*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "W":
        points = [(0,1*y),(0.2*x,1*y),(0.3*x,0.3*y),(0.4*x,1*y),(0.6*x,1*y),(0.7*x,0.3*y),(0.8*x,1*y),(1*x,1*y),(0.8*x,0),(0.6*x,0),(0.5*x,0.7*y),(0.4*x,0),(0.2*x,0),(0,1*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "X":
        points = [(0,1*y),(0.3*x,1*y),(1*x,0),(0.7*x,0),(0,1*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0,0),(0.7*x,1*y),(1*x,1*y),(0.3*x,0),(0,0)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "Y":
        points = [(0,1*y),(0.3*x,1*y),(0.5*x,0.6*y),(0.7*x,1*y),(1*x,1*y),(0.65*x,0.4*y),(0.65*x,0),(0.35*x,0),(0.35*x,0.4*y),(0,1*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "Z":
        points = [(0,1*y),(1*x,1*y),(1*x,0.75*y),(0.4*x,0.25*y),(1*x,0.25*y),(1*x,0),(0,0),(0,0.25*y),(0.6*x,0.75*y),(0,0.75*y),(0,1*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "0":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.2*x,0.2*y),(0.8*x,0.8*y))
        points = [(0.1*x,0),(0,0),(0,0.1*y),(0.9*x,1*y),(1*x,1*y),(1*x,0.9*y),(0.1*x,0)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "1":
        points = [(0.1*x,0),(0.1*x,0.25*y),(0.4*x,0.25*y),(0.4*x,0.7*y),(0.2*x,0.7*y),(0.2*x,0.9*y),(0.4*x,0.9*y),(0.4*x,1*y),(0.7*x,1*y),(0.7*x,0.25*y),(0.9*x,0.25*y),(0.9*x,0),(0.1*x,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "2":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.63*y),(0.7*x,0.75*y))
        rect3 = gdstk.rectangle((0.3*x,0.25*y),(1*x,0.38*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "3":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.63*y),(0.7*x,0.75*y))
        rect3 = gdstk.rectangle((0,0.25*y),(0.7*x,0.38*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "4":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0),(0.7*x,0.3*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "5":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.23*y),(0.7*x,0.37*y))
        rect3 = gdstk.rectangle((0.3*x,0.63*y),(1*x,0.77*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "6":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.23*y),(0.7*x,0.37*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(1*x,0.77*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "7":
        points = [(0,0.6*y),(0,1*y),(1*x,1*y),(1*x,0),(0.7*x,0),(0.7*x,0.7*y),(0.3*x,0.7*y),(0.3*x,0.6*y),(0,0.6*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "8":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.23*y),(0.7*x,0.37*y))
        rect3 = gdstk.rectangle((0.3*x,0.63*y),(0.7*x,0.77*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "9":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.63*y),(0.7*x,0.77*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
def in_box(process,layer_1,main_x,main_y,bar_in1,name_11,location,type):
    let_1 = gdstk.Cell("let_1_text")
    let_2 = gdstk.Cell("let_2_text")
    pre_result = gdstk.Cell("cell_name")
    #Box
    #if type == "FRAME" and ("SJ" in PROCESS[0] or "709AHE35BA" in PROCESS[0]):
    if type == "FRAME" and "SJ" in PROCESS[0]:
        box_center_x = (int(main_x)/2)+6
        box_center_y = int(main_y)/2
    else:
        box_center_x = (int(main_x)/2)+6
        box_center_y = (int(main_y)/2)+5
    # In:Box Center에서 +-3
    if type == "BOX":
        rect_1_in = gdstk.rectangle((box_center_x-3,box_center_y-3),(box_center_x+3,box_center_y+3),layer=int(layer_1[:-1]))
        rect_1_out = gdstk.rectangle((box_center_x-3-int(bar_in1),box_center_y-3-int(bar_in1)),(box_center_x+3+int(bar_in1),box_center_y+3+int(bar_in1)),layer=int(layer_1[:-1]))
        rect_in = gdstk.boolean(rect_1_in,rect_1_out,"xor",layer=int(layer_1[:-1]))
        pre_result.add(*rect_in)
    elif type == "CHAIN":
        for i in range(0,10):
            rect_rep_b = gdstk.rectangle((box_center_x-4.25-float(bar_in1)+(float(bar_in1)*(i*2)),box_center_y-4.25-float(bar_in1)),(box_center_x-4.25+(float(bar_in1)*(i*2)),box_center_y-4.25),layer=int(layer_1[:-1]))
            pre_result.add(rect_rep_b)
            rect_rep_t = gdstk.rectangle((box_center_x-4.25-float(bar_in1)+(float(bar_in1)*(i*2)),box_center_y+4.75-float(bar_in1)),(box_center_x-4.25+(float(bar_in1)*(i*2)),box_center_y+4.75),layer=int(layer_1[:-1]))
            pre_result.add(rect_rep_t)
            rect_rep_l = gdstk.rectangle((box_center_x-4.25-float(bar_in1),box_center_y-4.25-float(bar_in1)+(float(bar_in1)*(i*2))),(box_center_x-4.25,box_center_y-4.25+(float(bar_in1)*(i*2))),layer=int(layer_1[:-1]))
            pre_result.add(rect_rep_l)
            rect_rep_r = gdstk.rectangle((box_center_x+4.75-float(bar_in1),box_center_y-4.25-float(bar_in1)+(float(bar_in1)*(i*2))),(box_center_x+4.75,box_center_y-4.25+(float(bar_in1)*(i*2))),layer=int(layer_1[:-1]))
            pre_result.add(rect_rep_r)
    elif type == "BAR":
        rect_rep_b =  gdstk.rectangle((box_center_x-3.5,box_center_y-4-float(bar_in1)),(box_center_x+3.5,box_center_y-4),layer=int(layer_1[:-1]))
        pre_result.add(rect_rep_b)
        rect_rep_t =  gdstk.rectangle((box_center_x-3.5,box_center_y+4),(box_center_x+3.5,box_center_y+4+float(bar_in1)),layer=int(layer_1[:-1]))
        pre_result.add(rect_rep_t)
        rect_rep_l =  gdstk.rectangle((box_center_x-4-float(bar_in1),box_center_y-3.5),(box_center_x-4,box_center_y+3.5),layer=int(layer_1[:-1]))
        pre_result.add(rect_rep_l)
        rect_rep_r =  gdstk.rectangle((box_center_x+4,box_center_y-3.5),(box_center_x+4+float(bar_in1),box_center_y+3.5),layer=int(layer_1[:-1]))
        pre_result.add(rect_rep_r)
    elif type == "FRAME":
        rect = gdstk.rectangle((box_center_x-(int(bar_in1)/2),box_center_y-(int(bar_in1)/2)),(box_center_x+(int(bar_in1)/2),box_center_y+(int(bar_in1)/2)),layer=int(layer_1[:-1]))
        pre_result.add(rect)
    elif type == "TOP_CHAIN":
        top_box_center_x = (int(main_x)/2)+6
        top_box_center_y = 59
        for i in range(0,10):
            rect_rep_b = gdstk.rectangle((top_box_center_x-4.25-float(bar_in1)+(float(bar_in1)*(i*2)),top_box_center_y-4.25-float(bar_in1)),(top_box_center_x-4.25+(float(bar_in1)*(i*2)),top_box_center_y-4.25),layer=int(layer_1[:-1]))
            pre_result.add(rect_rep_b)
            rect_rep_t = gdstk.rectangle((top_box_center_x-4.25-float(bar_in1)+(float(bar_in1)*(i*2)),top_box_center_y+4.75-float(bar_in1)),(top_box_center_x-4.25+(float(bar_in1)*(i*2)),top_box_center_y+4.75),layer=int(layer_1[:-1]))
            pre_result.add(rect_rep_t)
            rect_rep_l = gdstk.rectangle((top_box_center_x-4.25-float(bar_in1),top_box_center_y-4.25-float(bar_in1)+(float(bar_in1)*(i*2))),(top_box_center_x-4.25,top_box_center_y-4.25+(float(bar_in1)*(i*2))),layer=int(layer_1[:-1]))
            pre_result.add(rect_rep_l)
            rect_rep_r = gdstk.rectangle((top_box_center_x+4.75-float(bar_in1),top_box_center_y-4.25-float(bar_in1)+(float(bar_in1)*(i*2))),(top_box_center_x+4.75,top_box_center_y-4.25+(float(bar_in1)*(i*2))),layer=int(layer_1[:-1]))
            pre_result.add(rect_rep_r)
    elif type == "TOP_BOX":
        top_box_center_x = (int(main_x)/2)+6
        top_box_center_y = 59
        rect_1_in = gdstk.rectangle((top_box_center_x-3,top_box_center_y-3),(top_box_center_x+3,top_box_center_y+3),layer=int(layer_1[:-1]))
        rect_1_out = gdstk.rectangle((top_box_center_x-3-int(bar_in1),top_box_center_y-3-int(bar_in1)),(top_box_center_x+3+int(bar_in1),top_box_center_y+3+int(bar_in1)),layer=int(layer_1[:-1]))
        rect_in = gdstk.boolean(rect_1_in,rect_1_out,"xor",layer=int(layer_1[:-1]))
        pre_result.add(*rect_in)
    elif type == "BOT_BAR":
        bot_box_center_x = (int(main_x)/2)+6
        bot_box_center_y = 17
        rect_rep_b =  gdstk.rectangle((bot_box_center_x-3.5,bot_box_center_y-4-float(bar_in1)),(bot_box_center_x+3.5,bot_box_center_y-4),layer=int(layer_1[:-1]))
        pre_result.add(rect_rep_b)
        rect_rep_t =  gdstk.rectangle((bot_box_center_x-3.5,bot_box_center_y+4),(bot_box_center_x+3.5,bot_box_center_y+4+float(bar_in1)),layer=int(layer_1[:-1]))
        pre_result.add(rect_rep_t)
        rect_rep_l =  gdstk.rectangle((bot_box_center_x-4-float(bar_in1),bot_box_center_y-3.5),(bot_box_center_x-4,bot_box_center_y+3.5),layer=int(layer_1[:-1]))
        pre_result.add(rect_rep_l)
        rect_rep_r =  gdstk.rectangle((bot_box_center_x+4,bot_box_center_y-3.5),(bot_box_center_x+4+float(bar_in1),bot_box_center_y+3.5),layer=int(layer_1[:-1]))
        pre_result.add(rect_rep_r)
    rect_bound = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
    
    # Make_letter(글씨,layer_no,size_x,size_y)
    LAYER_NUM=[]
    BD18_NAME=[]
    XH18_NAME=[]
    BD15_NAME=[]
    GEN2_NAME=[]
    GEN3_NAME=[]
    BD35_NAME=[]
    with open('./fab1/layer_name.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line_st=line.strip()
            line_sp=line_st.split()
            LAYER_NUM.append(line_sp[0])
            BD18_NAME.append(line_sp[1])
            XH18_NAME.append(line_sp[2])
            BD15_NAME.append(line_sp[3])
            GEN2_NAME.append(line_sp[4])
            GEN3_NAME.append(line_sp[5])
            BD35_NAME.append(line_sp[6])
    #Name
    if process=="1830AN18BA":
        Layer_name_1 = BD18_NAME[int(layer_1[:-1])]
    elif process=="181ABD18BA":
        Layer_name_1 = XH18_NAME[int(layer_1[:-1])]
    elif process=="1830BD15BA":
        Layer_name_1 = BD15_NAME[int(layer_1[:-1])]
    elif process=="0600SJ00BB":
        Layer_name_1 = GEN2_NAME[int(layer_1[:-1])]
    elif process=="0650SJ00BD":
        Layer_name_1 = GEN3_NAME[int(layer_1[:-1])]
    elif process=="709AHE35BA":
        Layer_name_1 = BD35_NAME[int(layer_1[:-1])]
    else:
        print("Layer Name Is Not Defined :"+process)
        sys.exit()
    # Letter Make
    #if type == "FRAME" and ("SJ" in PROCESS[0] or "709AHE35BA" in PROCESS[0]):
    if type == "FRAME" and "SJ" in PROCESS[0]:
        let_center_x = box_center_x-23-(int(name_11.split("X")[0])/2)
    else:
        let_center_x = box_center_x-22-(int(name_11.split("X")[0])/2)
    
    if "TOP_" in type:
        let_bottom_y1 = 59+3+int(name_11.split("X")[-1])
        let_bottom_y2 = 59+1
    elif "BOT_" in type:
        let_bottom_y1 = 17+3+int(name_11.split("X")[-1])
        let_bottom_y2 = 17+1
    else:
        #if type == "FRAME" and ("SJ" in PROCESS[0] or "709AHE35BA" in PROCESS[0]):
        if type == "FRAME" and "SJ" in PROCESS[0]:
            let_bottom_y1 = box_center_y+5+int(name_11.split("X")[-1])
        else:
            let_bottom_y1 = box_center_y+3+int(name_11.split("X")[-1])
        let_bottom_y2 = box_center_y+1
    polygons = Make_letter(Layer_name_1[0],int(layer_1[:-1]),name_11.split("X")[0],name_11.split("X")[1])
    try:
        let_1.add(*polygons)
    except:
        let_1.add(polygons)
    polygons = Make_letter(Layer_name_1[1],int(layer_1[:-1]),name_11.split("X")[0],name_11.split("X")[1])
    try:
        let_2.add(*polygons)
    except:
        let_2.add(polygons)
    name_box = gdstk.rectangle((0,0),(3000,3000))
    xor1 = gdstk.boolean(name_box,gdstk.Reference(let_1,(let_center_x,let_bottom_y1)),"and")
    pre_result.add(*xor1)
    xor2 = gdstk.boolean(name_box,gdstk.Reference(let_2,(let_center_x,let_bottom_y2)),"and")
    pre_result.add(*xor2)
    if "M" in layer_1:
        step1=gdstk.boolean(rect_bound,gdstk.Reference(pre_result,(0,0)),"not",layer=int(layer_1[:-1]))
    else:
        step1=gdstk.boolean(rect_bound,gdstk.Reference(pre_result,(0,0)),"and",layer=int(layer_1[:-1]))
    return step1
def out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,type,lay_name_option):
    let_3 = gdstk.Cell("let_3_text")
    let_4 = gdstk.Cell("let_4_text")
    let_5 = gdstk.Cell("let_5_text")
    let_6 = gdstk.Cell("let_6_text")
    pre_result = gdstk.Cell("cell_name")
    #Box
    #if type == "FRAME" and ("SJ" in PROCESS[0] or "709AHE35BA" in PROCESS[0]):
    if type == "FRAME" and "SJ" in PROCESS[0]:
        box_center_x = (int(main_x)/2)+6
        box_center_y = int(main_y)/2
    else:
        box_center_x = (int(main_x)/2)+6
        box_center_y = (int(main_y)/2)+5
    # In:Box Center에서 +-3
    if type == "BOX":
        rect_2_in = gdstk.rectangle((box_center_x-9,box_center_y-9),(box_center_x+9,box_center_y+9),layer=int(layer_2[:-1]))
        rect_2_out = gdstk.rectangle((box_center_x-9-int(bar_out1),box_center_y-9-int(bar_out1)),(box_center_x+9+int(bar_out1),box_center_y+9+int(bar_out1)),layer=int(layer_2[:-1]))
        rect_out = gdstk.boolean(rect_2_in,rect_2_out,"xor",layer=int(layer_2[:-1]))
        pre_result.add(*rect_out)
    if type == "BAR":
        rect_rep_b =  gdstk.rectangle((box_center_x-9.5,box_center_y-10-float(bar_out1)),(box_center_x+9.5,box_center_y-10),layer=int(layer_2[:-1]))
        pre_result.add(rect_rep_b)
        rect_rep_t =  gdstk.rectangle((box_center_x-9.5,box_center_y+10),(box_center_x+9.5,box_center_y+10+float(bar_out1)),layer=int(layer_2[:-1]))
        pre_result.add(rect_rep_t)
        rect_rep_l =  gdstk.rectangle((box_center_x-10-float(bar_out1),box_center_y-9.5),(box_center_x-10,box_center_y+9.5),layer=int(layer_2[:-1]))
        pre_result.add(rect_rep_l)
        rect_rep_r =  gdstk.rectangle((box_center_x+10,box_center_y-9.5),(box_center_x+10+float(bar_out1),box_center_y+9.5),layer=int(layer_2[:-1]))
        pre_result.add(rect_rep_r)
    elif type == "FRAME":
        rect = gdstk.rectangle((box_center_x-(int(bar_out1)/2),box_center_y-(int(bar_out1)/2)),(box_center_x+(int(bar_out1)/2),box_center_y+(int(bar_out1)/2)),layer=int(layer_2[:-1]))
        pre_result.add(rect)
    elif type == "TOP_BOX":
        top_box_center_x = (int(main_x)/2)+6
        top_box_center_y = 59
        rect_2_in = gdstk.rectangle((top_box_center_x-9,top_box_center_y-9),(top_box_center_x+9,top_box_center_y+9),layer=int(layer_2[:-1]))
        rect_2_out = gdstk.rectangle((top_box_center_x-9-int(bar_out1),top_box_center_y-9-int(bar_out1)),(top_box_center_x+9+int(bar_out1),top_box_center_y+9+int(bar_out1)),layer=int(layer_2[:-1]))
        rect_out = gdstk.boolean(rect_2_in,rect_2_out,"xor",layer=int(layer_2[:-1]))
        pre_result.add(*rect_out)
    elif type == "BOT_BAR":
        bot_box_center_x = (int(main_x)/2)+6
        bot_box_center_y = 17
        rect_rep_b =  gdstk.rectangle((bot_box_center_x-9.5,bot_box_center_y-10-float(bar_out1)),(bot_box_center_x+9.5,bot_box_center_y-10),layer=int(layer_2[:-1]))
        pre_result.add(rect_rep_b)
        rect_rep_t =  gdstk.rectangle((bot_box_center_x-9.5,bot_box_center_y+10),(bot_box_center_x+9.5,bot_box_center_y+10+float(bar_out1)),layer=int(layer_2[:-1]))
        pre_result.add(rect_rep_t)
        rect_rep_l =  gdstk.rectangle((bot_box_center_x-10-float(bar_out1),bot_box_center_y-9.5),(bot_box_center_x-10,bot_box_center_y+9.5),layer=int(layer_2[:-1]))
        pre_result.add(rect_rep_l)
        rect_rep_r =  gdstk.rectangle((bot_box_center_x+10,bot_box_center_y-9.5),(bot_box_center_x+10+float(bar_out1),bot_box_center_y+9.5),layer=int(layer_2[:-1]))
        pre_result.add(rect_rep_r)
    rect_bound = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
    # Make_letter(글씨,layer_no,size_x,size_y)
    LAYER_NUM=[]
    BD18_NAME=[]
    XH18_NAME=[]
    BD15_NAME=[]
    GEN2_NAME=[]
    GEN3_NAME=[]
    BD35_NAME=[]
    with open('./fab1/layer_name.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line_st=line.strip()
            line_sp=line_st.split()
            LAYER_NUM.append(line_sp[0])
            BD18_NAME.append(line_sp[1])
            XH18_NAME.append(line_sp[2])
            BD15_NAME.append(line_sp[3])
            GEN2_NAME.append(line_sp[4])
            GEN3_NAME.append(line_sp[5])
            BD35_NAME.append(line_sp[6])
    #Name
    if lay_name_option == "-":
        if process=="1830AN18BA":
            Layer_name_2 = BD18_NAME[int(layer_2[:-1])]
        elif process=="181ABD18BA":
            Layer_name_2 = XH18_NAME[int(layer_2[:-1])]
        elif process=="1830BD15BA":
            Layer_name_2 = BD15_NAME[int(layer_2[:-1])]
        elif process=="0600SJ00BB":
            Layer_name_2 = GEN2_NAME[int(layer_2[:-1])]
        elif process=="0650SJ00BD":
            Layer_name_2 = GEN3_NAME[int(layer_2[:-1])]
        elif process=="709AHE35BA":
            Layer_name_2 = BD35_NAME[int(layer_2[:-1])]
        else:
            print("Layer Name Is Not Defined :"+process)
            sys.exit()
    else:
        Layer_name_2 = lay_name_option
    #if type == "FRAME" and ("SJ" in PROCESS[0] or "709AHE35BA" in PROCESS[0]):
    if type == "FRAME" and "SJ" in PROCESS[0]:
        let_center_x = box_center_x-23-(int(name_12.split("X")[0])/2)
    else:
        let_center_x = box_center_x-22-(int(name_12.split("X")[0])/2)
    # Letter Make
    #if type == "FRAME" and ("SJ" in PROCESS[0] or "709AHE35BA" in PROCESS[0]):
    if type == "FRAME" and "SJ" in PROCESS[0]:
        let_bottom_y3 = box_center_y-1-int(name_12.split("X")[-1])
        let_bottom_y4 = box_center_y-5-(int(name_12.split("X")[-1])*2)
    else:
        if "TOP_" in type:
            let_bottom_y3 = 59-1-int(name_12.split("X")[-1])
            let_bottom_y4 = 59-3-(int(name_12.split("X")[-1])*2)
        elif "BOT_" in type:
            let_bottom_y3 = 17-1-int(name_12.split("X")[-1])
            let_bottom_y4 = 17-3-(int(name_12.split("X")[-1])*2)
        else:
            let_bottom_y3 = box_center_y-1-int(name_12.split("X")[-1])
            let_bottom_y4 = box_center_y-3-(int(name_12.split("X")[-1])*2)
    polygons = Make_letter(Layer_name_2[0],int(layer_2[:-1]),name_12.split("X")[0],name_12.split("X")[1])
    try:
        let_3.add(*polygons)
    except:
        let_3.add(polygons)
    polygons = Make_letter(Layer_name_2[1],int(layer_2[:-1]),name_12.split("X")[0],name_12.split("X")[1])
    try:
        let_4.add(*polygons)
    except:
        let_4.add(polygons)
    polygons = Make_letter(location[0],int(layer_2[:-1]),8,8)
    try:
        let_5.add(*polygons)
    except:
        let_5.add(polygons)
    polygons = Make_letter(location[1],int(layer_2[:-1]),8,8)
    try:
        let_6.add(*polygons)
    except:
        let_6.add(polygons)
    name_box = gdstk.rectangle((0,0),(3000,3000))
    xor3 = gdstk.boolean(name_box,gdstk.Reference(let_3,(let_center_x,let_bottom_y3)),"and")
    pre_result.add(*xor3)
    xor4 = gdstk.boolean(name_box,gdstk.Reference(let_4,(let_center_x,let_bottom_y4)),"and")
    pre_result.add(*xor4)
    if type == "FRAME" or "BOT_" in type:
        pass
    else:
        if "TOP_" in type:
            xor5 = gdstk.boolean(name_box,gdstk.Reference(let_5,(box_center_x-10,34)),"and")
            pre_result.add(*xor5)
            xor6 = gdstk.boolean(name_box,gdstk.Reference(let_6,(box_center_x+2,34)),"and")
            pre_result.add(*xor6)
        else: 
            xor5 = gdstk.boolean(name_box,gdstk.Reference(let_5,(box_center_x-10,box_center_y-25)),"and")
            pre_result.add(*xor5)
            xor6 = gdstk.boolean(name_box,gdstk.Reference(let_6,(box_center_x+2,box_center_y-25)),"and")
            pre_result.add(*xor6)
    if "M" in layer_2:
        step1=gdstk.boolean(rect_bound,gdstk.Reference(pre_result,(0,0)),"not",layer=int(layer_2[:-1]))
    else:
        step1=gdstk.boolean(rect_bound,gdstk.Reference(pre_result,(0,0)),"and",layer=int(layer_2[:-1]))

    return step1

def generate_vernier(process,priority,gds_name,boundary,main_x,main_y,location):
    # gds split
    vernier_type = gds_name.split("_")[1][-1]
    layer_1 = gds_name.split("_")[3]
    layer_2 = gds_name.split("_")[4]
    if gds_name.split("_")[5][0] == "0":
        bar_in1 = "0."+gds_name.split("_")[5][1:]
    else:
        bar_in1 = gds_name.split("_")[5]
    name_11 = gds_name.split("_")[6]
    if gds_name.split("_")[7][0] == "0":
        bar_out1 = "0."+gds_name.split("_")[7][1:]
    else:
        bar_out1 = gds_name.split("_")[7]
    name_12 = gds_name.split("_")[8]
    if len(gds_name.split("_")) > 10:
        if gds_name.split("_")[9][0] == "0":
            bar_in2 = "0."+gds_name.split("_")[9][1:]
        else:
            bar_in2 = gds_name.split("_")[9]
        name_21 = gds_name.split("_")[10]
        if gds_name.split("_")[11][0] == "0":
            bar_out2 = "0."+gds_name.split("_")[11][1:]
        else:
            bar_out2 = gds_name.split("_")[11]
        name_22 = gds_name.split("_")[12]
    else:
        bar_in2 = "-"
        name_21 = "-"
        bar_out2 = "-"
        name_22 = "-"
    #Main
    cell_name = gds_name
    result = gdstk.Cell(cell_name)
    if vernier_type == "1":
        a = in_box(process,layer_1,main_x,main_y,bar_in1,name_11,location,"BOX")
        # Metal Name TM으로 변경
        if PROCESS[0] == "1830AN18BA" or PROCESS[0] == "181ABD18BA":
            if (layer_1[:-1] == "21" or layer_1[:-1] == "186" or layer_1[:-1] == "158") and (layer_2[:-1] == "10" or layer_2[:-1] == "12" or layer_2[:-1] == "14" or layer_2[:-1] == "16" or layer_2[:-1] == "18" or layer_2[:-1] == "20"):
                b = out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,"BOX","TM")
            else:
                b = out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,"BOX","-")
        elif PROCESS[0] == "709AHE35BA":
            if (layer_1[:-1] == "34" or layer_1[:-1] == "94" or layer_1[:-1] == "108") and (layer_2[:-1] == "27" or layer_2[:-1] == "29" or layer_2[:-1] == "31" or layer_2[:-1] == "33" or layer_2[:-1] == "43"):
                b = out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,"BOX","TM")
            else:
                b = out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,"BOX","-")
        else:
            b = out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,"BOX","-")
        try:
            result.add(*a)
            result.add(*b) 
        except:
            pass
    elif vernier_type == "2":
        a = in_box(process,layer_1,main_x,main_y,bar_in2,name_21,location,"TOP_CHAIN")
        b = out_box(process,layer_2,main_x,main_y,bar_out2,name_22,location,"TOP_BOX","-")
        c = in_box(process,layer_1,main_x,main_y,bar_in1,name_11,location,"BOT_BAR")
        d = out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,"BOT_BAR","-")
        try:
            result.add(*a)
            result.add(*b) 
            result.add(*c)
            result.add(*d) 
        except:
            pass
    elif vernier_type == "3":
        a = in_box(process,layer_1,main_x,main_y,bar_in2,name_21,location,"TOP_BOX")
        b = out_box(process,layer_2,main_x,main_y,bar_out2,name_22,location,"TOP_BOX","-")
        c = in_box(process,layer_1,main_x,main_y,bar_in1,name_11,location,"BOT_BAR")
        d = out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,"BOT_BAR","-")
        try:
            result.add(*a)
            result.add(*b) 
            result.add(*c)
            result.add(*d) 
        except:
            pass
    elif vernier_type == "4":
        a = in_box(process,layer_1,main_x,main_y,bar_in1,name_11,location,"CHAIN")
        b = out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,"BOX","-")
        try:
            result.add(*a)
            result.add(*b) 
        except:
            pass
    elif vernier_type == "5":
        a = in_box(process,layer_1,main_x,main_y,bar_in1,name_11,location,"FRAME")
        b = out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,"FRAME","-")
        try:
            result.add(*a)
            result.add(*b) 
        except:
            pass
    elif vernier_type == "6":
        a = in_box(process,layer_1,main_x,main_y,bar_in1,name_11,location,"CHAIN")
        b = out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,"BAR","-")
        try:
            result.add(*a)
            result.add(*b) 
        except:
            pass
    elif vernier_type == "7":
        a = in_box(process,layer_1,main_x,main_y,bar_in1,name_11,location,"BAR")
        b = out_box(process,layer_2,main_x,main_y,bar_out1,name_12,location,"BOX","-")
        try:
            result.add(*a)
            result.add(*b) 
        except:
            pass
    if boundary != "-":
        boundary_sp = boundary.split(",")
        for i in range(0,len(boundary_sp)):
            bound_1 = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=int(boundary_sp[i]))
            result.add(bound_1)
        if PROCESS[0] == "709AHE35BA":
            pass
        else:
            bound_56 = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=56)
            result.add(bound_56)
    else:
        if PROCESS[0] == "709AHE35BA":
            pass
        else:        
            bound_56 = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=56)
            result.add(bound_56)
    #name boundary
    box_center_x = (int(main_x)/2)+6
    box_center_y = (int(main_y)/2)+5
    #if vernier_type == "5" and ("SJ" in PROCESS[0] or "709AHE35BA" in PROCESS[0]):
    if vernier_type == "5" and "SJ" in PROCESS[0]:
        let_center_x = box_center_x-23
        box_center_y = int(main_y)/2
    else:
        let_center_x = box_center_x-22

    if vernier_type == "2" or vernier_type == "3":
        let_bottom_lay2_y1 = 17-3-int(name_11.split("X")[-1])-int(name_11.split("X")[-1])-0.5
        let_bottom_lay2_y2 = 17-0.5
        let_bottom_lay2_y3 = 59-3-int(name_12.split("X")[-1])-int(name_12.split("X")[-1])-0.5
        let_bottom_lay2_y4 = 59-0.5
        let_bottom_lay1_y1 = 17+0.5
        let_bottom_lay1_y2 = 17+3+int(name_21.split("X")[-1])+int(name_21.split("X")[-1])+0.5
        let_bottom_lay1_y3 = 59+0.5
        let_bottom_lay1_y4 = 59+3+int(name_22.split("X")[-1])+int(name_22.split("X")[-1])+0.5
    else:
        #if vernier_type == "5" and ("SJ" in PROCESS[0] or "709AHE35BA" in PROCESS[0]):
        if vernier_type == "5" and "SJ" in PROCESS[0]:
            if name_12.split("X")[-1] == "8":
                let_bottom_lay2_y1 = box_center_y-3-(int(name_12.split("X")[-1])*2)-0.5-2
            else:
                let_bottom_lay2_y1 = box_center_y-3-(int(name_12.split("X")[-1])*2)-0.5
            let_bottom_lay2_y2 = box_center_y-0.5
            let_bottom_lay1_y1 = box_center_y+0.5
            if  name_11.split("X")[-1] == "8":
                let_bottom_lay1_y2 = box_center_y+3+(int(name_11.split("X")[-1])*2)+0.5+2
            else:
                let_bottom_lay1_y2 = box_center_y+3+(int(name_11.split("X")[-1])*2)+0.5
        else:
            let_bottom_lay2_y1 = box_center_y-3-(int(name_12.split("X")[-1])*2)-0.5
            let_bottom_lay2_y2 = box_center_y-0.5
            let_bottom_lay1_y1 = box_center_y+0.5
            let_bottom_lay1_y2 = box_center_y+3+(int(name_11.split("X")[-1])*2)+0.5
    
    global NAME_PAD_1830AN18BA
    global NAME_PAD_1830BD15BA
    global NAME_PAD_709AHE35BA
    global NAME_PAD_SJ
    # NAME PAD
    if process == "1830AN18BA" or process == "181ABD18BA":
        try:
            ck_pad_1 = int(NAME_PAD_1830AN18BA[layer_1[:-1]]) 
        except:
            ck_pad_1 = ""
        try:
            ck_pad_2 = int(NAME_PAD_1830AN18BA[layer_2[:-1]])
        except:
            ck_pad_2 = ""
        if ck_pad_1 != "":
            let_bound_1 = gdstk.rectangle((let_center_x-(float(name_11.split("X")[0])/2)-0.5,let_bottom_lay1_y1),(let_center_x+(float(name_11.split("X")[0])/2)+0.5,let_bottom_lay1_y2), layer=ck_pad_1)
            result.add(let_bound_1)
        if ck_pad_2 != "":
            let_bound_2 = gdstk.rectangle((let_center_x-(float(name_12.split("X")[0])/2)-0.5,let_bottom_lay2_y1),(let_center_x+(float(name_12.split("X")[0])/2)+0.5,let_bottom_lay2_y2), layer=ck_pad_2)
            result.add(let_bound_2)

        if vernier_type == "2" or vernier_type == "3":
            if ck_pad_1 != "":
                let_bound_1_1 = gdstk.rectangle((let_center_x-(float(name_21.split("X")[0])/2)-0.5,let_bottom_lay1_y3),(let_center_x+(float(name_21.split("X")[0])/2)+0.5,let_bottom_lay1_y4), layer=ck_pad_1)
                result.add(let_bound_1_1)
            if ck_pad_2 != "":
                let_bound_2_1 = gdstk.rectangle((let_center_x-(float(name_22.split("X")[0])/2)-0.5,let_bottom_lay2_y3),(let_center_x+(float(name_22.split("X")[0])/2)+0.5,let_bottom_lay2_y4), layer=ck_pad_2)
                result.add(let_bound_2_1)
    elif process == "1830BD15BA":
        try:
            ck_pad_1 = int(NAME_PAD_1830BD15BA[layer_1[:-1]]) 
        except:
            ck_pad_1 = ""
        try:
            ck_pad_2 = int(NAME_PAD_1830BD15BA[layer_2[:-1]])
        except:
            ck_pad_2 = ""
        if ck_pad_1 != "":
            let_bound_1 = gdstk.rectangle((let_center_x-(float(name_11.split("X")[0])/2)-0.5,let_bottom_lay1_y1),(let_center_x+(float(name_11.split("X")[0])/2)+0.5,let_bottom_lay1_y2), layer=ck_pad_1)
            result.add(let_bound_1)
        if ck_pad_2 != "":
            let_bound_2 = gdstk.rectangle((let_center_x-(float(name_12.split("X")[0])/2)-0.5,let_bottom_lay2_y1),(let_center_x+(float(name_12.split("X")[0])/2)+0.5,let_bottom_lay2_y2), layer=ck_pad_2)
            result.add(let_bound_2)

        if vernier_type == "2" or vernier_type == "3":
            if ck_pad_1 != "":
                let_bound_1_1 = gdstk.rectangle((let_center_x-(float(name_21.split("X")[0])/2)-0.5,let_bottom_lay1_y3),(let_center_x+(float(name_21.split("X")[0])/2)+0.5,let_bottom_lay1_y4), layer=ck_pad_1)
                result.add(let_bound_1_1)
            if ck_pad_2 != "":
                let_bound_2_1 = gdstk.rectangle((let_center_x-(float(name_22.split("X")[0])/2)-0.5,let_bottom_lay2_y3),(let_center_x+(float(name_22.split("X")[0])/2)+0.5,let_bottom_lay2_y4), layer=ck_pad_2)
                result.add(let_bound_2_1)
    else:
        if "SJ" in process:
            try:
                ck_pad_1 = int(NAME_PAD_SJ[layer_1[:-1]]) 
            except:
                ck_pad_1 = ""
            try:
                ck_pad_2 = int(NAME_PAD_SJ[layer_2[:-1]])
            except:
                ck_pad_2 = ""
            if ck_pad_1 != "":
                let_bound_1 = gdstk.rectangle((let_center_x-(float(name_11.split("X")[0])/2)-0.5,let_bottom_lay1_y1),(let_center_x+(float(name_11.split("X")[0])/2)+0.5,let_bottom_lay1_y2), layer=ck_pad_1)
                result.add(let_bound_1)
            if ck_pad_2 != "":
                let_bound_2 = gdstk.rectangle((let_center_x-(float(name_12.split("X")[0])/2)-0.5,let_bottom_lay2_y1),(let_center_x+(float(name_12.split("X")[0])/2)+0.5,let_bottom_lay2_y2), layer=ck_pad_2)
                result.add(let_bound_2)

            if vernier_type == "2" or vernier_type == "3":
                if ck_pad_1 != "":
                    let_bound_1_1 = gdstk.rectangle((let_center_x-(float(name_21.split("X")[0])/2)-0.5,let_bottom_lay1_y3),(let_center_x+(float(name_21.split("X")[0])/2)+0.5,let_bottom_lay1_y4), layer=ck_pad_1)
                    result.add(let_bound_1_1)
                if ck_pad_2 != "":
                    let_bound_2_1 = gdstk.rectangle((let_center_x-(float(name_22.split("X")[0])/2)-0.5,let_bottom_lay2_y3),(let_center_x+(float(name_22.split("X")[0])/2)+0.5,let_bottom_lay2_y4), layer=ck_pad_2)
                    result.add(let_bound_2_1)
        else:
            try:
                ck_pad_1 = int(NAME_PAD_709AHE35BA[layer_1[:-1]]) 
            except:
                ck_pad_1 = ""
            try:
                ck_pad_2 = int(NAME_PAD_709AHE35BA[layer_2[:-1]])
            except:
                ck_pad_2 = ""
            if ck_pad_1 != "":
                let_bound_1 = gdstk.rectangle((let_center_x-(float(name_11.split("X")[0])/2)-0.5,let_bottom_lay1_y1),(let_center_x+(float(name_11.split("X")[0])/2)+0.5,let_bottom_lay1_y2), layer=ck_pad_1)
                result.add(let_bound_1)
            if ck_pad_2 != "":
                let_bound_2 = gdstk.rectangle((let_center_x-(float(name_12.split("X")[0])/2)-0.5,let_bottom_lay2_y1),(let_center_x+(float(name_12.split("X")[0])/2)+0.5,let_bottom_lay2_y2), layer=ck_pad_2)
                result.add(let_bound_2)

            if vernier_type == "2" or vernier_type == "3":
                if ck_pad_1 != "":
                    let_bound_1_1 = gdstk.rectangle((let_center_x-(float(name_21.split("X")[0])/2)-0.5,let_bottom_lay1_y3),(let_center_x+(float(name_21.split("X")[0])/2)+0.5,let_bottom_lay1_y4), layer=ck_pad_1)
                    result.add(let_bound_1_1)
                if ck_pad_2 != "":
                    let_bound_2_1 = gdstk.rectangle((let_center_x-(float(name_22.split("X")[0])/2)-0.5,let_bottom_lay2_y3),(let_center_x+(float(name_22.split("X")[0])/2)+0.5,let_bottom_lay2_y4), layer=ck_pad_2)
                    result.add(let_bound_2_1)

    return result
def start():
    cell = None
    res = None
    global PROCESS
    global PRORITY
    global LAYER_NO_1
    global LAYER_NO_2
    global GDS_NAME
    global PAD_NO
    global TYPE
    global MAIN_X
    global MAIN_Y

    PROCESS=[]
    PRORITY=[]
    LAYER_NO_1=[]
    LAYER_NO_2=[]
    GDS_NAME=[]
    PAD_NO=[]
    TYPE=[]
    MAIN_X=[]
    MAIN_Y=[]

    get_arr()
    lib1 = gdstk.Library()
    lib2 = gdstk.Library()
    lib3 = gdstk.Library()
    lib4 = gdstk.Library()
    cell1 = lib1.new_cell(PROCESS[0]+"_VERNIER_LL_"+MAIN_X[0]+"_"+time.strftime("%Y%m%d"))
    cell2 = lib2.new_cell(PROCESS[0]+"_VERNIER_LR_"+MAIN_X[0]+"_"+time.strftime("%Y%m%d"))
    cell3 = lib3.new_cell(PROCESS[0]+"_VERNIER_UL_"+MAIN_X[0]+"_"+time.strftime("%Y%m%d"))
    cell4 = lib4.new_cell(PROCESS[0]+"_VERNIER_UR"+MAIN_X[0]+"_"+time.strftime("%Y%m%d"))
    end_y1 = 0
    end_y2 = 0
    end_y3 = 0
    end_y4 = 0
    for i in range(0,len(PRORITY)):
        res = ""
        res = generate_vernier(PROCESS[0],PRORITY[i],GDS_NAME[i],PAD_NO[i],MAIN_X[i],MAIN_Y[i],"LL")   
        lib1.add(res)
        cell1.add(gdstk.Reference(res,(0,end_y1)))
        try:
            if PRORITY[i+1] == PRORITY[i]:
                pass
            else:
                if "SJ" in PROCESS[0]:
                    if (GDS_NAME[i].split('_')[4] == "21T" or GDS_NAME[i].split('_')[4] == "24T" or GDS_NAME[i].split('_')[4] == "27T") and (GDS_NAME[i+1].split('_')[4] == "21T" or GDS_NAME[i+1].split('_')[4] == "24T" or GDS_NAME[i+1].split('_')[4] == "27T"):
                        sj_bound_11=gdstk.rectangle((0,end_y1+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y1+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=11)
                        cell1.add(sj_bound_11)
                        sj_bound_17=gdstk.rectangle((0,end_y1+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y1+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=17)
                        cell1.add(sj_bound_17)
                        sj_bound_56=gdstk.rectangle((0,end_y1+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y1+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=56)
                        cell1.add(sj_bound_56)
                        end_y1=end_y1+int(MAIN_Y[i])+int(MAIN_Y[i])
                    else:
                        end_y1=end_y1+int(MAIN_Y[i])
                else:
                    end_y1=end_y1+int(MAIN_Y[i])
        except:
            pass
        res = ""
        res = generate_vernier(PROCESS[0],PRORITY[i],GDS_NAME[i],PAD_NO[i],MAIN_X[i],MAIN_Y[i],"LR")   
        lib2.add(res)
        cell2.add(gdstk.Reference(res,(0,end_y2)))
        try:
            if PRORITY[i+1] == PRORITY[i]:
                pass
            else:
                if "SJ" in PROCESS[0]:
                    if (GDS_NAME[i].split('_')[4] == "21T" or GDS_NAME[i].split('_')[4] == "24T" or GDS_NAME[i].split('_')[4] == "27T") and (GDS_NAME[i+1].split('_')[4] == "21T" or GDS_NAME[i+1].split('_')[4] == "24T" or GDS_NAME[i+1].split('_')[4] == "27T"):
                        sj_bound_11=gdstk.rectangle((0,end_y2+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y2+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=11)
                        cell2.add(sj_bound_11)
                        sj_bound_17=gdstk.rectangle((0,end_y2+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y2+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=17)
                        cell2.add(sj_bound_17)
                        sj_bound_56=gdstk.rectangle((0,end_y2+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y2+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=56)
                        cell2.add(sj_bound_56)
                        end_y2=end_y2+int(MAIN_Y[i])+int(MAIN_Y[i])
                    else:
                        end_y2=end_y2+int(MAIN_Y[i])
                else:
                    end_y2=end_y2+int(MAIN_Y[i])
        except:
            pass
        res = ""
        res = generate_vernier(PROCESS[0],PRORITY[i],GDS_NAME[i],PAD_NO[i],MAIN_X[i],MAIN_Y[i],"UL")   
        lib3.add(res)
        cell3.add(gdstk.Reference(res,(0,end_y3)))
        try:
            if PRORITY[i+1] == PRORITY[i]:
                pass
            else:
                if "SJ" in PROCESS[0]:
                    if (GDS_NAME[i].split('_')[4] == "21T" or GDS_NAME[i].split('_')[4] == "24T" or GDS_NAME[i].split('_')[4] == "27T") and (GDS_NAME[i+1].split('_')[4] == "21T" or GDS_NAME[i+1].split('_')[4] == "24T" or GDS_NAME[i+1].split('_')[4] == "27T"):
                        sj_bound_11=gdstk.rectangle((0,end_y3+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y3+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=11)
                        cell3.add(sj_bound_11)
                        sj_bound_17=gdstk.rectangle((0,end_y3+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y3+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=17)
                        cell3.add(sj_bound_17)
                        sj_bound_56=gdstk.rectangle((0,end_y3+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y3+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=56)
                        cell3.add(sj_bound_56)
                        end_y3=end_y3+int(MAIN_Y[i])+int(MAIN_Y[i])
                    else:
                        end_y3=end_y3+int(MAIN_Y[i])
                else:
                    end_y3=end_y3+int(MAIN_Y[i])
        except:
            pass
        res = ""
        res = generate_vernier(PROCESS[0],PRORITY[i],GDS_NAME[i],PAD_NO[i],MAIN_X[i],MAIN_Y[i],"UR")   
        lib4.add(res)
        cell4.add(gdstk.Reference(res,(0,end_y4)))
        try:
            if PRORITY[i+1] == PRORITY[i]:
                pass
            else:
                if "SJ" in PROCESS[0]:
                    if (GDS_NAME[i].split('_')[4] == "21T" or GDS_NAME[i].split('_')[4] == "24T" or GDS_NAME[i].split('_')[4] == "27T") and (GDS_NAME[i+1].split('_')[4] == "21T" or GDS_NAME[i+1].split('_')[4] == "24T" or GDS_NAME[i+1].split('_')[4] == "27T"):
                        sj_bound_11=gdstk.rectangle((0,end_y4+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y4+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=11)
                        cell4.add(sj_bound_11)
                        sj_bound_17=gdstk.rectangle((0,end_y4+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y4+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=17)
                        cell4.add(sj_bound_17)
                        sj_bound_56=gdstk.rectangle((0,end_y4+int(MAIN_Y[i])),(int(MAIN_X[i]),end_y4+int(MAIN_Y[i])+int(MAIN_Y[i])), layer=56)
                        cell4.add(sj_bound_56)
                        end_y4=end_y4+int(MAIN_Y[i])+int(MAIN_Y[i])
                    else:
                        end_y4=end_y4+int(MAIN_Y[i])
                else:
                    end_y4=end_y4+int(MAIN_Y[i])
        except:
            pass
    if cell1.references != [] :
        lib1.write_gds("./fab1/f1_gdsout/"+PROCESS[0]+"_VERNIER_LL_"+MAIN_X[0]+"_"+time.strftime("%Y%m%d")+".gds")
    if cell2.references != [] :
        lib2.write_gds("./fab1/f1_gdsout/"+PROCESS[0]+"_VERNIER_LR_"+MAIN_X[0]+"_"+time.strftime("%Y%m%d")+".gds")
    if cell3.references != [] :
        lib3.write_gds("./fab1/f1_gdsout/"+PROCESS[0]+"_VERNIER_UL_"+MAIN_X[0]+"_"+time.strftime("%Y%m%d")+".gds")
    if cell4.references != [] :
        lib4.write_gds("./fab1/f1_gdsout/"+PROCESS[0]+"_VERNIER_UR_"+MAIN_X[0]+"_"+time.strftime("%Y%m%d")+".gds")

if __name__ == "__main__":
    start()