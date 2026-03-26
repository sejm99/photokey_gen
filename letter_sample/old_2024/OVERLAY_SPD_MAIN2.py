import gdstk, datetime
#from fab2 import OVERLAY_SPD_BL_BR_LL_LR
import OVERLAY_SPD_BL_BR_LL_LR
import pandas as pd

def main(process,priority,outlayer,inlayer,key_type,boundary):
    ## OVERLAY_SPD
    date = datetime.datetime.now().strftime("%y%m%d")
    bllib = gdstk.Library()                    ## BL_lib 생성
    brlib = gdstk.Library()                    ## BR_lib 생성
    ullib = gdstk.Library()                    ## UL_lib 생성
    urlib = gdstk.Library()                    ## UR_lib 생성
    bl_top_cell = process + "_BL_" + str(date)
    br_top_cell = process + "_BR_" + str(date)
    ul_top_cell = process + "_UL_" + str(date)
    ur_top_cell = process + "_UR_" + str(date)
    bl_t = bllib.new_cell(bl_top_cell)         ## BL_top_cell 생성
    br_t = brlib.new_cell(br_top_cell)         ## BR_top_cell 생성
    ul_t = ullib.new_cell(ul_top_cell)         ## UL_top_cell 생성
    ur_t = urlib.new_cell(ur_top_cell)         ## UR_top_cell 생성
    
    data = {'priority':priority,'outlayer':outlayer,'inlayer':inlayer, 'key_type':key_type,'boundary':boundary}
    df = pd.DataFrame(data)
    df_sort = df.sort_values('priority')        ## sort by priority  

    rect_y = 0
    y_max = 0   ## External_Y_Max 생성 

    for i in range(0,len(df_sort)) :
        PRIORITY = df_sort.iloc[i,0]
        OUTLAYER = df_sort.iloc[i,1]
        INLAYER  = df_sort.iloc[i,2]
        KEY_TYPE = df_sort.iloc[i,3]
        BOUNDARY = df_sort.iloc[i,4]
        bl, br, ul, ur = OVERLAY_SPD_BL_BR_LL_LR.start(int(PRIORITY),int(OUTLAYER),int(INLAYER),KEY_TYPE,BOUNDARY)
        bllib.add(bl)
        brlib.add(br)
        ullib.add(ul)
        urlib.add(ur)

        bl_t.add(gdstk.Reference(bl,(0,0)))
        br_t.add(gdstk.Reference(br,(0,0)))
        ul_t.add(gdstk.Reference(ul,(0,0)))
        ur_t.add(gdstk.Reference(ur,(0,0)))

        bl_lib.write_gds(bl_top_cell + ".gds")
        br_lib.write_gds(br_top_cell + ".gds")
        ul_lib.write_gds(ul_top_cell + ".gds")
        ur_lib.write_gds(ur_top_cell + ".gds")
        pro_now = int(PRIORITY)
        over_y = int(KEY_TYPE.split('_')[9])+10
        rect_y = over_y

        ## cell.add(gdstk.Reference(res,(x,0)))
        if i == 0 :  ## 첫번째 셀 배치 0,0 부터
            pro_bak = pro_now
            bl_t.add(gdstk.Reference(bl,(0,0)))
            br_t.add(gdstk.Reference(br,(0,0)))
            ul_t.add(gdstk.Reference(ul,(0,0)))
            ur_t.add(gdstk.Reference(ur,(0,0)))
            #x_hot = (float(bar_xy)/2)+10    ## External_X_hotspot
            #y_hot = (float(bar_xy)/2)+10    ## External_Y_hotspot
            #x_max = float(bar_xy)+10        ## External_X_Max
            y_max = over_y                  ## External_Y_Max
        else:
            if pro_bak == pro_now :
                rect_y = rect_y
                y_max = y_max
            else :
                pro_bak = pro_now
                rect_y = rect_y + over_y
                y_max = y_max + over_y
            bl_t.add(gdstk.Reference(bl,(0,rect_y)))
            br_t.add(gdstk.Reference(br,(0,rect_y)))
            ul_t.add(gdstk.Reference(ul,(0,rect_y)))
            ur_t.add(gdstk.Reference(ur,(0,rect_y)))
    bl_lib.write_gds(bl_top_cell + ".gds")
    br_lib.write_gds(br_top_cell + ".gds")
    ul_lib.write_gds(ul_top_cell + ".gds")
    ur_lib.write_gds(ur_top_cell + ".gds")
    return bl_t, br_t, ul_t, ur_t
    #output_name1 = "./fab2/f2_gdsout/" + bl_top_cell + ".gds"
    #output_name2 = "./fab2/f2_gdsout/" + br_top_cell + ".gds"
    #output_name3 = "./fab2/f2_gdsout/" + ul_top_cell + ".gds"
    #output_name4 = "./fab2/f2_gdsout/" + ur_top_cell + ".gds"
    #bl_lib.write_gds(process + "_BL_" + str(date) + ".gds")
    #br_lib.write_gds(process + "_BR_" + str(date) + ".gds")
    #ul_lib.write_gds(process + "_BR_" + str(date) + ".gds")
    #ur_lib.write_gds(process + "_UR_" + str(date) + ".gds")
    #return process + "_BL_" + ".gds",process + "_BR_" + ".gds",process + "_BR_" + ".gds",process + "_UR_" + ".gds"
   
