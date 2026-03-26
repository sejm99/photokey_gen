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

def get_arr():
    #input 파일 정보 가져오기
    with open('./fab1/1st_overlay_input','r') as f:
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
                ETCH_TYPE.append(line_sp[2].split('_')[2][-1])
                MAIN_X.append(line_sp[2].split('_')[3])
                MAIN_Y.append(line_sp[2].split('_')[4])

def gen_20X20_box(layer_no,x,y):
    rect_20X20 = gdstk.rectangle((0+x,0+y),(20+x,20+y),layer=int(layer_no))
    return rect_20X20
def gen_20X20_4X4_ring(layer_no,x,y):
    rect_20X20 = gdstk.rectangle((0+x,0+y),(20+x,20+y),layer=int(layer_no))
    rect_8X8 = gdstk.rectangle((6+x,6+y),(14+x,14+y),layer=int(layer_no))
    rect_4X4 = gdstk.rectangle((8+x,8+y),(12+x,12+y),layer=int(layer_no))
    step1 = gdstk.boolean(rect_20X20,rect_8X8,"not",layer=int(layer_no))
    step2 = gdstk.boolean(step1,rect_4X4,"or",layer=int(layer_no))
    return step2
def gen_16X16_8X8_ring(layer_no,x,y):
    rect_16X16 = gdstk.rectangle((2+x,2+y),(18+x,18+y),layer=int(layer_no))
    rect_12X12 = gdstk.rectangle((4+x,4+y),(16+x,16+y),layer=int(layer_no))
    rect_8X8 = gdstk.rectangle((6+x,6+y),(14+x,14+y),layer=int(layer_no))
    step1 = gdstk.boolean(rect_16X16,rect_12X12,"not",layer=int(layer_no))
    step2 = gdstk.boolean(step1,rect_8X8,"or",layer=int(layer_no))
    return step2
def gen_type2_ll(layer_no,x,y):
    rect = gdstk.rectangle((0,0),(100,100))
    pre_result = gdstk.Cell("pre_reuslt")
    pre_result.add(gdstk.rectangle((6+x,6+y),(10+x,10+y),layer=int(layer_no)))
    points = [(0+x,0+y),(0+x,8+y),(2+x,8+y),(2+x,2+y),(8+x,2+y),(8+x,0+y),(0+x,0+y)]
    pre_result.add(gdstk.Polygon(points))
    step1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"and",layer=int(layer_no))
    return step1
def gen_type2_lr(layer_no,x,y):
    rect = gdstk.rectangle((0,0),(100,100))
    pre_result = gdstk.Cell("pre_reuslt")
    pre_result.add(gdstk.rectangle((6+x,6+y),(10+x,10+y),layer=int(layer_no)))
    points = [(8+x,0+y),(8+x,2+y),(14+x,2+y),(14+x,8+y),(16+x,8+y),(16+x,0+y),(8+x,0+y)]
    pre_result.add(gdstk.Polygon(points))
    step1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"and",layer=int(layer_no))
    return step1
def gen_type2_ul(layer_no,x,y):
    rect = gdstk.rectangle((0,0),(100,100))
    pre_result = gdstk.Cell("pre_reuslt")
    pre_result.add(gdstk.rectangle((6+x,6+y),(10+x,10+y),layer=int(layer_no)))
    points = [(0+x,8+y),(0+x,16+y),(8+x,16+y),(8+x,14+y),(2+x,14+y),(2+x,8+y),(0+x,8+y)]
    pre_result.add(gdstk.Polygon(points))
    step1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"and",layer=int(layer_no))
    return step1
def gen_type2_ur(layer_no,x,y):
    rect = gdstk.rectangle((0,0),(100,100))
    pre_result = gdstk.Cell("pre_reuslt")
    pre_result.add(gdstk.rectangle((6+x,6+y),(10+x,10+y),layer=int(layer_no)))
    points = [(14+x,8+y),(14+x,14+y),(8+x,14+y),(8+x,16+y),(16+x,16+y),(16+x,8+y),(14+x,8+y)]
    pre_result.add(gdstk.Polygon(points))
    step1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"and",layer=int(layer_no))
    return step1
