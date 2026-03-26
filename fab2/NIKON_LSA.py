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
    
    ## LSA pattern drawing
    if int(main_y) == 75 :
        x1 = 35-(float(bar_x)/2)
        for i in range(0,5):
            y1 = 13.5 -(float(bar_y)/2)
            for i in range(0,7):
                lsa_s = gdstk.rectangle((x1,y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
                pre.add(lsa_s)
                y1 += 8
            x1 += 20
    elif int(main_y) == 54 :
        x1 = 35-(float(bar_x)/2)
        for i in range(0,5):
            y1 = 7 -(float(bar_y)/2)
            for i in range(0,6):
                lsa_s = gdstk.rectangle((x1,y1),(x1+float(bar_x),y1+float(bar_y)), layer=int(layer_no))
                pre.add(lsa_s)
                y1 += 8
            x1 += 20
    else:
        lsa_s = gdstk.rectangle((0,0),(int(main_x),int(main_y)),layer=int(layer_no))
        pre.add(lsa_s)
    
    ## Trench/Mesa
    if etch_type == "T":
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        lsa = gdstk.boolean(rect,gdstk.Reference(pre),"not",layer=int(layer_no))
        result.add(*lsa)
    else:
        rect = gdstk.rectangle((0,0),(int(main_x),int(main_y)))
        lsa = gdstk.boolean(rect,gdstk.Reference(pre),"and",layer=int(layer_no))
        result.add(*lsa) 
    
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
    key_type = "LSA_150_54_2_0_4_0_M"
    boundary = [63,100]# list Type

    lib = gdstk.Library() # lib 생성
    cell_name=key_type
    cell = lib.new_cell(cell_name) # cell 생성

    output_name = cell_name + ".gds"
    res = main(priority,layer_no,key_type,boundary)
    lib.add(res)
    cell.add(gdstk.Reference(res,(0,0)))
    lib.write_gds(output_name)