import glob
import os
import sys
import tarfile
import time

import gdstk

PROCESS=[]
PRORITY=[]
LAYER_NO=[]
GDS_NAME=[]
PAD_NO=[]
ETCH_TYPE=[]
MAIN_X=[]
MAIN_Y=[]
BAR_X=[]
BAR_Y=[]
ARR_X=[]
ARR_Y=[]
NAME_NUM=[]

def get_arr():
    global PROCESS
    global PRORITY
    global LAYER_NO
    global GDS_NAME
    global PAD_NO
    global ETCH_TYPE
    global MAIN_X
    global MAIN_Y
    global BAR_X
    global BAR_Y
    global ARR_X
    global ARR_Y
    PROCESS=[]
    PRORITY=[]
    LAYER_NO=[]
    GDS_NAME=[]
    PAD_NO=[]
    ETCH_TYPE=[]
    MAIN_X=[]
    MAIN_Y=[]
    BAR_X=[]
    BAR_Y=[]
    ARR_X=[]
    ARR_Y=[]
    
    #input 파일 정보 가져오기
    with open('./fab1/input','r') as f:
        lines = f.readlines()
        for line in lines:
            line_st=line.strip()
            line_sp=line_st.split()
            if line_sp == []:
                pass
            else:
                if line_sp[0] == "PROCESS":
                    PROCESS.append(line_sp[1])
                else:
                    PRORITY.append(line_sp[0])
                    GDS_NAME.append(line_sp[1])
                    PAD_NO.append(line_sp[2])
                    if "VERNIER_" in line_sp[1]:
                        MAIN_X.append(line_sp[1].split('_')[2])
                        if line_sp[1].split('_')[1][-1] == "2" or line_sp[1].split('_')[1][-1] == "3":
                            MAIN_Y.append("76")
                        else:
                            if line_sp[1].split('_')[1][-1] == "5" and "SJ" in PROCESS[0] and line_sp[1][3][:-1] == "10" and line_sp[1][4][:-1] == "9":
                                MAIN_Y.append("48")
                            else:
                                MAIN_Y.append("44")
                    elif "S8000_" in line_sp[1]:
                        MAIN_X.append(line_sp[1].split('_')[1])
                        MAIN_Y.append(line_sp[1].split('_')[2])
                    elif "1ST_" in line_sp[1]:
                        MAIN_X.append(line_sp[1].split('_')[3])
                        MAIN_Y.append(line_sp[1].split('_')[4])

def VER_ARR_SIZE_SORT_Y():
    #PRORITY 별 최대 Size 찾기 - Y
    v_count=1
    END_Y=0
    for i in range(0,len(GDS_NAME)):
        if "VERNIER" in GDS_NAME[i]:
            if int(PRORITY[i]) == v_count:
                END_Y = END_Y+float(MAIN_Y[i])
                #print(END_Y)
                v_count=v_count+1
    return END_Y

### Main ###
def main():
    cell = None
    res = None
    res1 = None
    global PROCESS
    global PRORITY
    global LAYER_NO
    global GDS_NAME
    global PAD_NO
    global MAIN_X
    global MAIN_Y
    get_arr()
    rem_gds_list = glob.glob('./fab1/f1_gdsout/*.KEY')
    for i in range(0,len(rem_gds_list)):
        try:
            os.remove(rem_gds_list[i])
        except:
            pass
    VERNIER_MAX_Y=VER_ARR_SIZE_SORT_Y()
    gds_arr=glob.glob('./fab1/f1_gdsout/*.gds')
    for i in range(0,len(gds_arr)):
        MAX_X=0
        MAX_Y=0
        gds_name = gds_arr[i].split('\\')[-1][:-4]
        for j in range(0,len(GDS_NAME)):
            if "VERNIER" in gds_name:
                if "VERNIER" in GDS_NAME[j]:
                    MAX_X=MAIN_X[j]
                    MAX_Y=VERNIER_MAX_Y
                    break
            elif "S8000" in gds_name:
                if "S8000" in GDS_NAME[j]:
                    MAX_X=MAIN_X[j]
                    MAX_Y=MAIN_Y[j]
                    break
            elif "OVERLAY" in gds_name:
                if "OVERLAY" in GDS_NAME[j]:
                    MAX_X=MAIN_X[j]
                    MAX_Y=MAIN_Y[j]
                    break
        with open('./fab1/f1_gdsout/'+gds_name+'.KEY', 'w') as f:
            f.write('File_Type                                "GDS"\n')
            f.write('Hotspot_End\n')
            f.write('Version                                  9\n')
            f.write('File                                     "/user/PGWORK/'+PROCESS[0]+'/STD_FRAME/STD_PHOTOKEY/'+gds_name+'.gds"\n')
            f.write('Topstr                                   "'+gds_name+'"\n')
            f.write('BlTopStr                                 "NONE"\n')
            f.write('SizeLay                                  -1\n')
            f.write('SizeDT                                   -1\n')
            f.write('Strip                                    0\n')
            f.write('Missing_OK                               0\n')
            f.write('Snap_OK                                  0\n')
            f.write('Inhibit_Autosize                         0\n')
            f.write('X_Min                                    "0"\n')
            f.write('Y_Min                                    "0"\n')
            f.write('X_Max                                    "'+str(MAX_X)+'"\n')
            f.write('Y_Max                                    "'+str(MAX_Y)+'"\n')
            f.write('SB_Ext                                   0\n')
            f.write('SB_File_Loc                              "NONE"\n')
            f.write('SB_Min_X                                 0\n')
            f.write('SB_Min_Y                                 0\n')
            f.write('SB_Max_X                                 0\n')
            f.write('SB_Max_Y                                 0\n')
            f.write('SB_Align                                 "CC"\n')
            f.write('Comment                                  0\n')
            f.write('End_Processes')


if __name__ == "__main__":
    main()