def generate_LL(priority,layer_no,gds_name,boundary,etch_type,main_x,main_y):
    cell_name = gds_name + "_" + layer_no
    result = gdstk.Cell(cell_name)
    box_ll = ""
    box_lr = ""
    box_ul = ""
    box_ur = ""
    if etch_type == "1":
        box_ll = gen_20X20_4X4_ring(layer_no,3,3)
        box_lr = gen_20X20_4X4_ring(layer_no,27,3)
        box_ul = gen_20X20_box(layer_no,3,27)
        box_ur = gen_20X20_box(layer_no,27,27)
    else:
        box_ll = gen_type2_ll(layer_no,5,5)
        box_lr = gen_type2_ll(layer_no,29,5)
        box_ul = gen_type2_ll(layer_no,5,29)
        box_ur = gen_type2_ll(layer_no,29,29)
    try:
        result.add(*box_ll)
    except:
        result.add(box_ll)
    try:
        result.add(*box_lr)
    except:
        result.add(box_lr)
    try:
        result.add(*box_ul)
    except:
        result.add(box_ul)
    try:
        result.add(*box_ur)
    except:
        result.add(box_ur)
    boundary_sp = boundary.split(",")
    for i in range(0,len(boundary_sp)):
        bound_1 = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=int(boundary_sp[i]))
        result.add(bound_1)
    if PROCESS[0] == "709AHE35BA":
        pass
    else:
        bound_56 = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=56)
        result.add(bound_56)
    return result

def generate_LR(priority,layer_no,gds_name,boundary,etch_type,main_x,main_y):
    cell_name = gds_name + "_" + layer_no
    result = gdstk.Cell(cell_name)
    box_ll = ""
    box_lr = ""
    box_ul = ""
    box_ur = ""
    if etch_type == "1":
        box_ll = gen_16X16_8X8_ring(layer_no,3,3)
        box_lr = gen_20X20_box(layer_no,27,3)
        box_ul = gen_20X20_box(layer_no,3,27)
        box_ur = gen_20X20_4X4_ring(layer_no,27,27)
    else:
        box_ll = gen_type2_lr(layer_no,5,5)
        box_lr = gen_type2_lr(layer_no,29,5)
        box_ul = gen_type2_lr(layer_no,5,29)
        box_ur = gen_type2_lr(layer_no,29,29)
    try:
        result.add(*box_ll)
    except:
        result.add(box_ll)
    try:
        result.add(*box_lr)
    except:
        result.add(box_lr)
    try:
        result.add(*box_ul)
    except:
        result.add(box_ul)
    try:
        result.add(*box_ur)
    except:
        result.add(box_ur)
    boundary_sp = boundary.split(",")
    for i in range(0,len(boundary_sp)):
        bound_1 = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=int(boundary_sp[i]))
        result.add(bound_1)
    if PROCESS[0] == "709AHE35BA":
        pass
    else:
        bound_56 = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=56)
        result.add(bound_56)
    return result

def generate_UL(priority,layer_no,gds_name,boundary,etch_type,main_x,main_y):
    cell_name = gds_name + "_" + layer_no
    result = gdstk.Cell(cell_name)
    box_ll = ""
    box_lr = ""
    box_ul = ""
    box_ur = ""
    if etch_type == "1":
        box_ll = gen_20X20_box(layer_no,3,3)
        box_lr = gen_16X16_8X8_ring(layer_no,27,3)
        box_ul = gen_20X20_4X4_ring(layer_no,3,27)
        box_ur = gen_20X20_box(layer_no,27,27)
    else:
        box_ll = gen_type2_ul(layer_no,5,5)
        box_lr = gen_type2_ul(layer_no,29,5)
        box_ul = gen_type2_ul(layer_no,5,29)
        box_ur = gen_type2_ul(layer_no,29,29)
    try:
        result.add(*box_ll)
    except:
        result.add(box_ll)
    try:
        result.add(*box_lr)
    except:
        result.add(box_lr)
    try:
        result.add(*box_ul)
    except:
        result.add(box_ul)
    try:
        result.add(*box_ur)
    except:
        result.add(box_ur)
    boundary_sp = boundary.split(",")
    for i in range(0,len(boundary_sp)):
        bound_1 = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=int(boundary_sp[i]))
        result.add(bound_1)
    if PROCESS[0] == "709AHE35BA":
        pass
    else:
        bound_56 = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=56)
        result.add(bound_56)
    return result

