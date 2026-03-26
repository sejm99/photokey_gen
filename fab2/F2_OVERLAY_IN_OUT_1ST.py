import gdstk
from fab2 import F2_MAKE_LETTER

def generate(outlayer,inlayer,key_type,boundary,text):
    
    layer_out=(key_type.split('_')[1])
    drty_out=(key_type.split('_')[2])
    bar_out=(key_type.split('_')[3]+'.'+key_type.split('_')[4])
    layer_in=(key_type.split('_')[5])
    drty_in=(key_type.split('_')[6])
    bar_in=(key_type.split('_')[7]+'.'+key_type.split('_')[8])
    bar_xy=(key_type.split('_')[9])
    boundary_tmp = boundary.split('\n')
    boundary_sp=boundary_tmp[0].split(',')
    ## CELL_NAME_Define
    pre_in = gdstk.Cell("pre_in_"+key_type)
    pre_out = gdstk.Cell("pre_out_"+key_type)
    box_in = gdstk.Cell("in_"+key_type)       # 1ST_OVERLAY_BOX_Define
    box_out = gdstk.Cell("out_"+key_type)
  
    in_1 = gdstk.Cell("in_1_text"+key_type)
    in_2 = gdstk.Cell("in_2_text"+key_type)
    pre_text = gdstk.Cell("pre_"+layer_in+"_"+str(inlayer))
    text_out = gdstk.Cell("TEXT_"+layer_in+"_"+str(inlayer))
       
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
    elif float(bar_xy) == 37.0 and float(bar_in) < 12.0 :
        x1 = 6-(float(bar_out)/2)
        y1 = 9
        for i in range(0,2):
            out_x = gdstk.rectangle((x1,y1),(x1+float(bar_out),y1+float(19)), layer=int(outlayer))
            pre_out.add(out_x)
            x1 += 25
        x2 = 9
        y2 = 6-(float(bar_out)/2)
        for i in range(0,2):
            out_y = gdstk.rectangle((x2,y2),(x2+float(19),y2+float(bar_out)), layer=int(outlayer))
            pre_out.add(out_y)
            y2 += 25
        x3 = 13-(float(bar_in)/2)
        y3 = 15
        for i in range(0,2):
            in_x = gdstk.rectangle((x3,y3),(x3+float(bar_in),y3+float(7)), layer=int(inlayer))
            pre_in.add(in_x)
            x3 += 11
        x4 = 15
        y4 = 13-(float(bar_in)/2)
        for i in range(0,2):
            in_y = gdstk.rectangle((x4,y4),(x4+float(7),y4+float(bar_in)), layer=int(inlayer))
            pre_in.add(in_y)
            y4 += 11
    elif float(bar_xy) == 37.0 and float(bar_in) == 12.0 :
        x1 = 6-(float(bar_out)/2)
        y1 = 9
        for i in range(0,2):
            out_x = gdstk.rectangle((x1,y1),(x1+float(bar_out),y1+float(19)), layer=int(outlayer))
            pre_out.add(out_x)
            x1 += 25
        x2 = 9
        y2 = 6-(float(bar_out)/2)
        for i in range(0,2):
            out_y = gdstk.rectangle((x2,y2),(x2+float(19),y2+float(bar_out)), layer=int(outlayer))
            pre_out.add(out_y)
            y2 += 25
        x3 = 18.5-(float(bar_in)/2)
        y3 = 18.5-(float(bar_in)/2)
        for i in range(0,2):
            in_x = gdstk.rectangle((x3,y3),(x3+float(bar_in),y3+float(bar_in)), layer=int(inlayer))
            pre_in.add(in_x)
  
    # OVERLAY_BOX Trench/Mesa
    rect = gdstk.rectangle((0,0),(float(bar_xy),float(bar_xy))) 
    if drty_out == "T":  
        over_out = gdstk.boolean(rect,gdstk.Reference(pre_out),"not", layer=int(outlayer))
        box_out.add(*over_out)
    else:
        over_out = gdstk.boolean(rect,gdstk.Reference(pre_out),"and", layer=int(outlayer))
        box_out.add(*over_out)
    if drty_in == "T":
        over_in = gdstk.boolean(rect,gdstk.Reference(pre_in),"not", layer=int(inlayer))
        box_in.add(*over_in)
    else:
        over_in = gdstk.boolean(rect,gdstk.Reference(pre_in),"and",layer=int(inlayer))
        box_in.add(*over_in) 
    
    # 1ST_OVERLAY_TEXT_Define  ## letter,layer_no,size_x,size_y,thin
    bar_xy=(key_type.split('_')[9])
    txy=(text.split('_')[0][0])
    if txy !='7':
        txt_y = 12
    else:
        txt_y =10
    bb_1 = (float(bar_xy) - ((float(txy)*2)+2))/2
    txy_half = (txt_y-float(txy))/2
    polygons = F2_MAKE_LETTER.main(layer_out[0],int(inlayer),txy,txy)
    try:
        in_1.add(*polygons)
    except:
        in_1.add(polygons)
    pre_text.add(gdstk.Reference(in_1,(float(bb_1),float(txy_half))))
    polygons = F2_MAKE_LETTER.main(layer_out[1],int(inlayer),txy,txy)
    try:
        in_2.add(*polygons)
    except:
        in_2.add(polygons)
    pre_text.add(gdstk.Reference(in_2,(float(bb_1)+float(txy)+2,float(txy_half))))
    # 1ST_OVERLAY_TEXT_Define  ## letter,layer_no,size_x,size_y,thin
    rect = gdstk.rectangle((0,0),(float(bar_xy),txt_y))
    if drty_in == "T":
        text = gdstk.boolean(rect,gdstk.Reference(pre_text),"not",layer=int(inlayer))
        text_out.add(*text) 
    else:
        text = gdstk.boolean(rect,gdstk.Reference(pre_text),"and",layer=int(inlayer))
        text_out.add(*text) 
 
    # Boundary
    for i in range(0,len(boundary_sp)):
        bound = gdstk.rectangle((0,0),(float(bar_xy),(float(bar_xy))), layer=int(boundary_sp[i]))
        box_in.add(bound)
        box_out.add(bound)
        bound2 = gdstk.rectangle((0,0),(float(bar_xy),txt_y),layer=int(boundary_sp[i]))
        text_out.add(bound2)   
    return box_in, box_out, text_out

def start(outlayer,inlayer,key_type,boundary,text,inlib,outlib):
    in_1st = gdstk.Cell("IN_"+str(inlayer))
    out_1st = gdstk.Cell("OUT_"+str(outlayer))   
    box_in, box_out, text_out = generate(outlayer,inlayer,key_type,boundary,text)
    inlib.add(box_in, text_out)
    outlib.add(box_out, text_out)
    txy=(text.split('_')[0][0])
    if txy != '7':
        txt_y = 12
    else:
        txt_y =10
    in_1st.add(gdstk.Reference(box_in,(0,txt_y)))
    in_1st.add(gdstk.Reference(text_out,(0,0)))
    out_1st.add(gdstk.Reference(box_out,(0,txt_y)))
    out_1st.add(gdstk.Reference(text_out,(0,0)))
    return in_1st, out_1st

if __name__ == "__main__":
    process = "BD130S_60um"
    priority = 1
    outlayer = [3]
    inlayer = [3]
    key_type = ["1STOVER_AA_T_1_0_AA_T_1_0_28_7"]
    boundary = [[63]]
    text     = ["72K_0"]
    inlib = gdstk.Library()
    outlib = gdstk.Library()
    in_1st, out_1st = start(outlayer,inlayer,key_type,boundary,text,inlib,outlib)