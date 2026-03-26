## History ##
# Si-Capacitor process overlay. - 2025/12/30
# Change the BASEPAD define. - 2026/02/28
import os, gdstk, datetime, glob
from fab2 import F2_OVERLAY_BL_BR_LETTER, F2_OVERLAY_IN_OUT_1ST,F2_OVERLAY_SPD_LL_LR_UL_UR_LETTER
import pandas as pd

PRIORITY  = []
OUTLAYER  = []
INLAYER   = []
KEY_TYPE  = []
BOUNDARY  = []
TEXT      = []
RETICLE_ID =[]
LAYER_NO  = []
DA_TONE   = []
SL_TONE   = []
DICER     = []
OVERTYPE  = []
# CIS_BSI
BPRIORITY = []
BOUTLAYER = []
BINLAYER  = []
BKEY_TYPE = []
BOUNDARY  = []
BTEXT     = []

def split_file():
    with open('./fab2/text/input_overlay.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        count_dict = {}
        current_content = []
        output_file = None
        is_recording = False
        previous_name = None 
        
        for line in lines:
            line = line.strip()
            if line.startswith('Priority'): #'Priority'로 무시
                continue
            if line.startswith('001'): #'01'로 시작
                parts = line.split()
                if len(parts) > 1:
                    name = parts[3].split('_')[0]  # KEY_NAME
                    if name != previous_name:
                        if name not in count_dict:
                            count_dict[name] = 0 # NAME_Define
                        count_dict[name] += 1  # count+1
                        output_file = f'./fab2/text/{name}_{count_dict[name]:02d}.txt'
                        previous_name = name 
                    is_recording = True
                if not is_recording :
                    if output_file is not None and current_content:
                        with open(output_file, 'a') as out_file:
                            out_file.write('\n'.join(current_content)+'\n')
                    current_content = []  # 현재 내용 초기화 

            #'001'로 시작하지 않는 줄 현재 내용 추가
            if is_recording:
                current_content.append(line)

            #'001'로 시작하지 않는 줄 현재 내용 저장
            if not line.startswith('001') and current_content:
                with open(output_file, 'a') as out_file:
                    out_file.write('\n'.join(current_content)+'\n')
                current_content = []
                previous_name = None

        # 파일 끝내용 저장
        if output_file is not None and current_content:
            with open(output_file, 'a') as out_file:
                out_file.write('\n'.join(current_content)+'\n')

def main(process):
    PRIORITY  = []
    OUTLAYER  = []
    INLAYER   = []
    KEY_TYPE  = []
    BOUNDARY  = []
    TEXT      = []
    LAYER_NO  = []
    RETICLE_ID =[]
    DA_TONE   = []
    SL_TONE   = []
    DICER     = []
    OVERTYPE  = []
    # OVERLAY_BLOCK
    BASEPAD  = []
    DK_LAYER = []
    DK_LAYER_NO = []
    
    if os.path.isfile('./fab2/text/input_overlay.txt'):
        split_file()
    else:
        print("Please check thoe Input excel_overlay_sheet file.")
    OVERLAY_01 = ('./fab2/text/OVERLAY_01.txt')
    if os.path.isfile(OVERLAY_01):
        with open('./fab2/text/OVERLAY_01.txt','r') as f:
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
            elif line.startswith('OVERTYPE'):
                line_st = line.strip()
                line_sp = line_st.split()
                temp1=[]
                temp1.append(line_sp[1])
                OVERTYPE = temp1[0]
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
  
    pad_temp = 'AA,'
    pad_temp1 = pad_temp.strip()
    BASEPAD = pad_temp1.split(',')
    date = datetime.datetime.now().strftime("%y%m%d")

    if 'HC' in process:
    ## HC18_Normal_overlay
        key_name = process+'_PHOTOKEY_'+date
        path = ('./fab2/f2_gdsout/'+key_name)
        if os.path.isdir(path):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name)
        path2 = ('./fab2/f2_gdsout/'+key_name+'/'+key_name+'/')
        if os.path.isdir(path2):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name+'/'+key_name+'/')
        t_out= './fab2/f2_gdsout/'+key_name+'/'+key_name+'/'+key_name+'.txt'

        if (OVERTYPE == '1' or OVERTYPE == '2') and os.path.isfile(OVERLAY_01) == True:
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

                txy = (TEXT.split('_')[0][0])
                if int(txy) == 7:
                    txt_y = 10
                else:
                    txt_y = 12
                pro_now = int(PRIORITY)
                over_y = int(KEY_TYPE.split('_')[9]) + txt_y
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
                if i == 0:
                    pro_bak = pro_now
                    bl_t.add(gdstk.Reference(bl,(float(bar_xy),0)))
                    br_t.add(gdstk.Reference(br,(0,0)))
                    blx_hot = float(bar_xy)+(float(bar_xy)/2)  # External_bl_X_hotspot
                    brx_hot = (float(bar_xy)/2)                # External_br_X_hotspot
                    y_hot = txt_y+float(bar_xy)/2  # External_Y_hotspot
                    x_max = float(bar_xy)*2        # External_X_Max
                    y_max = over_y                 # External_Y_Max
                    if in_typ == "T":
                        if in_lay in DK_LAYER:
                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,0),(float(bar_xy),y_max), layer=int(in_num)))
                            br_t.add(gdstk.rectangle((float(bar_xy),0),((float(bar_xy)+1),y_max), layer=int(in_num)))                     
                    if out_typ == "T":
                        if out_lay in DK_LAYER:
                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,txt_y),(float(bar_xy),y_max), layer=int(out_num)))
                            br_t.add(gdstk.rectangle((float(bar_xy),txt_y),((float(bar_xy)+1),y_max), layer=int(out_num))) 
                    if any(no in DK_LAYER_NO for no in BOUNDARY):   #BOUNDARY의 어떤 요소가 DK_LAYER_NO에 존재하면 -> True
                        for no in BOUNDARY:                         #no는 BOUNDARY의 각 요소 순차 확인
                            if no in DK_LAYER_NO:                   #no가 DK_LAYER_NO 포함여부 확인
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(no)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(no)))
                            else:
                                continue
                    if txy_f == 'N':
                        for no in txy_lay:
                            if no in DK_LAYER_NO:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),(y_max-float(bar_xy))), layer=int(no)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),(y_max-float(bar_xy))), layer=int(no)))
                            else:
                                continue
                    if BASEPAD != "":
                        for i in range(0,len(BASEPAD)):
                            no = BASEPAD[i]
                            if no == in_lay:
                                pass
                            elif no == out_lay:
                                if out_typ == "M":
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,0),((float(bar_xy),txt_y)), layer=int(out_num)))
                                    bl_t.add(gdstk.rectangle((float(bar_xy),0),(((float(bar_xy)*2),txt_y)), layer=int(out_num)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),0),(((float(bar_xy)+1),txt_y)), layer=int(out_num)))
                                    br_t.add(gdstk.rectangle((0,0),((float(bar_xy),(txt_y))), layer=int(out_num)))            
                                else:
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,0),((float(bar_xy),txt_y)), layer=int(out_num)))
                                    bl_t.add(gdstk.rectangle((float(bar_xy),0),(((float(bar_xy)*2),txt_y)), layer=int(out_num)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),0),(((float(bar_xy)+1),txt_y)), layer=int(out_num)))
                                    br_t.add(gdstk.rectangle((0,0),((float(bar_xy),(txt_y))), layer=int(out_num)))
                            else:
                                pass
                else:
                    if pro_bak == pro_now:
                        rect_y = rect_y
                        y_max = y_max
                        if in_typ == "T":
                            if in_lay in DK_LAYER or BASEPAD in DK_LAYER:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(in_num)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(in_num)))
                        if out_typ == "T":
                            if out_lay in DK_LAYER or BASEPAD in DK_LAYER:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,y_max-(float(bar_xy))),(float(bar_xy),y_max), layer=int(out_num)))
                                br_t.add(gdstk.rectangle((float(bar_xy),y_max-(float(bar_xy))),((float(bar_xy)+1),y_max), layer=int(out_num)))
                        if any(no in DK_LAYER_NO for no in BOUNDARY):
                            for no in BOUNDARY:                 
                                if no in DK_LAYER_NO:
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(no)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(no)))
                                else:
                                    continue
                        if txy_f == 'N':
                            for no in txy_lay:
                                if no in DK_LAYER_NO:
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),(y_max-float(bar_xy))), layer=int(no)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),(y_max-float(bar_xy))), layer=int(no)))
                                else:
                                    continue
                        if BASEPAD != "":
                            if any(no in RETICLE_ID for no in BASEPAD):
                                for i in range(0,len(LAYER_NO)):
                                    layer = LAYER_NO[i]
                                    name = RETICLE_ID[i]
                                    for no in BASEPAD:
                                        if no == in_lay:
                                            pass
                                        elif no == out_lay:
                                            if out_typ == "M":
                                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(out_num)))
                                                bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                            else:   
                                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                                bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                        elif no == name:
                                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                            bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(layer)))
                                            br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max-(float(bar_xy))), layer=int(layer)))
                                            br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                        else:
                                            pass                              
                    else:
                        pro_bak = pro_now
                        rect_y = rect_y + over_y
                        y_max = y_max + over_y
                        if in_typ == "T":
                            if in_lay in DK_LAYER or BASEPAD in DK_LAYER:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(in_num)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(in_num)))
                        if out_typ == "T":
                            if out_lay in DK_LAYER or BASEPAD in DK_LAYER:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,y_max-(float(bar_xy))),(float(bar_xy),y_max), layer=int(out_num)))
                                br_t.add(gdstk.rectangle((float(bar_xy),y_max-(float(bar_xy))),((float(bar_xy)+1),y_max), layer=int(out_num)))
                        if any(no in DK_LAYER_NO for no in BOUNDARY):
                            for no in BOUNDARY:
                                if no in DK_LAYER_NO:
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(no)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(no)))
                                else:
                                    continue
                        if txy_f == 'N':
                            for no in txy_lay:
                                if no in DK_LAYER_NO:
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),(y_max-float(bar_xy))), layer=int(no)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),(y_max-float(bar_xy))), layer=int(no)))
                                else:
                                    continue
                        if BASEPAD != "":  # AA LAYER
                            if any(no in RETICLE_ID for no in BASEPAD):
                                for i in range(0,len(LAYER_NO)):
                                    layer = LAYER_NO[i]
                                    name = RETICLE_ID[i]
                                    for no in BASEPAD:
                                        if no == in_lay:
                                            pass
                                        elif no == out_lay:   
                                            if out_typ == "M":
                                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(out_num)))
                                                bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                            else:   
                                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                                bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                        elif no == name:
                                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                            bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(layer)))
                                            br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max-(float(bar_xy))), layer=int(layer)))
                                            br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                        else:
                                            pass
                    bl_t.add(gdstk.Reference(bl,(float(bar_xy),rect_y)))
                    br_t.add(gdstk.Reference(br,(0,rect_y)))
                for i in range(0,len(LAYER_NO)):
                    layer = LAYER_NO[i]
                    if DA_TONE[i] == "DK":
                        bl_t.add(gdstk.rectangle((0,0),(float(bar_xy)-1,y_max), layer=int(layer)))
                        br_t.add(gdstk.rectangle((float(bar_xy)+1,0),((float(bar_xy)*2),y_max), layer=int(layer)))               
            # Add Block_boundary
            bl_t.add(gdstk.rectangle((0,0),(float(bar_xy),y_max), layer=int(63)))
            br_t.add(gdstk.rectangle((float(bar_xy),0),((float(bar_xy)*2),y_max), layer=int(63)))           
            output_name1 = './fab2/f2_gdsout/'+key_name+'/'+bl_top_cell+'.gds'
            output_name2 = './fab2/f2_gdsout/'+key_name+'/'+br_top_cell+'.gds'
            bllib.write_gds(output_name1)
            brlib.write_gds(output_name2)
        ## HC18_Normal_overlay_TEXT
        pro = process.split('_')[0]
        gds_over = glob.glob('./fab2/f2_gdsout/'+key_name+'/'+'*OVERLAY*.gds')
        if gds_over:
            for i in range(0,len(gds_over)) :
                top1 = gds_over[i].split('.gds')[0]
                top = os.path.basename(top1)
                ovlist = top.split('_')
                for i in range(0,len(ovlist)):
                    if "OVERLAY" in ovlist[i]:
                        over = ovlist[i]
                        overty = ovlist[i+1]
                out = './fab2/f2_gdsout/'+key_name+'/'+key_name+'/'+top+"."+over+'_'+overty
                with open (out,"w")as f:
                    f.write("File_Type\t\t\t \"GDS\"\n")
                    f.write("Hotspot_Name\t\t\t \"1\"\n")
                    if overty == 'BL':
                        f.write("Hotspot_X\t\t\t \"%s\"\n" %(blx_hot))
                    elif overty == 'BR':
                        f.write("Hotspot_X\t\t\t \"%s\"\n" %(brx_hot))
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
                        f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top,over+'_'+overty,top,x_max,y_max,blx_hot,y_hot))
                    elif overty == 'BR':
                        f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top,over+'_'+overty,top,x_max,y_max,brx_hot,y_hot))
        else:
            pass

        ## HC18_SPD_overlay [Delete only Blocking form Normal_overlay]
        PRIORITY  = []
        OUTLAYER  = []
        INLAYER   = []
        KEY_TYPE  = []
        BOUNDARY  = []
        TEXT      = []
        OVERLAY_01 = ('./fab2/text/OVERLAY_01.txt')
        if os.path.isfile(OVERLAY_01):
            with open('./fab2/text/OVERLAY_01.txt','r') as f:
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
                elif line.startswith('OVERTYPE'):
                    line_st = line.strip()
                    line_sp = line_st.split()
                    temp1=[]
                    temp1.append(line_sp[1])
                    OVERTYPE = temp1[0]
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
        process_spd = process+"_SPD"
        key_name_spd = process_spd+'_PHOTOKEY_'+date
        path_s1 = ('./fab2/f2_gdsout/'+key_name_spd)
        if os.path.isdir(path_s1):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name_spd)
        path_s2 = ('./fab2/f2_gdsout/'+key_name_spd+'/'+key_name_spd+'/')
        if os.path.isdir(path_s2):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name_spd+'/'+key_name_spd+'/')
        t2_out= './fab2/f2_gdsout/'+key_name_spd+'/'+key_name_spd+'/'+key_name_spd+'.txt'
        
        if process.find('HC18') == 0 and os.path.isfile(OVERLAY_01) == True:
            bllib = gdstk.Library()                    #BL_LIB
            brlib = gdstk.Library()                    #BR_LIB
            bl_top_cell = process_spd + "_OVERLAY_BL_" + str(date)
            br_top_cell = process_spd + "_OVERLAY_BR_" + str(date)
            bl_t = bllib.new_cell(bl_top_cell)         #BL_TOP_CELL
            br_t = brlib.new_cell(br_top_cell)         #BR_TOP_CELL

            data = {'priority':PRIORITY,'outlayer':OUTLAYER,'inlayer':INLAYER, 'key_type':KEY_TYPE,'boundary':BOUNDARY, 'text':TEXT}
            df = pd.DataFrame(data)
            df_sort = df.sort_values('priority')  #sort by priority  

            rect_y = 0
            y_max = 0
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
                txy = (TEXT.split('_')[0][0])
                if int(txy) == 7 :
                    txt_y = 10
                else:
                    txt_y = 12
                pro_now = int(PRIORITY)
                over_y = int(KEY_TYPE.split('_')[9]) + txt_y
                bar_xy=(KEY_TYPE.split('_')[9])
                out_lay = (KEY_TYPE.split('_')[1])
                out_num = OUTLAYER
                out_typ = (KEY_TYPE.split('_')[2])
                in_num = INLAYER
                in_lay = (KEY_TYPE.split('_')[5])
                in_typ = (KEY_TYPE.split('_')[6])
                if i == 0 :  
                    pro_bak = pro_now
                    bl_t.add(gdstk.Reference(bl,(0,0)))
                    br_t.add(gdstk.Reference(br,(0,0)))
                    blx_hot = (float(bar_xy)/2)                
                    brx_hot = (float(bar_xy)/2)   # External_X_hotspot
                    y_hot = txt_y+float(bar_xy)/2 # External_Y_hotspot
                    x_max = float(bar_xy)         # External_X_Max
                    y_max = over_y                # External_Y_Max
                    if BASEPAD != '-':
                        for i in range(0,len(BASEPAD)):
                            no = BASEPAD[i]
                            if no == in_lay:
                                pass
                            elif no == out_lay:
                                if out_typ == "M":
                                    bl_t.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y), layer=int(out_num)))
                                    br_t.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y), layer=int(out_num)))            
                                else:
                                    bl_t.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y), layer=int(out_num)))
                                    br_t.add(gdstk.rectangle((0,0),(float(bar_xy),txt_y), layer=int(out_num)))
                            else:
                                pass
                else:
                    if pro_bak == pro_now:
                        rect_y = rect_y
                        y_max = y_max
                        if BASEPAD != '-':
                            if any(no in RETICLE_ID for no in BASEPAD):
                                for i in range(0,len(LAYER_NO)):
                                    layer = LAYER_NO[i]
                                    name = RETICLE_ID[i]
                                    for no in BASEPAD:
                                        if no == in_lay:
                                            pass
                                        elif no == out_lay:
                                            if out_typ == "M":
                                                bl_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                            else:   
                                                bl_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                        elif no == name:
                                            bl_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                            br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                        else:
                                            pass  
                    else :
                        pro_bak = pro_now
                        rect_y = rect_y + over_y
                        y_max = y_max + over_y
                        if BASEPAD != '-':  # AA LAYER
                            if any(no in RETICLE_ID for no in BASEPAD):
                                for i in range(0,len(LAYER_NO)):
                                    layer = LAYER_NO[i]
                                    name = RETICLE_ID[i]
                                    for no in BASEPAD:
                                        if no == in_lay:
                                            pass
                                        elif no == out_lay:   
                                            if out_typ == "M":
                                                bl_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                            else:   
                                                bl_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                        elif no == name:
                                            bl_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                            br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                        else:
                                            pass
                    bl_t.add(gdstk.Reference(bl,(0,rect_y)))
                    br_t.add(gdstk.Reference(br,(0,rect_y)))
            bl_t.add(gdstk.rectangle((0,0),(float(bar_xy),y_max), layer=int(63)))
            br_t.add(gdstk.rectangle((0,0),(float(bar_xy),y_max), layer=int(63)))                                  
            output_name1_spd = './fab2/f2_gdsout/'+key_name_spd+'/'+bl_top_cell+'.gds'
            output_name2_spd = './fab2/f2_gdsout/'+key_name_spd+'/'+br_top_cell+'.gds'
            bllib.write_gds(output_name1_spd)
            brlib.write_gds(output_name2_spd)
        
        ## HC18_SPD_overlay_TEXT       
        pro = process.split('_')[0]
        gds_over_spd = glob.glob('./fab2/f2_gdsout/'+key_name_spd+'/'+'*OVERLAY*.gds')
        for i in range(0,len(gds_over_spd)) :
            top1_spd = gds_over_spd[i].split('.gds')[0]
            top_spd = os.path.basename(top1_spd)
            ovlist_spd = top1_spd.split('_')
            for i in range(0,len(ovlist_spd)):
                if "OVERLAY" in ovlist_spd[i]:
                    over = ovlist_spd[i]
                    overty = ovlist_spd[i+1]
            out2_spd = './fab2/f2_gdsout/'+key_name_spd+'/'+key_name_spd+'/'+top_spd+"."+over+'_'+overty
            with open (out2_spd,"w")as f:
                f.write("File_Type\t\t\t \"GDS\"\n")
                f.write("Hotspot_Name\t\t\t \"1\"\n")
                if overty == 'BL':
                    f.write("Hotspot_X\t\t\t \"%s\"\n" %(blx_hot))
                elif overty == 'BR':
                    f.write("Hotspot_X\t\t\t \"%s\"\n" %(brx_hot))
                f.write("Hotspot_End\n")
                f.write("Version\t\t\t\t 9\n")
                f.write("File\t\t\t\t \"$STD_KEY/%s/%s/%s.gds\"\n" %(pro,key_name_spd,top_spd))
                f.write("Topstr\t\t\t\t \"%s\"\n" %(top_spd))
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
            with open (t2_out,"a")as f:
                if overty == 'BL':
                    f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top_spd,over+'_'+overty,top_spd,x_max,y_max,blx_hot,y_hot))
                elif overty == 'BR':
                    f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top_spd,over+'_'+overty,top_spd,x_max,y_max,brx_hot,y_hot))

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
                    elif line.startswith('OVERTYPE'):
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
        pro = process.split('_')[0]
        # Layers_file
        if os.path.isfile('./fab2/text/dicer.txt'):  
            out = './fab2/f2_gdsout/'+key_name+'/'+key_name+'/'+key_name+".layers"
            out2 = './fab2/f2_gdsout/'+key_name_spd+'/'+key_name_spd+'/'+key_name_spd+".layers"
            with open (out,"w")as f1, open (out2,"w")as f2 :    
                pre_layer = []
                f1.write("Version\t\t\t\t\t 6\n")
                f2.write("Version\t\t\t\t\t 6\n")
                for i in range(0,len(LAYER_NO)):
                    layer = LAYER_NO[i]
                    name = RETICLE_ID[i]
                    if layer in pre_layer:
                        continue
                    else:                     
                        if DA_TONE[i] == "DK":
                            filed_tone = "Clear"
                        elif DA_TONE[i] == "CL":
                            filed_tone = "Dark"
                        if SL_TONE[i] == "DK":
                            sl_tone = "Dark"
                        elif SL_TONE[i] == "CL":
                            sl_tone = "Clear"   
                        pre_layer.append(layer)                         
                        f1.write("Layer\t\t\t\t\t %s\n"%(layer))
                        f1.write("Layer_Datatype\t\t\t\t 0\n")
                        f1.write("Field_Polarity\t\t\t\t \"%s\"\n" %(filed_tone))
                        f1.write("Scribe_Polarity\t\t\t\t \"%s\"\n" %(sl_tone)) 
                        f1.write("Drop\t\t\t\t\t \"\"\n")
                        f1.write("Comment\t\t\t\t\t \"%s\"\n" %(name)) 
                        f1.write("Groups\t\t\t\t\t \"\"\n")
                        f1.write("\n")
                        f2.write("Layer\t\t\t\t\t %s\n"%(layer))
                        f2.write("Layer_Datatype\t\t\t\t 0\n")
                        f2.write("Field_Polarity\t\t\t\t \"%s\"\n" %(filed_tone))
                        f2.write("Scribe_Polarity\t\t\t\t \"%s\"\n" %(sl_tone)) 
                        f2.write("Drop\t\t\t\t\t \"\"\n")
                        f2.write("Comment\t\t\t\t\t \"%s\"\n" %(name)) 
                        f2.write("Groups\t\t\t\t\t \"\"\n")
                        f2.write("\n")
                if process.find("HC18") == 0:
                    f1.write("Layer\t\t\t\t\t 98\n")
                    f1.write("Layer_Datatype\t\t\t\t 0\n")
                    f1.write("Field_Polarity\t\t\t\t \"Dark\"\n")
                    f1.write("Scribe_Polarity\t\t\t\t \"Dark\"\n") 
                    f1.write("Drop\t\t\t\t\t \"\"\n")
                    f1.write("Comment\t\t\t\t\t \"PSM\"\n") 
                    f1.write("Groups\t\t\t\t\t \"\"\n")
                    f1.write("\n")
                    f1.write("Layer\t\t\t\t\t 100\n")
                    f1.write("Layer_Datatype\t\t\t\t 0\n")
                    f1.write("Field_Polarity\t\t\t\t \"Dark\"\n")
                    f1.write("Scribe_Polarity\t\t\t\t \"Dark\"\n") 
                    f1.write("Drop\t\t\t\t\t \"\"\n")
                    f1.write("Comment\t\t\t\t\t \"FR_BOUNDARY\"\n") 
                    f1.write("Groups\t\t\t\t\t \"\"\n")
                    f1.write("\n")
                    f1.write("End_of_Layers\n")
                    f1.write("\n")
                    f1.write("Layer\t\t\t\t\t 98\n")
                    f1.write("Layer_Datatype\t\t\t\t 0\n")
                    f1.write("Comment\t\t\t\t\t \"PSM\"\n") 
                    f1.write("Field_Polarity\t\t\t\t \"Dark\"\n")
                    f1.write("Scribe_Polarity\t\t\t\t \"Dark\"\n") 
                    f1.write("Inv\t\t\t\t\t 0\n")
                    f1.write("Item\t\t\t\t\t \"CHIP,CDBAR,TP,OPCTP\"\n") 
                    f1.write("Any\t\t\t\t\t 0\n")
                    f1.write("Restrict\t\t\t\t \"DevType\"\n") 
                    f1.write("What\t\t\t\t\t \"Shape\"\n") 
                    f1.write("Operation\t\t\t\t \"GENSHAPE\"\n") 
                    f1.write("Version_Num\t\t\t\t 8\n")
                    f1.write("Gen_Region\t\t\t\t 0\n")
                    f1.write("Do_Regular_Regions\t\t\t 0\n")
                    f1.write("Do_Computed_Regions\t\t\t 0\n")
                    f1.write("Is_Ring\t\t\t\t\t 0\n")
                    f1.write("External\t\t\t\t 0\n")
                    f1.write("Size_LEFT\t\t\t\t \"\"\n")
                    f1.write("Size_RIGHT\t\t\t\t \"\"\n")
                    f1.write("Size_BOTTOM\t\t\t\t \"\"\n")
                    f1.write("Size_TOP\t\t\t\t \"\"\n")
                    f1.write("ResHole\t\t\t\t\t 0\n")
                    f1.write("Trim_To_Field\t\t\t\t 0\n")
                    f1.write("Drop\t\t\t\t\t \"\"\n")
                    f1.write("Comments\t\t\t\t 0\n")
                    f1.write("\n")
                    f1.write("Layer\t\t\t\t\t 100\n")
                    f1.write("Layer_Datatype\t\t\t\t 0\n")
                    f1.write("Comment\t\t\t\t\t \"FR_BOUNDARY\"\n") 
                    f1.write("Field_Polarity\t\t\t\t \"Dark\"\n")
                    f1.write("Scribe_Polarity\t\t\t\t \"Dark\"\n") 
                    f1.write("Inv\t\t\t\t\t 0\n")
                    f1.write("Item\t\t\t\t\t \"FRAME\"\n") 
                    f1.write("Any\t\t\t\t\t 0\n")
                    f1.write("Restrict\t\t\t\t \"OldStlyle\"\n") 
                    f1.write("What\t\t\t\t\t \"Outline\"\n") 
                    f1.write("Operation\t\t\t\t \"GENSHAPE\"\n") 
                    f1.write("Version_Num\t\t\t\t 8\n")
                    f1.write("Gen_Region\t\t\t\t 0\n")
                    f1.write("Do_Regular_Regions\t\t\t 0\n")
                    f1.write("Do_Computed_Regions\t\t\t 0\n")
                    f1.write("Is_Ring\t\t\t\t\t 0\n")
                    f1.write("External\t\t\t\t 0\n")
                    f1.write("Size_LEFT\t\t\t\t \"\"\n")
                    f1.write("Size_RIGHT\t\t\t\t \"\"\n")
                    f1.write("Size_BOTTOM\t\t\t\t \"\"\n")
                    f1.write("Size_TOP\t\t\t\t \"\"\n")
                    f1.write("ResHole\t\t\t\t\t 0\n")
                    f1.write("Trim_To_Field\t\t\t\t 0\n")
                    f1.write("Drop\t\t\t\t\t \"\"\n")
                    f1.write("Comments\t\t\t\t 0\n")
                    f1.write("\n")
                    f1.write("End_of_Operations\n")
                    f1.close()
                if process.find("HC18") == 0:
                    f2.write("Layer\t\t\t\t\t 98\n")
                    f2.write("Layer_Datatype\t\t\t\t 0\n")
                    f2.write("Field_Polarity\t\t\t\t \"Dark\"\n")
                    f2.write("Scribe_Polarity\t\t\t\t \"Dark\"\n") 
                    f2.write("Drop\t\t\t\t\t \"\"\n")
                    f2.write("Comment\t\t\t\t\t \"PSM\"\n") 
                    f2.write("Groups\t\t\t\t\t \"\"\n")
                    f2.write("\n")
                    f2.write("Layer\t\t\t\t\t 100\n")
                    f2.write("Layer_Datatype\t\t\t\t 0\n")
                    f2.write("Field_Polarity\t\t\t\t \"Dark\"\n")
                    f2.write("Scribe_Polarity\t\t\t\t \"Dark\"\n") 
                    f2.write("Drop\t\t\t\t\t \"\"\n")
                    f2.write("Comment\t\t\t\t\t \"FR_BOUNDARY\"\n") 
                    f2.write("Groups\t\t\t\t\t \"\"\n")
                    f2.write("\n")
                    f2.write("End_of_Layers\n")
                    f2.write("\n")
                    f2.write("Layer\t\t\t\t\t 98\n")
                    f2.write("Layer_Datatype\t\t\t\t 0\n")
                    f2.write("Comment\t\t\t\t\t \"PSM\"\n") 
                    f2.write("Field_Polarity\t\t\t\t \"Dark\"\n")
                    f2.write("Scribe_Polarity\t\t\t\t \"Dark\"\n") 
                    f2.write("Inv\t\t\t\t\t 0\n")
                    f2.write("Item\t\t\t\t\t \"CHIP,CDBAR,TP,OPCTP\"\n") 
                    f2.write("Any\t\t\t\t\t 0\n")
                    f2.write("Restrict\t\t\t\t \"DevType\"\n") 
                    f2.write("What\t\t\t\t\t \"Shape\"\n") 
                    f2.write("Operation\t\t\t\t \"GENSHAPE\"\n") 
                    f2.write("Version_Num\t\t\t\t 8\n")
                    f2.write("Gen_Region\t\t\t\t 0\n")
                    f2.write("Do_Regular_Regions\t\t\t 0\n")
                    f2.write("Do_Computed_Regions\t\t\t 0\n")
                    f2.write("Is_Ring\t\t\t\t\t 0\n")
                    f2.write("External\t\t\t\t 0\n")
                    f2.write("Size_LEFT\t\t\t\t \"\"\n")
                    f2.write("Size_RIGHT\t\t\t\t \"\"\n")
                    f2.write("Size_BOTTOM\t\t\t\t \"\"\n")
                    f2.write("Size_TOP\t\t\t\t \"\"\n")
                    f2.write("ResHole\t\t\t\t\t 0\n")
                    f2.write("Trim_To_Field\t\t\t\t 0\n")
                    f2.write("Drop\t\t\t\t\t \"\"\n")
                    f2.write("Comments\t\t\t\t 0\n")
                    f2.write("\n")
                    f2.write("Layer\t\t\t\t\t 100\n")
                    f2.write("Layer_Datatype\t\t\t\t 0\n")
                    f2.write("Comment\t\t\t\t\t \"FR_BOUNDARY\"\n") 
                    f2.write("Field_Polarity\t\t\t\t \"Dark\"\n")
                    f2.write("Scribe_Polarity\t\t\t\t \"Dark\"\n") 
                    f2.write("Inv\t\t\t\t\t 0\n")
                    f2.write("Item\t\t\t\t\t \"FRAME\"\n") 
                    f2.write("Any\t\t\t\t\t 0\n")
                    f2.write("Restrict\t\t\t\t \"OldStlyle\"\n") 
                    f2.write("What\t\t\t\t\t \"Outline\"\n") 
                    f2.write("Operation\t\t\t\t \"GENSHAPE\"\n") 
                    f2.write("Version_Num\t\t\t\t 8\n")
                    f2.write("Gen_Region\t\t\t\t 0\n")
                    f2.write("Do_Regular_Regions\t\t\t 0\n")
                    f2.write("Do_Computed_Regions\t\t\t 0\n")
                    f2.write("Is_Ring\t\t\t\t\t 0\n")
                    f2.write("External\t\t\t\t 0\n")
                    f2.write("Size_LEFT\t\t\t\t \"\"\n")
                    f2.write("Size_RIGHT\t\t\t\t \"\"\n")
                    f2.write("Size_BOTTOM\t\t\t\t \"\"\n")
                    f2.write("Size_TOP\t\t\t\t \"\"\n")
                    f2.write("ResHole\t\t\t\t\t 0\n")
                    f2.write("Trim_To_Field\t\t\t\t 0\n")
                    f2.write("Drop\t\t\t\t\t \"\"\n")
                    f2.write("Comments\t\t\t\t 0\n")
                    f2.write("\n")
                    f2.write("End_of_Operations\n")
                    f2.close()
            #DICER
            process_spd = process+"_SPD"
            lib = gdstk.Library() # lib 생성
            cell_name = process +"_DICER_"+ date
            cell = lib.new_cell(cell_name) # cell 생성
            lib_spd = gdstk.Library() # lib 생성
            cell_name_spd = process_spd+"_DICER_"+ date
            cell_spd = lib_spd.new_cell(cell_name_spd) # cell 생성
            error = []
            for i in range(0,len(LAYER_NO)) :
                layer_no = LAYER_NO[i]
                #print(layer_no)
                if DICER[i] == "1" :
                    type1_0 = gdstk.rectangle((0,20),(25,25))
                    type1_1 = gdstk.rectangle((20,0),(25,25))
                    type1 = gdstk.boolean(type1_0,type1_1,"or",layer=int(layer_no))
                    cell.add(*type1)
                    cell_spd.add(*type1)
                    bound = gdstk.rectangle((0,0),(25,25), layer=int(63))
                    cell.add(bound)
                    cell_spd.add(bound)
                    x_max = 25
                    y_max = 25
                elif DICER[i] == "11" :
                    type11_0 = gdstk.rectangle((0,20),(25,25))
                    type11_1 = gdstk.rectangle((20,0),(25,25))
                    type11_2 =  gdstk.rectangle((0,0),(25,25))
                    type11_3 = gdstk.boolean(type11_0,type11_1,"or")
                    type11 = gdstk.boolean(type11_2,type11_3,"not",layer=int(layer_no))                                   
                    cell.add(*type11)
                    cell_spd.add(*type11)
                    bound = gdstk.rectangle((0,0),(25,25), layer=int(63))
                    cell.add(bound)
                    cell_spd.add(bound)
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
                            cell_spd.add(type2_0)
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
                            cell_spd.add(type2_1)
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
                    cell_spd.add(bound)
                    x_max = 19.5
                    y_max = 19.5
                elif DICER[i] == "33" :
                    type33_0 = gdstk.rectangle((0,15.5),(19.5,19.5))
                    type33_1 = gdstk.rectangle((15.5,0),(19.5,19.5))
                    type33_2 = gdstk.boolean(type33_0,type33_1,"or")
                    type33_3 = gdstk.rectangle((0,0),(19.5,19.5))
                    type33 = gdstk.boolean(type33_2,type33_3,"not",layer=int(layer_no))
                    cell.add(*type33)
                    cell_spd.add(*type33)
                    bound = gdstk.rectangle((0,0),(19.5,19.5), layer=int(63))
                    cell.add(bound)
                    cell_spd.add(bound)
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
                            cell_spd.add(type4_0)
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
                            cell_spd.add(type4_1)
                            y2 += 1
                        else:
                            pass
                elif DICER[i] == "5" :
                    type5_0 = gdstk.rectangle((0,25),(30,30))
                    type5_1 = gdstk.rectangle((25,0),(30,30))
                    type5 = gdstk.boolean(type5_0,type5_1,"or",layer=int(layer_no))
                    cell.add(*type5)
                    cell_spd.add(*type5)
                    bound = gdstk.rectangle((0,0),(30,30), layer=int(63))
                    cell.add(bound)
                    cell_spd.add(bound)
                    x_max = 30
                    y_max = 30
                elif DICER[i] == "55" :
                    type55_0 = gdstk.rectangle((0,25),(30,30))
                    type55_1 = gdstk.rectangle((25,0),(30,30))
                    type55_2 = gdstk.rectangle((0,0),(30,30))
                    type55_3 = gdstk.boolean(type55_0,type55_1,"or")
                    type55 = gdstk.boolean(type55_2,type55_3,"not",layer=int(layer_no))
                    cell.add(*type55)
                    cell_spd.add(*type55)
                    bound = gdstk.rectangle((0,0),(30,30), layer=int(63))
                    cell.add(bound)
                    cell_spd.add(bound)
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
                            cell_spd.add(type6_0)
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
                            cell_spd.add(type6_1)
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
                
            output_name ='./fab2/f2_gdsout/'+key_name+'/'+cell_name+".gds"
            output_name_spd ='./fab2/f2_gdsout/'+key_name_spd+'/'+cell_name_spd+".gds"
            lib.write_gds(output_name)
            lib_spd.write_gds(output_name_spd)

            gds_dicer = glob.glob('./fab2/f2_gdsout/'+key_name+'/'+'*DICER*.gds')
            for i in range(0,len(gds_dicer)) :
                top1 = gds_dicer[i].split('.gds')[0]
                top = os.path.basename(top1)
                out = './fab2/f2_gdsout/'+key_name+'/'+key_name+'/'+cell_name+".DICER"
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

            gds_dicer_spd = glob.glob('./fab2/f2_gdsout/'+key_name_spd+'/'+'*DICER*.gds')
            for i in range(0,len(gds_dicer_spd)) :
                top1_spd = gds_dicer_spd[i].split('.gds')[0]
                top_spd = os.path.basename(top1_spd)
                out2 = './fab2/f2_gdsout/'+key_name_spd+'/'+key_name_spd+'/'+cell_name_spd+".DICER"
                with open (out2,"w")as f:
                    f.write("File_Type\t\t\t \"GDS\"\n")
                    f.write("Hotspot_Name\t\t\t \"1\"\n")
                    f.write("Hotspot_X\t\t\t \"0\"\n")
                    f.write("Hotspot_Y\t\t\t \"0\"\n") 
                    f.write("Hotspot_End\n")
                    f.write("Version\t\t\t\t 9\n")
                    f.write("File\t\t\t\t \"$STD_KEY/%s/%s/%s.gds\"\n" %(pro,key_name_spd,top_spd))
                    f.write("Topstr\t\t\t\t \"%s\"\n" %(top_spd))
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
                with open (t2_out,"a")as f:
                    f.write("%s.gds\t\tDICER\t%s\t0\t0\t%s\t%s\t0\t0\n" %(top_spd,top_spd,x_max,y_max))
        else:
            pass

        # Normal_1ST_OVERLAY
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
                    txy = int(key_type.split('_')[-1])
                    if txy != 7:
                        txt_y = 12
                    else:
                        txt_y = 10
                    x_max = int(overlay_1st.split('_')[9])
                    yy_max = int(overlay_1st.split('_')[9])+txt_y
                    if i == 0 :
                        in_top.add(gdstk.Reference(in_1st,(0,0)))
                        out_top.add(gdstk.Reference(out_1st,(0,0)))
                    else:
                        in_top.add(gdstk.Reference(in_1st,(0,0)))
                        out_top.add(gdstk.Reference(out_1st,(0,0)))
                else:
                    pass
            output1 = './fab2/f2_gdsout/'+key_name+'/'+in_top_cell+".gds"
            output2 = './fab2/f2_gdsout/'+key_name+'/'+out_top_cell+".gds"
            inlib.write_gds(output1)
            outlib.write_gds(output2)
        else:
            pass
        gds_tar = glob.glob('./fab2/f2_gdsout/'+key_name+'/'+"*1ST*.gds")
        for i in range(0,len(gds_tar)) :
            top1 = gds_tar[i].split('.gds')[0]
            top = os.path.basename(top1)
            frist_list = top.split('_')
            for i in range(0,len(frist_list)):
                if "1ST" in frist_list[i]:
                    frsty = frist_list[i+1]
            out = './fab2/f2_gdsout/'+key_name+'/'+key_name+'/'+top+".1ST_"+frsty
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
                f.write("Y_Max\t\t\t\t \"%s\"\n" %(yy_max))
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
                f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t0\t0\n" %(top,'1ST_'+frsty,top,x_max,yy_max))
    ## HC180S_SPD(In_Chip) -> No need for 1ST_OVERLAY.   

    if 'BD13' in process:
        ## BD13_Normal_overlay
        key_name = process+'_PHOTOKEY_'+date
        path = ('./fab2/f2_gdsout/'+key_name)
        if os.path.isdir(path):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name)
        path2 = ('./fab2/f2_gdsout/'+key_name+'/'+key_name+'/')
        if os.path.isdir(path2):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name+'/'+key_name+'/')
        t_out= './fab2/f2_gdsout/'+key_name+'/'+key_name+'/'+key_name+'.txt'
        
        if (OVERTYPE == '1' or OVERTYPE == '2') and os.path.isfile(OVERLAY_01) == True:
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

                txy = (TEXT.split('_')[0][0])
                if int(txy) == 7:
                    txt_y = 10
                else:
                    txt_y = 12
                pro_now = int(PRIORITY)
                over_y = int(KEY_TYPE.split('_')[9]) + txt_y
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
                if i == 0:
                    pro_bak = pro_now
                    bl_t.add(gdstk.Reference(bl,(float(bar_xy),0)))
                    br_t.add(gdstk.Reference(br,(0,0)))
                    blx_hot = float(bar_xy)+(float(bar_xy)/2)  # External_bl_X_hotspot
                    brx_hot = (float(bar_xy)/2)                # External_br_X_hotspot
                    y_hot = txt_y+float(bar_xy)/2  # External_Y_hotspot
                    x_max = float(bar_xy)*2        # External_X_Max
                    y_max = over_y                 # External_Y_Max
                    if in_typ == "T":
                        if in_lay in DK_LAYER:
                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,0),(float(bar_xy),y_max), layer=int(in_num)))
                            br_t.add(gdstk.rectangle((float(bar_xy),0),((float(bar_xy)+1),y_max), layer=int(in_num)))                     
                    if out_typ == "T":
                        if out_lay in DK_LAYER:
                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,txt_y),(float(bar_xy),y_max), layer=int(out_num)))
                            br_t.add(gdstk.rectangle((float(bar_xy),txt_y),((float(bar_xy)+1),y_max), layer=int(out_num))) 
                    if any(no in DK_LAYER_NO for no in BOUNDARY):   #BOUNDARY의 어떤 요소가 DK_LAYER_NO에 존재하면 -> True
                        for no in BOUNDARY:                         #no는 BOUNDARY의 각 요소 순차 확인
                            if no in DK_LAYER_NO:                   #no가 DK_LAYER_NO 포함여부 확인
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(no)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(no)))
                            else:
                                continue
                    if txy_f == 'N' or 'GN' in process:
                        for no in txy_lay:
                            if no in DK_LAYER_NO:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),(y_max-float(bar_xy))), layer=int(no)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),(y_max-float(bar_xy))), layer=int(no)))
                            else:
                                continue
                    if BASEPAD != "":
                        for i in range(0,len(BASEPAD)):
                            no = BASEPAD[i]
                            if no == in_lay:
                                pass
                            elif no == out_lay:
                                if out_typ == "M":
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,0),((float(bar_xy),txt_y)), layer=int(out_num)))
                                    bl_t.add(gdstk.rectangle((float(bar_xy),0),(((float(bar_xy)*2),txt_y)), layer=int(out_num)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),0),(((float(bar_xy)+1),txt_y)), layer=int(out_num)))
                                    br_t.add(gdstk.rectangle((0,0),((float(bar_xy),(txt_y))), layer=int(out_num)))            
                                else:
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,0),((float(bar_xy),txt_y)), layer=int(out_num)))
                                    bl_t.add(gdstk.rectangle((float(bar_xy),0),(((float(bar_xy)*2),txt_y)), layer=int(out_num)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),0),(((float(bar_xy)+1),txt_y)), layer=int(out_num)))
                                    br_t.add(gdstk.rectangle((0,0),((float(bar_xy),(txt_y))), layer=int(out_num)))
                            else:
                                pass
                else:
                    if pro_bak == pro_now:
                        rect_y = rect_y
                        y_max = y_max
                        if in_typ == "T":
                            if in_lay in DK_LAYER or BASEPAD in DK_LAYER:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(in_num)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(in_num)))
                        if out_typ == "T":
                            if out_lay in DK_LAYER or BASEPAD in DK_LAYER:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,y_max-(float(bar_xy))),(float(bar_xy),y_max), layer=int(out_num)))
                                br_t.add(gdstk.rectangle((float(bar_xy),y_max-(float(bar_xy))),((float(bar_xy)+1),y_max), layer=int(out_num)))
                        if any(no in DK_LAYER_NO for no in BOUNDARY):
                            for no in BOUNDARY:                 
                                if no in DK_LAYER_NO:
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(no)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(no)))
                                else:
                                    continue
                        if txy_f == 'N' or 'GN' in process:
                            for no in txy_lay:
                                if no in DK_LAYER_NO:
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),(y_max-float(bar_xy))), layer=int(no)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),(y_max-float(bar_xy))), layer=int(no)))
                                else:
                                    continue
                        if BASEPAD != "":
                            if any(no in RETICLE_ID for no in BASEPAD):
                                for i in range(0,len(LAYER_NO)):
                                    layer = LAYER_NO[i]
                                    name = RETICLE_ID[i]
                                    for no in BASEPAD:
                                        if no == in_lay:
                                            pass
                                        elif no == out_lay:
                                            if out_typ == "M":
                                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(out_num)))
                                                bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                            else:   
                                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                                bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                        elif no == name:
                                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                            bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(layer)))
                                            br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max-(float(bar_xy))), layer=int(layer)))
                                            br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                        else:
                                            pass                                
                    else:
                        pro_bak = pro_now
                        rect_y = rect_y + over_y
                        y_max = y_max + over_y
                        if in_typ == "T":
                            if in_lay in DK_LAYER or BASEPAD in DK_LAYER:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(in_num)))
                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(in_num)))
                        if out_typ == "T":
                            if out_lay in DK_LAYER or BASEPAD in DK_LAYER:
                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,y_max-(float(bar_xy))),(float(bar_xy),y_max), layer=int(out_num)))
                                br_t.add(gdstk.rectangle((float(bar_xy),y_max-(float(bar_xy))),((float(bar_xy)+1),y_max), layer=int(out_num)))
                        if any(no in DK_LAYER_NO for no in BOUNDARY):
                            for no in BOUNDARY:
                                if no in DK_LAYER_NO:
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(no)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),y_max), layer=int(no)))
                                else:
                                    continue
                        if txy_f == 'N' or 'GN' in process:
                            for no in txy_lay:
                                if no in DK_LAYER_NO:
                                    bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),(y_max-float(bar_xy))), layer=int(no)))
                                    br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),((float(bar_xy)+1),(y_max-float(bar_xy))), layer=int(no)))
                                else:
                                    continue
                        if BASEPAD != "":  # AA LAYER
                            if any(no in RETICLE_ID for no in BASEPAD):
                                for i in range(0,len(LAYER_NO)):
                                    layer = LAYER_NO[i]
                                    name = RETICLE_ID[i]
                                    for no in BASEPAD:
                                        if no == in_lay:
                                            pass
                                        elif no == out_lay:   
                                            if out_typ == "M":
                                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max), layer=int(out_num)))
                                                bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                            else:   
                                                bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                                bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max-(float(bar_xy))), layer=int(out_num)))
                                                br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(out_num)))
                                        elif no == name:
                                            bl_t.add(gdstk.rectangle((float(bar_xy)-1,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                            bl_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)*2,y_max-(float(bar_xy))), layer=int(layer)))
                                            br_t.add(gdstk.rectangle((float(bar_xy),(y_max-over_y)),(float(bar_xy)+1,y_max-(float(bar_xy))), layer=int(layer)))
                                            br_t.add(gdstk.rectangle((0,(y_max-over_y)),(float(bar_xy),y_max-(float(bar_xy))), layer=int(layer)))
                                        else:
                                            pass
                    bl_t.add(gdstk.Reference(bl,(float(bar_xy),rect_y)))
                    br_t.add(gdstk.Reference(br,(0,rect_y)))
                for i in range(0,len(LAYER_NO)):
                    layer = LAYER_NO[i]
                    if DA_TONE[i] == "DK":
                        bl_t.add(gdstk.rectangle((0,0),(float(bar_xy)-1,y_max), layer=int(layer)))
                        br_t.add(gdstk.rectangle((float(bar_xy)+1,0),((float(bar_xy)*2),y_max), layer=int(layer)))
            # Add Block_boundary
            bl_t.add(gdstk.rectangle((0,0),(float(bar_xy),y_max), layer=int(63)))
            br_t.add(gdstk.rectangle((float(bar_xy),0),((float(bar_xy)*2),y_max), layer=int(63)))           
            output_name1 = './fab2/f2_gdsout/'+key_name+'/'+bl_top_cell+'.gds'
            output_name2 = './fab2/f2_gdsout/'+key_name+'/'+br_top_cell+'.gds'
            bllib.write_gds(output_name1)
            brlib.write_gds(output_name2)       
        elif (OVERTYPE == '3' or OVERTYPE == '4') and os.path.isfile(OVERLAY_01) == True:
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

            for i in range(0,len(df_sort)):
                PRIORITY = df_sort.iloc[i,0]
                OUTLAYER = df_sort.iloc[i,1]
                INLAYER  = df_sort.iloc[i,2]
                KEY_TYPE = df_sort.iloc[i,3]
                BOUNDARY = df_sort.iloc[i,4]
                TEXT     = df_sort.iloc[i,5]
                ll, lr, ul, ur = F2_OVERLAY_SPD_LL_LR_UL_UR_LETTER.start(int(PRIORITY),int(OUTLAYER),int(INLAYER),KEY_TYPE,BOUNDARY,TEXT,lllib,lrlib,ullib,urlib)  
                ## 9,10번 overlay special work
                if int(PRIORITY) == 9 or int(PRIORITY) == 10 :
                    # flattern_layers
                    def flat_all(cell,level):
                            flat_lay = cell
                            for _ in range(level):
                                flat_lay = flat_lay.flatten()
                            return flat_lay
                    # flattern_layers추출
                    flat = flat_all(ll,level=1)
                    p_lay03 = [p for p in flat.polygons if p.layer == 3]
                    p_lay06 = [p for p in flat.polygons if p.layer == 6]
                    p_lay10 = [p for p in flat.polygons if p.layer == 10]
                    p_lay12 = [p for p in flat.polygons if p.layer == 12]
                    p_lay14 = [p for p in flat.polygons if p.layer == 14]
                    p_lay48 = [p for p in flat.polygons if p.layer == 48]
                    p_lay73 = [p for p in flat.polygons if p.layer == 73]
                    p_lay74 = [p for p in flat.polygons if p.layer == 74]
                    p_lay81 = [p for p in flat.polygons if p.layer == 81]
                    p_lay89 = [p for p in flat.polygons if p.layer == 89]
                    p_lay63 = [p for p in flat.polygons if p.layer == 63]
                    # flattern_layers_merge
                    def union_polygons(polygons):
                        if not polygons:
                            return []
                        result = polygons[0]
                        for p in polygons[1:]:
                            result = gdstk.boolean(result, p, "or", precision=1e-9)
                        if isinstance(result, gdstk.Polygon):
                            return [result]
                        return result
                    # flattern_layers_merge수행
                    union_lay03 = union_polygons(p_lay03)
                    union_lay06 = union_polygons(p_lay06)
                    union_lay74 = union_polygons(p_lay74)
                    # polygons_boundary_define
                    def boundary_box(polygons):
                        if not polygons:
                            return None
                        xmin = ymin = float('inf')
                        xmax = ymax = float('-inf')
                        for p in polygons:
                            box = p.bounding_box()
                            xmin = min(xmin, box[0][0])
                            ymin = min(ymin, box[0][1])
                            xmax = max(xmax, box[1][0])
                            ymax = max(ymax, box[1][1])
                        return [(xmin, ymin), (xmax, ymax)]
                    # boundary define 후 offset 진행
                    def offset_box(polygons, distance, layer):
                        bbox = boundary_box(polygons)
                        if bbox is None:
                            return []
                        rect = gdstk.rectangle(bbox[0], bbox[1], layer=layer)
                        offset_polys = gdstk.offset(rect, distance, layer=layer)
                        return offset_polys
                    # flattern 후 offset 진행
                    def offset_union(polygons, distance, layer):
                        offset_polys = []
                        for p in polygons:
                            offset_polys.extend(gdstk.offset(p, distance, layer=layer))
                        return union_polygons(offset_polys)
                    # layer별 offset 적용/ offset이 필요없는 layer는 이후 그대로 output
                    p1_lay03 = offset_box(union_lay03, -0.1, 3)
                    p1_lay06 = offset_union(union_lay06, -0.05, 6)
                    p1_lay74 = offset_union(union_lay74, -0.05, 74)

                    # Delete cell name
                    PRI = PRIORITY.lstrip('0')
                    old_name_ll = PRI+"_"+KEY_TYPE+"_"+OUTLAYER+"_"+INLAYER+"_LL"
                    old_name_lr = PRI+"_"+KEY_TYPE+"_"+OUTLAYER+"_"+INLAYER+"_LR"
                    old_name_ul = PRI+"_"+KEY_TYPE+"_"+OUTLAYER+"_"+INLAYER+"_UL"
                    old_name_ur = PRI+"_"+KEY_TYPE+"_"+OUTLAYER+"_"+INLAYER+"_UR"
                    old_ll = gdstk.Cell(old_name_ll)
                    old_lr = gdstk.Cell(old_name_lr)
                    old_ul = gdstk.Cell(old_name_ul)
                    old_ur = gdstk.Cell(old_name_ur)
                    lllib.add(old_ll)
                    lrlib.add(old_lr)
                    ullib.add(old_ul)
                    urlib.add(old_ur)
                    def remove_cell(lib,cell_name):
                        for i, cell in enumerate(lib.cells):
                            if cell.name == cell_name:
                                cell.polygons.clear()
                                cell.paths.clear()
                                cell.references.clear()
                                del lib.cells[i]
                                #print(f"Deleted cell '{cell_name}' from library.")
                                return True
                        #print(f"Cell '{cell_name}' not found in library.")
                        return False
                    remove_cell(lllib,old_name_ll)
                    remove_cell(lrlib,old_name_lr)
                    remove_cell(ullib,old_name_ul)
                    remove_cell(urlib,old_name_ur)
                    
                    # special 작업 후 newcell  define 및 저장
                    new_name_ll = PRI+"_"+KEY_TYPE+"_"+OUTLAYER+"_"+INLAYER+"_NEW_LL"
                    new_name_lr = PRI+"_"+KEY_TYPE+"_"+OUTLAYER+"_"+INLAYER+"_NEW_LR"
                    new_name_ul = PRI+"_"+KEY_TYPE+"_"+OUTLAYER+"_"+INLAYER+"_NEW_UL"
                    new_name_ur = PRI+"_"+KEY_TYPE+"_"+OUTLAYER+"_"+INLAYER+"_NEW_UR"
                    new_ll = gdstk.Cell(new_name_ll)
                    new_lr = gdstk.Cell(new_name_lr)
                    new_ul = gdstk.Cell(new_name_ul)
                    new_ur = gdstk.Cell(new_name_ur)
                    for p in p1_lay03+p1_lay06+p1_lay74+p_lay10+p_lay12+p_lay14+p_lay48+p_lay73+p_lay81+p_lay89+p_lay63:
                        new_ll.add(p)
                        new_lr.add(p)
                        new_ul.add(p)
                        new_ur.add(p)
                    lllib.add(new_ll)
                    lrlib.add(new_lr)
                    ullib.add(new_ul)
                    urlib.add(new_ur) ### specail work-end.
                else:
                    lllib.add(ll)
                    lrlib.add(lr)
                    ullib.add(ul)
                    urlib.add(ur)

                txy = (TEXT.split('_')[0][0])
                if int(txy) == 7:
                    txt_y = 10
                else:
                    txt_y = 12
                pro_now = int(PRIORITY)
                over_y = int(KEY_TYPE.split('_')[9]) + txt_y
                bar_xy=(KEY_TYPE.split('_')[9])

                if i == 0:  
                    pro_bak = pro_now
                    ll_t.add(gdstk.Reference(ll,(0,0)))
                    lr_t.add(gdstk.Reference(lr,(0,0)))
                    ul_t.add(gdstk.Reference(ul,(0,0)))
                    ur_t.add(gdstk.Reference(ur,(0,0)))
                    x_hot = float(bar_xy)/2       # External_X_hotspot
                    y_hot = txt_y+float(bar_xy)/2 # External_Y_hotspot
                    x_max = float(bar_xy)+txt_y   # External_X_Max
                    y_max = over_y                # External_Y_Max
                else:
                    if pro_bak == pro_now:
                        rect_y = rect_y
                        y_max = y_max
                    else :
                        pro_bak = pro_now
                        rect_y = rect_y + over_y
                        y_max = y_max + over_y
                    # specal cell add
                    if int(PRIORITY) == 9 or int(PRIORITY) == 10:
                        # old cell name define & delete
                        ll_t.add(gdstk.Reference(new_ll,(0,rect_y)))
                        lr_t.add(gdstk.Reference(new_lr,(0,rect_y)))
                        ul_t.add(gdstk.Reference(new_ul,(0,rect_y)))
                        ur_t.add(gdstk.Reference(new_ur,(0,rect_y)))
                    ll_t.add(gdstk.Reference(ll,(0,rect_y)))
                    lr_t.add(gdstk.Reference(lr,(0,rect_y)))
                    ul_t.add(gdstk.Reference(ul,(0,rect_y)))
                    ur_t.add(gdstk.Reference(ur,(0,rect_y)))
            output_name1 = './fab2/f2_gdsout/'+key_name+'/'+ll_top_cell+'.gds'
            output_name2 = './fab2/f2_gdsout/'+key_name+'/'+lr_top_cell+'.gds'
            output_name3 = './fab2/f2_gdsout/'+key_name+'/'+ul_top_cell+'.gds'
            output_name4 = './fab2/f2_gdsout/'+key_name+'/'+ur_top_cell+'.gds'
            lllib.write_gds(output_name1)
            lrlib.write_gds(output_name2)
            ullib.write_gds(output_name3)
            urlib.write_gds(output_name4)
            
        # OVERLAY_NORMAL/SPD_external_file
        pro = process.split('_')[0]
        gds_over = glob.glob('./fab2/f2_gdsout/'+key_name+'/'+'*OVERLAY*.gds')
        for i in range(0,len(gds_over)) :
            top1 = gds_over[i].split('.gds')[0]
            top = os.path.basename(top1)
            ovlist = top.split('_')

            for i in range(0,len(ovlist)):
                if "OVERLAY" in ovlist[i]:
                    over = ovlist[i]
                    overty=ovlist[i+1]
            out = './fab2/f2_gdsout/'+key_name+'/'+key_name+'/'+top+"."+over+'_'+overty
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
                    f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top,over+'_'+overty,top,x_max,y_max,blx_hot,y_hot))
                elif overty == 'BR':
                    f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top,over+'_'+overty,top,x_max,y_max,brx_hot,y_hot))
                else:
                    f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top,over+'_'+overty,top,x_max,y_max,x_hot,y_hot))
    
        ## BD13_ETC_KEY
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
        S8000    = []

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
                    elif line.startswith('OVERTYPE'):
                        continue          
                    else:
                        line_st=line.strip()
                        line_sp=line_st.split()
                        LAYER_NO.append(line_sp[0])
                        RETICLE_ID.append(line_sp[1])         
                        DA_TONE.append(line_sp[2])
                        SL_TONE.append(line_sp[3])
                        DICER.append(line_sp[4])
                        S8000.append(line_sp[5])
                f.close()
        else:
            pass    
        # Layers_file_make
        if os.path.isfile('./fab2/text/dicer.txt'):  
            out = './fab2/f2_gdsout/'+key_name+'/'+key_name+'/'+key_name+".layers"
            with open (out,"w")as f:    
                pre_layer = []
                f.write("Version\t\t\t\t\t 6\n")
                for i in range(0,len(LAYER_NO)):
                    layer = LAYER_NO[i]
                    name = RETICLE_ID[i]
                    if layer in pre_layer:
                        continue
                    else:                     
                        if DA_TONE[i] == "DK":
                            filed_tone = "Clear"
                        elif DA_TONE[i] == "CL":
                            filed_tone = "Dark"
                        if SL_TONE[i] == "DK":
                            sl_tone = "Dark"
                        elif SL_TONE[i] == "CL":
                            sl_tone = "Clear"   
                        pre_layer.append(layer)                       
                        f.write("Layer\t\t\t\t\t %s\n"%(layer))
                        f.write("Layer_Datatype\t\t\t\t 0\n")
                        f.write("Field_Polarity\t\t\t\t \"%s\"\n" %(filed_tone))
                        f.write("Scribe_Polarity\t\t\t\t \"%s\"\n" %(sl_tone)) 
                        f.write("Drop\t\t\t\t\t \"\"\n")
                        f.write("Comment\t\t\t\t\t \"%s\"\n" %(name)) 
                        f.write("Groups\t\t\t\t\t \"\"\n")
                        f.write("\n")
                if process.find("BD18") == -1 or process.find("AN18") == -1 or process.find("BD15") == -1:
                    f.write("Layer\t\t\t\t\t 98\n")
                    f.write("Layer_Datatype\t\t\t\t 0\n")
                    f.write("Field_Polarity\t\t\t\t \"Dark\"\n")
                    f.write("Scribe_Polarity\t\t\t\t \"Dark\"\n") 
                    f.write("Drop\t\t\t\t\t \"\"\n")
                    f.write("Comment\t\t\t\t\t \"PSM\"\n") 
                    f.write("Groups\t\t\t\t\t \"\"\n")
                    f.write("\n")
                    f.write("Layer\t\t\t\t\t 100\n")
                    f.write("Layer_Datatype\t\t\t\t 0\n")
                    f.write("Field_Polarity\t\t\t\t \"Dark\"\n")
                    f.write("Scribe_Polarity\t\t\t\t \"Dark\"\n") 
                    f.write("Drop\t\t\t\t\t \"\"\n")
                    f.write("Comment\t\t\t\t\t \"FR_BOUNDARY\"\n") 
                    f.write("Groups\t\t\t\t\t \"\"\n")
                    f.write("\n")
                    f.write("End_of_Layers\n")
                    f.write("\n")
                    f.write("Layer\t\t\t\t\t 98\n")
                    f.write("Layer_Datatype\t\t\t\t 0\n")
                    f.write("Comment\t\t\t\t\t \"*\"\n") 
                    f.write("Field_Polarity\t\t\t\t \"*\"\n")
                    f.write("Scribe_Polarity\t\t\t\t \"*\"\n") 
                    f.write("Inv\t\t\t\t\t 0\n")
                    f.write("Item\t\t\t\t\t \"CHIP,CDBAR,TP,OPCTP\"\n") 
                    f.write("Any\t\t\t\t\t 0\n")
                    f.write("Restrict\t\t\t\t \"DevType\"\n") 
                    f.write("What\t\t\t\t\t \"Shape\"\n") 
                    f.write("Operation\t\t\t\t \"GENSHAPE\"\n") 
                    f.write("Version_Num\t\t\t\t 8\n")
                    f.write("Gen_Region\t\t\t\t 0\n")
                    f.write("Do_Regular_Regions\t\t\t 0\n")
                    f.write("Do_Computed_Regions\t\t\t 0\n")
                    f.write("Is_Ring\t\t\t\t\t 0\n")
                    f.write("External\t\t\t\t 0\n")
                    f.write("Size_LEFT\t\t\t\t \"\"\n")
                    f.write("Size_RIGHT\t\t\t\t \"\"\n")
                    f.write("Size_BOTTOM\t\t\t\t \"\"\n")
                    f.write("Size_TOP\t\t\t\t \"\"\n")
                    f.write("ResHole\t\t\t\t\t 0\n")
                    f.write("Trim_To_Field\t\t\t\t 0\n")
                    f.write("Drop\t\t\t\t\t \"\"\n")
                    f.write("Comments\t\t\t\t 0\n")
                    f.write("\n")
                    f.write("Layer\t\t\t\t\t 100\n")
                    f.write("Layer_Datatype\t\t\t\t 0\n")
                    f.write("Comment\t\t\t\t\t \"*\"\n") 
                    f.write("Field_Polarity\t\t\t\t \"*\"\n")
                    f.write("Scribe_Polarity\t\t\t\t \"*\"\n") 
                    f.write("Inv\t\t\t\t\t 0\n")
                    f.write("Item\t\t\t\t\t \"FRAME\"\n") 
                    f.write("Any\t\t\t\t\t 0\n")
                    f.write("Restrict\t\t\t\t \"OldStlyle\"\n") 
                    f.write("What\t\t\t\t\t \"Outline\"\n") 
                    f.write("Operation\t\t\t\t \"GENSHAPE\"\n") 
                    f.write("Version_Num\t\t\t\t 8\n")
                    f.write("Gen_Region\t\t\t\t 0\n")
                    f.write("Do_Regular_Regions\t\t\t 0\n")
                    f.write("Do_Computed_Regions\t\t\t 0\n")
                    f.write("Is_Ring\t\t\t\t\t 0\n")
                    f.write("External\t\t\t\t 0\n")
                    f.write("Size_LEFT\t\t\t\t \"\"\n")
                    f.write("Size_RIGHT\t\t\t\t \"\"\n")
                    f.write("Size_BOTTOM\t\t\t\t \"\"\n")
                    f.write("Size_TOP\t\t\t\t \"\"\n")
                    f.write("ResHole\t\t\t\t\t 0\n")
                    f.write("Trim_To_Field\t\t\t\t 0\n")
                    f.write("Drop\t\t\t\t\t \"\"\n")
                    f.write("Comments\t\t\t\t 0\n")
                    f.write("\n")
                    f.write("End_of_Operations\n")
                    f.close()
        
            # DICER
            lib = gdstk.Library() # lib 생성
            cell_name = process +"_DICER_"+ date
            #cell_name = process +"_DICER_"+'240423'
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
                elif DICER[i] == "11" :
                    type11_0 = gdstk.rectangle((0,20),(25,25))
                    type11_1 = gdstk.rectangle((20,0),(25,25))
                    type11_2 =  gdstk.rectangle((0,0),(25,25))
                    type11_3 = gdstk.boolean(type11_0,type11_1,"or")
                    type11 = gdstk.boolean(type11_2,type11_3,"not",layer=int(layer_no))                                   
                    cell.add(*type11)
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
                elif DICER[i] == "33" :
                    type33_0 = gdstk.rectangle((0,15.5),(19.5,19.5))
                    type33_1 = gdstk.rectangle((15.5,0),(19.5,19.5))
                    type33_2 = gdstk.boolean(type33_0,type33_1,"or")
                    type33_3 = gdstk.rectangle((0,0),(19.5,19.5))
                    type33 = gdstk.boolean(type33_2,type33_3,"not",layer=int(layer_no))
                    cell.add(*type33)
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
                elif DICER[i] == "55" :
                    type55_0 = gdstk.rectangle((0,25),(30,30))
                    type55_1 = gdstk.rectangle((25,0),(30,30))
                    type55_2 = gdstk.rectangle((0,0),(30,30))
                    type55_3 = gdstk.boolean(type55_0,type55_1,"or")
                    type55 = gdstk.boolean(type55_2,type55_3,"not",layer=int(layer_no))
                    cell.add(*type55)
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
            output_name ='./fab2/f2_gdsout/'+key_name+'/'+cell_name+".gds"
            lib.write_gds(output_name)
            # DICER_external_file
            gds_dicer = glob.glob('./fab2/f2_gdsout/'+key_name+'/'+'*DICER*.gds')
            for i in range(0,len(gds_dicer)) :
                top1 = gds_dicer[i].split('.gds')[0]
                top = os.path.basename(top1)
                out = './fab2/f2_gdsout/'+key_name+'/'+key_name+'/'+cell_name+".DICER"
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
        
            # S8000
            slib = gdstk.Library() # lib 생성
            scell_name = process +"_S8000_"+ date
            scell = slib.new_cell(scell_name) # cell 생성
            scheck = 0
            for i in range(0,len(LAYER_NO)) :
                layer_no = LAYER_NO[i]
                if S8000[i] == "1" :
                    type1_a = gdstk.rectangle((15,3),(31,43))
                    type1_b = gdstk.rectangle((3,15),(43,31))
                    type1 = gdstk.boolean(type1_a,type1_b,"or",layer=int(layer_no))
                    scell.add(*type1)
                    scheck = scheck + 1
                elif S8000[i] == "2" :
                    type2_a = gdstk.rectangle((17,3),(29,43))
                    type2_b = gdstk.rectangle((3,17),(43,29))
                    type2 = gdstk.boolean(type2_a,type2_b,"or",layer=int(layer_no))
                    scell.add(*type2)
                    scheck = scheck + 1
                elif S8000[i] == "3" :
                    type3_a = gdstk.rectangle((20.5,9),(25.5,37))
                    type3_b = gdstk.rectangle((9,20.5),(37,25.5))
                    type3 = gdstk.boolean(type3_a,type3_b,"or",layer=int(layer_no))
                    scell.add(*type3)
                    scheck = scheck + 1
                elif S8000[i] == "4" :
                    array_x = 7
                    array_y = 23
                    width_xy = 0.24
                    pitch_xy = 1.6
                    start_x1 = 18.08
                    start_y1 = 5.28
                    start_x2 = 5.28
                    start_y2 = 18.08
                    for ax in range(array_x):
                        for ay in range(array_y):
                            x0 = start_x1+ ax*pitch_xy
                            y0 = start_y1+ ay*pitch_xy
                            type4_a = gdstk.rectangle((x0,y0),(x0+width_xy,y0+width_xy),layer=int(layer_no))
                            scell.add(type4_a)
                    for ax in range(array_y):
                        for ay in range(array_x):
                            x1 = start_x2+ ax*pitch_xy
                            y1 = start_y2+ ay*pitch_xy
                            type4_b = gdstk.rectangle((x1,y1),(x1+width_xy,y1+width_xy),layer=int(layer_no))
                            scell.add(type4_b)
                    scheck = scheck + 1
                elif S8000[i] == "5" :
                    array_x = 7
                    array_y = 23
                    width_xy = 0.38
                    pitch_xy = 1.6
                    start_x1 = 18.01
                    start_y1 = 5.21
                    start_x2 = 5.21
                    start_y2 = 18.01
                    for ax in range(array_x):
                        for ay in range(array_y):
                            x0 = start_x1+ ax*pitch_xy
                            y0 = start_y1+ ay*pitch_xy
                            type5_a = gdstk.rectangle((x0,y0),(x0+width_xy,y0+width_xy),layer=int(layer_no))
                            scell.add(type5_a)
                    for ax in range(array_y):
                        for ay in range(array_x):
                            x1 = start_x2+ ax*pitch_xy
                            y1 = start_y2+ ay*pitch_xy
                            type5_b = gdstk.rectangle((x1,y1),(x1+width_xy,y1+width_xy),layer=int(layer_no))
                            scell.add(type5_b)
                    scheck = scheck + 1
                elif S8000[i] == "6" :
                    array_x = 7
                    array_y = 23
                    width_xy = 0.66
                    pitch_xy = 1.6
                    start_x1 = 17.87
                    start_y1 = 5.07
                    start_x2 = 5.07
                    start_y2 = 17.87
                    for ax in range(array_x):
                        for ay in range(array_y):
                            x0 = start_x1+ ax*pitch_xy
                            y0 = start_y1+ ay*pitch_xy
                            type6_a = gdstk.rectangle((x0,y0),(x0+width_xy,y0+width_xy),layer=int(layer_no))
                            scell.add(type6_a)
                    for ax in range(array_y):
                        for ay in range(array_x):
                            x1 = start_x2+ ax*pitch_xy
                            y1 = start_y2+ ay*pitch_xy
                            type6_b = gdstk.rectangle((x1,y1),(x1+width_xy,y1+width_xy),layer=int(layer_no))
                            scell.add(type6_b)
                    scheck = scheck + 1
                elif S8000[i] == "7" :
                    array_x = 5
                    array_y = 15
                    width_xy = 1.3
                    pitch_xy = 2.6
                    start_x1 = 17.15
                    start_y1 = 4.15
                    start_x2 = 4.15
                    start_y2 = 17.15
                    for ax in range(array_x):
                        for ay in range(array_y):
                            x0 = start_x1+ ax*pitch_xy
                            y0 = start_y1+ ay*pitch_xy
                            type7_a = gdstk.rectangle((x0,y0),(x0+width_xy,y0+width_xy),layer=int(layer_no))
                            scell.add(type7_a)
                    for ax in range(array_y):
                        for ay in range(array_x):
                            x1 = start_x2+ ax*pitch_xy
                            y1 = start_y2+ ay*pitch_xy
                            type7_b = gdstk.rectangle((x1,y1),(x1+width_xy,y1+width_xy),layer=int(layer_no))
                            scell.add(type7_b)
                    scheck = scheck + 1                     
                elif S8000[i] == "-" :
                    pass
            #print(scheck)
            if scheck != 0:
                bound = gdstk.rectangle((0,0),(46,46), layer=int(63))
                scell.add(bound)
                x1_max = 46
                y1_max = 46
                output_name ='./fab2/f2_gdsout/'+key_name+'/'+scell_name+".gds"
                slib.write_gds(output_name)
                # S8000_external_file
                gds_tar = glob.glob('./fab2/f2_gdsout/'+key_name+'/'+'*S8000*.gds')
                for i in range(0,len(gds_tar)) :
                        s_top1 = gds_tar[i].split('.gds')[0]
                        s_top = os.path.basename(s_top1)
                        out = './fab2/f2_gdsout/'+key_name+'/'+key_name+'/'+scell_name+".S8000"
                        with open (out,"w")as f:
                            f.write("File_Type\t\t\t \"GDS\"\n")
                            f.write("Hotspot_Name\t\t\t \"1\"\n")
                            f.write("Hotspot_X\t\t\t \"0\"\n")
                            f.write("Hotspot_Y\t\t\t \"0\"\n") 
                            f.write("Hotspot_End\n")
                            f.write("Version\t\t\t\t 9\n")
                            f.write("File\t\t\t\t \"$STD_KEY/%s/%s/%s.gds\"\n" %(pro,key_name,s_top))
                            f.write("Topstr\t\t\t\t \"%s\"\n" %(s_top))
                            f.write("BlTopStr\t\t\t \"NONE\"\n")
                            f.write("SizeLay\t\t\t\t -1\n")
                            f.write("SizeDT\t\t\t\t -1\n")
                            f.write("Strip\t\t\t\t 0\n")
                            f.write("Missing_OK\t\t\t 0\n")
                            f.write("Snap_OK\t\t\t\t 0\n")
                            f.write("Inhibit_Autosize\t\t 0\n")
                            f.write("X_Min\t\t\t\t \"0\"\n")
                            f.write("Y_Min\t\t\t\t \"0\"\n")
                            f.write("X_Max\t\t\t\t \"%s\"\n" %(x1_max))
                            f.write("Y_Max\t\t\t\t \"%s\"\n" %(y1_max))
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
                            f.write("%s.gds\tS8000\t%s\t0\t0\t%s\t%s\t0\t0\n" %(s_top,s_top,x1_max,y1_max))              
            else:
                pass

        # 1ST_OVERLAY
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
                    txy = int(key_type.split('_')[-1])
                    if txy != 7:
                        txt_y = 12
                    else:
                        txt_y = 10
                    x_max = int(overlay_1st.split('_')[9])
                    yy_max = int(overlay_1st.split('_')[9])+txt_y
                    if i == 0 :
                        in_top.add(gdstk.Reference(in_1st,(0,0)))
                        out_top.add(gdstk.Reference(out_1st,(0,0)))
                    else:
                        in_top.add(gdstk.Reference(in_1st,(0,0)))
                        out_top.add(gdstk.Reference(out_1st,(0,0)))
                else:
                    pass
            output1 = './fab2/f2_gdsout/'+key_name+'/'+in_top_cell+".gds"
            output2 = './fab2/f2_gdsout/'+key_name+'/'+out_top_cell+".gds"
            inlib.write_gds(output1)
            outlib.write_gds(output2)
        else:
            pass
        # 1ST_OVERLAY_external_file
        gds_tar = glob.glob('./fab2/f2_gdsout/'+key_name+'/'+"*1ST*.gds")
        for i in range(0,len(gds_tar)) :
            top1 =gds_tar[i].split('.gds')[0]
            top = os.path.basename(top1)
            frist_list=top.split('_')
            for i in range(0,len(frist_list)):
                if "1ST" in frist_list[i]:
                    frsty=frist_list[i+1]
            out = './fab2/f2_gdsout/'+key_name+'/'+key_name+'/'+top+".1ST_"+frsty
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
                f.write("Y_Max\t\t\t\t \"%s\"\n" %(yy_max))
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
                f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t0\t0\n" %(top,'1ST_'+frsty,top,x_max,yy_max))

if __name__ == '__main__':
    process  = "BD130S_60um"
    priority = [1,2,3]
    outlayer = [119,3,3]
    inlayer  = [77,77,2]
    key_type = ["OVERLAY_KY_M_2_0_PB_M_2_0_28_6","OVERLAY_AA_T_1_0_PB_M_2_0_28_6","OVERLAY_AA_T_1_0_NB_M_8_0_28_6"]
    boundary = [[63,3],[63],[63]]
    text     = ["70_0","75_11","70_0"]
    bl, br, = main(process,priority,outlayer,inlayer,key_type,boundary,text)