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
   
   # OVERLAY_In/Out_Layer_TEXT_Define
    left_1 = gdstk.Cell("left_1t"+key_type) 
    left_2 = gdstk.Cell("left_2t"+key_type)
    right_1 = gdstk.Cell("right_1t"+key_type)
    right_2 = gdstk.Cell("right_2t"+key_type) 
    pre_left = gdstk.Cell("pre_left"+key_type)
    pre_right = gdstk.Cell("pre_right"+key_type)
    left = gdstk.Cell(no+"_TEXT_"+layer_out+"_"+layer_in+"_"+str(inlayer))   # LEFT_TEXTBOX_Define
    right = gdstk.Cell(no+"_TEXT_"+layer_in+"_"+str(inlayer)+"_"+layer_out)  # RIGHT_TEXTBOX_Define

    # OVERLAY_LL/LR/UL/UR_Define
    l_1 = gdstk.Cell("L_1t"+key_type)
    l_2 = gdstk.Cell("L_2t"+key_type)
    u_1 = gdstk.Cell("U_1t"+key_type)
    r_2 = gdstk.Cell("R_2t"+key_type) 
    pre_ll = gdstk.Cell("pre_ll"+key_type)
    pre_lr = gdstk.Cell("pre_lr"+key_type)
    pre_ul = gdstk.Cell("pre_ul"+key_type)
    pre_ur = gdstk.Cell("pre_ur"+key_type)
    ll_p = gdstk.Cell(no+"_TEXT_"+layer_in+"_LL_"+str(inlayer)+"_"+layer_out)     # LL_Define
    lr_p = gdstk.Cell(no+"_TEXT_"+layer_in+"_LR_"+str(inlayer)+"_"+layer_out)     # LR_Define
    ul_p = gdstk.Cell(no+"_TEXT_"+layer_in+"_UL_"+str(inlayer)+"_"+layer_out)     # UL_Define
    ur_p = gdstk.Cell(no+"_TEXT_"+layer_in+"_UR_"+str(inlayer)+"_"+layer_out)     # UR_Define
    
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
    txy_f = (text.split('_')[0][2])
    if txy_f == 'K':
        txy = (text.split('_')[0][0])
        bb_1 = (((float(bar_xy)+10)/2)-((float(txy)*2)+2))/2
        ul_1 = ((float(bar_xy))-((float(txy)*2)+2))/2
        txy_half = (10-float(txy))/2
        polygons = F2_MAKE_LETTER.main(layer_in[0],int(inlayer),txy,txy)
        try:
            left_1.add(*polygons)
        except:
            left_1.add(polygons)
        pre_left.add(gdstk.Reference(left_1,(float(bb_1),float(txy_half))))
        polygons = F2_MAKE_LETTER.main(layer_in[1],int(inlayer),txy,txy)
        try:
            left_2.add(*polygons)
        except:
            left_2.add(polygons)
        pre_left.add(gdstk.Reference(left_2,(float(bb_1)+float(txy)+2,float(txy_half))))
        # OVERLAY_Inlayer_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(((float(bar_xy)+10)/2),10))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_left),"not",layer=int(inlayer))
            left.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_left),"and",layer=int(inlayer))
            left.add(*text)

        # OVERLAY_Outlayer_TEXT_Define   ## letter,layer_no,size_x,size_y,thin
        polygons =F2_MAKE_LETTER.main(layer_out[0],int(inlayer),txy,txy)
        try:
            right_1.add(*polygons)
        except:
            right_1.add(polygons)
        pre_right.add(gdstk.Reference(right_1,(float(bb_1),float(txy_half))))
        polygons = F2_MAKE_LETTER.main(layer_out[1],int(inlayer),txy,txy)
        try:
            right_2.add(*polygons)
        except:
            right_2.add(polygons)
        pre_right.add(gdstk.Reference(right_2,(float(bb_1)+float(txy)+2,float(txy_half))))
        # OVERLAY_Outlayer_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(((float(bar_xy)+10)/2),10))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_right),"not",layer=int(inlayer))
            right.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_right),"and",layer=int(inlayer))
            right.add(*text)
    
        # OVERLAY_LL/LR/UL/UR_TEXT_Define  ### letter,layer_no,size_x,size_y,thin
        polygons = F2_MAKE_LETTER.main("L",int(inlayer),txy,txy)
        try:
            l_1.add(*polygons)
        except:
            l_1.add(polygons)
        pre_ll.add(gdstk.Reference(l_1,(float(txy_half),float(ul_1)+float(txy)+2)))
        pre_lr.add(gdstk.Reference(l_1,(float(txy_half),float(ul_1)+float(txy)+2)))
        polygons = F2_MAKE_LETTER.main("L",int(inlayer),txy,txy)
        try:
            l_2.add(*polygons)
        except:
            l_2.add(polygons)
        pre_ll.add(gdstk.Reference(l_2,(float(txy_half),float(ul_1))))
        pre_ul.add(gdstk.Reference(l_2,(float(txy_half),float(ul_1))))
        polygons = F2_MAKE_LETTER.main("U",int(inlayer),txy,txy)
        try:
            u_1.add(*polygons)
        except:
            u_1.add(polygons)
        pre_ul.add(gdstk.Reference(u_1,(float(txy_half),float(ul_1)+float(txy)+2)))
        pre_ur.add(gdstk.Reference(u_1,(float(txy_half),float(ul_1)+float(txy)+2)))
        polygons = F2_MAKE_LETTER.main("R",int(inlayer),txy,txy)
        try:
            r_2.add(*polygons)
        except:
            r_2.add(polygons)
        pre_lr.add(gdstk.Reference(r_2,(float(txy_half),float(ul_1))))
        pre_ur.add(gdstk.Reference(r_2,(float(txy_half),float(ul_1))))

        # OVERLAY_LL_TEXT Trench/Mesa)
        rect = gdstk.rectangle((0,0),(10,float(bar_xy)))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_ll),"not",layer=int(inlayer))
            ll_p.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_ll),"and",layer=int(inlayer))
            ll_p.add(*text) 
        # OVERLAY_LR_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(10,float(bar_xy)))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_lr),"not",layer=int(inlayer))
            lr_p.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_lr),"and",layer=int(inlayer))
            lr_p.add(*text)
        # OVERLAY_UL_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(10,float(bar_xy)))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_ul),"not",layer=int(inlayer))
            ul_p.add(*text)    
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_ul),"and",layer=int(inlayer))
            ul_p.add(*text)
        # OVERLAY_UR_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(10,float(bar_xy)))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_ur),"not",layer=int(inlayer))
            ur_p.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_ur),"and",layer=int(inlayer))
            ur_p.add(*text)
    else:
        txy = (text.split('_')[0][0])
        txy2 = (text.split('_')[0][1])
        txy_layer = (text.split('_')[1])
        thin = float(int(txy2)/10)  #0.5N(5)
        bb_1 = (((float(bar_xy)+10)/2)-((float(txy)*2)+2))/2
        ul_1 = ((float(bar_xy))-((float(txy)*2)+2))/2
        txy_half = (10-float(txy))/2
        bxy_half = (float(bar_xy)+10)/2
        bar_half = (float(bar_xy)/2)       #OVERLAY_INBOX BLOCK
        in_half = int(12/2)                #OVERLAY_INBOX BLOCK
        xy = float(bar_half - in_half)     #OVERLAY_INBOX BLOCK
        if txy_layer !='0':
            txy_lay = txy_layer.split(',')
            for i in range(0,len(txy_lay)):
                left.add(gdstk.rectangle((0,0),(float(bxy_half),10),layer=int(txy_lay[i])))
                right.add(gdstk.rectangle((0,0),(bxy_half,10),layer=int(txy_lay[i])))
                box.add(gdstk.rectangle((xy,xy),(xy+12,xy+12),layer=int(txy_lay[i])))
                ll_p.add(gdstk.rectangle((0,0),(10,float(bar_xy)),layer=int(txy_lay[i])))
                lr_p.add(gdstk.rectangle((0,0),(10,float(bar_xy)),layer=int(txy_lay[i])))
                ul_p.add(gdstk.rectangle((0,0),(10,float(bar_xy)),layer=int(txy_lay[i])))
                ur_p.add(gdstk.rectangle((0,0),(10,float(bar_xy)),layer=int(txy_lay[i]))) 
        else:
            pass

        # OVERLAY_Inlayer_TEXT_Define   ## letter,layer_no,size_x,size_y,thin
        polygons = F2_MAKE_LETTER_THIN.main(layer_in[0],int(inlayer),txy,txy,thin)
        try:
            left_1.add(*polygons)
        except:
            left_1.add(polygons)
        pre_left.add(gdstk.Reference(left_1,(float(bb_1),float(txy_half))))
        polygons = F2_MAKE_LETTER_THIN.main(layer_in[1],int(inlayer),txy,txy,thin)
        try:
            left_2.add(*polygons)
        except:
            left_2.add(polygons)
        pre_left.add(gdstk.Reference(left_2,(float(bb_1)+float(txy)+2,float(txy_half))))    
        # OVERLAY_Inlayer_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(((float(bar_xy)+10)/2),10))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_left),"not",layer=int(inlayer))
            left.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_left),"and",layer=int(inlayer))
            left.add(*text)

        # OVERLAY_Outlayer_TEXT_Define   ## letter,layer_no,size_x,size_y,thin
        polygons =F2_MAKE_LETTER_THIN.main(layer_out[0],int(inlayer),txy,txy,thin)
        try:
            right_1.add(*polygons)
        except:
            right_1.add(polygons)
        pre_right.add(gdstk.Reference(right_1,(float(bb_1),float(txy_half))))
        polygons = F2_MAKE_LETTER_THIN.main(layer_out[1],int(inlayer),txy,txy,thin)
        try:
            right_2.add(*polygons)
        except:
            right_2.add(polygons)
        pre_right.add(gdstk.Reference(right_2,(float(bb_1)+float(txy)+2,float(txy_half))))
        # OVERLAY_Outlayer_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(((float(bar_xy)+10)/2),10))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_right),"not",layer=int(inlayer))
            right.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_right),"and",layer=int(inlayer))
            right.add(*text)
    
        # OVERLAY_LL/LR/UR/UR_TEXT_Define  ### letter,layer_no,size_x,size_y,thin
        polygons = F2_MAKE_LETTER_THIN.main("L",int(inlayer),txy,txy,thin)
        try:
            l_1.add(*polygons)
        except:
            l_1.add(polygons)
        pre_ll.add(gdstk.Reference(l_1,(float(txy_half),float(ul_1)+float(txy)+2)))
        pre_lr.add(gdstk.Reference(l_1,(float(txy_half),float(ul_1)+float(txy)+2)))
        polygons = F2_MAKE_LETTER_THIN.main("L",int(inlayer),txy,txy,thin)
        try:
            l_2.add(*polygons)
        except:
            l_2.add(polygons)
        pre_ll.add(gdstk.Reference(l_2,(float(txy_half),float(ul_1))))
        pre_ul.add(gdstk.Reference(l_2,(float(txy_half),float(ul_1))))
        polygons = F2_MAKE_LETTER_THIN.main("U",int(inlayer),txy,txy,thin)
        try:
            u_1.add(*polygons)
        except:
            u_1.add(polygons)
        pre_ul.add(gdstk.Reference(u_1,(float(txy_half),float(ul_1)+float(txy)+2)))
        pre_ur.add(gdstk.Reference(u_1,(float(txy_half),float(ul_1)+float(txy)+2)))
        polygons = F2_MAKE_LETTER_THIN.main("R",int(inlayer),txy,txy,thin)
        try:
            r_2.add(*polygons)
        except:
            r_2.add(polygons)
        pre_lr.add(gdstk.Reference(r_2,(float(txy_half),float(ul_1))))
        pre_ur.add(gdstk.Reference(r_2,(float(txy_half),float(ul_1))))

        # OVERLAY_LL_TEXT Trench/Mesa)
        rect = gdstk.rectangle((0,0),(10,float(bar_xy)))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_ll),"not",layer=int(inlayer))
            ll_p.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_ll),"and",layer=int(inlayer))
            ll_p.add(*text) 
        # OVERLAY_LR_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(10,float(bar_xy)))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_lr),"not",layer=int(inlayer))
            lr_p.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_lr),"and",layer=int(inlayer))
            lr_p.add(*text)
        # OVERLAY_UL_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(10,float(bar_xy)))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_ul),"not",layer=int(inlayer))
            ul_p.add(*text)    
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_ul),"and",layer=int(inlayer))
            ul_p.add(*text)
        # OVERLAY_UR_TEXT Trench/Mesa
        rect = gdstk.rectangle((0,0),(10,float(bar_xy)))
        if drty_in == "T":
            text = gdstk.boolean(rect,gdstk.Reference(pre_ur),"not",layer=int(inlayer))
            ur_p.add(*text)
        else:
            text = gdstk.boolean(rect,gdstk.Reference(pre_ur),"and",layer=int(inlayer))
            ur_p.add(*text)

    for i in range(0,len(str(outlayer))):
        if outlayer == int(3) :
            text1 =bound2 = gdstk.rectangle((0,0),(((float(bar_xy)+10)/2),10), layer=int(outlayer))
            left.add(text1)
            text2 = gdstk.rectangle((0,0),(((float(bar_xy)+10)/2),10),layer=int(outlayer))
            right.add(text2) 
            text3 = gdstk.rectangle((0,0),(10,(float(bar_xy))),layer=int(outlayer))
            ll_p.add(text3)
            lr_p.add(text3)
            ul_p.add(text3)
            ur_p.add(text3)
                
        # Boundary
        for i in range(0,len(boundary)):
            bound = gdstk.rectangle((0,0),(float(bar_xy),(float(bar_xy))), layer=int(boundary[i]))
            box.add(bound)
            bound2 = gdstk.rectangle((0,0),(((float(bar_xy)+10)/2),10), layer=int(boundary[i]))
            left.add(bound2)
            bound3 = gdstk.rectangle((0,0),(((float(bar_xy)+10)/2),10),layer=int(boundary[i]))
            right.add(bound3) 
            bound4 = gdstk.rectangle((0,0),(10,(float(bar_xy))),layer=int(boundary[i]))
            ll_p.add(bound4)
            lr_p.add(bound4)
            ul_p.add(bound4)
            ur_p.add(bound4)
        return box, left, right, ll_p, lr_p, ul_p, ur_p
    
