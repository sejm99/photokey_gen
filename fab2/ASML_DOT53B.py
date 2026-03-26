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
    
    ## DOT53B pattern drawing
    if int(main_y) == 74:
       for i in range(0,40):
        if i < 21:
            x1 = 36+((14.4+float(bar_x))*i)
        else:
            x1 = 437.8+((16+float(bar_x))*(i-21))
        y1 = 2-(float(bar_y))/2
        for j in range(0,15):
            dot53_s = gdstk.rectangle((x1,y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
            pre.add(dot53_s)
            y1 += 5
        y1 = 2-(float(bar_y))/2
        x2 = float(x1+float(bar_x)+1.6)
        for j in range(0,15):
            dot53_s = gdstk.rectangle((x2,y1),(x2+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
            pre.add(dot53_s)
            y1 += 5
        y1 = 2-(float(bar_y))/2
        x3 = float(x2+float(bar_x)+1.6)
        for j in range(0,15):
            dot53_s = gdstk.rectangle((x3,y1),(x3+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
            pre.add(dot53_s)
            y1 += 5   
        cross = gdstk.cross((400,37),5,1, layer=int(layer_no))
        pre.add(cross)
    elif int(main_y) == 54:
       for i in range(0,40):
        if i < 21:
            x1 = 36+((14.4+float(bar_x))*i)
        else:
            x1 = 437.8+((16+float(bar_x))*(i-21))
        y1 = 7-(float(bar_y))/2
        for j in range(0,9):
            dot53_s = gdstk.rectangle((x1,y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
            pre.add(dot53_s)
            y1 += 5
        y1 = 7-(float(bar_y))/2
        x2 = float(x1+float(bar_x)+1.6)
        for j in range(0,9):
            dot53_s = gdstk.rectangle((x2,y1),(x2+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
            pre.add(dot53_s)
            y1 += 5
        y1 = 7-(float(bar_y))/2
        x3 = float(x2+float(bar_x)+1.6)
        for j in range(0,9):
            dot53_s = gdstk.rectangle((x3,y1),(x3+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
            pre.add(dot53_s)
            y1 += 5
        cross = gdstk.cross((400,27),5,1, layer=int(layer_no))
        pre.add(cross)
       
    ## Trench/Mesa
    if etch_type == "T":
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        dot53 = gdstk.boolean(rect,gdstk.Reference(pre),"not",layer=int(layer_no))
        result.add(*dot53)
    else:
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        dot53 = gdstk.boolean(rect,gdstk.Reference(pre),"and",layer=int(layer_no))
        result.add(*dot53)
    
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
    key_type = "DOT53_800_54_1_6_1_6_T"
    boundary = [63,3,10,1] # list Type

    lib = gdstk.Library() # lib 생성
    cell_name=key_type
    cell = lib.new_cell(cell_name) # cell 생성

    output_name = cell_name + ".gds"
    res = main(priority,layer_no,key_type,boundary)
    lib.add(res)
    cell.add(gdstk.Reference(res,(0,0)))
    lib.write_gds(output_name)