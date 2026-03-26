import gdstk

LAYER_NO=[]
DA_TONE=[]
SL_TONE=[]

def layer_define():
    global LAYER_NO
    global DA_TONE
    global SL_TONE
    LAYER_NO=[]
    DA_TONE=[]
    SL_TONE=[]
    with open('./BD18_LAYER.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line_st=line.strip()
            line_sp=line_st.split()
            LAYER_NO.append(line_sp[0])
            DA_TONE.append(line_sp[2])
            SL_TONE.append(line_sp[3])

def Make_letter(input,layer_no,scale_x,scale_y):
    x=float(scale_x)
    y=float(scale_y)
    if input == "A":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "B":
        points = [(0,0),(0,1*y),(0.85*x,1*y),(1*x,0.85*y),(1*x,0.6*y),(0.9*x,0.5*y),(1*x,0.4*y),(1*x,0.15*y),(0.85*x,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "C":
        points = [(0.2*x,0),(0,0.2*y),(0,0.3*y),(0.9*x,0.3*y),(1*x,0.2*y),(1*x,0.1*y),(0.9*x,0),(0.2*x,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0,0.3*y),(0.3*x,0.7*y))
        points = [(0,0.7*y),(0,0.8*y),(0.2*x,1*y),(0.9*x,1*y),(1*x,0.9*y),(1*x,0.8*y),(0.9*x,0.7*y),(0,0.7*y)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "D":
        points = [(0,0),(0,1*y),(0.85*x,1*y),(1*x,0.85*y),(1*x,0.15*y),(0.85*x,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "E":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(1*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "F":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0),(1*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "G":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.4*y),(0.5*x,0.6*y))
        rect4 = gdstk.rectangle((0.3*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        step3 = gdstk.boolean(step2,rect4,"not",layer=int(layer_no))
        return step3
    elif input == "H":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "I":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.2*y),(0.35*x,0.8*y))
        rect3 = gdstk.rectangle((0.65*x,0.2*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "J":
        points = [(0,0),(0,0.2*y),(0.35*x,0.2*y),(0.45*x,0.3*y),(0.45*x,0.8*y),(0.7*x,0.8*y),(0.7*x,0.2*y),(0.5*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0,0.8*y),(1*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "K":
        rect1 = gdstk.rectangle((0,0),(0.3*x,1*y))
        points = [(0.3*x,0.35*y),(0.45*x,0.35*y),(0.8*x,0),(1*x,0),(1*x,0.2*y),(0.7*x,0.5*y),(1*x,0.8*y),(1*x,1*y),(0.8*x,1*y),(0.45*x,0.6*y),(0.3*x,0.6*y),(0.3*x,0.4*y),(0.3*x,0.35*y)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "L":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.3*y),(1*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "M":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0),(0.75*x,0),(0.75*x,0.6*y),(0.5*x,0.35*y),(0.25*x,0.6*y),(0.25*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.2*x,1*y),(0.5*x,0.7*y),(0.8*x,1*y),(0.2*x,1*y)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "N":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        points = [(0.3*x,0),(0.3*x,0.5*y),(0.8*x,0),(0.3*x,0)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.2*x,1*y),(0.7*x,0.5*y),(0.7*x,1*y),(0.2*x,1*y)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "O":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "P":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0),(1*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "Q":
        points = [(0,0.2*y),(0,0.8*y),(0.2*x,1*y),(0.8*x,1*y),(1*x,0.8*y),(1*x,0.2*y),(0.8*x,0),(0.2*x,0),(0,0.2*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.8*y))
        points = [(0.8*x,0),(0.9*x,-0.1*y),(1*x,0),(0.9*x,0.1*y),(0.8*x,0)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "R":
        points = [(0,0),(0,1*y),(0.8*x,1*y),(1*x,0.8*y),(1*x,0.6*y),(0.9*x,0.5*y),(1*x,0.4*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.3*x,0),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "S":
        points = [(0.2*x,0),(0,0.2*y),(0,0.3*y),(0.3*x,0.3*y),(0.3*x,0.2*y),(0.7*x,0.2*y),(0.7*x,0.4*y),(1*x,0.4*y),(1*x,0.2*y),(0.8*x,0),(0.2*x,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.7*x,0.4*y),(0.2*x,0.4*y),(0,0.6*y),(0,0.8*y),(0.2*x,1*y),(0.8*x,1*y),(1*x,0.8*y),(1*x,0.7*y),(0.7*x,0.7*y),(0.7*x,0.8*y),(0.3*x,0.8*y),(0.3*x,0.6*y),(0.8*x,0.6*y),(1*x,0.4*y),(0.7*x,0.4*y)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "T":
        rect1 = gdstk.rectangle((0,0.7*y),(1*x,1*y))
        rect2 = gdstk.rectangle((0.35*x,0),(0.65*x,0.7*y))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "U":
        points = [(0,0),(0,1*y),(0.3*x,1*y),(0.3*x,0.35*y),(0.35*x,0.3*y),(0.65*x,0.3*y),(0.7*x,0.35*y),(0.7*x,1*y),(1*x,1*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0,0),(0,0.2*y),(0.2*x,0),(0,0)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.8*x,0),(1*x,0.2*y),(1*x,0),(0.8*x,0)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "V":
        points = [(0.32*x,0),(0,0.32*y),(0,1*y),(1*x,1*y),(1*x,0.32*y),(0.68*x,0),(0.32*x,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.3*x,1*y),(0.3*x,0.44*y),(0.5*x,0.24*y),(0.7*x,0.44*y),(0.7*x,1*y),(0.3*x,1*y)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "W":
        points = [(0,0.2*y),(0,1*y),(1*x,1*y),(1*x,0.2*y),(0.8*x,0),(0.5*x,0.3*y),(0.2*x,0),(0,0.2*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.3*x,1*y),(0.3*x,0.4*y),(0.5*x,0.6*y),(0.7*x,0.4*y),(0.7*x,1*y),(0.3*x,1*y)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "X":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        points = [(0.2*x,0),(0.5*x,0.3*y),(0.8*x,0),(0.2*x,0)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0,0.2*y),(0.3*x,0.5*y),(0,0.8*y),(0,0.2*y)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.2*x,1*y),(0.5*x,0.7*y),(0.8*x,1*y),(0.2*x,1*y)]
        rect4 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(1*x,0.8*y),(0.7*x,0.5*y),(1*x,0.2*y),(1*x,0.8*y)]
        rect5 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect2,rect3,"or",layer=int(layer_no))
        step2 = gdstk.boolean(rect4,rect5,"or",layer=int(layer_no))
        step3 = gdstk.boolean(step1,step2,"or",layer=int(layer_no))
        step4 = gdstk.boolean(rect1,step3,"not",layer=int(layer_no))
        return step4
    elif input == "Y":
        rect1 = gdstk.rectangle((0.35*x,0),(0.65*x,0.45*y))
        points = [(0.35*x,0.45*y),(0,0.8*y),(0,1*y),(0.2*x,1*y),(0.5*x,0.7*y),(0.8*x,1*y),(1*x,1*y),(1*x,0.8*y),(0.65*x,0.45*y),(0.35*x,0.45*y)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "Z":
        points = [(0,0),(0,0.2*y),(0.55*x,0.75*y),(0,0.75*y),(0,1*y),(1*x,1*y),(1*x,0.8*y),(0.45*x,0.25*y),(1*x,0.25*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "0":
        points = [(0,0.15*y),(0,0.85*y),(0.15*x,1*y),(0.85*x,1*y),(1*x,0.85*y),(1*x,0.15*y),(0.85*x,0),(0.15*x,0),(0,0.15*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.25*x,0.25*y),(0.75*x,0.75*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "1":
        rect1 = gdstk.rectangle((0,0),(1*x,0.2*y))
        rect2 = gdstk.rectangle((0,0.8*y),(0.65*x,1*y))
        rect3 = gdstk.rectangle((0.35*x,0.2*y),(0.65*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "2":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(1*x,0.4*y))
        rect3 = gdstk.rectangle((0,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "3":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "4":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0),(0.7*x,0.3*y))
        rect3 = gdstk.rectangle((0.3*x,0.5*y),(0.7*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "5":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "6":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "7":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "8":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "9":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2

def generate(priority,outlayer,inlayer,key_type,boundary):

    layer_out=(key_type.split('_')[1])
    drty_out=(key_type.split('_')[2])
    bar_out=(key_type.split('_')[3]+'.'+key_type.split('_')[4])
    layer_in=(key_type.split('_')[5])
    drty_in=(key_type.split('_')[6])
    bar_in=(key_type.split('_')[7]+'.'+key_type.split('_')[8])
    bar_xy=(key_type.split('_')[9])
    txy=(key_type.split('_')[10])
   
    # OVERLAY_BOX_Define
    pre_in = gdstk.Cell("pre_in")               # pre_inbox
    pre_out = gdstk.Cell("pre_out")             # pre_outbox
    cell_name = key_type
    result_box = gdstk.Cell(cell_name)          # OVERLAY_BOX_Define
   
   # OVERLAY_In/Out_Layer_TEXT_Define
    left_1 = gdstk.Cell("left_1t")              # left_1 : 1st letter
    left_2 = gdstk.Cell("left_2t")              # left_2 : 2nd letter
    right_1 = gdstk.Cell("right_1t")            # right_1 : 1st letter
    right_2 = gdstk.Cell("right_2t")            # right_2 : 2nd letter
    pre_left = gdstk.Cell("pre_left")           # pre_left_outlayer_text
    pre_right = gdstk.Cell("pre_right")         # Pre_right_inlayer_text
    left_outlayer = "TEXT_" + layer_in + "_" + layer_out
    right_inlayer = "TEXT_" + layer_in
    result_left = gdstk.Cell(left_outlayer)     # left_outlayer_TEXT_Define
    result_right = gdstk.Cell(right_inlayer)    # right_inlayer_TEXT_Define

    # OVERLAY_BL/BR/UL/UR_TEXT_Define
    b_1 = gdstk.Cell("B_1t")                   # B : 1st letter
    l_2 = gdstk.Cell("L_2t")                   # L : 2nd letter
    u_1 = gdstk.Cell("U_1t")                   # U : 1st letter
    r_2 = gdstk.Cell("R_2t")                   # R : 2nd letter 
    pre_bl = gdstk.Cell("pre_bl")               # bl_text
    pre_br = gdstk.Cell("pre_br")               # br_text
    pre_ul = gdstk.Cell("pre_ul")               # ul_text
    pre_ur = gdstk.Cell("pre_ur")               # ur_text
    text_bl = "TEXT_" + layer_in + "_BL"
    text_br = "TEXT_" + layer_in + "_BR"
    text_ul = "TEXT_" + layer_in + "_UL"
    text_ur = "TEXT_" + layer_in + "_UR"
    result_bl = gdstk.Cell(text_bl)             # BL_TEXT_Define
    result_br = gdstk.Cell(text_br)             # BR_TEXT_Define
    result_ul = gdstk.Cell(text_ul)             # UL_TEXT_Define
    result_ur = gdstk.Cell(text_ur)             # UR_TEXT_Define

    # OVERLAY_BOX drawing
    if float(bar_xy) == 27.0 and float(bar_in) < 8.0 :
        x1 = 4-(float(bar_out)/2)
        y1 = 6.5
        for i in range(0,2):
            out_x = gdstk.rectangle((x1,y1),(x1+float(bar_out),y1+float(14)), layer=int(outlayer))
            pre_out.add(out_x)
            x1 += 19
        x2 = 6.5
        y2 = 4-(float(bar_out)/2)
        for i in range(0,2):
            out_y = gdstk.rectangle((x2,y2),(x2+float(14),y2+float(bar_out)), layer=int(outlayer))
            pre_out.add(out_y)
            y2 += 19
        x3 = 9.5-(float(bar_in)/2)
        y3 = 11.5
        for i in range(0,2):
            in_x = gdstk.rectangle((x3,y3),(x3+float(bar_in),y3+float(4)), layer=int(inlayer))
            pre_in.add(in_x)
            x3 += 8
        x4 = 11.5
        y4 = 9.5-(float(bar_in)/2)
        for i in range(0,2):
            in_y = gdstk.rectangle((x4,y4),(x4+float(4),y4+float(bar_in)), layer=int(inlayer))
            pre_in.add(in_y)
            y4 += 8
    elif float(bar_xy) == 27.0 and float(bar_in) == 8.0 :
        x1 = 4-(float(bar_out)/2)
        y1 = 6.5
        for i in range(0,2):
            out_x = gdstk.rectangle((x1,y1),(x1+float(bar_out),y1+float(14)), layer=int(outlayer))
            pre_out.add(out_x)
            x1 += 19
        x2 = 6.5
        y2 = 4-(float(bar_out)/2)
        for i in range(0,2):
            out_y = gdstk.rectangle((x2,y2),(x2+float(14),y2+float(bar_out)), layer=int(outlayer))
            pre_out.add(out_y)
            y2 += 19
        x3 = 13.5-(float(bar_in)/2)
        y3 = 13.5-(float(bar_in)/2)
        for i in range(0,2):
            in_x = gdstk.rectangle((x3,y3),(x3+float(bar_in),y3+float(bar_in)), layer=int(inlayer))
            pre_in.add(in_x)
    elif float(bar_xy) == 28.0 and float(bar_in) < 8.0 :
        x1 = 4.5-(float(bar_out)/2)
        y1 = 7
        for i in range(0,2):
            out_x = gdstk.rectangle((x1,y1),(x1+float(bar_out),y1+float(14)), layer=int(outlayer))
            pre_out.add(out_x)
            x1 += 19
        x2 = 7
        y2 = 4.5-(float(bar_out)/2)
        for i in range(0,2):
            out_y = gdstk.rectangle((x2,y2),(x2+float(14),y2+float(bar_out)), layer=int(outlayer))
            pre_out.add(out_y)
            y2 += 19
        x3 = 10-(float(bar_in)/2)
        y3 = 12
        for i in range(0,2):
            in_x = gdstk.rectangle((x3,y3),(x3+float(bar_in),y3+float(4)), layer=int(inlayer))
            pre_in.add(in_x)
            x3 += 8
        x4 = 12
        y4 = 10-(float(bar_in)/2)
        for i in range(0,2):
            in_y = gdstk.rectangle((x4,y4),(x4+float(4),y4+float(bar_in)), layer=int(inlayer))
            pre_in.add(in_y)
            y4 += 8
    elif float(bar_xy) == 28.0 and float(bar_in) == 8.0 :
        x1 = 4.5-(float(bar_out)/2)
        y1 = 7
        for i in range(0,2):
            out_x = gdstk.rectangle((x1,y1),(x1+float(bar_out),y1+float(14)), layer=int(outlayer))
            pre_out.add(out_x)
            x1 += 19
        x2 = 7
        y2 = 4.5-(float(bar_out)/2)
        for i in range(0,2):
            out_y = gdstk.rectangle((x2,y2),(x2+float(14),y2+float(bar_out)), layer=int(outlayer))
            pre_out.add(out_y)
            y2 += 19
        x3 = 14-(float(bar_in)/2)
        y3 = 14-(float(bar_in)/2)
        for i in range(0,2):
            in_x = gdstk.rectangle((x3,y3),(x3+float(bar_in),y3+float(bar_in)), layer=int(inlayer))
            pre_in.add(in_x)
    # OVERLAY_BOX Trench/Mesa
    rect = gdstk.rectangle((0,0),(int(bar_xy),int(bar_xy))) 
    if drty_out == "T":  
        over_out = gdstk.boolean(rect,gdstk.Reference(pre_out),"not", layer=int(outlayer))
        result_box.add(*over_out)
    else:
        over_out = gdstk.boolean(rect,gdstk.Reference(pre_out),"and", layer=int(outlayer))
        result_box.add(*over_out)  
    if drty_in == "T":
        over_in = gdstk.boolean(rect,gdstk.Reference(pre_in),"not", layer=int(inlayer))
        result_box.add(*over_in)
    else:
        over_in = gdstk.boolean(rect,gdstk.Reference(pre_in),"and",layer=int(inlayer))
        result_box.add(*over_in)

    # OVERLAY_Inlayer_TEXT_Define  ##글자,layer_no,size_x,size_y
    polygons = Make_letter(layer_out[0],int(inlayer),txy,txy)
    try:
        left_1.add(*polygons)
    except:
        left_1.add(polygons)
    pre_left.add(gdstk.Reference(left_1,(2.8,2)))
    polygons = Make_letter(layer_out[1],int(inlayer),txy,txy)
    try:
        left_2.add(*polygons)
    except:
        left_2.add(polygons)
    pre_left.add(gdstk.Reference(left_2,(2.8+int(txy)+1.4,2)))
    # OVERLAY_Inlayer_TEXT Trench/Mesa
    rect = gdstk.rectangle((0,0),(((int(bar_xy)+10)/2),10))
    if drty_out == "T":
        text = gdstk.boolean(rect,gdstk.Reference(pre_left),"not",layer=int(inlayer))
        result_left.add(*text)
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_left),"and",layer=int(inlayer))
        result_left.add(*text)
    
    # OVERLAY_Outlayer_TEXT_Define   ##글자,layer_no,size_x,size_y
    polygons = Make_letter(layer_in[0],int(inlayer),txy,txy)
    try:
        right_1.add(*polygons)
    except:
        right_1.add(polygons)
    pre_right.add(gdstk.Reference(right_1,(2.8,2)))
    polygons = Make_letter(layer_in[1],int(inlayer),txy,txy)
    try:
        right_2.add(*polygons)
    except:
        right_2.add(polygons)
    pre_right.add(gdstk.Reference(right_2,(2.8+int(txy)+1.4,2)))
    # OVERLAY_Outlayer_TEXT Trench/Mesa
    rect = gdstk.rectangle((0,0),(((int(bar_xy)+10)/2),10))
    if drty_in == "T":
        text = gdstk.boolean(rect,gdstk.Reference(pre_right),"not",layer=int(inlayer))
        result_right.add(*text)
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_right),"and",layer=int(inlayer))
        result_right.add(*text)

    # OVERLAY_B/L/U/R_TEXT_Define  ##글자,layer_no,size_x,size_y
    polygons = Make_letter("B",int(inlayer),txy,txy)
    try:
        b_1.add(*polygons)
    except:
        b_1.add(polygons)
    pre_bl.add(gdstk.Reference(b_1,(2,16)))
    pre_br.add(gdstk.Reference(b_1,(2,16)))
    polygons = Make_letter("L",int(inlayer),txy,txy)
    try:
        l_2.add(*polygons)
    except:
        l_2.add(polygons)
    pre_bl.add(gdstk.Reference(l_2,(2,6)))
    pre_ul.add(gdstk.Reference(l_2,(2,6)))
    polygons = Make_letter("U",int(inlayer),txy,txy)
    try:
        u_1.add(*polygons)
    except:
        u_1.add(polygons)
    pre_ul.add(gdstk.Reference(u_1,(2,16)))
    pre_ur.add(gdstk.Reference(u_1,(2,16)))
    polygons = Make_letter("R",int(inlayer),txy,txy)
    try:
        r_2.add(*polygons)
    except:
        r_2.add(polygons)
    pre_br.add(gdstk.Reference(r_2,(2,6)))
    pre_ur.add(gdstk.Reference(r_2,(2,6)))

    # OVERLAY_BL_TEXT Trench/Mesa)
    rect = gdstk.rectangle((0,0),(10,int(bar_xy)))
    if drty_out == "T":
        text = gdstk.boolean(rect,gdstk.Reference(pre_bl),"not",layer=int(inlayer))
        result_bl.add(*text)
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_bl),"and",layer=int(inlayer))
        result_bl.add(*text)
    
    # OVERLAY_BR_TEXT Trench/Mesa
    rect = gdstk.rectangle((0,0),(10,int(bar_xy)))
    if drty_in == "T":
        text = gdstk.boolean(rect,gdstk.Reference(pre_br),"not",layer=int(inlayer))
        result_br.add(*text)
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_br),"and",layer=int(inlayer))
        result_br.add(*text)
    
    # OVERLAY_UL_TEXT Trench/Mesa
    rect = gdstk.rectangle((0,0),(10,int(bar_xy)))
    if drty_out == "T":
        text = gdstk.boolean(rect,gdstk.Reference(pre_ul),"not",layer=int(inlayer))
        result_ul.add(*text)    
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_ul),"and",layer=int(inlayer))
        result_ul.add(*text)
    
    # OVERLAY_UR_TEXT Trench/Mesa
    rect = gdstk.rectangle((0,0),(10,int(bar_xy)))
    if drty_in == "T":
        text = gdstk.boolean(rect,gdstk.Reference(pre_ur),"not",layer=int(inlayer))
        result_ur.add(*text)
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_ur),"and",layer=int(inlayer))
        result_ur.add(*text)
     
    # Boundary
    for i in range(0,len(boundary)):
        bound = gdstk.rectangle((0,0),(int(bar_xy),(int(bar_xy))), layer=int(boundary[i]))
        result_box.add(bound)
        bound2 = gdstk.rectangle((0,0),(((int(bar_xy)+10)/2),10), layer=int(boundary[i]))
        result_left.add(bound2)
        bound3 = gdstk.rectangle((0,0),(((int(bar_xy)+10)/2),10),layer=int(boundary[i]))
        result_right.add(bound3) 
        bound4 = gdstk.rectangle((0,0),(10,int(bar_xy)),layer=int(boundary[i]))
        result_bl.add(bound4)
        result_br.add(bound4)
        result_ul.add(bound4)
        result_ur.add(bound4)    
    return result_box, result_left, result_right, result_bl, result_br, result_ul, result_ur

def main(priority,outlayer,inlayer,key_type,boundary):
    result_box, result_left, result_right, result_bl, result_br, result_ul, result_ur = generate(priority,outlayer,inlayer,key_type,boundary)
    return result_box, result_left, result_right, result_bl, result_br, result_ul, result_ur

if __name__ == "__main__":
    priority = 1
    outlayer = 77
    inlayer = 96
    key_type = "OVERLAY_KY_M_1_0_PB_M_8_0_28_6"
    boundary = [63,3] # list Type

    bllib = gdstk.Library()             # BL_lib 생성
    brlib = gdstk.Library()             # BR_lib 생성
    ullib = gdstk.Library()             # UL_lib 생성
    urlib = gdstk.Library()             # UR_lib 생성
    over_bl = key_type +"_BL"
    over_br = key_type +"_BR"
    over_ul = key_type +"_UL"
    over_ur = key_type +"_UR"
    cell_bl = bllib.new_cell(over_bl)   # BL_cell 생성
    cell_br = brlib.new_cell(over_br)   # BR_cell 생성
    cell_ul = ullib.new_cell(over_ul)   # UL_cell 생성
    cell_ur = urlib.new_cell(over_ur)   # UR_cell 생성

    output_name1 = over_bl + ".gds"
    output_name2 = over_br + ".gds"
    output_name3 = over_ul + ".gds"
    output_name4 = over_ur + ".gds"
    result_box, result_left, result_right, result_bl, result_br, result_ul, result_ur = main(priority,outlayer,inlayer,key_type,boundary)
    bllib.add(result_box, result_left, result_right, result_bl)
    brlib.add(result_box, result_left, result_right, result_br)
    ullib.add(result_box, result_left, result_right, result_ul)
    urlib.add(result_box, result_left, result_right, result_ur)
    bar_xy=(key_type.split('_')[9])
    bar_half = (int(bar_xy)+10)/2
    cell_bl.add(gdstk.Reference(result_box,(0,10)))
    cell_bl.add(gdstk.Reference(result_left,(0,0)))
    cell_bl.add(gdstk.Reference(result_right,((int(bar_half),0))))
    cell_bl.add(gdstk.Reference(result_bl,(int(bar_xy),10)))

    cell_br.add(gdstk.Reference(result_box,(0,10)))
    cell_br.add(gdstk.Reference(result_left,(0,0)))
    cell_br.add(gdstk.Reference(result_right,(int(bar_half),0)))
    cell_br.add(gdstk.Reference(result_br,(int(bar_xy),10)))

    cell_ul.add(gdstk.Reference(result_box,(0,10)))
    cell_ul.add(gdstk.Reference(result_left,(0,0)))
    cell_ul.add(gdstk.Reference(result_right,(int(bar_half),0)))
    cell_ul.add(gdstk.Reference(result_ul,(int(bar_xy),10)))

    cell_ur.add(gdstk.Reference(result_box,(0,10)))
    cell_ur.add(gdstk.Reference(result_left,(0,0)))
    cell_ur.add(gdstk.Reference(result_right,(int(bar_half),0)))
    cell_ur.add(gdstk.Reference(result_ur,(int(bar_xy),10)))
    
    bllib.write_gds(output_name1)
    brlib.write_gds(output_name2)
    ullib.write_gds(output_name3)
    urlib.write_gds(output_name4)