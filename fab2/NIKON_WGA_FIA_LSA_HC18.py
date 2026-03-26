import gdstk, datetime, shutil
from fab2 import NIKON_WGA, NIKON_FIA, NIKON_LSA
import pandas as pd

def main(process,priority,layer_no,key_type,boundary,file_n):
    ## WGA/FIA/LSA_ALL
    fn=(str(file_n))
    date = datetime.datetime.now().strftime("%y%m%d")
    process_spd = process+"_SPD"
    key_name_spd = process_spd+"_PHOTOKEY_"+date
    top_cell = process_spd +'_'+fn+'_'+str(date)
    lib = gdstk.Library() ## lib 생성
    cell = lib.new_cell(top_cell) ## cell 생성

    data = {'priority':priority,'layer_no':layer_no,'key_type':key_type,'boundary':boundary}
    df = pd.DataFrame(data)
    df_sort = df.sort_values('priority')  ## sort by priority  

    rect_x = 0
    x_max = 0 ## External_X_Max 생성
    y_max = 0
    for i in range(0,len(df_sort)) :
        PRIORITY = df_sort.iloc[i,0]
        LAYER_NO = df_sort.iloc[i,1]
        KEY_TYPE = df_sort.iloc[i,2]
        BOUNDARY = df_sort.iloc[i,3]
        if KEY_TYPE.split('_')[0] =="WGA":
            res = NIKON_WGA.generate(int(PRIORITY),int(LAYER_NO),KEY_TYPE,BOUNDARY)
            lib.add(res)
            main_x = int(KEY_TYPE.split('_')[1])
            main_y = int(KEY_TYPE.split('_')[2])
            y_offset = 0
        elif KEY_TYPE.split('_')[0] =="FIA":
            res = NIKON_FIA.generate(int(PRIORITY),int(LAYER_NO),KEY_TYPE,BOUNDARY)
            lib.add(res)
            main_x = int(KEY_TYPE.split('_')[1])
            main_y = int(KEY_TYPE.split('_')[2])
            y_offset = (main_y - 54) / 2 
        elif KEY_TYPE.split('_')[0] =="LSA":
            res = NIKON_LSA.generate(int(PRIORITY),int(LAYER_NO),KEY_TYPE,BOUNDARY)
            lib.add(res)
            main_x = int(KEY_TYPE.split('_')[1])
            main_y = int(KEY_TYPE.split('_')[2])
            y_offset = (main_y - 54) / 2
        y_max = max(y_max,main_y)
        pro_now = int(PRIORITY)
        if i == 0 :  ## 첫번째 셀 배치 0,0 부터
            pro_bak = pro_now
            x_max = main_x
            bk_bound = int(KEY_TYPE.split('_')[1])
            x_hot = int(main_x)/2   ## External_X_hotspot
            cell.add(gdstk.Reference(res,(0,0)))
            if KEY_TYPE.split('_')[0] =="WGA":
                y_hot = int(main_y)/2+3  ## External_Y_hotspot
            else:
                y_hot = int(main_y)/2
        elif KEY_TYPE.split('_')[0] =="WGA" and main_x == 50 :
            rect_s = rect_x + bk_bound
            rect_x = rect_x + main_x
            x_max = x_max + main_x
            if y_max == main_y:
                cell.add(gdstk.Reference(res,(rect_s,0)))
            else:
                cell.add(gdstk.Reference(res,(rect_s,2)))
        else:
            if KEY_TYPE.split('_')[0] =="WGA" :
                if y_max == main_y :
                    if pro_bak == pro_now :
                        rect_x = rect_x
                        x_max = x_max
                    else:
                        pro_bak = pro_now
                        rect_x = rect_x + main_x
                        x_max = x_max + main_x
                    cell.add(gdstk.Reference(res,(rect_x,0)))
                else:
                    if pro_bak == pro_now :
                        rect_x = rect_x
                        x_max = x_max
                    else:
                        pro_bak = pro_now
                        rect_s = rect_x + bk_bound
                        rect_x = rect_x + main_x
                        x_max = x_max + main_x
                    cell.add(gdstk.Reference(res,(rect_s,2)))
            else:
                if y_max == main_y :
                    if pro_bak == pro_now :
                        rect_x = rect_x
                        x_max = x_max
                    else:
                        pro_bak = pro_now
                        rect_s = rect_x + bk_bound
                        rect_x = rect_x + main_x
                        x_max = x_max + main_x
                    cell.add(gdstk.Reference(res,(rect_x,y_offset)))
                else:
                    if pro_bak == pro_now :
                        rect_s = rect_x + bk_bound
                        rect_x = rect_x
                        x_max = x_max
                    else:
                        pro_bak = pro_now
                        rect_x = rect_x + main_x
                        rect_s = rect_x + bk_bound
                        x_max = x_max + main_x
                    cell.add(gdstk.Reference(res,(rect_s,y_offset+2)))
    output_name = "./fab2/f2_gdsout/"+key_name_spd+"/"+top_cell+".gds"
    lib.write_gds(output_name)

    pro = process.split('_')
    out = "./fab2/f2_gdsout/"+key_name_spd+"/"+key_name_spd+"/"+top_cell+'.'+fn+'_x'
    with open (out,"w")as f:
        f.write("File_Type\t\t\t \"GDS\"\n")
        f.write("Hotspot_Name\t\t\t \"1\"\n")
        f.write("Hotspot_X\t\t\t \"%s\"\n" %(x_hot))
        f.write("Hotspot_Y\t\t\t \"%s\"\n" %(y_hot)) 
        f.write("Hotspot_End\n")
        f.write("Version\t\t\t\t 9\n")
        f.write("File\t\t\t\t \"$STD_KEY/%s/%s/%s.gds\"\n" %(pro[0],key_name_spd,top_cell))
        f.write("Topstr\t\t\t\t \"%s\"\n" %(top_cell))
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
    out2 = "./fab2/f2_gdsout/"+key_name_spd+"/"+key_name_spd+"/"+top_cell+'.'+fn+'_y'
    shutil.copy2(out,out2)
    out3= "./fab2/f2_gdsout/"+key_name_spd+"/"+key_name_spd+"/"+key_name_spd+'.txt'
    with open (out3,"a")as f:
        f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top_cell,fn+'_x',top_cell,x_max,y_max,x_hot,y_hot))
        f.write("%s.gds\t%s\t%s\t0\t0\t%s\t%s\t%s\t%s\n" %(top_cell,fn+'_y',top_cell,x_max,y_max,x_hot,y_hot))
    return output_name
    
