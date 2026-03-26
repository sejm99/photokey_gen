import gdstk

def generate(priority,layer_no,key_type,boundary):

    key_name=(key_type.split('_')[0])
    etch_type=(key_type.split('_')[-1])
    main_x=(key_type.split('_')[1])
    main_y=(key_type.split('_')[2])
    bar_x=(key_type.split('_')[3]+'.'+key_type.split('_')[4])
    bar_y=(key_type.split('_')[5]+'.'+key_type.split('_')[6])
    pri=f'{priority:02d}'
    lay=f'{layer_no:03d}'
    
    cell_name = str(key_name)+"_"+str(pri)+"_"+str(lay)+"_"+ key_type
    result = gdstk.Cell(cell_name)
    pre = gdstk.Cell("pre")
    
    ## WGA_BSI pattern drawing
    if float(bar_x) == 4.0 and float(bar_y) == 5.0:
        if int(main_y) == 75 :
            for i in range(3):
                if i == 0 :
                    y1 = 14.5-float(bar_y)/2
                elif i == 1 :
                    y1 = 40.5-float(bar_y)/2
                elif i == 2 :
                    y1 = 60.5-float(bar_y)/2
                if int(main_x) != 75:
                    x1 = 4-(float(bar_x)/2)
                    for i in range(25):
                        wga_s1 = gdstk.rectangle((x1, y1),(x1+float(bar_x),y1+float(bar_y)))
                        wga_s2= gdstk.rectangle((x1+1, y1+1),((x1+float(bar_x))-1,(y1+float(bar_y))-1))
                        wga_s = gdstk.boolean(wga_s1,wga_s2,"not",layer=int(layer_no))
                        pre.add(*wga_s)
                        x1 += 8
                else:
                    pass
        elif int(main_y) == 50 :
            for i in range(3):
                if i == 0 :
                    y1 = 9-float(bar_y)/2
                elif i == 1 :
                    y1 = 28-float(bar_y)/2
                elif i == 2 :
                    y1 = 41-float(bar_y)/2
                if int(main_x) != 50:
                    x1 = 4-(float(bar_x)/2)
                    for i in range(25):
                        wga_s1 = gdstk.rectangle((x1, y1),(x1+float(bar_x),y1+float(bar_y)))
                        wga_s2= gdstk.rectangle((x1+1, y1+1),((x1+float(bar_x))-1,(y1+float(bar_y))-1))
                        wga_s = gdstk.boolean(wga_s1,wga_s2,"not",layer=int(layer_no))
                        pre.add(*wga_s)
                        x1 += 8
                else:
                    pass
    else:
        pass
    ## Trench/Mesa
    if etch_type == "T":
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        wga = gdstk.boolean(rect,gdstk.Reference(pre),"not",layer=int(layer_no))
        result.add(*wga)
    else:
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        wga = gdstk.boolean(rect,gdstk.Reference(pre),"and",layer=int(layer_no))
        result.add(*wga)
    
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
    layer_no = 0
    key_type = "WGAB_200_75_4_0_5_0_T"
    boundary = [63,121] # list Type

    lib = gdstk.Library() # lib 생성
    cell_name=key_type
    cell = lib.new_cell(cell_name) # cell 생성

    output_name = cell_name + ".gds"
    res = main(priority,layer_no,key_type,boundary)
    lib.add(res)
    cell.add(gdstk.Reference(res,(0,0)))
    lib.write_gds(output_name)