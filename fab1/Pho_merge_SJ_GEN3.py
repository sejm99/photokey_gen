import gdstk
import sys, time
import numpy as np
import glob,os
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

def get_arr():
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
                    LAYER_NO.append(line_sp[1])
                    GDS_NAME.append(line_sp[2])
                    PAD_NO.append(line_sp[3])
                    ETCH_TYPE.append(line_sp[2].split('_')[-1])
                    if line_sp[2].split('_')[0] == "LSA":
                        ARR_Y.append(line_sp[2].split('_')[-2])
                        ARR_X.append(line_sp[2].split('_')[-3])
                        BAR_Y.append(line_sp[2].split('_')[-5]+'.'+line_sp[2].split('_')[-4])
                        BAR_X.append(line_sp[2].split('_')[-7]+'.'+line_sp[2].split('_')[-6])
                        MAIN_Y.append(line_sp[2].split('_')[-8])
                        MAIN_X.append(line_sp[2].split('_')[-9])
                    else:
                        BAR_Y.append(line_sp[2].split('_')[-3]+'.'+line_sp[2].split('_')[-2])
                        BAR_X.append(line_sp[2].split('_')[-5]+'.'+line_sp[2].split('_')[-4])
                        MAIN_Y.append(line_sp[2].split('_')[-6])
                        MAIN_X.append(line_sp[2].split('_')[-7])

def start():
    cell = None
    res = None
    res1 = None
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
    get_arr()
 
    gds_pre = glob.glob("./fab1/f1_gdsout/pre_*.gds")
    for i in range(0,len(gds_pre)):
        re_gds_name=gds_pre[i].replace("pre_","")
        if glob.glob(gds_pre[i]):
            os.rename(gds_pre[i],re_gds_name)
    rem_file_list = glob.glob('./fab1/f1_gdsout/pre_*.gds')
    for i in range(0,len(rem_file_list)):
        try:
            os.remove(rem_file_list[i])
        except:
            pass

if __name__ == "__main__":
    start()