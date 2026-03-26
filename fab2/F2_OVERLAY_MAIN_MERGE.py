import os, gdstk, datetime, glob, tarfile
from fab2 import F2_OVERLAY_SPD_LL_LR_UL_UR_LETTER, F2_OVERLAY_BL_BR_LETTER, F2_OVERLAY_IN_OUT_1ST
import pandas as pd

PRIORITY = []
OUTLAYER = []
INLAYER  = []
KEY_TYPE = []
BOUNDARY = []
TEXT     = []
RETICLE_ID=[]
LAYER_NO = []
DA_TONE  = []
SL_TONE  = []
DICER    = []

def main(process):
    PRIORITY = []
    OUTLAYER = []
    INLAYER  = []
    KEY_TYPE = []
    BOUNDARY = []
    TEXT     = []
    LAYER_NO = []
    RETICLE_ID=[]
    DA_TONE  = []
    SL_TONE  = []
    DICER    = []
    
    BASEPAD  = []
    DK_LAYER = []
    DK_LAYER_NO = []
    with open('./fab2/text/input_overlay.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line_st = line.strip()
            line_sp = line_st.split()
            if line_sp == []:
                pass
            elif 'OVERLAY' in line:
                PRIORITY.append(line_sp[0])
                OUTLAYER.append(line_sp[1])
                INLAYER.append(line_sp[2])
                KEY_TYPE.append(line_sp[3])
                TEXT.append(line_sp[5])
                temp = []
                temp.append(line_sp[4])
                str_tmp = temp[0].split(',')
                BOUNDARY.append(str_tmp)
            else:
                pass
        f.close()
    with open('./fab2/text/dicer.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line_st = line.strip()
            line_sp = line_st.split()
            if line_sp == []:
                pass
            elif line.startswith('BASEPAD'):
                line_st = line.strip()
                line_sp = line_st.split()
                temp = []
                temp.append(line_sp[1])
                BASEPAD = temp[0].split(',')
                continue
            else:
                LAYER_NO.append(line_sp[0])
                RETICLE_ID.append(line_sp[1])         
                DA_TONE.append(line_sp[2])
                SL_TONE.append(line_sp[3])
                DICER.append(line_sp[4])
        f.close()
   
    for i in range(0,len(RETICLE_ID)):
        layer = RETICLE_ID[i]
        tone = DA_TONE[i]
        layer_no = LAYER_NO[i]
        if tone == "DK" :
            DK_LAYER.append(layer)
            DK_LAYER_NO.append(layer_no)
    date = datetime.datetime.now().strftime("%y%m%d")
    key_name = process+"_PHOTOKEY_"+date
    path = ("./fab2/f2_gdsout/"+key_name)
    if os.path.isdir(path):
        pass
    else:
        os.makedirs("./fab2/f2_gdsout/"+key_name)
    path2 = ('./fab2/f2_gdsout/'+key_name+'/'+key_name+'/')
    if os.path.isdir(path2):
        pass
    else:
        os.makedirs('./fab2/f2_gdsout/'+key_name+'/'+key_name+'/')

    if process.find("SPD") == -1 and process.find("NORMAL") == -1 :
    ## OVERLAY_Normal
        bllib = gdstk.Library()                    #BL_LIB
        brlib = gdstk.Library()                    #BR_LIB
        bl_top_cell = process + "_OVERLAY_BL_" + str(date)
        br_top_cell = process + "_OVERLAY_BR_" + str(date)
        bl_t = bllib.new_cell(bl_top_cell)         #BL_TOP_CELL
        br_t = brlib.new_cell(br_top_cell)         #BR_TOP_CELL

        data = {'priority':PRIORITY,'outlayer':OUTLAYER,'inlayer':INLAYER, 'key_type':KEY_TYPE,'boundary':BOUNDARY, 'text':TEXT}
        df = pd.DataFrame(data)
        df_sort = df.sort_values('priority')  #sort by priority  

        rect_y = 0
        y_max = 0   ## External_Y_Max 생성
        for i in range(0,len(df_sort)) :
            PRIORITY = df_sort.iloc[i,0]
            OUTLAYER = df_sort.iloc[i,1]
            INLAYER  = df_sort.iloc[i,2]
            KEY_TYPE = df_sort.iloc[i,3]
            BOUNDARY = df_sort.iloc[i,4]
            TEXT     = df_sort.iloc[i,5]
            bl, br, = F2_OVERLAY_BL_BR_LETTER.start(int(PRIORITY),int(OUTLAYER),int(INLAYER),KEY_TYPE,BOUNDARY,TEXT,bllib,brlib)
            bllib.add(bl)
            brlib.add(br)

            pro_now = int(PRIORITY)
            over_y = int(KEY_TYPE.split('_')[9])+10
            bar_xy=(KEY_TYPE.split('_')[9])

            out_lay = (KEY_TYPE.split('_')[1])
            out_num = OUTLAYER
            out_typ = (KEY_TYPE.split('_')[2])
            in_num = INLAYER
            in_lay = (KEY_TYPE.split('_')[5])
            in_typ = (KEY_TYPE.split('_')[6])
            txy_f = (TEXT.split('_')[0][2])
            txy_split = (TEXT.split('_')[1])
            txy_lay = txy_split.split(',')
            
            ## 첫번째 셀 배치 시작 (0,0)
            if i == 0 :
                pro_bak = pro_now
                bl_t.add(gdstk.Reference(bl,(float(bar_xy),0)))
                br_t.add(gdstk.Reference(br,(0,0)))
                blx_hot = float(bar_xy)+(float(bar_xy)/2)     # External_bl_X_hotspot
                brx_hot = (float(bar_xy)/2)                   # External_br_X_hotspot
                y_hot = 10+float(bar_xy)/2    # External_Y_hotspot
                x_max = float(bar_xy)*2       # External_X_Max
                y_max = over_y                # External_Y_Max
                if in_typ == "T" :
                    if in_lay in DK_LAYER:
                        bl_t.add(gdstk.rectangle((float(bar_xy)-1,0),(float(bar_xy),y_max), layer=int(in_num)))
                        br_t.add(gdstk.rectangle((float(bar_xy),0),((float(bar_xy)+1),y_max), layer=int(in_num)))                     
                if out_typ == "T" :
                    if out_lay in DK_LAYER:
                        bl_t.add(gdstk.rectangle((float(bar_xy)-1,10),(float(bar_xy),y_max), layer=int(out_num)))
                        br_t.add(gdstk.rectangle((float(bar_xy),10),((float(bar_xy)+1),y_max), layer=int(out_num)))
            else:
                if pro_bak == pro_now :
                    rect_y = rect_y
                    y_max = y_max
                    if in_typ == "T":
                        if in_lay in DK_LAYER:
                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(in_num)))
                            br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(in_num)))
                    if out_typ == "T" :
                        if out_lay in DK_LAYER:
                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,y_max-(float(bar_xy))),(float(bar_xy),y_max), layer=int(out_num)))
                            br_t.add(gdstk.rectangle((float(bar_xy),y_max-(float(bar_xy))),((float(bar_xy)+1),y_max), layer=int(out_num)))
                    if any(no in DK_LAYER_NO for no in BOUNDARY):
                        for no in BOUNDARY:
                            if no in DK_LAYER_NO:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(no)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(no)))
                            else:
                                continue
                    if txy_f == 'K':
                        for no2 in txy_lay:
                            if no2 in DK_LAYER_NO :
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),(y_max-float(bar_xy))), layer=int(no2)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),(y_max-float(bar_xy))), layer=int(no2)))
                            else:
                                continue
                else:
                    pro_bak = pro_now
                    rect_y = rect_y + over_y
                    y_max = y_max + over_y
                    if in_typ == "T":
                        if in_lay in DK_LAYER:
                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(in_num)))
                            br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(in_num)))
                    if out_typ == "T" :
                        if out_lay in DK_LAYER:
                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,y_max-(float(bar_xy))),(float(bar_xy),y_max), layer=int(out_num)))
                            br_t.add(gdstk.rectangle((float(bar_xy),y_max-(float(bar_xy))),((float(bar_xy)+1),y_max), layer=int(out_num)))
                    if any(no in DK_LAYER_NO for no in BOUNDARY):
                        for no in BOUNDARY:
                            if no in DK_LAYER_NO:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(no)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(no)))
                            else:
                                continue
                    if txy_f == 'K':
                        for no2 in txy_lay:
                            if no2 in DK_LAYER_NO :
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),(y_max-float(bar_xy))), layer=int(no2)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),(y_max-float(bar_xy))), layer=int(no2)))
                            else:
                                continue

                bl_t.add(gdstk.Reference(bl,(float(bar_xy),rect_y)))
                br_t.add(gdstk.Reference(br,(0,rect_y)))               
            for i in range(0,len(LAYER_NO)):
                layer = LAYER_NO[i]
                if DA_TONE[i] == "DK":
                    bl_t.add(gdstk.rectangle((0,0),(float(bar_xy)-1,y_max), layer=int(layer)))
                    br_t.add(gdstk.rectangle((float(bar_xy)+1,0),((float(bar_xy)*2),y_max), layer=int(layer)))
                if BASEPAD != '-':
                    if RETICLE_ID[i] in BASEPAD:
                        bl_t.add(gdstk.rectangle((float(bar_xy)-1,0),(float(bar_xy),y_max), layer=int(layer)))
                        br_t.add(gdstk.rectangle((float(bar_xy),0),((float(bar_xy)+1),y_max), layer=int(layer))) 
                else:
                    pass
        # Add Block_boundary
        bl_t.add(gdstk.rectangle((0,0),(float(bar_xy),y_max), layer=int(63)))
        br_t.add(gdstk.rectangle((float(bar_xy),0),((float(bar_xy)*2),y_max), layer=int(63)))           
        output_name1 = "./fab2/f2_gdsout/"+key_name+"/"+bl_top_cell+".gds"
        output_name2 = "./fab2/f2_gdsout/"+key_name+"/"+br_top_cell+".gds"
        bllib.write_gds(output_name1)
        brlib.write_gds(output_name2)
    else:
        ## OVERLAY_SPD
        lllib = gdstk.Library()                    #LL_LIB
        lrlib = gdstk.Library()                    #LR_LIB
        ullib = gdstk.Library()                    #UL_LIB
        urlib = gdstk.Library()                    #UR_LIB
        ll_top_cell = process + "_OVERLAY_LL_" + str(date)
        lr_top_cell = process + "_OVERLAY_LR_" + str(date)
        ul_top_cell = process + "_OVERLAY_UL_" + str(date)
        ur_top_cell = process + "_OVERLAY_UR_" + str(date)
        ll_t = lllib.new_cell(ll_top_cell)         #LL_TOP_CELL
        lr_t = lrlib.new_cell(lr_top_cell)         #LR_TOP_CELL
        ul_t = ullib.new_cell(ul_top_cell)         #UL_TOP_CELL
        ur_t = urlib.new_cell(ur_top_cell)         #UR_TOP_CELL
        
        data = {'priority':PRIORITY,'outlayer':OUTLAYER,'inlayer':INLAYER, 'key_type':KEY_TYPE,'boundary':BOUNDARY, 'text':TEXT}
        df = pd.DataFrame(data)
        df_sort = df.sort_values('priority')  #sort by priority  

        rect_y = 0
        y_max = 0   ## External_Y_Max 생성

        for i in range(0,len(df_sort)) :
            PRIORITY = df_sort.iloc[i,0]
            OUTLAYER = df_sort.iloc[i,1]
            INLAYER  = df_sort.iloc[i,2]
            KEY_TYPE = df_sort.iloc[i,3]
            BOUNDARY = df_sort.iloc[i,4]
            TEXT     = df_sort.iloc[i,5]
            ll, lr, ul, ur = F2_OVERLAY_SPD_LL_LR_UL_UR_LETTER.start(int(PRIORITY),int(OUTLAYER),int(INLAYER),KEY_TYPE,BOUNDARY,TEXT,lllib,lrlib,ullib,urlib)
            lllib.add(ll)
            lrlib.add(lr)
            ullib.add(ul)
            urlib.add(ur)
            pro_now = int(PRIORITY)
            over_y = int(KEY_TYPE.split('_')[9])+10
            bar_xy=(KEY_TYPE.split('_')[9])
            if i == 0 :  
                pro_bak = pro_now
                ll_t.add(gdstk.Reference(ll,(0,0)))
                lr_t.add(gdstk.Reference(lr,(0,0)))
                ul_t.add(gdstk.Reference(ul,(0,0)))
                ur_t.add(gdstk.Reference(ur,(0,0)))
                x_hot = float(bar_xy)/2    # External_X_hotspot
                y_hot = 10+float(bar_xy)/2 # External_Y_hotspot
                x_max = float(bar_xy)+10   # External_X_Max
                y_max = over_y             # External_Y_Max
            else:
                if pro_bak == pro_now :
                    rect_y = rect_y
                    y_max = y_max
                else :
                    pro_bak = pro_now
                    rect_y = rect_y + over_y
                    y_max = y_max + over_y
                ll_t.add(gdstk.Reference(ll,(0,rect_y)))
                lr_t.add(gdstk.Reference(lr,(0,rect_y)))
                ul_t.add(gdstk.Reference(ul,(0,rect_y)))
                ur_t.add(gdstk.Reference(ur,(0,rect_y)))
        output_name1 = "./fab2/f2_gdsout/"+key_name+"/"+ll_top_cell+".gds"
        output_name2 = "./fab2/f2_gdsout/"+key_name+"/"+lr_top_cell+".gds"
        output_name3 = "./fab2/f2_gdsout/"+key_name+"/"+ul_top_cell+".gds"
        output_name4 = "./fab2/f2_gdsout/"+key_name+"/"+ur_top_cell+".gds"
        lllib.write_gds(output_name1)
        lrlib.write_gds(output_name2)
        ullib.write_gds(output_name3)
        urlib.write_gds(output_name4)
    
    pro = process.split('_')[0]
    gds_over = glob.glob("./fab2/f2_gdsout/"+key_name+"/*OVERLAY*.gds")
    for i in range(0,len(gds_over)) :
        top1=(gds_over[i].split('.gds')[0])
        top=(top1.split('\\')[-1])
        ovlist=top1.split('_')
        for i in range(0,len(ovlist)):
            if "OVERLAY" in ovlist[i]:
                overty=ovlist[i+1]
        out = "./fab2/f2_gdsout/"+key_name+'/'+key_name+'/'+top+ ".OVERLAY_"+overty
        t_out= "./fab2/f2_gdsout/"+key_name+'/'+key_name+'/'+key_name+'.txt'
        with open (out,"w")as f:
            f.write("File_Type\t\t\t \"GDS\"\n")
            f.write("Hotspot_Name\t\t\t \"1\"\n")
            if overty == 'BL':
                f.write("Hotspot_X\t\t\t \"%s\"\n" %(blx_hot))
            elif overty == 'BR':
                f.write("Hotspot_X\t\t\t \"%s\"\n" %(brx_hot))
            else:
                f.write("Hotspot_X\t\t\t \"%s\"\n" %(x_hot))
            f.write("Hotspot_Y\t\t\t \"%s\"\n" %(y_hot)) 
            f.write("Hotspot_End\n")
            f.write("Version\t\t\t\t 9\n")
            f.write("File\t\t\t\t \"$STD_KEY/%s/%s/%s.gds\"\n" %(pro,key_name,top))
            f.write("Topstr\t\t\t\t \"%s\"\n" %(top))
            f.write("BlTopStr\t\t\t \"NONE\"\n")
            f.write("SizeLay\t\t\t\t -1\n")
            f.write("SizeDT\t\t\t\t -1\n")
            f.write("Strip\t\t\t\t 0\n")
            f.write("Missing_OK\t\t\t 0\n")
            f.write("Snap_OK\t\t\t\t 0\n")
            f.write("Inhibit_Autosize\t\t 0\n")
            f.write("X_Min\t\t\t\t \"0\"\n")
            f.write("Y_Min\t\t\t\t \"0\"\n")
            f.write("X_Max\t\t\t\t \"%s\"\n" %(x_max))
            f.write("Y_Max\t\t\t\t \"%s\"\n" %(y_max))
            f.write("SB_Ext\t\t\t\t 0\n")
            f.write("SB_File_Loc\t\t\t \"NONE\"\n")
            f.write("SB_Min_X\t\t\t 0\n")
            f.write("SB_Min_Y\t\t\t 0\n")
            f.write("SB_Max_X\t\t\t 0\n")
            f.write("SB_Max_Y\t\t\t 0\n")
            f.write("SB_Align\t\t\t \"CC\"\n")
            f.write("Comment\t\t\t\t 0\n")
            f.write("End_Processes\n")
            f.close()
        with open (t_out,"a")as f:
            if overty == 'BL':
                f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top,'OVERLAY_'+overty,top,x_max,y_max,blx_hot,y_hot))
            elif overty == 'BR' :
                f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top,'OVERLAY_'+overty,top,x_max,y_max,brx_hot,y_hot))
            else:
                f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top,'OVERLAY_'+overty,top,x_max,y_max,x_hot,y_hot))

    ## ETC_KEY_Drawing
    OUTLAYER = []
    INLAYER  = []
    KEY_TYPE = []
    BOUNDARY = []
    TEXT     = []
    LAYER_NO = []
    RETICLE_ID=[]
    DA_TONE  = []
    SL_TONE  = []
    DICER    = []

    if os.path.isfile('./fab2/text/1st_overlay.txt'):
        with open('./fab2/text/1st_overlay.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                line_st=line.strip()
                line_sp=line_st.split()
                if line_sp == []:
                    pass
                elif '1STOVER' in line:
                    line_st=line.strip()
                    line_sp=line_st.split()
                    OUTLAYER.append(line_sp[0])
                    INLAYER.append(line_sp[1])
                    KEY_TYPE.append(line_sp[2])
                    BOUNDARY.append(line_sp[3])
                    TEXT.append(line_sp[4])
            f.close()
    else:
        pass
    if os.path.isfile('./fab2/text/dicer.txt'):
        with open('./fab2/text/dicer.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                line_st=line.strip()
                line_sp=line_st.split()
                if line_sp == []:
                    pass
                elif line.startswith('BASEPAD'):
                    continue       
                else:
                    line_st=line.strip()
                    line_sp=line_st.split()
                    LAYER_NO.append(line_sp[0])
                    RETICLE_ID.append(line_sp[1])         
                    DA_TONE.append(line_sp[2])
                    SL_TONE.append(line_sp[3])
                    DICER.append(line_sp[4])
            f.close()
    else:
        pass

    # Layers_file
    if os.path.isfile('./fab2/text/dicer.txt'):  
        out = "./fab2/f2_gdsout/"+key_name+'/'+key_name+'/'+key_name+".layers"
        with open (out,"w")as f:    
            pre_layer = []
            f.write("Version\t\t\t\t\t 6\n")
            for i in range(0,len(LAYER_NO)):
                layer = LAYER_NO[i]
                name = RETICLE_ID[i]
                if layer in pre_layer:
                    continue
                else:
                    pre_layer.append(layer)                        
                    if DA_TONE[i] == "DK":
                        filed_tone = "Clear"
                    elif DA_TONE[i] == "CL":
                        filed_tone = "Dark"
                    if SL_TONE[i] == "DK":
                        sl_tone = "Dark"
                    elif SL_TONE[i] == "CL":
                        sl_tone = "Clear"
                    else:
                        print("Please Check the Input Layers Information file.")
                        break   
                    pre_layer.append(layer)                         
                    f.write("Layer\t\t\t\t\t %s\n"%(layer))
                    f.write("Layer_Datatype\t\t\t\t 0\n")
                    f.write("Field_Polarity\t\t\t\t \"%s\"\n" %(filed_tone))
                    f.write("Scribe_Polarity\t\t\t\t \"%s\"\n" %(sl_tone)) 
                    f.write("Drop\t\t\t\t\t \"\"\n")
                    f.write("Comment\t\t\t\t\t \"%s\"\n" %(name)) 
                    f.write("Groups\t\t\t\t\t \"\"\n")
                    f.write("\n")
            f.write("End_of_Operations\n")
            f.close()
        #DICER
        lib = gdstk.Library() # lib 생성
        cell_name = process +"_DICER_"+date
        cell = lib.new_cell(cell_name) # cell 생성
        error = []
        for i in range(0,len(LAYER_NO)) :
            layer_no = LAYER_NO[i]
            #print(layer_no)
            if DICER[i] == "1" :
                type1_0 = gdstk.rectangle((0,20),(25,25))
                type1_1 = gdstk.rectangle((20,0),(25,25))
                type1 = gdstk.boolean(type1_0,type1_1,"or",layer=int(layer_no))
                cell.add(*type1)
                bound = gdstk.rectangle((0,0),(25,25), layer=int(63))
                cell.add(bound)
                x_max = 25
                y_max = 25
            elif DICER[i] == "2" :
                for i in range(4):
                    x1 = 1 
                    if i == 0 :
                        y1 = 21
                    elif i  == 1 :
                        y1 = 22
                    elif i == 2 :
                        y1 = 23
                    elif i == 3 :
                        y1 = 24
                    for i in range(24):
                        type2_0 = gdstk.rectangle((x1,y1),(x1+0.5,y1+0.5), layer=int(layer_no))
                        cell.add(type2_0)
                        x1 += 1
                    else:
                        pass
                for i in range(4):
                    y2 = 1 
                    if i == 0 :
                        x2 = 21
                    elif i  == 1 :
                        x2 = 22
                    elif i == 2 :
                        x2 = 23
                    elif i == 3 :
                        x2 = 24
                    for i in range(24):
                        type2_1 = gdstk.rectangle((x2,y2),(x2+0.5,y2+0.5), layer=int(layer_no))
                        cell.add(type2_1)
                        y2 += 1
                    else:
                        pass
            elif DICER[i] == "3" :
                type3_0 = gdstk.rectangle((0,15.5),(19.5,19.5))
                type3_1 = gdstk.rectangle((15.5,0),(19.5,19.5))
                type3 = gdstk.boolean(type3_0,type3_1,"or",layer=int(layer_no))
                cell.add(*type3)
                bound = gdstk.rectangle((0,0),(19.5,19.5), layer=int(63))
                cell.add(bound)
                x_max = 19.5
                y_max = 19.5
            elif DICER[i] == "4" :
                for i in range(3):
                    x1 = 0.5 
                    if i == 0 :
                        y1 = 16.5
                    elif i  == 1 :
                        y1 = 17.5
                    elif i == 2 :
                        y1 = 18.5
                    for i in range(19):
                        type4_0 = gdstk.rectangle((x1,y1),(x1+0.5,y1+0.5), layer=int(layer_no))
                        cell.add(type4_0)
                        x1 += 1
                    else:
                        pass
                for i in range(4):
                    y2 = 0.5 
                    if i == 0 :
                        x2 = 16.5
                    elif i  == 1 :
                        x2 = 17.5
                    elif i == 2 :
                        x2 = 18.5
                    for i in range(19):
                        type4_1 = gdstk.rectangle((x2,y2),(x2+0.5,y2+0.5), layer=int(layer_no))
                        cell.add(type4_1)
                        y2 += 1
                    else:
                        pass
            elif DICER[i] == "5" :
                type5_0 = gdstk.rectangle((0,25),(30,30))
                type5_1 = gdstk.rectangle((25,0),(30,30))
                type5 = gdstk.boolean(type5_0,type5_1,"or",layer=int(layer_no))
                cell.add(*type5)
                bound = gdstk.rectangle((0,0),(30,30), layer=int(63))
                cell.add(bound)
                x_max = 30
                y_max = 30
            elif DICER[i] == "6" :
                for i in range(4):
                    x1 = 1 
                    if i == 0 :
                        y1 = 26
                    elif i  == 1 :
                        y1 = 27
                    elif i == 2 :
                        y1 = 28
                    elif i == 3 :
                        y1 = 29
                    for i in range(29):
                        type6_0 = gdstk.rectangle((x1,y1),(x1+0.5,y1+0.5), layer=int(layer_no))
                        cell.add(type6_0)
                        x1 += 1
                    else:
                        pass
                for i in range(4):
                    y2 = 1 
                    if i == 0 :
                        x2 = 26
                    elif i  == 1 :
                        x2 = 27
                    elif i == 2 :
                        x2 = 28
                    elif i == 3 :
                        x2 = 29
                    for i in range(29):
                        type6_1 = gdstk.rectangle((x2,y2),(x2+0.5,y2+0.5), layer=int(layer_no))
                        cell.add(type6_1)
                        y2 += 1
                    else:
                        pass
            elif DICER[i] == "-" :
                pass 
            else:
                error.append(layer_no)
        if len(error) == 0 :
            pass
        else:
            print (" ERROR DICER LAYER_NO : %s "%(error))                
        output_name ="./fab2/f2_gdsout/"+key_name+"/"+cell_name+".gds"
        lib.write_gds(output_name)

        gds_dicer = glob.glob("./fab2/f2_gdsout/"+key_name+"/"+"*DICER*.gds")
        for i in range(0,len(gds_dicer)) :
            top1=(gds_dicer[i].split('.gds')[0])
            top=(top1.split('\\')[-1])
            out = "./fab2/f2_gdsout/"+key_name+'/'+key_name+'/'+cell_name+".DICER"
            t_out= "./fab2/f2_gdsout/"+key_name+'/'+key_name+'/'+key_name+'.txt'
            with open (out,"w")as f:
                f.write("File_Type\t\t\t \"GDS\"\n")
                f.write("Hotspot_Name\t\t\t \"1\"\n")
                f.write("Hotspot_X\t\t\t \"0\"\n")
                f.write("Hotspot_Y\t\t\t \"0\"\n") 
                f.write("Hotspot_End\n")
                f.write("Version\t\t\t\t 9\n")
                f.write("File\t\t\t\t \"$STD_KEY/%s/%s/%s.gds\"\n" %(pro,key_name,top))
                f.write("Topstr\t\t\t\t \"%s\"\n" %(top))
                f.write("BlTopStr\t\t\t \"NONE\"\n")
                f.write("SizeLay\t\t\t\t -1\n")
                f.write("SizeDT\t\t\t\t -1\n")
                f.write("Strip\t\t\t\t 0\n")
                f.write("Missing_OK\t\t\t 0\n")
                f.write("Snap_OK\t\t\t\t 0\n")
                f.write("Inhibit_Autosize\t\t 0\n")
                f.write("X_Min\t\t\t\t \"0\"\n")
                f.write("Y_Min\t\t\t\t \"0\"\n")
                f.write("X_Max\t\t\t\t \"%s\"\n" %(x_max))
                f.write("Y_Max\t\t\t\t \"%s\"\n" %(y_max))
                f.write("SB_Ext\t\t\t\t 0\n")
                f.write("SB_File_Loc\t\t\t \"NONE\"\n")
                f.write("SB_Min_X\t\t\t 0\n")
                f.write("SB_Min_Y\t\t\t 0\n")
                f.write("SB_Max_X\t\t\t 0\n")
                f.write("SB_Max_Y\t\t\t 0\n")
                f.write("SB_Align\t\t\t \"CC\"\n")
                f.write("Comment\t\t\t\t 0\n")
                f.write("End_Processes\n")
                f.close()
            with open (t_out,"a")as f:
                f.write("%s.gds\tDICER\t%s\t0\t0\t%s\t%s\t0\t0\n" %(top,top,x_max,y_max))
    else:
        pass

    #1ST_OVERLAY
    if os.path.isfile('./fab2/text/1st_overlay.txt'):
        inlib = gdstk.Library() # lib 생성
        outlib = gdstk.Library()
        in_top_cell = process + "_1ST_IN_" + date
        out_top_cell = process + "_1ST_OUT_" + date
        in_top = inlib.new_cell(in_top_cell)
        out_top = outlib.new_cell(out_top_cell)
        for i in range(0,len(KEY_TYPE)):
            overlay_1st=KEY_TYPE[i]
            if overlay_1st.split('_')[0] == "1STOVER":
                outlayer = OUTLAYER[i]
                inlayer  = INLAYER[i]
                key_type = KEY_TYPE[i]
                boundary = BOUNDARY[i]
                text     = TEXT[i]
                in_1st, out_1st = F2_OVERLAY_IN_OUT_1ST.start(outlayer,inlayer,key_type,boundary,text,inlib,outlib)
                inlib.add(in_1st)
                outlib.add(out_1st)
                x_max = int(overlay_1st.split('_')[9])
                y_max = int(overlay_1st.split('_')[9])+10
                if i == 0 :
                    in_top.add(gdstk.Reference(in_1st,(0,0)))
                    out_top.add(gdstk.Reference(out_1st,(0,0)))
                else:
                    in_top.add(gdstk.Reference(in_1st,(0,0)))
                    out_top.add(gdstk.Reference(out_1st,(0,0)))
            else:
                pass
        output1 = "./fab2/f2_gdsout/"+key_name+"/"+in_top_cell+".gds"
        output2 = "./fab2/f2_gdsout/"+key_name+"/"+out_top_cell+".gds"
        inlib.write_gds(output1)
        outlib.write_gds(output2)
    else:
        pass

    gds_tar = glob.glob("./fab2/f2_gdsout/"+key_name+"/"+"*1ST*.gds")
    for i in range(0,len(gds_tar)) :
        top1=(gds_tar[i].split('.gds')[0])
        top=(top1.split('\\')[-1])
        frist_list=top1.split('_')
        for i in range(0,len(frist_list)):
            if "1ST" in frist_list[i]:
                frsty=frist_list[i+1]
        out = "./fab2/f2_gdsout/"+key_name+'/'+key_name+'/'+top+".1ST_"+frsty
        t_out= "./fab2/f2_gdsout/"+key_name+'/'+key_name+'/'+key_name+'.txt'
        with open (out,"w")as f:
            f.write("File_Type\t\t\t \"GDS\"\n")
            f.write("Hotspot_Name\t\t\t \"1\"\n")
            f.write("Hotspot_X\t\t\t \"0\"\n")
            f.write("Hotspot_Y\t\t\t \"0\"\n") 
            f.write("Hotspot_End\n")
            f.write("Version\t\t\t\t 9\n")
            f.write("File\t\t\t\t \"$STD_KEY/%s/%s/%s.gds\"\n" %(pro,key_name,top))
            f.write("Topstr\t\t\t\t \"%s\"\n" %(top))
            f.write("BlTopStr\t\t\t \"NONE\"\n")
            f.write("SizeLay\t\t\t\t -1\n")
            f.write("SizeDT\t\t\t\t -1\n")
            f.write("Strip\t\t\t\t 0\n")
            f.write("Missing_OK\t\t\t 0\n")
            f.write("Snap_OK\t\t\t\t 0\n")
            f.write("Inhibit_Autosize\t\t 0\n")
            f.write("X_Min\t\t\t\t \"0\"\n")
            f.write("Y_Min\t\t\t\t \"0\"\n")
            f.write("X_Max\t\t\t\t \"%s\"\n" %(x_max))
            f.write("Y_Max\t\t\t\t \"%s\"\n" %(y_max))
            f.write("SB_Ext\t\t\t\t 0\n")
            f.write("SB_File_Loc\t\t\t \"NONE\"\n")
            f.write("SB_Min_X\t\t\t 0\n")
            f.write("SB_Min_Y\t\t\t 0\n")
            f.write("SB_Max_X\t\t\t 0\n")
            f.write("SB_Max_Y\t\t\t 0\n")
            f.write("SB_Align\t\t\t \"CC\"\n")
            f.write("Comment\t\t\t\t 0\n")
            f.write("End_Processes\n")
            f.close()
        with open (t_out,"a")as f:
            f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t0\t0\n" %(top,'1ST_'+frsty,top,x_max,y_max))

if __name__ == '__main__':
    process  = "BD130S_60um"
    priority = [1,2,3]
    outlayer = [119,3,3]
    inlayer  = [77,77,2]
    key_type = ["OVERLAY_KY_M_2_0_PB_M_2_0_28_6","OVERLAY_AA_T_1_0_PB_M_2_0_28_6","OVERLAY_AA_T_1_0_NB_M_8_0_28_6"]
    boundary = [[63,3],[63],[63]]
    text     = ["70_0","75_11","70_0"]
    bl, br, = main(process,priority,outlayer,inlayer,key_type,boundary,text)