import gdstk
import sys,glob,os
from fab1 import S8000_maker
from fab1 import overlay_maker
from fab1 import vernier_maker
from fab1 import external_maker_overlay
import time, tarfile

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
LAY1=[]
LAY2=[]

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
                    GDS_NAME.append(line_sp[1])
                    try:
                        PAD_NO.append(line_sp[2])
                    except:
                        PAD_NO.append("-")
    for i in range(0,len(GDS_NAME)):
        if 'VERNIER' in GDS_NAME[i]:
            LAY1.append(GDS_NAME[i].split('_')[3][:-1])
            LAY2.append(GDS_NAME[i].split('_')[4][:-1])
            LAYER_NO.append("-")
        else:
            LAY1.append("-")
            LAY2.append("-")
            LAYER_NO.append(GDS_NAME[i].split('_')[-1])

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
    global LAY1
    global LAY2
    
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
    LAY1=[]
    LAY2=[]
    
    get_arr()
    # remove input
    rem_file_list = glob.glob('./fab1/*_input')
    rem_file_list1 = glob.glob('./*_input')
    for i in range(0,len(rem_file_list)):
        try:
            os.remove(rem_file_list[i])
        except:
            pass
    for i in range(0,len(rem_file_list1)):
        try:
            os.remove(rem_file_list1[i])
        except:
            pass
    rem_gds_list = glob.glob('./fab1/f1_gdsout/*.gds')
    for i in range(0,len(rem_gds_list)):
        try:
            os.remove(rem_gds_list[i])
        except:
            pass
    rem_gds_list = glob.glob('./fab1/f1_gdsout/*.tar')
    for i in range(0,len(rem_gds_list)):
        try:
            os.remove(rem_gds_list[i])
        except:
            pass
    rem_gds_list = glob.glob('./fab1/f1_gdsout/*.KEY')
    for i in range(0,len(rem_gds_list)):
        try:
            os.remove(rem_gds_list[i])
        except:
            pass
    # make input
    for i in range(0,len(GDS_NAME)):
        if "S8000" in GDS_NAME[i]:
            if glob.glob("./fab1/s8000_input"):
                with open("./fab1/s8000_input", "a", encoding="utf8") as f:
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+'\n')
            else:
                with open("./fab1/s8000_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+'\n')
        elif "OVERLAY" in GDS_NAME[i]:
            if glob.glob("./fab1/1st_overlay_input"):
                with open("./fab1/1st_overlay_input", "a", encoding="utf8") as f:
                    
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+'\n')
            else:
                with open("./fab1/1st_overlay_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+'\n')
        elif "VERNIER" in GDS_NAME[i]:
            if glob.glob("./fab1/vernier_input"):
                with open("./fab1/vernier_input", "a", encoding="utf8") as f:
                    f.write(PRORITY[i]+' '+LAY1[i]+' '+LAY2[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+'\n')
            else:
                with open("./fab1/vernier_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAY1[i]+' '+LAY2[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+'\n')
    
    # 프로그램 실행
    if glob.glob("./fab1/s8000_input"):
        S8000_maker.start()
    if glob.glob("./fab1/1st_overlay_input"):
        overlay_maker.start()
    if glob.glob("./fab1/vernier_input"):
        vernier_maker.start()

    external_maker_overlay.main()

    gds_list = glob.glob("./fab1/f1_gdsout/*.gds")
    key_list = glob.glob("./fab1/f1_gdsout/*.KEY")
    for i in range(0,len(key_list)):
        gds_list.append(key_list[i])
    tar = tarfile.open("./fab1/f1_gdsout/"+str(PROCESS[0]) +"_OVERLAY_Web_"+ time.strftime("%Y%m%d") + ".tar", "w")
    for name in gds_list:
        tar.add(name)
    tar.close()
    return ("./fab1/f1_gdsout/"+str(PROCESS[0]) +"_OVERLAY_Web_"+ time.strftime("%Y%m%d") + ".tar")


if __name__ == "__main__":
    main()