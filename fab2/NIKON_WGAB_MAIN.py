import gdstk, datetime, numpy
from fab2 import NIKON_WGAB1, NIKON_WGAB2
import pandas as pd

def main(process,priority,layer_no,key_type,boundary,file_n):
    ## BSI_WGA_ALL
    fn=(str(file_n))
    #fn=(str(file_n[-2]))
    date = datetime.datetime.now().strftime("%y%m%d")
    key_names = process+"_PHOTOKEY_"+date
    xtop_cell = process +'_'+fn+'_X_'+str(date)
    ytop_cell = process +'_'+fn+'_Y_'+str(date)
    xlib = gdstk.Library() ## lib 생성
    ylib = gdstk.Library() ## lib 생성
    xcell = xlib.new_cell(xtop_cell) ## cell 생성
    ycell = ylib.new_cell(ytop_cell) ## cell 생성

    data = {'priority':priority,'layer_no':layer_no,'key_type':key_type,'boundary':boundary}
    df = pd.DataFrame(data)
    df_sort = df.sort_values('priority')  ## sort by priority  

    rect_x = 0
    x_max = 0 
    for i in range(0,len(df_sort)) :
        PRIORITY = df_sort.iloc[i,0]
        LAYER_NO = df_sort.iloc[i,1]
        KEY_TYPE = df_sort.iloc[i,2]
        BOUNDARY = df_sort.iloc[i,3]
        bar_x=(KEY_TYPE.split('_')[3]+'.'+KEY_TYPE.split('_')[4])
        bar_y=(KEY_TYPE.split('_')[5]+'.'+KEY_TYPE.split('_')[6])
        if (LAYER_NO == "129" or LAYER_NO == "132") and float(bar_x) == 4.0 and float(bar_y) == 5.0 :
            res = NIKON_WGAB2.generate(int(PRIORITY),int(LAYER_NO),KEY_TYPE,BOUNDARY)
            xlib.add(res)
            ylib.add(res)
        else:
            res = NIKON_WGAB1.generate(int(PRIORITY),int(LAYER_NO),KEY_TYPE,BOUNDARY)
            xlib.add(res)
            ylib.add(res)
        pro_now = int(PRIORITY)
        main_x = int(KEY_TYPE.split('_')[1])
        main_y = int(KEY_TYPE.split('_')[2])
        
        if i == 0 :  ## 첫번째 셀 배치 0,0 부터
            pro_bak = pro_now
            xcell.add(gdstk.Reference(res,(0,0)))
            ycell.add(gdstk.Reference(res,(0,main_x),rotation=numpy.pi*3/2))
            bk_bound = int(KEY_TYPE.split('_')[1])
            x_hot = int(main_x)/2   ## External_X_hotspot
            y_hot = int(main_y)/2+3   ## External_Y_hotspot
            y_max = int(main_y)     ## External_Y_Max
            x_max = main_x          ## External_X_Max
        elif main_x == 50 or main_x == 75:
            rect_s = rect_x + bk_bound
            rect_x = rect_x + main_x
            x_max = x_max + main_x
            xcell.add(gdstk.Reference(res,(rect_s,0)))
            ycell.add(gdstk.Reference(res,(0,main_x+rect_s),rotation=numpy.pi*3/2))  
        else:
            if pro_bak == pro_now :
                rect_x = rect_x
                x_max = x_max
            else :
                pro_bak = pro_now
                rect_x = rect_x + main_x
                x_max = x_max + main_x
            xcell.add(gdstk.Reference(res,(rect_x,0)))
            ycell.add(gdstk.Reference(res,(0,main_x+rect_x),rotation=numpy.pi*3/2))   
    xoutput_name = "./fab2/f2_gdsout/" + key_names +"/"+ xtop_cell + ".gds"
    youtput_name = "./fab2/f2_gdsout/" + key_names +"/"+ ytop_cell + ".gds"
    xlib.write_gds(xoutput_name)
    ylib.write_gds(youtput_name)

    pro = process.split('_')
    out = "./fab2/f2_gdsout/"+key_names+"/"+key_names+"/"+xtop_cell+'.'+fn+'_x'
    with open (out,"w")as f:
        f.write("File_Type\t\t\t \"GDS\"\n")
        f.write("Hotspot_Name\t\t\t \"1\"\n")
        f.write("Hotspot_X\t\t\t \"%s\"\n" %(x_hot))
        f.write("Hotspot_Y\t\t\t \"%s\"\n" %(y_hot)) 
        f.write("Hotspot_End\n")
        f.write("Version\t\t\t\t 9\n")
        f.write("File\t\t\t\t \"$STD_KEY/%s/%s/%s.gds\"\n" %(pro[0],key_names,xtop_cell))
        f.write("Topstr\t\t\t\t \"%s\"\n" %(xtop_cell))
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
    out2 = "./fab2/f2_gdsout/"+key_names+"/"+key_names+"/"+xtop_cell+'.'+fn+'_y'
    with open (out2,"w")as f:
        f.write("File_Type\t\t\t \"GDS\"\n")
        f.write("Hotspot_Name\t\t\t \"1\"\n")
        f.write("Hotspot_X\t\t\t \"%s\"\n" %(y_hot))
        f.write("Hotspot_Y\t\t\t \"%s\"\n" %(x_hot)) 
        f.write("Hotspot_End\n")
        f.write("Version\t\t\t\t 9\n")
        f.write("File\t\t\t\t \"$STD_KEY/%s/%s.gds\"\n" %(pro[0],ytop_cell))
        f.write("Topstr\t\t\t\t \"%s\"\n" %(ytop_cell))
        f.write("BlTopStr\t\t\t \"NONE\"\n")
        f.write("SizeLay\t\t\t\t -1\n")
        f.write("SizeDT\t\t\t\t -1\n")
        f.write("Strip\t\t\t\t 0\n")
        f.write("Missing_OK\t\t\t 0\n")
        f.write("Snap_OK\t\t\t\t 0\n")
        f.write("Inhibit_Autosize\t\t 0\n")
        f.write("X_Min\t\t\t\t 0\"\n")
        f.write("Y_Min\t\t\t\t 0\"\n")
        f.write("X_Max\t\t\t\t \"%s\"\n" %(y_max))
        f.write("Y_Max\t\t\t\t \"%s\"\n" %(x_max))
        f.write("SB_Ext\t\t\t\t 0\n")
        f.write("SB_File_Loc\t\t\t \"NONE\"\n")
        f.write("SB_Min_X\t\t\t 0\n")
        f.write("SB_Min_Y\t\t\t 0\n")
        f.write("SB_Max_X\t\t\t 0\n")
        f.write("SB_Max_Y\t\t\t 0\n")
        f.write("SB_Align\t\t\t \"CC\"\n")
        f.write("Comment\t\t\t\t 0\n")
        f.write("End_Processes\n")
    out3= "./fab2/f2_gdsout/"+key_names+"/"+key_names+"/"+key_names+'.txt'
    with open (out3,"a")as f:
        f.write("%s.gds \t%s \t%s \t0 \t0 \t%s \t%s \t%s \t%s\n" %(xtop_cell,fn+'_x',xtop_cell,x_max,y_max,x_hot,y_hot))
        f.write("%s.gds \t%s \t%s \t0 \t0 \t%s \t%s \t%s \t%s\n" %(ytop_cell,fn+'_y',ytop_cell,y_max,x_max,y_hot,x_hot))
    return xoutput_name,youtput_name

if __name__ == '__main__':
    process = "IL110S_60um"
    priority = [1,2,3,4,5]
    layer_no = [77,77,3,3,3]
    key_type = ["WGA_200_75_3_0_4_0_T","WGA_200_75_4_0_2_0_T","WGA_75_75_2_8_2_8_T","WGA_200_75_4_0_2_0_T","WGAB_200_75_4_0_5_0_T"]
    boundary = [[63,3],[63,3],[63,3],[63],[63]]
    res = main(process,priority,layer_no,key_type,boundary)
