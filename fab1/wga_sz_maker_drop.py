import gdstk
import sys, time
import numpy as np

PROCESS=[]
PRORITY=[]
LAYER_NO=[]
GDS_NAME=[]
PAD_NO=[]
ETCH_TYPE=[]
MAIN_X=[]
MAIN_Y=[]
BAR_X=[]
BAR_Y=[]
ARR_X=[]
ARR_Y=[]

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

def get_arr():
    #input 파일 정보 가져오기
    with open('./fab1/wga_sz_input','r') as f:
        lines = f.readlines()
        for line in lines:
            line_st=line.strip()
            line_sp=line_st.split()
            if line_sp[0] == "PROCESS":
                PROCESS.append(line_sp[1])
            else:
                PRORITY.append(line_sp[0])
                LAYER_NO.append(line_sp[1])
                GDS_NAME.append(line_sp[2])
                PAD_NO.append(line_sp[3])
                ETCH_TYPE.append(line_sp[2].split('_')[-1])
                BAR_Y.append(line_sp[2].split('_')[-3]+'.'+line_sp[2].split('_')[-2])
                BAR_X.append(line_sp[2].split('_')[-5]+'.'+line_sp[2].split('_')[-4])
                MAIN_Y.append(line_sp[2].split('_')[-6])
                MAIN_X.append(line_sp[2].split('_')[-7])


def PRO_ARR_SIZE_SORT_X():
    #PRORITY 별 최대 Size 찾기 - X
    ARR_SIZE_PRE=[]
    ARR_DEL=[]
    for i in range(0,len(PRORITY)):
        if int(PRORITY[i]) < 10:
            if '0'+PRORITY[i]+"_"+MAIN_X[i] in ARR_SIZE_PRE:
                pass
            else:
                ARR_SIZE_PRE.append('0'+PRORITY[i]+"_"+MAIN_X[i])
        else:
            if PRORITY[i]+"_"+MAIN_X[i] in ARR_SIZE_PRE:
                pass
            else:
                ARR_SIZE_PRE.append(PRORITY[i]+"_"+MAIN_X[i])
    for i in range(0,len(ARR_SIZE_PRE)):
        for j in range(0,len(ARR_SIZE_PRE)):
            if i == j:
                pass
            else:
                if ARR_SIZE_PRE[i][:2] == ARR_SIZE_PRE[j][:2]:
                    if float(ARR_SIZE_PRE[i].split("_")[-1]) > float(ARR_SIZE_PRE[j].split("_")[-1]):
                        ARR_DEL.append(ARR_SIZE_PRE[j])
                    else:
                        ARR_DEL.append(ARR_SIZE_PRE[i])
    for i in range(0,len(ARR_DEL)):
        try:
            ARR_SIZE_PRE.remove(ARR_DEL[i])
        except:
            pass
    ARR_SIZE_PRE.sort(key=lambda x:(x[0],x[1]))
    #빈공간 채우기
    for i in range(1, int(ARR_SIZE_PRE[-1].split("_")[0])):
        st_ck=0
        for j in range(0,len(ARR_SIZE_PRE)):
            if "0"+str(i)+"_" in ARR_SIZE_PRE[j]:
                st_ck=1
                break
            else:
                pass
        if st_ck == 0:
            ARR_SIZE_PRE.append("0"+str(i)+"_"+ARR_SIZE_PRE[0].split("_")[-1])
    
    ARR_SIZE_PRE.sort(key=lambda x:(x[0],x[1]))
    
    return ARR_SIZE_PRE

