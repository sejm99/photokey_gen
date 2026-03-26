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
    
    ## DOT32 pattern drawing
    if int(main_y) == 54:
       for i in range(0,40):
        if i < 21:
            x1 = 36+((13.4+float(bar_x))*i)
        else:
            x1 = 437.8+((15+float(bar_x))*(i-21))
        y1 = 3-(float(bar_y))/2
        for j in range(0,9):
            dot32_s = gdstk.rectangle((x1,y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
            pre.add(dot32_s)
            y1 += 6
        y1 = 3-(float(bar_y))/2
        x2 = float(x1+float(bar_x)+2.8)
        for j in range(0,9):
            dot32_s = gdstk.rectangle((x2,y1),(x2+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
            pre.add(dot32_s)
            y1 += 6
        cross = gdstk.cross((400,27),5,1, layer=int(layer_no))
        pre.add(cross)
    else :
        pass
       
    ## Trench/Mesa
    if etch_type == "T":
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        dot32 = gdstk.boolean(rect,gdstk.Reference(pre),"not",layer=int(layer_no))
        result.add(*dot32)
    else:
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        dot32 = gdstk.boolean(rect,gdstk.Reference(pre),"and",layer=int(layer_no))
        result.add(*dot32)
    
    ## Boundary
    for i in range(0,len(boundary)):
        bound = gdstk.rectangle((0, 0),(int(main_x),int(main_y)), layer=int(boundary[i]))
        result.add(bound)

    return result

def main(priority,layer_no,key_type,boundary):
    res = generate(priority,layer_no,key_type,boundary)
    return res

if __name__ == "__main__":
    priority = 1
    layer_no = 0
    key_type = "DOT32_800_54_2_6_2_6_T"
    boundary = [63,0] # list Type

    lib = gdstk.Library() # lib 생성
    cell_name=key_type
    cell = lib.new_cell(cell_name) # cell 생성

    output_name = cell_name + ".gds"
    res = main(priority,layer_no,key_type,boundary)
    lib.add(res)
    cell.add(gdstk.Reference(res,(0,0)))
    lib.write_gds(output_name)