if __name__ == '__main__':
    process = "BD130S_60um"
    priority = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    layer_no = [119,119,3,3,6,9,9,10,10,11,11,12,12,13,13,14]
    key_type = ["FIA_150_54_6_0_49_0_T","FIA_150_54_1_5_6_0_T","FIA_150_54_6_0_49_0_T","FIA_150_54_1_5_6_0_T","FIA_150_54_6_0_49_0_M","FIA_150_54_1_5_6_0_T","FIA_150_54_2_0_6_0_T","FIA_150_54_6_0_49_0_M","FIA_150_54_1_5_6_0_M","FIA_150_54_1_5_6_0_T","FIA_150_54_2_0_6_0_T","FIA_150_54_6_0_49_0_M","FIA_150_54_1_5_6_0_M","FIA_150_54_1_5_6_0_T","FIA_150_54_2_0_6_0_T","FIA_150_54_6_0_49_0_M"]
    boundary = [[63,48,73,89],[63,48,73,89],[63,48,73,89],[63,48,73,89],[63,3,48,73,89],[63,3,48,73,89,10],[63,3,48,73,89,10],[63,3,48,73,89],[63,3,48,73,89],[63,3,48,73,89,12],[63,3,48,73,89,12],[63,3,48,73,89],[63,3,48,73,89],[63,3,48,73,89,14],[63,3,48,73,89,14],[63,3,48,73,89]]
    res = main(process,priority,layer_no,key_type,boundary)