def PRO_ARR_SIZE_SORT_Y():
    #PRORITY 별 최대 Size 찾기 - Y
    ARR_SIZE_PRE=[]
    ARR_DEL=[]
    for i in range(0,len(PRORITY)):
        if int(PRORITY[i]) < 10:
            if '0'+PRORITY[i]+"_"+MAIN_Y[i] in ARR_SIZE_PRE:
                pass
            else:
                ARR_SIZE_PRE.append('0'+PRORITY[i]+"_"+MAIN_Y[i])
        else:
            if PRORITY[i]+"_"+MAIN_Y[i] in ARR_SIZE_PRE:
                pass
            else:
                ARR_SIZE_PRE.append(PRORITY[i]+"_"+MAIN_Y[i])
    for i in range(0,len(ARR_SIZE_PRE)):
        for j in range(0,len(ARR_SIZE_PRE)):
            if i == j:
                pass
            else:
                if ARR_SIZE_PRE[i][:2] == ARR_SIZE_PRE[j][:2]:
                    if float(ARR_SIZE_PRE[i].split("_")[-1]) > float(ARR_SIZE_PRE[j].split("_")[-1]):
                        ARR_DEL.append(ARR_SIZE_PRE[j])
                    else:
                        ARR_DEL.append(ARR_SIZE_PRE[i])
    for i in range(0,len(ARR_DEL)):
        try:
            ARR_SIZE_PRE.remove(ARR_DEL[i])
        except:
            pass
    ARR_SIZE_PRE.sort(key=lambda x:(x[0],x[1]))
    #빈공간 채우기
    for i in range(1, int(ARR_SIZE_PRE[-1].split("_")[0])):
        st_ck=0
        for j in range(0,len(ARR_SIZE_PRE)):
            if "0"+str(i)+"_" in ARR_SIZE_PRE[j]:
                st_ck=1
                break
            else:
                pass
        if st_ck == 0:
            ARR_SIZE_PRE.append("0"+str(i)+"_"+ARR_SIZE_PRE[0].split("_")[-1])
    
    ARR_SIZE_PRE.sort(key=lambda x:(x[0],x[1]))
    return ARR_SIZE_PRE
def generate(priority,layer_no,gds_name,boundary,etch_type,main_x,main_y,bar_x,bar_y,process):
    cell_name = gds_name+"_"+layer_no+"_"+etch_type
    result = gdstk.Cell(cell_name)
    pre_result = gdstk.Cell("pre_reuslt")
    boundary_sp = boundary.split(",")
    #Boundary
    for i in range(0,len(boundary_sp)):
        if process == "0600SJ00BB" or process == "0650SJ00BD":
            if boundary_sp[i] == "11" or boundary_sp[i] == "17":
                bound_1 = gdstk.rectangle((15, 0),(int(main_x)+15+50,int(main_y)), layer=int(boundary_sp[i]))
                result.add(bound_1)
            else:
                bound_1 = gdstk.rectangle((15, 0),(int(main_x)+15,int(main_y)), layer=int(boundary_sp[i]))
                result.add(bound_1)
        elif process == "709AHE35BA":
            if boundary_sp[i] == "34" or boundary_sp[i] == "108" or boundary_sp[i] == "94" or boundary_sp[i] == "112":
                bound_1 = gdstk.rectangle((15, 0),(int(main_x)+15+50,int(main_y)), layer=int(boundary_sp[i]))
                result.add(bound_1)
            else:
                bound_1 = gdstk.rectangle((15, 0),(int(main_x)+15,int(main_y)), layer=int(boundary_sp[i]))
                result.add(bound_1)
        else:
            if boundary_sp[i] == "21" or boundary_sp[i] == "158" or boundary_sp[i] == "186" or boundary_sp[i] == "86":
                bound_1 = gdstk.rectangle((15, 0),(int(main_x)+15+50,int(main_y)), layer=int(boundary_sp[i]))
                result.add(bound_1)
            else:
                bound_1 = gdstk.rectangle((15, 0),(int(main_x)+15,int(main_y)), layer=int(boundary_sp[i]))
                result.add(bound_1)
    #Main
    for i in range(0,3):
        if i == 0:
            x1=59+15-float(bar_x)/2
        elif i ==1:
            x1=72+15-float(bar_x)/2
        elif i==2:
            x1=91+15-float(bar_x)/2
        for j in range(0,8):
            y1 = 2.5+((3+float(bar_y))*j)
            wga_s_z1 = gdstk.rectangle((x1, y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
            pre_result.add(wga_s_z1)
    if etch_type == "M":
        rect = gdstk.rectangle((15, 0),(int(main_x)+15,int(main_y)))
        wga_s_z2 = gdstk.boolean(rect,gdstk.Reference(pre_result),"not",layer=int(layer_no))
        result.add(*wga_s_z2)
    else:
        rect = gdstk.rectangle((15, 0),(int(main_x)+15,int(main_y)))
        wga_s_z2 = gdstk.boolean(rect,gdstk.Reference(pre_result),"and",layer=int(layer_no))
        result.add(*wga_s_z2)
    return result

def generate_name(priority,layer_no,gds_name,boundary,etch_type,main_x,main_y,bar_x,bar_y,process):
    cell_name = gds_name+"_"+layer_no+"_name"
    result = gdstk.Cell(cell_name)
    pre_result = gdstk.Cell("cell_name")
    let_1 = gdstk.Cell("let_1_text")
    let_2 = gdstk.Cell("let_2_text")
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
        Layer_name = BD18_NAME[int(layer_no)]
    elif process=="181ABD18BA":
        Layer_name = XH18_NAME[int(layer_no)]
    elif process=="1830BD15BA":
        Layer_name = BD15_NAME[int(layer_no)]
    elif process=="0600SJ00BB":
        Layer_name = GEN2_NAME[int(layer_no)]
    elif process=="0650SJ00BD":
        Layer_name = GEN3_NAME[int(layer_no)]
    elif process=="709AHE35BA":
        Layer_name = BD35_NAME[int(layer_no)]
    else:
        print("Layer Name Is Not Defined :"+process)
        sys.exit()
    if Layer_name == "-":
        print("Layer Name Is Not Defined :"+process)
        print(layer_no)
        sys.exit()
    polygons = Make_letter(Layer_name[0],int(layer_no),10,10)
    try:
        let_1.add(*polygons)
    except:
        let_1.add(polygons)
    pre_result.add(gdstk.Reference(let_1,((int(main_y)/4)-5,2.5)))
    polygons = Make_letter(Layer_name[1],int(layer_no),10,10)
    try:
        let_2.add(*polygons)
    except:
        let_2.add(polygons)
    pre_result.add(gdstk.Reference(let_2,(((int(main_y)/4)*3)-5,2.5)))  

    rect = gdstk.rectangle((0, 0),(int(main_y),15))
    if etch_type == "M":
        text_1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"not",layer=int(layer_no))
    else:
        text_1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"and",layer=int(layer_no))
    result.add(*text_1)
    
    #boundary
    boundary_sp = boundary.split(",")
    for i in range(0,len(boundary_sp)):
        bound_1 = gdstk.rectangle((0, 0),(int(main_y),15), layer=int(boundary_sp[i]))
        result.add(bound_1)
    return result
    
