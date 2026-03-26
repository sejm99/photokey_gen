import gdstk

#priority =[]
#layer_out=[]
#drty_out=[]
#bar_out=[]
#layer_in=[]
#drty_in=[]
#bar_in=[]
#bar_xy=[]
#txy=[]

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
    pre_in = gdstk.Cell("pre_in"+key_type)               # pre_inbox
    pre_out = gdstk.Cell("pre_out"+key_type)             # pre_outbox
    cell_name = key_type
    box = gdstk.Cell(cell_name)                 # OVERLAY_BOX_Define
   
   # OVERLAY_In/Out_Layer_TEXT_Define
    left_1 = gdstk.Cell("left_1t"+key_type)                          # left_1 : 1st letter
    left_2 = gdstk.Cell("left_2t"+key_type)                          # left_2 : 2nd letter
    right_1 = gdstk.Cell("right_1t"+key_type)                        # right_1 : 1st letter
    right_2 = gdstk.Cell("right_2t"+key_type)                        # right_2 : 2nd letter
    pre_left = gdstk.Cell("pre_left"+key_type)                       # pre_left_outlayer_text
    pre_right = gdstk.Cell("pre_right"+key_type)                     # Pre_right_inlayer_text
    left = gdstk.Cell("TEXT_" + layer_in + "_" + layer_out+key_type) # left_outlayer_TEXT_Define
    right = gdstk.Cell("TEXT_" + layer_in+key_type)                  # right_inlayer_TEXT_Define

    # OVERLAY_BL/BR/UL/UR_TEXT_Define
    b_1 = gdstk.Cell("B_1t"+key_type)                              # B : 1st letter
    l_2 = gdstk.Cell("L_2t"+key_type)                              # L : 2nd letter
    u_1 = gdstk.Cell("U_1t"+key_type)                              # U : 1st letter
    r_2 = gdstk.Cell("R_2t"+key_type)                              # R : 2nd letter 
    pre_bl = gdstk.Cell("pre_bl"+key_type)                         # bl_text
    pre_br = gdstk.Cell("pre_br"+key_type)                         # br_text
    pre_ul = gdstk.Cell("pre_ul"+key_type)                         # ul_text
    pre_ur = gdstk.Cell("pre_ur"+key_type)                         # ur_text
    bl_p = gdstk.Cell("TEXT_" + layer_in + "_BL"+key_type)           # BL_TEXT_Define
    br_p = gdstk.Cell("TEXT_" + layer_in + "_BR"+key_type)      # BR_TEXT_Define
    ul_p = gdstk.Cell("TEXT_" + layer_in + "_UL"+key_type)       # UL_TEXT_Define
    ur_p = gdstk.Cell("TEXT_" + layer_in + "_UR"+key_type)      # UR_TEXT_Define
    
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
        box.add(*over_out)
    else:
        over_out = gdstk.boolean(rect,gdstk.Reference(pre_out),"and", layer=int(outlayer))
        box.add(*over_out)
    if drty_in == "T":
        over_in = gdstk.boolean(rect,gdstk.Reference(pre_in),"not", layer=int(inlayer))
        box.add(*over_in)
    else:
        over_in = gdstk.boolean(rect,gdstk.Reference(pre_in),"and",layer=int(inlayer))
        box.add(*over_in) 

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
        left.add(*text)
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_left),"and",layer=int(inlayer))
        left.add(*text)

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
        right.add(*text)
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_right),"and",layer=int(inlayer))
        right.add(*text)
 
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
        bl_p.add(*text)
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_bl),"and",layer=int(inlayer))
        bl_p.add(*text)
    
    # OVERLAY_BR_TEXT Trench/Mesa
    rect = gdstk.rectangle((0,0),(10,int(bar_xy)))
    if drty_in == "T":
        text = gdstk.boolean(rect,gdstk.Reference(pre_br),"not",layer=int(inlayer))
        br_p.add(*text)
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_br),"and",layer=int(inlayer))
        br_p.add(*text)
    
    # OVERLAY_UL_TEXT Trench/Mesa
    rect = gdstk.rectangle((0,0),(10,int(bar_xy)))
    if drty_out == "T":
        text = gdstk.boolean(rect,gdstk.Reference(pre_ul),"not",layer=int(inlayer))
        ul_p.add(*text)    
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_ul),"and",layer=int(inlayer))
        ul_p.add(*text)
    
    # OVERLAY_UR_TEXT Trench/Mesa
    rect = gdstk.rectangle((0,0),(10,int(bar_xy)))
    if drty_in == "T":
        text = gdstk.boolean(rect,gdstk.Reference(pre_ur),"not",layer=int(inlayer))
        ur_p.add(*text)
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_ur),"and",layer=int(inlayer))
        ur_p.add(*text)
       
    # Boundary
    for i in range(0,len(boundary)):
        bound = gdstk.rectangle((0,0),(int(bar_xy),(int(bar_xy))), layer=int(boundary[i]))
        box.add(bound)
        bound2 = gdstk.rectangle((0,0),(((int(bar_xy)+10)/2),10), layer=int(boundary[i]))
        left.add(bound2)
        bound3 = gdstk.rectangle((0,0),(((int(bar_xy)+10)/2),10),layer=int(boundary[i]))
        right.add(bound3) 
        bound4 = gdstk.rectangle((0,0),(10,(int(bar_xy))),layer=int(boundary[i]))
        bl_p.add(bound4)
        br_p.add(bound4)
        ul_p.add(bound4)
        ur_p.add(bound4)

    return box, left, right, bl_p, br_p, ul_p, ur_p
    
