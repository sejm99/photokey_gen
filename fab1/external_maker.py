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
HOT_SPOT_NAME=[]

def get_arr(input_file):
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
    global HOT_SPOT_NAME
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
    HOT_SPOT_NAME=[]
    
    #input 파일 정보 가져오기
    with open(input_file,'r') as f:
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
                    HOT_SPOT_NAME.append(line_sp[4])
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

def center_x_asml(GDS,P,MX,offset):
    result = ""
    for i in range(1,3):
        for j in range(1,5):
            if "_"+str(i)+"_"+str(j)+"_" in GDS:
                result = float(15 + (int(MX)/2))+ float(offset)
                break
        if result == "":
            if PROCESS[0] == "0600SJ00BB":
                if "_"+str(i)+"_" in GDS:
                    if i == 1:
                        result = float(int(P)*(15+int(MX)+50) - (50 + (int(MX)/2))) + float(offset)
                        break
                    else:
                        result = float((int(P)-3)*(15+int(MX)+50) - (50 + (int(MX)/2)))+ float(offset)
                        break
        else:
            break
    if result == "":
        result = float(int(P)*(15+int(MX)+50) - (50 + (int(MX)/2))) + float(offset)
    if ".0" in str(result):
        result = str(result).split(".0")[0]
    else:
        result = str(result)
    return result
def center_x(X,MX,offset):
    result = float(X + 15 + (int(MX)/2)) + float(offset)
    if ".0" in str(result):
        result = str(result).split(".0")[0]
    else:
        result = str(result)
    return result
def PRO_ARR_SIZE_SORT_X():
    #PRORITY 별 최대 Size 찾기 - X
    ARR_SIZE_PRE=[]
    ARR_DEL=[]
    for i in range(0,len(PRORITY)):
        if int(PRORITY[i]) < 10:
            if '0'+PRORITY[i]+"_"+MAIN_X[i] in ARR_SIZE_PRE:
                pass
            else:
                ARR_SIZE_PRE.append('0'+PRORITY[i]+"_"+MAIN_X[i])
        else:
            if PRORITY[i]+"_"+MAIN_X[i] in ARR_SIZE_PRE:
                pass
            else:
                ARR_SIZE_PRE.append(PRORITY[i]+"_"+MAIN_X[i])
    for i in range(0,len(ARR_SIZE_PRE)):
        for j in range(0,len(ARR_SIZE_PRE)):
            if i == j:
                pass
            else:
                if ARR_SIZE_PRE[i][:2] == ARR_SIZE_PRE[j][:2]:
                    if float(ARR_SIZE_PRE[i].split("_")[-1]) > float(ARR_SIZE_PRE[j].split("_")[-1]):
                        ARR_DEL.append(ARR_SIZE_PRE[j])
                    else:
                        ARR_DEL.append(ARR_SIZE_PRE[i])
    for i in range(0,len(ARR_DEL)):
        try:
            ARR_SIZE_PRE.remove(ARR_DEL[i])
        except:
            pass
    ARR_SIZE_PRE.sort(key=lambda x:(x[0],x[1]))
    #빈공간 채우기
    for i in range(1, int(ARR_SIZE_PRE[-1].split("_")[0])):
        st_ck=0
        for j in range(0,len(ARR_SIZE_PRE)):
            if "0"+str(i)+"_" in ARR_SIZE_PRE[j]:
                st_ck=1
                break
            else:
                pass
        if st_ck == 0:
            ARR_SIZE_PRE.append("0"+str(i)+"_"+ARR_SIZE_PRE[0].split("_")[-1])
    
    ARR_SIZE_PRE.sort(key=lambda x:(x[0],x[1]))
    return ARR_SIZE_PRE