def main(priority,layer_no,gds_name,boundary,etch_type,main_x,main_y,bar_x,bar_y,process):
    res = generate(priority,layer_no,gds_name,boundary,etch_type,main_x,main_y,bar_x,bar_y,process)
    return res

def main_name(priority,layer_no,gds_name,boundary,etch_type,main_x,main_y,bar_x,bar_y,process):
    res = generate_name(priority,layer_no,gds_name,boundary,etch_type,main_x,main_y,bar_x,bar_y,process)
    return res

def start():
    cell = None
    res = None
    res1 = None
    global PROCESS
    global PRORITY
    global LAYER_NO
    global GDS_NAME
    global PAD_NO
    global ETCH_TYPE
    global MAIN_X
    global MAIN_Y
    global BAR_X
    global BAR_Y
    global ARR_X
    global ARR_Y
    PROCESS=[]
    PRORITY=[]
    LAYER_NO=[]
    GDS_NAME=[]
    PAD_NO=[]
    ETCH_TYPE=[]
    MAIN_X=[]
    MAIN_Y=[]
    BAR_X=[]
    BAR_Y=[]
    ARR_X=[]
    ARR_Y=[]
    get_arr()
    ARR_SIZE_X = PRO_ARR_SIZE_SORT_X()
    #ARR_SIZE_Y = PRO_ARR_SIZE_SORT_Y()
    lib = gdstk.Library()
    cell = lib.new_cell(PROCESS[0]+"_WGA_SZ_50_"+time.strftime("%Y%m%d"))
    for i in range(0,len(PRORITY)):
        res = main(PRORITY[i],LAYER_NO[i],GDS_NAME[i],PAD_NO[i],ETCH_TYPE[i],MAIN_X[i],MAIN_Y[i],BAR_X[i],BAR_Y[i],PROCESS[0]) 
        lib.add(res)
        str_x = 0
        for j in range(0,len(ARR_SIZE_X)):
            if int(ARR_SIZE_X[j].split("_")[0]) < int(PRORITY[i]):
                str_x = str_x + 15 + int(ARR_SIZE_X[j].split("_")[-1]) + 50
            else:
                break
        cell.add(gdstk.Reference(res,(str_x,0)))
        res1 = main_name(PRORITY[i],LAYER_NO[i],GDS_NAME[i],PAD_NO[i],ETCH_TYPE[i],MAIN_X[i],MAIN_Y[i],BAR_X[i],BAR_Y[i],PROCESS[0]) 
        lib.add(res1)
        cell.add(gdstk.Reference(res1,(str_x,float(MAIN_Y[i])),rotation=np.pi*1.5))
    lib.write_gds("./fab1/f1_gdsout/WGA_SZ.gds")

if __name__ == "__main__":
    start()