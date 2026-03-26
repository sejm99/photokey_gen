import gdstk
from fab2 import F2_MAKE_LETTER, F2_MAKE_LETTER_THIN

def generate(priority,outlayer,inlayer,key_type,boundary,text):

    layer_out=(key_type.split('_')[1])
    drty_out=(key_type.split('_')[2])
    bar_out=(key_type.split('_')[3]+'.'+key_type.split('_')[4])
    layer_in=(key_type.split('_')[5])
    drty_in=(key_type.split('_')[6])
    bar_in=(key_type.split('_')[7]+'.'+key_type.split('_')[8])
    bar_xy=(key_type.split('_')[9])
    txy_f=(text.split('_')[0][2])
    no=str(priority)
   
    ## CELL_NAME_Define
    pre_in = gdstk.Cell("pre_in"+key_type)
    pre_out = gdstk.Cell("pre_out"+key_type)
    box = gdstk.Cell(no+"_"+key_type)       # OVERLAY_BOX_Define
  
    bl_1 = gdstk.Cell("bl_1_text"+key_type)
    bl_2 = gdstk.Cell("bl_2_text"+key_type)
    br_1 = gdstk.Cell("br_1_text"+key_type)
    br_2 = gdstk.Cell("br_2_text"+key_type)
    pre_bl = gdstk.Cell("text_bl"+key_type)     
    pre_br = gdstk.Cell("text_br"+key_type)    
    bl_p = gdstk.Cell(no+"_TEXT_"+layer_out+"_"+layer_in+"_"+str(inlayer))   # LEFT_TEXTBOX_Define
    br_p = gdstk.Cell(no+"_TEXT_"+layer_in+"_"+str(inlayer)+"_"+layer_out)   # RIGHT_TEXTBOX_Define
    
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
    # OVERLAY_CIS_BOX
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
    
    # OVERLAY_Inlayer_TEXT_Define  ## letter,layer_no,size_x,size_y,thin
    bar_xy = (key_type.split('_')[9])
    txy = (key_type.split('_')[-1])
    txy_f = (text.split('_')[0][2])
    if txy_f == 'K' and int(txy) == 7 :
        txy = (text.split('_')[0][0])
        if int(txy) == 7:
            txt_y = 10
        else:
            txt_y = 12
        txy_layer = (text.split('_')[1])
        txy_lay = txy_layer.split(',')
        for i in range(0,len(txy_lay)):
            if txy_layer !='0':      
                bl_p.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y),layer=int(txy_lay[i])))
                br_p.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y),layer=int(txy_lay[i])))
            else:
                pass
        bb_1 = (float(bar_xy) - ((float(txy)*2)+2))/2
        txy_half = (txt_y-float(txy))/2
        polygons = F2_MAKE_LETTER.main(layer_out[0],int(inlayer),txy,txy)
        try:
            bl_1.add(*polygons)
        except:
            bl_1.add(polygons)
        pre_bl.add(gdstk.Reference(bl_1,(float(bb_1),float(txy_half))))
        polygons = F2_MAKE_LETTER.main(layer_out[1],int(inlayer),txy,txy)
        try:
            bl_2.add(*polygons)
        except:
            bl_2.add(polygons)
        pre_bl.add(gdstk.Reference(bl_2,(float(bb_1)+float(txy)+2,float(txy_half))))
      
        # OVERLAY_BL_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(float(bar_xy),txt_y))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_bl),"not",layer=int(inlayer))
            bl_p.add(*text)    
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_bl),"and",layer=int(inlayer))
            bl_p.add(*text)
        
        # OVERLAY_BR_TEXT_Define   ## letter,layer_no,size_x,size_y,thin
        polygons =F2_MAKE_LETTER.main(layer_in[0],int(inlayer),txy,txy)
        try:
            br_1.add(*polygons)
        except:
            br_1.add(polygons)
        pre_br.add(gdstk.Reference(br_1,((float(bb_1),float(txy_half)))))
        polygons = F2_MAKE_LETTER.main(layer_in[1],int(inlayer),txy,txy)
        try:
            br_2.add(*polygons)
        except:
            br_2.add(polygons)
        pre_br.add(gdstk.Reference(br_2,(float(bb_1)+float(txy)+2,float(txy_half))))

        # OVERLAY_BR_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(float(bar_xy),txt_y))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_br),"not",layer=int(inlayer))
            br_p.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_br),"and",layer=int(inlayer))
            br_p.add(*text)
    # OVERLAY_INBOX BLOCK
    elif txy_f == 'N' and int(txy) == 7 :
        txy = (text.split('_')[0][0])
        if int(txy) == 7:
            txt_y = 10
        else:
            txt_y = 12 
        bar_half = (float(bar_xy)/2)
        in_half = int(12/2)
        xy = float(bar_half - in_half)
        txy2=(text.split('_')[0][1])
        txy_layer=(text.split('_')[1])
        txy_lay = txy_layer.split(',')
        for i in range(0,len(txy_lay)):
            if txy_layer !='0':
                box.add(gdstk.rectangle((xy,xy),(xy+(in_half*2),xy+(in_half*2)),layer=int(txy_lay[i])))
                bl_p.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y),layer=int(txy_lay[i])))
                br_p.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y),layer=int(txy_lay[i])))
            else:
                pass
        thin=float(int(txy2)/txt_y)
        bb_1 = (float(bar_xy) - ((float(txy)*2)+2))/2
        txy_half = (txt_y-float(txy))/2
        polygons = F2_MAKE_LETTER_THIN.main(layer_out[0],int(inlayer),txy,txy,thin)
        try:
            bl_1.add(*polygons)
        except:
            bl_1.add(polygons)
        pre_bl.add(gdstk.Reference(bl_1,(float(bb_1),float(txy_half))))
        polygons = F2_MAKE_LETTER_THIN.main(layer_out[1],int(inlayer),txy,txy,thin)
        try:
            bl_2.add(*polygons)
        except:
            bl_2.add(polygons)
        pre_bl.add(gdstk.Reference(bl_2,(float(bb_1)+float(txy)+2,float(txy_half))))

        # OVERLAY_BL_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(float(bar_xy),txt_y))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_bl),"not",layer=int(inlayer))
            bl_p.add(*text)    
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_bl),"and",layer=int(inlayer))
            bl_p.add(*text)
        
        # OVERLAY_BR_TEXT_Define   ##글자,layer_no,size_x,size_y
        polygons = F2_MAKE_LETTER_THIN.main(layer_in[0],int(inlayer),txy,txy,thin)
        try:
            br_1.add(*polygons)
        except:
            br_1.add(polygons)
        pre_br.add(gdstk.Reference(br_1,((float(bb_1),float(txy_half)))))
        polygons = F2_MAKE_LETTER_THIN.main(layer_in[1],int(inlayer),txy,txy,thin)
        try:
            br_2.add(*polygons)
        except:
            br_2.add(polygons)
        pre_br.add(gdstk.Reference(br_2,(float(bb_1)+float(txy)+2,float(txy_half))))

        # OVERLAY_BR_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(float(bar_xy),txt_y))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_br),"not",layer=int(inlayer))
            br_p.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_br),"and",layer=int(inlayer))
            br_p.add(*text)
    #OVERLAY_TEXT_9um_BOUNDARY_12um
    elif txy_f == 'K' and int(txy) !=7 :
        txy = (text.split('_')[0][0])
        if int(txy) == 7:
            txt_y = 10
        else:
            txt_y = 12 
        txy_layer=(text.split('_')[1])
        txy_lay = txy_layer.split(',')
        for i in range(0,len(txy_lay)):
            if txy_layer !='0':      
                bl_p.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y),layer=int(txy_lay[i])))
                br_p.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y),layer=int(txy_lay[i])))
            else:
                pass
        bb_1 = (float(bar_xy) - ((float(txy)*2)+2))/2
        txy_half = (txt_y-float(txy))/2
        polygons = F2_MAKE_LETTER.main(layer_out[0],int(inlayer),txy,txy)
        try:
            bl_1.add(*polygons)
        except:
            bl_1.add(polygons)
        pre_bl.add(gdstk.Reference(bl_1,(float(bb_1),float(txy_half))))
        polygons = F2_MAKE_LETTER.main(layer_out[1],int(inlayer),txy,txy)
        try:
            bl_2.add(*polygons)
        except:
            bl_2.add(polygons)
        pre_bl.add(gdstk.Reference(bl_2,(float(bb_1)+float(txy)+2,float(txy_half))))
        # OVERLAY_BL_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(float(bar_xy),txt_y))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_bl),"not",layer=int(inlayer))
            bl_p.add(*text)    
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_bl),"and",layer=int(inlayer))
            bl_p.add(*text)
        
        # OVERLAY_BR_TEXT_Define   ## letter,layer_no,size_x,size_y,thin
        polygons =F2_MAKE_LETTER.main(layer_in[0],int(inlayer),txy,txy)
        try:
            br_1.add(*polygons)
        except:
            br_1.add(polygons)
        pre_br.add(gdstk.Reference(br_1,((float(bb_1),float(txy_half)))))
        polygons = F2_MAKE_LETTER.main(layer_in[1],int(inlayer),txy,txy)
        try:
            br_2.add(*polygons)
        except:
            br_2.add(polygons)
        pre_br.add(gdstk.Reference(br_2,(float(bb_1)+float(txy)+2,float(txy_half))))
        # OVERLAY_BR_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(float(bar_xy),txt_y))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_br),"not",layer=int(inlayer))
            br_p.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_br),"and",layer=int(inlayer))
            br_p.add(*text)
    # OVERLAY_TEXT_9um_BOUNDARY_12um
    elif txy_f == 'N' and int(txy) != 7 :
        txy = (text.split('_')[0][0])
        if int(txy) == 7:
            txt_y = 10
        else:
            txt_y = 12 
        bar_half = (float(bar_xy)/2)
        in_half = int(16/2)
        xy = float(bar_half - in_half)        
        txy2=(text.split('_')[0][1])
        txy_layer=(text.split('_')[1])
        txy_lay = txy_layer.split(',')
        for i in range(0,len(txy_lay)):
            if txy_layer !='0':
                box.add(gdstk.rectangle((xy,xy),(xy+(in_half*2),xy+(in_half*2)),layer=int(txy_lay[i])))
                bl_p.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y),layer=int(txy_lay[i])))
                br_p.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y),layer=int(txy_lay[i])))
            else:
                pass
        thin=float(int(txy2)/12)
        bb_1 = (float(bar_xy) - ((float(txy)*2)+2))/2
        txy_half = (txt_y-float(txy))/2
        polygons = F2_MAKE_LETTER_THIN.main(layer_out[0],int(inlayer),txy,txy,thin)
        try:
            bl_1.add(*polygons)
        except:
            bl_1.add(polygons)
        pre_bl.add(gdstk.Reference(bl_1,(float(bb_1),float(txy_half))))
        polygons = F2_MAKE_LETTER_THIN.main(layer_out[1],int(inlayer),txy,txy,thin)
        try:
            bl_2.add(*polygons)
        except:
            bl_2.add(polygons)
        pre_bl.add(gdstk.Reference(bl_2,(float(bb_1)+float(txy)+2,float(txy_half))))

        # OVERLAY_BL_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(float(bar_xy),txt_y))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_bl),"not",layer=int(inlayer))
            bl_p.add(*text)    
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_bl),"and",layer=int(inlayer))
            bl_p.add(*text)
        
        # OVERLAY_BR_TEXT_Define   ##글자,layer_no,size_x,size_y
        polygons = F2_MAKE_LETTER_THIN.main(layer_in[0],int(inlayer),txy,txy,thin)
        try:
            br_1.add(*polygons)
        except:
            br_1.add(polygons)
        pre_br.add(gdstk.Reference(br_1,((float(bb_1),float(txy_half)))))
        polygons = F2_MAKE_LETTER_THIN.main(layer_in[1],int(inlayer),txy,txy,thin)
        try:
            br_2.add(*polygons)
        except:
            br_2.add(polygons)
        pre_br.add(gdstk.Reference(br_2,(float(bb_1)+float(txy)+2,float(txy_half))))

        # OVERLAY_BR_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(float(bar_xy),txt_y))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_br),"not",layer=int(inlayer))
            br_p.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_br),"and",layer=int(inlayer))
            br_p.add(*text)
   # Boundary
    for i in range(0,len(boundary)):
        bound = gdstk.rectangle((0,0),(float(bar_xy),(float(bar_xy))), layer=int(boundary[i]))
        box.add(bound)
        if int(txy) == 7 :
            bound2 = gdstk.rectangle((0,0),(float(bar_xy),10),layer=int(boundary[i]))
            bl_p.add(bound2)
            br_p.add(bound2)
        else:
            bound2 = gdstk.rectangle((0,0),(float(bar_xy),12),layer=int(boundary[i]))
            bl_p.add(bound2)
            br_p.add(bound2)     
    return box, bl_p, br_p

