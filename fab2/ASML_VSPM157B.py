import gdstk

def generate(priority,layer_no,key_type,boundary):
    
    key_name=(key_type.split('_')[0])
    etch_type=(key_type.split('_')[-1])
    main_x=(key_type.split('_')[1])
    main_y=(key_type.split('_')[2])
    bar_x=(key_type.split('_')[3]+'.'+key_type.split('_')[4])
    bar_y=(key_type.split('_')[5]+'.'+key_type.split('_')[6])
    
    cell_name = key_name +"_"+ str(priority) +"_"+ str(layer_no) +"_"+ key_type
    result = gdstk.Cell(cell_name)
    pre = gdstk.Cell("pre")
    
    bar_x2=float(1.6)
    bar_x3=float(1.15)
    bar_x4=float(8.8)
    
    ## VSPM157B pattern drawing
    if int(main_y) == 74 and float(bar_x3) == 1.15:
        y1=1
        x1=428
        x2=430.3
        x3=432.55
        x4=434.85
        x5=437.15
        x6=439.45
        x7=441.7
        for i in range(0,9):               
            vspm157_s = gdstk.rectangle((x1,y1),(x1+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x1 +=16
            vspm157_s = gdstk.rectangle((x2,y1),(x2+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x2 +=16 
            vspm157_s = gdstk.rectangle((x3,y1),(x3+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x3 +=16 
            vspm157_s = gdstk.rectangle((x4,y1),(x4+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x4 +=16
        for i in range(0,8):
            vspm157_s = gdstk.rectangle((x5,y1),(x5+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x5 +=16 
            vspm157_s = gdstk.rectangle((x6,y1),(x6+float(1.1),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x6 +=16 
            vspm157_s = gdstk.rectangle((x7,y1),(x7+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x7 +=16
    if int(main_y) == 54 and float(bar_x3) == 1.15:
        y1=1
        x1=428
        x2=430.3
        x3=432.55
        x4=434.85
        x5=437.15
        x6=439.45
        x7=441.7
        for i in range(0,9):               
            vspm157_s = gdstk.rectangle((x1,y1),(x1+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x1 +=16
            vspm157_s = gdstk.rectangle((x2,y1),(x2+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x2 +=16 
            vspm157_s = gdstk.rectangle((x3,y1),(x3+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x3 +=16 
            vspm157_s = gdstk.rectangle((x4,y1),(x4+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x4 +=16
        for i in range(0,8):
            vspm157_s = gdstk.rectangle((x5,y1),(x5+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x5 +=16 
            vspm157_s = gdstk.rectangle((x6,y1),(x6+float(1.1),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x6 +=16 
            vspm157_s = gdstk.rectangle((x7,y1),(x7+float(bar_x3),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
            x7 +=16  

    if int(main_y) == 74:
       for i in range(0,60):
        y1 = 1 
        if i < 9 :
            x1 = 44+((8+float(bar_x))*(i))
            vspm157_s = gdstk.rectangle((x1,y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
            pre.add(vspm157_s)
        else:
            if i < (9+43) :
                x1 = 236+((1.6+float(bar_x2))*(i-9))
                vspm157_s = gdstk.rectangle((x1,y1),(x1+float(bar_x2),y1+float(bar_y)), layer=int(layer_no))
                pre.add(vspm157_s)
            else:
                x1 = 622.2+((8.8+float(bar_x4))*(i-(9+43)))
                vspm157_s = gdstk.rectangle((x1,y1),(x1+float(bar_x4),y1+float(bar_y)), layer=int(layer_no))
                pre.add(vspm157_s)
        cross = gdstk.cross((400,37),5,1, layer=int(layer_no))
        pre.add(cross)

    elif int(main_y) == 54:
       for i in range(0,60):
        y1 = 1
        if i < 9 :
            x1 = 44+((8+float(bar_x))*(i))
            vspm157_s = gdstk.rectangle((x1,y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
        else:
            if i < (9+43) :
                x1 = 236+((1.6+float(bar_x2))*(i-9))
                vspm157_s = gdstk.rectangle((x1,y1),(x1+float(bar_x2),y1+float(bar_y)), layer=int(layer_no))
            else:
                x1 = 622.2+((8.8+float(bar_x4))*(i-(9+43)))
                vspm157_s = gdstk.rectangle((x1,y1),(x1+float(bar_x4),y1+float(bar_y)), layer=int(layer_no))
        pre.add(vspm157_s)
        cross = gdstk.cross((400,27),5,1, layer=int(layer_no))
        pre.add(cross)
  
    ## Trench/Mesa
    if etch_type == "T":
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        vspm157 = gdstk.boolean(rect,gdstk.Reference(pre),"not",layer=int(layer_no))
        result.add(*vspm157)
    else:
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        vspm157 = gdstk.boolean(rect,gdstk.Reference(pre),"and",layer=int(layer_no))
        result.add(*vspm157)
    
    ## Boundary
    for i in range(0,len(boundary)):
        if int(boundary[i]) == 121:
            bsm0 = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
            bsm1 = gdstk.rectangle((0,0),(10,10))
            bsm2 = gdstk.rectangle((int(main_x)-10,0),(int(main_x),10))
            bsm3 = gdstk.rectangle((0,int(main_y)-10),(10,int(main_y)))
            bsm4 = gdstk.rectangle((int(main_x)-10,int(main_y)-10),(int(main_x),int(main_y)))
            bsm5 = gdstk.boolean(bsm1,bsm2,"or")
            bsm6 = gdstk.boolean(bsm3,bsm4,"or")
            bsm7 = gdstk.boolean(bsm5,bsm6,"or")
            bsm8 = gdstk.boolean(bsm0,bsm7,"not")
            bsm9 = gdstk.ellipse((10,10), 10)
            bsm10 = gdstk.ellipse((int(main_x)-10,10), 10)
            bsm11 = gdstk.ellipse((10,int(main_y)-10), 10)
            bsm12 = gdstk.ellipse((int(main_x)-10,int(main_y)-10), 10)
            bsm13 = gdstk.boolean(bsm9,bsm10,"or")
            bsm14 = gdstk.boolean(bsm11,bsm12,"or")
            bsm15 = gdstk.boolean(bsm13,bsm14,"or")
            bsm = gdstk.boolean(bsm8,bsm15,"or", layer=int(boundary[i]))
            result.add(*bsm)
        else:
            bound = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=int(boundary[i]))
            result.add(bound)

    return result

def main(priority,layer_no,key_type,boundary):
    res = generate(priority,layer_no,key_type,boundary)
    return res

if __name__ == "__main__":
    priority = 1
    layer_no = 1
    key_type = "VSPM157_800_74_8_0_72_0_T"
    boundary = [63,0] # list Type

    lib = gdstk.Library() # lib 생성
    cell_name=key_type
    cell = lib.new_cell(cell_name) # cell 생성

    output_name = cell_name + ".gds"
    res = main(priority,layer_no,key_type,boundary)
    lib.add(res)
    cell.add(gdstk.Reference(res,(0,0)))
    lib.write_gds(output_name)