import gdstk, datetime
import OVERLAY_SPD_BL_BR_LL_LR
import pandas as pd

def main(process,priority,outlayer,inlayer,key_type,boundary):
    date = datetime.datetime.now().strftime("%y%m%d")
    bllib = gdstk.Library()                    ## BL_lib 생성
    bl_top_cell = process + "_BL_" + str(date)
    bl_t = bllib.new_cell(bl_top_cell)         ## BL_top_cell 생성
 
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
        print(PRIORITY,OUTLAYER,INLAYER,KEY_TYPE,BOUNDARY)
        bl = OVERLAY_SPD_BL_BR_LL_LR.start(int(PRIORITY),int(OUTLAYER),int(INLAYER),KEY_TYPE,BOUNDARY,bllib)
        bllib.add(bl)
        bl_t.add(gdstk.Reference(bl,(0,rect_y)))
        rect_y = rect_y + 37
        
    output_name = bl_top_cell + ".gds"
    bllib.write_gds(output_name)

    return bl_t
  
if __name__ == '__main__':
    process = "BD130S_60um"
    priority = [1,2,3]
    outlayer = [119,3,3]
    inlayer = [77,77,2]
    key_type = ["OVERLAY_KY_M_2_0_PB_M_2_0_27_7","OVERLAY_AA_T_1_0_PB_M_2_0_27_7","OVERLAY_AA_T_1_0_NB_M_8_0_27_7"]
    boundary = [[63,3],[63],[63]]
    bl = main(process,priority,outlayer,inlayer,key_type,boundary)