def generate_UR(priority,layer_no,gds_name,boundary,etch_type,main_x,main_y):
    cell_name = gds_name + "_" + layer_no
    result = gdstk.Cell(cell_name)
    box_ll = ""
    box_lr = ""
    box_ul = ""
    box_ur = ""
    if etch_type == "1":
        box_ll = gen_20X20_box(layer_no,3,3)
        box_lr = gen_20X20_box(layer_no,27,3)
        box_ul = gen_16X16_8X8_ring(layer_no,3,27)
        box_ur = gen_16X16_8X8_ring(layer_no,27,27)
    else:
        box_ll = gen_type2_ur(layer_no,5,5)
        box_lr = gen_type2_ur(layer_no,29,5)
        box_ul = gen_type2_ur(layer_no,5,29)
        box_ur = gen_type2_ur(layer_no,29,29)
    try:
        result.add(*box_ll)
    except:
        result.add(box_ll)
    try:
        result.add(*box_lr)
    except:
        result.add(box_lr)
    try:
        result.add(*box_ul)
    except:
        result.add(box_ul)
    try:
        result.add(*box_ur)
    except:
        result.add(box_ur)
    boundary_sp = boundary.split(",")
    for i in range(0,len(boundary_sp)):
        bound_1 = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=int(boundary_sp[i]))
        result.add(bound_1)
    if PROCESS[0] == "709AHE35BA":
        pass
    else:
        bound_56 = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=56)
        result.add(bound_56)
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
    global PAD_NO
    global ETCH_TYPE

    PROCESS=[]
    PRORITY=[]
    LAYER_NO=[]
    GDS_NAME=[]
    PAD_NO=[]
    ETCH_TYPE=[]
    MAIN_X=[]
    MAIN_Y=[]

    get_arr()
    lib1 = gdstk.Library()
    lib2 = gdstk.Library()
    lib3 = gdstk.Library()
    lib4 = gdstk.Library()
    cell1 = lib1.new_cell(PROCESS[0]+"_1ST_OVERLAY_LL_"+MAIN_X[0]+"_"+MAIN_Y[0]+"_"+time.strftime("%Y%m%d"))
    cell2 = lib2.new_cell(PROCESS[0]+"_1ST_OVERLAY_LR_"+MAIN_X[0]+"_"+MAIN_Y[0]+"_"+time.strftime("%Y%m%d"))
    cell3 = lib3.new_cell(PROCESS[0]+"_1ST_OVERLAY_UL_"+MAIN_X[0]+"_"+MAIN_Y[0]+"_"+time.strftime("%Y%m%d"))
    cell4 = lib4.new_cell(PROCESS[0]+"_1ST_OVERLAY_UR_"+MAIN_X[0]+"_"+MAIN_Y[0]+"_"+time.strftime("%Y%m%d"))
    for i in range(0,len(PRORITY)):
        res = ""
        res = generate_LL(PRORITY[i],LAYER_NO[i],GDS_NAME[i],PAD_NO[i],ETCH_TYPE[i],MAIN_X[i],MAIN_Y[i])   
        lib1.add(res)
        cell1.add(gdstk.Reference(res,(0,0)))
        res = ""
        res = generate_LR(PRORITY[i],LAYER_NO[i],GDS_NAME[i],PAD_NO[i],ETCH_TYPE[i],MAIN_X[i],MAIN_Y[i])   
        lib2.add(res)
        cell2.add(gdstk.Reference(res,(0,0)))
        res = ""
        res = generate_UL(PRORITY[i],LAYER_NO[i],GDS_NAME[i],PAD_NO[i],ETCH_TYPE[i],MAIN_X[i],MAIN_Y[i])   
        lib3.add(res)
        cell3.add(gdstk.Reference(res,(0,0)))
        res = ""
        res = generate_UR(PRORITY[i],LAYER_NO[i],GDS_NAME[i],PAD_NO[i],ETCH_TYPE[i],MAIN_X[i],MAIN_Y[i])   
        lib4.add(res)
        cell4.add(gdstk.Reference(res,(0,0)))
    if cell1.references != [] :
        lib1.write_gds("./fab1/f1_gdsout/"+PROCESS[0]+"_1ST_OVERLAY_LL_"+MAIN_X[0]+"_"+MAIN_Y[0]+"_"+time.strftime("%Y%m%d")+".gds")
    if cell2.references != [] :
        lib2.write_gds("./fab1/f1_gdsout/"+PROCESS[0]+"_1ST_OVERLAY_LR_"+MAIN_X[0]+"_"+MAIN_Y[0]+"_"+time.strftime("%Y%m%d")+".gds")
    if cell3.references != [] :
        lib3.write_gds("./fab1/f1_gdsout/"+PROCESS[0]+"_1ST_OVERLAY_UL_"+MAIN_X[0]+"_"+MAIN_Y[0]+"_"+time.strftime("%Y%m%d")+".gds")
    if cell4.references != [] :
        lib4.write_gds("./fab1/f1_gdsout/"+PROCESS[0]+"_1ST_OVERLAY_UR_"+MAIN_X[0]+"_"+MAIN_Y[0]+"_"+time.strftime("%Y%m%d")+".gds")

if __name__ == "__main__":
    start()