def start(priority,outlayer,inlayer,key_type,boundary,text,bllib,brlib):
    no=str(priority)
    bl = gdstk.Cell(no+"_"+key_type+"_BL") # cell 생성
    br = gdstk.Cell(no+"_"+key_type+"_BR") # cell 생성
    box, bl_p, br_p = generate(priority,outlayer,inlayer,key_type,boundary,text)
    bllib.add(box, bl_p)
    brlib.add(box, br_p)
    bl.add(gdstk.Reference(bl_p,(0,0)))
    br.add(gdstk.Reference(br_p,(0,0)))
    txy=(text.split('_')[0][0])
    if int(txy) == 7 :
        bl.add(gdstk.Reference(box,(0,10)))
        br.add(gdstk.Reference(box,(0,10)))
    else:
        bl.add(gdstk.Reference(box,(0,12)))
        br.add(gdstk.Reference(box,(0,12)))
    return bl, br

if __name__ == "__main__":
    priority = 1
    outlayer = 77
    inlayer = 96
    key_type = "OVERLAY_AA_T_2_0_TN_M_2_0_27_75"
    boundary = [63,3]  # list Type
    text      = "72K_0"
    bllib = gdstk.Library()
    brlib = gdstk.Library()
    bl_t = bllib.new_cell("bl_top_cell")
    br_t = brlib.new_cell("br_top_cell")
    bl, br = start(priority,outlayer,inlayer,key_type,boundary,text,bllib,brlib)