def start(priority,outlayer,inlayer,key_type,boundary,text,lllib,lrlib,ullib,urlib):
    no=str(priority)
    ll = gdstk.Cell(no+"_"+key_type+"_"+str(outlayer)+"_"+str(inlayer)+"_LL")      # BR_TEXT_Define
    lr = gdstk.Cell(no+"_"+key_type+"_"+str(outlayer)+"_"+str(inlayer)+"_LR")      # BL_TEXT_Define
    ul = gdstk.Cell(no+"_"+key_type+"_"+str(outlayer)+"_"+str(inlayer)+"_UL")      # UL_TEXT_Define
    ur = gdstk.Cell(no+"_"+key_type+"_"+str(outlayer)+"_"+str(inlayer)+"_UR")      # UR_TEXT_Define
    box, left, right,ll_p, lr_p, ul_p, ur_p  = generate(priority,outlayer,inlayer,key_type,boundary,text)
    lllib.add(box, left, right, ll_p)      
    lrlib.add(box, left, right, lr_p)
    ullib.add(box, left, right, ul_p)
    urlib.add(box, left, right, ur_p)

    bar_xy=(key_type.split('_')[9])
    bar_half = (float(bar_xy)+10)/2              
    ll.add(gdstk.Reference(box,(0,10)))
    ll.add(gdstk.Reference(left,(0,0)))
    ll.add(gdstk.Reference(right,((float(bar_half),0))))
    ll.add(gdstk.Reference(ll_p,(float(bar_xy),10)))

    lr.add(gdstk.Reference(box,(0,10)))
    lr.add(gdstk.Reference(left,(0,0)))
    lr.add(gdstk.Reference(right,(float(bar_half),0)))
    lr.add(gdstk.Reference(lr_p,(float(bar_xy),10)))
                      
    ul.add(gdstk.Reference(box,(0,10)))
    ul.add(gdstk.Reference(left,(0,0)))
    ul.add(gdstk.Reference(right,(float(bar_half),0)))
    ul.add(gdstk.Reference(ul_p,(float(bar_xy),10)))
                        
    ur.add(gdstk.Reference(box,(0,10)))
    ur.add(gdstk.Reference(left,(0,0)))
    ur.add(gdstk.Reference(right,(float(bar_half),0)))
    ur.add(gdstk.Reference(ur_p,(float(bar_xy),10)))
    
    ## Cell_rename_duplicate
    ll_cell_names={}
    for cell in lllib.cells:
        if cell.name in ll_cell_names:
            count = ll_cell_names[cell.name]+1
            new_name=f"{cell.name}_{count}"
            cell.name = new_name
            ll_cell_names[cell.name]=count
        else:
            ll_cell_names[cell.name]=1
    lr_cell_names={}
    for cell in lrlib.cells:
        if cell.name in lr_cell_names:
            count = lr_cell_names[cell.name]+1
            new_name=f"{cell.name}_{count}"
            cell.name = new_name
            lr_cell_names[cell.name]=count
        else:
            lr_cell_names[cell.name]=1
    ul_cell_names={}
    for cell in ullib.cells:
        if cell.name in ul_cell_names:
            count = ul_cell_names[cell.name]+1
            new_name=f"{cell.name}_{count}"
            cell.name = new_name
            ul_cell_names[cell.name]=count
        else:
            ul_cell_names[cell.name]=1
    ur_cell_names={}
    for cell in urlib.cells:
        if cell.name in ur_cell_names:
            count = ur_cell_names[cell.name]+1
            new_name=f"{cell.name}_{count}"
            cell.name = new_name
            ur_cell_names[cell.name]=count
        else:
            ur_cell_names[cell.name]=1
    
    return ll, lr, ul, ur

if __name__ == "__main__":
    priority = 1
    outlayer = 77
    inlayer = 96
    key_type = "OVERLAY_KY_M_1_0_PB_M_8_0_28"
    boundary = [63,3] # list Type
    text ="72K_0"
    lllib = gdstk.Library()
    lrlib = gdstk.Library()
    ullib = gdstk.Library()
    urlib = gdstk.Library()
    bl_t = lllib.new_cell("LL_TOP_CELL")
    br_t = lrlib.new_cell("LR_TOP_CELL")  
    ul_t = ullib.new_cell("UL_TOP_CELL")  
    ur_t = urlib.new_cell("UR_TOP_CELL")   
    ll, lr, ul, ur = start(priority,outlayer,inlayer,key_type,boundary,text,lllib,lrlib,ullib,urlib)