def start(priority,outlayer,inlayer,key_type,boundary,bllib):
    bl = gdstk.Cell(key_type +"_BL")      # BR_TEXT_Define
    # br = brlib.new_cell(key_type +"_BR")      # BL_TEXT_Define
    # ul = ullib.new_cell(key_type +"_UL")      # UL_TEXT_Define
    # ur = urlib.new_cell(key_type +"_UR")      # UR_TEXT_Define
    box, left, right, bl_p, br_p, ul_p, ur_p  = generate(priority,outlayer,inlayer,key_type,boundary)
    bllib.add(box, left, right, bl_p)      
    # brlib.add(box, left, right, br_p)
    # ullib.add(box, left, right, ul_p)
    # urlib.add(box, left, right, ur_p)

    bar_xy=(key_type.split('_')[9])
    bar_half = (float(bar_xy)+10)/2              
    bl.add(gdstk.Reference(box,(0,10)))
    bl.add(gdstk.Reference(left,(0,0)))
    bl.add(gdstk.Reference(right,((float(bar_half),0))))
    bl.add(gdstk.Reference(bl_p,(float(bar_xy),10)))

    # br.add(gdstk.Reference(box,(0,10)))
    # br.add(gdstk.Reference(left,(0,0)))
    # br.add(gdstk.Reference(right,(float(bar_half),0)))
    # br.add(gdstk.Reference(br_p,(float(bar_xy),10)))
                      
    # ul.add(gdstk.Reference(box,(0,10)))
    # ul.add(gdstk.Reference(left,(0,0)))
    # ul.add(gdstk.Reference(right,(float(bar_half),0)))
    # ul.add(gdstk.Reference(ul_p,(float(bar_xy),10)))
                        
    # ur.add(gdstk.Reference(box,(0,10)))
    # ur.add(gdstk.Reference(left,(0,0)))
    # ur.add(gdstk.Reference(right,(float(bar_half),0)))

    bllib.write_gds(key_type +"_BL" + ".gds")
    # brlib.write_gds(key_type +"_BR" + ".gds")
    # ullib.write_gds(key_type +"_UL" + ".gds")
    # urlib.write_gds(key_type +"_UR" + ".gds")
    return bl

if __name__ == "__main__":
    
    priority = 1
    outlayer = 77
    inlayer = 96
    key_type = "OVERLAY_KY_M_1_0_PB_M_8_0_28_6"
    boundary = [63,3] # list Type
    
    bllib = gdstk.Library() 
    brlib = gdstk.Library()
    ullib = gdstk.Library() 
    urlib = gdstk.Library() 
    bl = start(priority,outlayer,inlayer,key_type,boundary,bllib)
   