if __name__ == '__main__':
    process = "BD130S_60um"
    priority = [1,2,3]
    outlayer = [119,3,3]
    inlayer = [77,77,2]
    key_type = ["OVERLAY_KY_M_2_0_PB_M_2_0_27_7","OVERLAY_AA_T_1_0_PB_M_2_0_27_7","OVERLAY_AA_T_1_0_NB_M_8_0_27_7"]
    boundary = [[63,3],[63],[63]]
    bl, br, ul, ur = main(process,priority,outlayer,inlayer,key_type,boundary)

    """   
        bllib = gdstk.Library() 
        brlib = gdstk.Library()
        ullib = gdstk.Library() 
        urlib = gdstk.Library() 
        bl = bllib.new_cell(KEY_TYPE +"_BL")      # BL_cell_Define
        br = brlib.new_cell(KEY_TYPE +"_BR")      # BR_cell_Define
        ul = ullib.new_cell(KEY_TYPE +"_UL")      # UL_cell_Define
        ur = urlib.new_cell(KEY_TYPE +"_UR")      # UR_cell_Define
        box, left, right, bl_p, br_p, ul_p, ur_p = OVERLAY_SPD_BL_BR_LL_LR.generate(int(PRIORITY),int(OUTLAYER),int(INLAYER),KEY_TYPE,BOUNDARY)
        bllib.add(box, left, right, bl_p)      
        brlib.add(box, left, right, br_p)
        ullib.add(box, left, right, ul_p)
        urlib.add(box, left, right, ur_p)

        bar_xy = float(KEY_TYPE.split('_')[9])
        bar_half = (float(bar_xy)+10)/2              
        bl.add(gdstk.Reference(box,(0,10)))
        bl.add(gdstk.Reference(left,(0,0)))
        bl.add(gdstk.Reference(right,((float(bar_half),0))))
        bl.add(gdstk.Reference(bl_p,(float(bar_xy),10)))

        br.add(gdstk.Reference(box,(0,10)))
        br.add(gdstk.Reference(left,(0,0)))
        br.add(gdstk.Reference(right,(float(bar_half),0)))
        br.add(gdstk.Reference(br_p,(float(bar_xy),10)))
                        
        ul.add(gdstk.Reference(box,(0,10)))
        ul.add(gdstk.Reference(left,(0,0)))
        ul.add(gdstk.Reference(right,(float(bar_half),0)))
        ul.add(gdstk.Reference(ul_p,(float(bar_xy),10)))
                            
        ur.add(gdstk.Reference(box,(0,10)))
        ur.add(gdstk.Reference(left,(0,0)))
        ur.add(gdstk.Reference(right,(float(bar_half),0)))
        ur.add(gdstk.Reference(ur_p,(float(bar_xy),10)))

    top = [bl_top_cell,br_top_cell,ul_top_cell,ur_top_cell]
    pro = process.split('_')

    for i in range(0,len(top)) :
        out = "./fab2/f2_gdsout/" + top[i] + ".OVERLAY"
        with open (out,"w")as f:
            f.write("File_Type\t\t\t \"GDS\"\n")
            f.write("Hotspot_Name\t\t\t \"1\"\n")
            f.write("Hotspot_X\t\t\t \"%s\"\n" %(x_hot))
            f.write("Hotspot_Y\t\t\t \"%s\"\n" %(y_hot)) 
            f.write("Hotspot_End\n")
            f.write("Version\t\t\t\t 9\n")
            f.write("File\t\t\t\t \"$STD_KEY/%s/%s.gds\"\n" %(pro[0],top[i]))
            f.write("Topstr\t\t\t\t \"%s\"\n" %(top[i]))
            f.write("BlTopStr\t\t\t \"NONE\"\n")
            f.write("SizeLay\t\t\t\t -1\n")
            f.write("SizeDT\t\t\t\t -1\n")
            f.write("Strip\t\t\t\t 0\n")
            f.write("Missing_OK\t\t\t 0\n")
            f.write("Snap_OK\t\t\t\t 0\n")
            f.write("Inhibit_Autosize\t\t 0\n")
            f.write("X_Min\t\t\t\t 0\"\n")
            f.write("Y_Min\t\t\t\t 0\"\n")
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

    return output_name1,output_name2,output_name3,output_name4, out
    """

#if __name__ == '__main__':
#    process = "BD130S_60um"
#    priority = [1]
#    outlayer = [119]
#    inlayer = [77]
#    key_type = ["OVERLAY_KY_M_2_0_PB_M_2_0_27_7"]
#    boundary = [[63,3]]
#    bl, br, ul, ur = main(process,priority,outlayer,inlayer,key_type,boundary)

