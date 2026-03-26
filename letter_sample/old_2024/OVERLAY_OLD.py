import gdstk, sys, time
import numpy as np

def generate(priority,outlayer,inlayer,key_type,boundary):
    ## OVERLAY pattern drawing

    cell_name = "OVERLAY_" + str(outlayer) +"_"+ str(inlayer) +"_"+ key_type
    result = gdstk.Cell(cell_name)
    pre_in = gdstk.Cell("pre_in")
    pre_out = gdstk.Cell("pre_out")


    layer_out=(key_type.split('_')[1])
    drty_out=(key_type.split('_')[2])
    bar_out=(key_type.split('_')[3]+'.'+key_type.split('_')[4])
    layer_in=(key_type.split('_')[5])
    drty_in=(key_type.split('_')[6])
    bar_in=(key_type.split('_')[7]+'.'+key_type.split('_')[8])
    bar_xy=(key_type.split('_')[9])
    text_xy=(key_type.split('_')[10])
      
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

    ## Trench/Mesa
    if drty_out == "T":
        rect = gdstk.rectangle((0,0),(int(bar_xy),int(bar_xy)))
        over_out = gdstk.boolean(rect,gdstk.Reference(pre_out),"not", layer=int(outlayer))
        result.add(*over_out)
    else:
        rect = gdstk.rectangle((0,0),(int(bar_xy),int(bar_xy)))
        over_out = gdstk.boolean(rect,gdstk.Reference(pre_out),"and", layer=int(outlayer))
        result.add(*over_out)  
    if drty_in == "T":
        rect = gdstk.rectangle((0,0),(int(bar_xy),int(bar_xy)))
        over_in = gdstk.boolean(rect,gdstk.Reference(pre_in),"not", layer=int(inlayer))
        result.add(*over_in)
    else:
        rect = gdstk.rectangle((0,0),(int(bar_xy),int(bar_xy)))
        over_in = gdstk.boolean(rect,gdstk.Reference(pre_in),"and",layer=int(inlayer))
        result.add(*over_in)
    
    # Boundary
    for i in range(0,len(boundary)):
        bound = gdstk.rectangle((0, 0),(int(bar_xy),int(bar_xy)), layer=int(boundary[i]))
        result.add(bound)
    return result

def main(priority,outlayer,inlayer,key_type,boundary):
    res = generate(priority,outlayer,inlayer,key_type,boundary)
    return res

if __name__ == "__main__":
    priority = 1
    outlayer = 77
    inlayer = 96
    key_type = "OVERLAY_KY_M_1_0_NB_M_2_0_27_7"
    boundary = [63,3] # list Type

    lib = gdstk.Library() # lib 생성
    cell_name=key_type
    cell = lib.new_cell(cell_name) # cell 생성

    output_name = cell_name + ".gds"
    res = main(priority,outlayer,inlayer,key_type,boundary)
    lib.add(res)
    cell.add(gdstk.Reference(res,(0,0)))
    lib.write_gds(output_name)