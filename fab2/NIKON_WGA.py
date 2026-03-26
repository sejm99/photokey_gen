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
    
    ## WGA pattern drawing
    if int(main_y) == 75 and int(main_x) != 75  :
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
                    wga_s = gdstk.rectangle((x1, y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
                    pre.add(wga_s)
                    x1 += 8
            else:
                pass
    elif int(main_y) == 50 and int(main_x) != 50 :
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
                    wga_s = gdstk.rectangle((x1, y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
                    pre.add(wga_s)
                    x1 += 8
            else:
                pass
    elif int(main_y) == 54 and int(main_x) != 54 :
        for i in range(3):
            if i == 0 :
                y1 = 11-float(bar_y)/2
            elif i == 1 :
                y1 = 30-float(bar_y)/2
            elif i == 2 :
                y1 = 43-float(bar_y)/2
            if int(main_x) != 50:
                x1 = 4-(float(bar_x)/2)
                for i in range(25):
                    wga_s = gdstk.rectangle((x1, y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
                    pre.add(wga_s)
                    x1 += 8
            else:
                pass
    if int(main_x) and int(main_y)  == 75 :
        for i in range(3):
            if i == 0 :
                y1 = 14.5-float(bar_y)/2
            elif i == 1 :
                y1 = 40.5-float(bar_y)/2
            elif i == 2 :
                y1 = 60.5-float(bar_y)/2
            if int(main_x) == 75:
                x1 = 2.5
                for i in range(3):
                    wga_s = gdstk.rectangle((x1, y1),(72.5,y1+float(bar_y)), layer=int(layer_no))
                    pre.add(wga_s)
            else:
                pass
        for i in range(3):
            if i == 0 :
                x1 = 14.5-float(bar_x)/2
            elif i == 1 :
                x1 = 34.5-float(bar_x)/2
            elif i == 2 :
                x1 = 60.5-float(bar_x)/2
            if int(main_x) == 75:
                y1 = 2.5
                for i in range(3):
                    wga_s = gdstk.rectangle((x1, y1),(x1+float(bar_x),72.5), layer=int(layer_no))
                    pre.add(wga_s)
            else:
                pass
    elif int(main_x) and int(main_y) == 50 :
        for i in range(3):
            if i == 0 :
                y1 = 9.4-float(bar_y)/2
            elif i == 1 :
                y1 = 27-float(bar_y)/2
            elif i == 2 :
                y1 = 40.6-float(bar_y)/2
            if int(main_x) == 50:
                x1 = 1.8
                for i in range(3):
                    wga_s = gdstk.rectangle((x1, y1),(48.2,y1+float(bar_y)), layer=int(layer_no))
                    pre.add(wga_s)
            else:
                pass
        for i in range(3):
            if i == 0 :
                x1 = 9.4-float(bar_y)/2
            elif i == 1 :
                x1 = 23-float(bar_y)/2
            elif i == 2 :
                x1 = 40.6-float(bar_y)/2
            if int(main_x) == 50:
                y1 = 1.8
                for i in range(3):
                    wga_s = gdstk.rectangle((x1, y1),(x1+float(bar_x),48.2), layer=int(layer_no))
                    pre.add(wga_s)
            else:
                pass
    elif int(main_x) and int(main_y) == 54 :
        for i in range(3):
            if i == 0 :
                y1 = 10.4-float(bar_y)/2
            elif i == 1 :
                y1 = 29-float(bar_y)/2
            elif i == 2 :
                y1 = 43.6-float(bar_y)/2
            if int(main_x) == 54:
                x1 = 1.8
                for i in range(3):
                    wga_s = gdstk.rectangle((x1, y1),(52.2,y1+float(bar_y)), layer=int(layer_no))
                    pre.add(wga_s)
            else:
                pass
        for i in range(3):
            if i == 0 :
                x1 = 10.4-float(bar_y)/2
            elif i == 1 :
                x1 = 25-float(bar_y)/2
            elif i == 2 :
                x1 = 43.6-float(bar_y)/2
            if int(main_x) == 54:
                y1 = 1.8
                for i in range(3):
                    wga_s = gdstk.rectangle((x1, y1),(x1+float(bar_x),52.2), layer=int(layer_no))
                    pre.add(wga_s)
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
        bound = gdstk.rectangle((0,0),(int(main_x),int(main_y)), layer=int(boundary[i]))
        result.add(bound)
    return result

def main(priority,layer_no,key_type,boundary):
    res = generate(priority,layer_no,key_type,boundary)
    return res

if __name__ == "__main__":
    priority = 1
    layer_no = 0
    key_type = "WGA_50_50_2_8_2_8_T"
    boundary = [63,0] # list Type

    lib = gdstk.Library() # lib 생성
    cell_name=key_type
    cell = lib.new_cell(cell_name) # cell 생성

    output_name = cell_name + ".gds"
    res = main(priority,layer_no,key_type,boundary)
    lib.add(res)
    cell.add(gdstk.Reference(res,(0,0)))
    lib.write_gds(output_name)