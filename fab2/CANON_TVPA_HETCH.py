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
    
    ## TVPA-HETCH pattern drawing
    if float(bar_y) > 0.0 :
        if int(main_y) == 50 :
            # center box
            cxy = 3
            cx = 35-(float(cxy)/2)
            cy = 25-(float(cxy)/2)
            box_a = gdstk.rectangle((cx,cy),(cx+float(cxy),cy+float(cxy)), layer=int(layer_no))
            pre.add(box_a)
            # big box
            x1 = 16-(float(bar_x)/2)
            y1 = 7-(float(bar_y)/2)
            for i in range(0,9):
                box_a = gdstk.rectangle((x1,y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
                pre.add(box_a)
                x1 += 4
            x2 = 17-(float(bar_y)/2)
            y2 = 12-(float(bar_x)/2)
            for i in range(0,9):
                box_a = gdstk.rectangle((x2,y2),(x2+float(bar_y),y2+float(bar_x)), layer=int(layer_no))
                pre.add(box_a)
                y2 += 4
            x3 = 22-(float(bar_x)/2)
            y3 = 43-(float(bar_y)/2)
            for i in range(0,9):
                box_a = gdstk.rectangle((x3,y3),(x3+float(bar_x),y3+float(bar_y)), layer=int(layer_no))
                pre.add(box_a)
                x3 += 4
            x4 = 53-(float(bar_y)/2)
            y4 = 6-(float(bar_x)/2)
            for i in range(0,9):
                box_a = gdstk.rectangle((x4,y4),(x4+float(bar_y),y4+float(bar_x)), layer=int(layer_no))
                pre.add(box_a)
                y4 += 4
            # small box
            x5 = 22.5-(float(bar_x)/2)
            y5 = 25-(float(bar_y)/2)
            for i in range(0,3):
                box_a = gdstk.rectangle((x5,y5),(x5+float(bar_x),y5+float(bar_y)), layer=int(layer_no))
                pre.add(box_a)
                x5 += 4
            x6 = 39.5-(float(bar_x)/2)
            y6 = 25-(float(bar_y)/2)
            for i in range(0,3):
                box_a = gdstk.rectangle((x6,y6),(x6+float(bar_x),y6+float(bar_y)), layer=int(layer_no))
                pre.add(box_a)
                x6 += 4
            x7 = 35-(float(bar_y)/2)
            y7 = 12.5-(float(bar_x)/2)
            for i in range(0,3):
                box_a = gdstk.rectangle((x7,y7),(x7+float(bar_y),y7+float(bar_x)), layer=int(layer_no))
                pre.add(box_a)
                y7 += 4
            x8 = 35-(float(bar_y)/2)
            y8 = 29.5-(float(bar_x)/2)
            for i in range(0,3):
                box_a = gdstk.rectangle((x8,y8),(x8+float(bar_y),y8+float(bar_x)), layer=int(layer_no))
                pre.add(box_a)
                y8 += 4        
    else:
        box_s = gdstk.rectangle((0,0),(int(main_x),int(main_y)),layer=int(layer_no))
        pre.add(box_s)
    
    ## Trench/Mesa
    if etch_type == "T":
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        box = gdstk.boolean(rect,gdstk.Reference(pre),"not",layer=int(layer_no))
        result.add(*box)
    else:
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        box = gdstk.boolean(rect,gdstk.Reference(pre),"and",layer=int(layer_no))
        result.add(*box)
    
    ## Boundary
    for i in range(0,len(boundary)):
        bound = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=int(boundary[i]))
        result.add(bound)
    return result

def main(priority,layer_no,key_type,boundary):
    res = generate(priority,layer_no,key_type,boundary)
    return res

if __name__ == "__main__":
    priority = 1
    layer_no = 0
    key_type = "TVPA-HETCH_70_50_2_0_4_0_T"
    boundary = [63,0] # list Type

    lib = gdstk.Library() # lib 생성
    cell_name=key_type
    cell = lib.new_cell(cell_name) # cell 생성

    output_name = cell_name + ".gds"
    res = main(priority,layer_no,key_type,boundary)
    lib.add(res)
    cell.add(gdstk.Reference(res,(0,0)))
    lib.write_gds(output_name)