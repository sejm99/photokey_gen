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

def get_arr():
    #input 파일 정보 가져오기
    with open('./fab1/s8000_input','r') as f:
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
                MAIN_X.append(line_sp[2].split('_')[1])
                MAIN_Y.append(line_sp[2].split('_')[2])
                BAR_X.append(line_sp[2].split('_')[3])
                BAR_Y.append(line_sp[2].split('_')[4])

def generate(priority,layer_no,gds_name,main_x,main_y,bar_x,bar_y):
    cell_name = gds_name
    result = gdstk.Cell(cell_name)
    bound_1 = gdstk.rectangle((((int(main_x)/2)-(int(bar_x)/2)),((int(main_y)/2)-(int(bar_y)/2))), (((int(main_x)/2)+(int(bar_x)/2)),((int(main_y)/2)+(int(bar_y)/2))), layer=int(layer_no))
    result.add(bound_1)
    bound_2 = gdstk.rectangle((((int(main_y)/2)-(int(bar_y)/2)),((int(main_x)/2)-(int(bar_x)/2))), (((int(main_y)/2)+(int(bar_y)/2)),((int(main_x)/2)+(int(bar_x)/2))), layer=int(layer_no))
    result.add(bound_2)
    if PROCESS[0] == "709AHE35BA":
        pass
    else:
        bound_3 = gdstk.rectangle((0,0),(int(main_x), int(main_y)), layer=56)
        result.add(bound_3)
    return result

def start():
    cell = None
    res = None
    global PROCESS
    global PRORITY
    global LAYER_NO
    global GDS_NAME
    global MAIN_X
    global MAIN_Y
    global BAR_X
    global BAR_Y
    PROCESS=[]
    PRORITY=[]
    LAYER_NO=[]
    GDS_NAME=[]
    MAIN_X=[]
    MAIN_Y=[]
    BAR_X=[]
    BAR_Y=[]
    get_arr()
    lib1 = gdstk.Library()
    cell1 = lib1.new_cell(PROCESS[0]+"_S8000_"+MAIN_X[0]+"_"+MAIN_Y[0]+"_"+time.strftime("%Y%m%d"))
    for i in range(0,len(PRORITY)):
        res = ""
        res = generate(PRORITY[i],LAYER_NO[i],GDS_NAME[i],MAIN_X[i],MAIN_Y[i],BAR_X[i],BAR_Y[i])   
        lib1.add(res)
        cell1.add(gdstk.Reference(res,(0,0)))
    if cell1.references != [] :
        lib1.write_gds("./fab1/f1_gdsout/"+PROCESS[0]+"_S8000_"+MAIN_X[0]+"_"+MAIN_Y[0]+"_"+time.strftime("%Y%m%d")+".gds")

if __name__ == "__main__":
    start()