def PRO_ARR_SIZE_SORT_Y():
    #PRORITY 별 최대 Size 찾기 - Y
    ARR_SIZE_PRE=[]
    ARR_DEL=[]
    for i in range(0,len(PRORITY)):
        if int(PRORITY[i]) < 10:
            if '0'+PRORITY[i]+"_"+MAIN_Y[i] in ARR_SIZE_PRE:
                pass
            else:
                ARR_SIZE_PRE.append('0'+PRORITY[i]+"_"+MAIN_Y[i])
        else:
            if PRORITY[i]+"_"+MAIN_Y[i] in ARR_SIZE_PRE:
                pass
            else:
                ARR_SIZE_PRE.append(PRORITY[i]+"_"+MAIN_Y[i])
    for i in range(0,len(ARR_SIZE_PRE)):
        for j in range(0,len(ARR_SIZE_PRE)):
            if i == j:
                pass
            else:
                if ARR_SIZE_PRE[i][:2] == ARR_SIZE_PRE[j][:2]:
                    if float(ARR_SIZE_PRE[i].split("_")[-1]) > float(ARR_SIZE_PRE[j].split("_")[-1]):
                        ARR_DEL.append(ARR_SIZE_PRE[j])
                    else:
                        ARR_DEL.append(ARR_SIZE_PRE[i])
    for i in range(0,len(ARR_DEL)):
        try:
            ARR_SIZE_PRE.remove(ARR_DEL[i])
        except:
            pass
    ARR_SIZE_PRE.sort(key=lambda x:(x[0],x[1]))
    #빈공간 채우기
    for i in range(1, int(ARR_SIZE_PRE[-1].split("_")[0])):
        st_ck=0
        for j in range(0,len(ARR_SIZE_PRE)):
            if "0"+str(i)+"_" in ARR_SIZE_PRE[j]:
                st_ck=1
                break
            else:
                pass
        if st_ck == 0:
            ARR_SIZE_PRE.append("0"+str(i)+"_"+ARR_SIZE_PRE[0].split("_")[-1])
    
    ARR_SIZE_PRE.sort(key=lambda x:(x[0],x[1]))
    return ARR_SIZE_PRE
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
    global ETCH_TYPE
    global MAIN_X
    global MAIN_Y
    global BAR_X
    global BAR_Y
    global ARR_X
    global ARR_Y
    global HOT_SPOT_NAME
    
    rem_gds_list = glob.glob('./fab1/f1_gdsout/*.KEY')
    for i in range(0,len(rem_gds_list)):
        try:
            os.remove(rem_gds_list[i])
        except:
            pass

    NIKON_KEY = glob.glob("./fab1/fia*_input")
    NIKON_KEY.append(glob.glob("./fab1/wg*_z_input")[0])
    NIKON_KEY.append(glob.glob("./fab1/lsa*_input")[0])
    # NIKON 가로 긴거
    for j in range(0,len(NIKON_KEY)):
        if NIKON_KEY[j] == "":
            pass
        else:
            get_arr(NIKON_KEY[j])
            ARR_SIZE_X = PRO_ARR_SIZE_SORT_X()
            X_Max = 0
            for i in range(0,len(ARR_SIZE_X)):
                X_Max = int(X_Max) + int(ARR_SIZE_X[i].split('_')[-1]) + 65
            if "wga_z" in NIKON_KEY[j]:
                gds_name = glob.glob("./fab1/f1_gdsout/*WGAZ_*.gds")[0].split('\\')[-1][:-4]
            elif "lsa_" in NIKON_KEY[j]:
                gds_name = glob.glob("./fab1/f1_gdsout/*LSA_*.gds")[0].split('\\')[-1][:-4]
            elif "fia_2d_" in NIKON_KEY[j]:
                gds_name = glob.glob("./fab1/f1_gdsout/*FIA_2D_*.gds")[0].split('\\')[-1][:-4]
            elif "fia_s2_" in NIKON_KEY[j]:
                gds_name = glob.glob("./fab1/f1_gdsout/*FIA_S2_*.gds")[0].split('\\')[-1][:-4]
            else:
                gds_name = glob.glob("./fab1/f1_gdsout/*FIA_50*.gds")[0].split('\\')[-1][:-4]
            with open("./fab1/f1_gdsout/"+gds_name+'.KEY', 'w') as f:
                f.write('File_Type                                "GDS"\n')
                for i in range(0, len(PRORITY)):
                    f.write('Hotspot_Name                             "'+str(HOT_SPOT_NAME[i])+'"\n')
                    # MAIN_X[i] 이전까지의 Size 합
                    pre_size = 0
                    for j in range(0,len(ARR_SIZE_X)):
                        pre_prio = ARR_SIZE_X[j].split("_")[0]
                        pre_x=ARR_SIZE_X[j].split("_")[1]
                        if int(PRORITY[i]) == "01" or int(pre_prio) == int(PRORITY[i]):
                            break
                        else:
                            pre_size = float(pre_size + (15+float(pre_x)+50))
                    f.write('Hotspot_X                                "'+str(center_x(pre_size,MAIN_X[i],0))+'"\n')
                    if "WGA_Z" in GDS_NAME[i]:
                        f.write('Hotspot_Y                                "28"\n')
                    else:
                        f.write('Hotspot_Y                                "25"\n')
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
                f.write('X_Max                                    "'+str(X_Max)+'"\n')
                f.write('Y_Max                                    "50"\n')
                f.write('SB_Ext                                   0\n')
                f.write('SB_File_Loc                              "NONE"\n')
                f.write('SB_Min_X                                 0\n')
                f.write('SB_Min_Y                                 0\n')
                f.write('SB_Max_X                                 0\n')
                f.write('SB_Max_Y                                 0\n')
                f.write('SB_Align                                 "CC"\n')
                f.write('Comment                                  0\n')
                f.write('End_Processes')
    if glob.glob("./fab1/wga_x_input"):
        get_arr('./fab1/wga_x_input')
        ARR_SIZE_Y = PRO_ARR_SIZE_SORT_Y()
        #X_Max = 0
        Y_Max = 0
        for i in range(0,len(ARR_SIZE_Y)):
            Y_Max = int(Y_Max) + int(ARR_SIZE_Y[i].split('_')[-1]) + 65
        gds_name = glob.glob("./fab1/f1_gdsout/*WGAX_*.gds")[0].split('\\')[-1][:-4]
        with open("./fab1/f1_gdsout/"+gds_name+'.KEY', 'w') as f:
            f.write('File_Type                                "GDS"\n')
            for i in range(0, len(PRORITY)):
                if "WGA_X" in GDS_NAME[i]:
                    f.write('Hotspot_Name                             "'+str(HOT_SPOT_NAME[i])+'"\n')
                    f.write('Hotspot_X                                "22"\n')
                    # MAIN_X[i] 이전까지의 Size 합
                    pre_size = 0
                    for j in range(0,len(ARR_SIZE_Y)):
                        pre_prio = ARR_SIZE_Y[j].split("_")[0]
                        pre_x=ARR_SIZE_Y[j].split("_")[1]
                        if int(PRORITY[i]) == "01" or int(pre_prio) == int(PRORITY[i]):
                            break
                        else:
                            pre_size = float(pre_size + (15+float(pre_x)+50))
                    f.write('Hotspot_Y                                "'+str(center_x(pre_size,MAIN_Y[i],0))+'"\n')
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
            f.write('X_Max                                    "50"\n')
            f.write('Y_Max                                    "'+str(Y_Max)+'"\n')
            f.write('SB_Ext                                   0\n')
            f.write('SB_File_Loc                              "NONE"\n')
            f.write('SB_Min_X                                 0\n')
            f.write('SB_Min_Y                                 0\n')
            f.write('SB_Max_X                                 0\n')
            f.write('SB_Max_Y                                 0\n')
            f.write('SB_Align                                 "CC"\n')
            f.write('Comment                                  0\n')
            f.write('End_Processes')

    # BD18(FDOT:DOT53+SPM53_S), XH18(FDOT:DOT53+AA157+SPM53_S),(SPM53:SPM53+SPM11)
    # BD18,BD15,XH18 전체 분리, SJ 2개 분리
    if glob.glob("./fab1/fdot_input"):
        os.remove("./fab1/fdot_input")
    if glob.glob("./fab1/spm53_re_input"):
        os.remove("./fab1/spm53_re_input")
    # make input
    get_arr("./fab1/input")
    if PROCESS[0] == "1830AN18BA" or PROCESS[0] == "181ABD18BA":
        for i in range(0,len(GDS_NAME)):
            if "DOT53" in GDS_NAME[i]:
                if glob.glob("./fab1/fdot_input"):
                    with open("./fab1/fdot_input", "a", encoding="utf8") as f:
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                else:
                    with open("./fab1/fdot_input", "w", encoding="utf8") as f:
                        f.write("PROCESS "+PROCESS[0]+'\n')
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            if "SPM53" in GDS_NAME[i]:
                if BAR_X[i] == "2.2":
                    if glob.glob("./fab1/fdot_input"):
                        with open("./fab1/fdot_input", "a", encoding="utf8") as f:
                            f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                    else:
                        with open("./fab1/fdot_input", "w", encoding="utf8") as f:
                            f.write("PROCESS "+PROCESS[0]+'\n')
                            f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                else:
                    if glob.glob("./fab1/spm53_re_input"):
                        with open("./fab1/spm53_re_input", "a", encoding="utf8") as f:
                            f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                    else:
                        with open("./fab1/spm53_re_input", "w", encoding="utf8") as f:
                            f.write("PROCESS "+PROCESS[0]+'\n')
                            f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            if PROCESS[0] == "181ABD18BA":
                if "AA157" in GDS_NAME[i]:
                    if glob.glob("./fab1/fdot_input"):
                        with open("./fab1/fdot_input", "a", encoding="utf8") as f:
                            f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                    else:
                        with open("./fab1/fdot_input", "w", encoding="utf8") as f:
                            f.write("PROCESS "+PROCESS[0]+'\n')
                            f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
    if PROCESS[0] == "181ABD18BA":
        for i in range(0,len(GDS_NAME)):
            if "SPM11" in GDS_NAME[i]:
                if glob.glob("./fab1/spm53_re_input"):
                    with open("./fab1/spm53_re_input", "a", encoding="utf8") as f:
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                else:
                    with open("./fab1/spm53_re_input", "w", encoding="utf8") as f:
                        f.write("PROCESS "+PROCESS[0]+'\n')
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        '''
            if "SPM53" in GDS_NAME[i]:
                if BAR_X[i] != "2.2":
                    if glob.glob("./fab1/spm53_re_input"):
                        with open("./fab1/spm53_re_input", "a", encoding="utf8") as f:
                            f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                    else:
                        with open("./fab1/spm53_re_input", "w", encoding="utf8") as f:
                            f.write("PROCESS "+PROCESS[0]+'\n')
                            f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        '''
    ASML_KEY=[]
    if PROCESS[0] == "181ABD18BA":
        if glob.glob("./fab1/fdo*_input"):
            ASML_KEY.append(glob.glob("./fab1/fdo*_input")[0])
        if glob.glob("./fab1/spm*_re_input"):
            ASML_KEY.append(glob.glob("./fab1/spm*_re_input")[0])
    elif PROCESS[0] == "1830AN18BA":
        if glob.glob("./fab1/fdo*_input"):
            ASML_KEY.append(glob.glob("./fab1/fdo*_input")[0])
        if glob.glob("./fab1/spm*_re_input"):
            ASML_KEY.append(glob.glob("./fab1/spm*_re_input")[0])
    elif PROCESS[0] == "1830BD15BA":
        if len(glob.glob("./fab1/*SPM*_input")) > 1 :
            spm_list=glob.glob("./fab1/*SPM*_input")
            for i in range(0,len(spm_list)):
                ASML_KEY.append(spm_list[i])
        else:
            ASML_KEY.append(glob.glob("./fab1/*SPM*_input")[0])
        if glob.glob("./fab1/dot*_input"):
            ASML_KEY.append(glob.glob("./fab1/dot*_input")[0])
        if glob.glob("./fab1/thin*_input"):
            ASML_KEY.append(glob.glob("./fab1/thin*_input")[0])
    elif PROCESS[0] == "0600SJ00BB" or PROCESS[0] == "0650SJ00BD":
        if len(glob.glob("./fab1/*SPM*_input")) > 1 :
            spm_list=glob.glob("./fab1/*SPM*_input")
            for i in range(0,len(spm_list)):
                ASML_KEY.append(spm_list[i])
        else:
            ASML_KEY.append(glob.glob("./fab1/*SPM*_input")[0])
        if glob.glob("./fab1/dot*_input"):
            ASML_KEY.append(glob.glob("./fab1/dot*_input")[0])
        if glob.glob("./fab1/thin*_input"):
            ASML_KEY.append(glob.glob("./fab1/thin*_input")[0])
        if glob.glob("./fab1/aa15*_input"):
            ASML_KEY.append(glob.glob("./fab1/aa15*_input")[0])
    else:
        if len(glob.glob("./fab1/*SPM*_input")) > 1 :
            spm_list=glob.glob("./fab1/*SPM*_input")
            for i in range(0,len(spm_list)):
                ASML_KEY.append(spm_list[i])
        else:
            ASML_KEY.append(glob.glob("./fab1/*SPM*_input")[0])
        if glob.glob("./fab1/dot*_input"):
            ASML_KEY.append(glob.glob("./fab1/dot*_input")[0])
        if glob.glob("./fab1/thin*_input"):
            ASML_KEY.append(glob.glob("./fab1/thin*_input")[0])
        if glob.glob("./fab1/aa15*_input"):
            ASML_KEY.append(glob.glob("./fab1/aa15*_input")[0])

    for j in range(0,len(ASML_KEY)):
        if ASML_KEY[j] == "":
            pass
        else:
            get_arr(ASML_KEY[j])
            ARR_SIZE_X = PRO_ARR_SIZE_SORT_X()
            X_Max = 0
            X_Max_1 = 0
            X_Max_2 = 0
            for i in range(0,len(ARR_SIZE_X)):
                X_Max = int(X_Max) + int(ARR_SIZE_X[i].split('_')[-1]) + 65
                if int(ARR_SIZE_X[i].split('_')[0]) < 4:
                    #X_Max_1 = int(X_Max) + int(ARR_SIZE_X[i].split('_')[-1]) + 65
                    X_Max_1 = int(X_Max_1) + int(ARR_SIZE_X[i].split('_')[-1]) + 65
                else:
                    #X_Max_2 = int(X_Max) + int(ARR_SIZE_X[i].split('_')[-1]) + 65
                    X_Max_2 = int(X_Max_2) + int(ARR_SIZE_X[i].split('_')[-1]) + 65
            
            if "spm53" in ASML_KEY[j]:
                if "sspm53" in ASML_KEY[j]:
                    for k in range(0,9):
                        if glob.glob("./fab1/f1_gdsout/*SSPM53_*.gds"):
                            gds_all = glob.glob("./fab1/f1_gdsout/*SSPM53_*.gds")
                else:
                    for k in range(0,9):
                        if glob.glob("./fab1/f1_gdsout/*_SPM53_*.gds"):
                            gds_all = glob.glob("./fab1/f1_gdsout/*_SPM53_*.gds")
            elif "spm11" in ASML_KEY[j]:
                for k in range(0,9):
                    if glob.glob("./fab1/f1_gdsout/*SPM11_*.gds"):
                        gds_all = glob.glob("./fab1/f1_gdsout/*SPM11_*.gds")
            elif "thin32" in ASML_KEY[j]:
                for k in range(0,9):
                    if glob.glob("./fab1/f1_gdsout/*THIN32_*.gds"):
                        gds_all = glob.glob("./fab1/f1_gdsout/*THIN32_*.gds")
            elif "dot53" in ASML_KEY[j]:
                for k in range(0,9):
                    if glob.glob("./fab1/f1_gdsout/*DOT53_*.gds"):
                        gds_all = glob.glob("./fab1/f1_gdsout/*DOT53_*.gds")
            elif "aa157" in ASML_KEY[j]:
                for k in range(0,9):
                    if glob.glob("./fab1/f1_gdsout/*AA157_*.gds"):
                        gds_all = glob.glob("./fab1/f1_gdsout/*AA157_*.gds")
            elif "fdot" in ASML_KEY[j]:
                for k in range(0,9):
                    if glob.glob("./fab1/f1_gdsout/*FDOT_*.gds"):
                        gds_all = glob.glob("./fab1/f1_gdsout/*FDOT_*.gds")
            for k in range(0,len(gds_all)):
                gds_name = gds_all[k].split('\\')[-1][:-4]
                with open("./fab1/f1_gdsout/"+gds_name+'.KEY', 'w') as f:
                    f.write('File_Type                                "GDS"\n')
                    for i in range(0, len(PRORITY)):
                        if PROCESS[0] == "0600SJ00BB" :
                            if "_1_" in gds_name:
                                if int(PRORITY[i]) < 4:
                                    f.write('Hotspot_Name                             "'+str(HOT_SPOT_NAME[i])+'"\n')
                                    if "aa157" in ASML_KEY[j]:
                                        f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0.9))+'"\n')
                                    else:
                                        f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0))+'"\n')
                                    f.write('Hotspot_Y                                "25"\n')
                            elif "_2_" in gds_name:
                                if int(PRORITY[i]) > 3:
                                    f.write('Hotspot_Name                             "'+str(HOT_SPOT_NAME[i])+'"\n')
                                    if "aa157" in ASML_KEY[j]:
                                        f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0.9))+'"\n')
                                    else:
                                        f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0))+'"\n')
                                    f.write('Hotspot_Y                                "25"\n')
                        elif PROCESS[0] == "0650SJ00BD":
                            for o in range(1,9):
                                if "_1_"+str(o)+"_" in gds_name:
                                    if PRORITY[i] == str(o):
                                        f.write('Hotspot_Name                             "'+str(HOT_SPOT_NAME[i])+'"\n')
                                        if "aa157" in ASML_KEY[j]:
                                            f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0.9))+'"\n')
                                        else:
                                            f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0))+'"\n')
                                        f.write('Hotspot_Y                                "25"\n')
                                        break
                                elif "_2_"+str(o-2)+"_" in gds_name:
                                    if PRORITY[i] == str(o):
                                        f.write('Hotspot_Name                             "'+str(HOT_SPOT_NAME[i])+'"\n')
                                        if "aa157" in ASML_KEY[j]:
                                            f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0.9))+'"\n')
                                        else:
                                            f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0))+'"\n')
                                        f.write('Hotspot_Y                                "25"\n')
                                        break
                        else:
                            for o in range(1,9):
                                if "_1_"+str(o)+"_" in gds_name:
                                    if PRORITY[i] == str(o):
                                        f.write('Hotspot_Name                             "'+str(HOT_SPOT_NAME[i])+'"\n')
                                        if PROCESS[0] == "181ABD18BA" and "fdot" in ASML_KEY[j]:
                                            if LAYER_NO[i] == "77" or LAYER_NO[i] == "78" or LAYER_NO[i] == "55":
                                                f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0.9))+'"\n')
                                            else:
                                                f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0))+'"\n')
                                        else:
                                            if "aa157" in ASML_KEY[j]:
                                                f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0.9))+'"\n')
                                            else:
                                                f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0))+'"\n')
                                        f.write('Hotspot_Y                                "25"\n')
                                        break
                                elif "_2_"+str(o-3)+"_" in gds_name:
                                    if PRORITY[i] == str(o):
                                        f.write('Hotspot_Name                             "'+str(HOT_SPOT_NAME[i])+'"\n')
                                        if PROCESS[0] == "181ABD18BA" and "fdot" in ASML_KEY[j]:
                                            if LAYER_NO[i] == "77" or LAYER_NO[i] == "78" or LAYER_NO[i] == "55":
                                                f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0.9))+'"\n')
                                            else:
                                                f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0))+'"\n')
                                        else:
                                            if "aa157" in ASML_KEY[j]:
                                                f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0.9))+'"\n')
                                            else:
                                                f.write('Hotspot_X                                "'+str(center_x_asml(gds_name,PRORITY[i],MAIN_X[i],0))+'"\n')
                                        f.write('Hotspot_Y                                "25"\n')
                                        break
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
                    if PROCESS[0] == "0600SJ00BB":
                        if "_1_" in gds_name:
                            f.write('X_Max                                    "'+str(X_Max_1)+'"\n')
                        elif "_2_" in gds_name:
                            f.write('X_Max                                    "'+str(X_Max_2)+'"\n')
                    elif PROCESS[0] == "0650SJ00BD":
                        for o in range(1,9):
                            if "_1_"+str(o)+"_" in gds_name:
                                f.write('X_Max                                    "'+str(int(ARR_SIZE_X[o-1].split('_')[-1])+65)+'"\n')
                            elif "_2_"+str(o-2)+"_" in gds_name:
                                f.write('X_Max                                    "'+str(int(ARR_SIZE_X[o-1].split('_')[-1])+65)+'"\n')
                    else:
                        for o in range(1,9):
                            if "_1_"+str(o)+"_" in gds_name:
                                f.write('X_Max                                    "'+str(int(ARR_SIZE_X[o-1].split('_')[-1])+65)+'"\n')
                            elif "_2_"+str(o-3)+"_" in gds_name:
                                f.write('X_Max                                    "'+str(int(ARR_SIZE_X[o-1].split('_')[-1])+65)+'"\n')
                    f.write('Y_Max                                    "50"\n')
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
