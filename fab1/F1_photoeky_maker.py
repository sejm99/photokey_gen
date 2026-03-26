import gdstk
import sys,glob,os
from fab1 import Pho_merge_SJ, Pho_merge_SJ_GEN3,wga_z_maker,wga_x_maker, fia_s2_maker, fia_maker,fia_2d_maker, lsa_maker
from fab1 import spm53_maker, dot53_maker, thin32_maker, sspm53_maker, spm11_maker, aa157_maker
from fab1 import Pho_merge, external_maker
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
HOT_SPOT_NAME=[]

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
                    HOT_SPOT_NAME.append(line_sp[4])
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
    # remove input
    rem_file_list = glob.glob('./fab1/*_input')
    for i in range(0,len(rem_file_list)):
        try:
            os.remove(rem_file_list[i])
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
        if "WGA_Z" in GDS_NAME[i]:
            if glob.glob("./fab1/wga_z_input"):
                with open("./fab1/wga_z_input", "a", encoding="utf8") as f:
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            else:
                with open("./fab1/wga_z_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        elif "WGA_X" in GDS_NAME[i]:
            if glob.glob("./fab1/wga_x_input"):
                with open("./fab1/wga_x_input", "a", encoding="utf8") as f:
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            else:
                with open("./fab1/wga_x_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        elif "WGA_S_Z" in GDS_NAME[i]:
            if glob.glob("./fab1/wga_sz_input"):
                with open("./fab1/wga_sz_input", "a", encoding="utf8") as f:
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            else:
                with open("./fab1/wga_sz_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        elif "WGA_S_X" in GDS_NAME[i]:
            if glob.glob("./fab1/wga_sx_input"):
                with open("./fab1/wga_sx_input", "a", encoding="utf8") as f:
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            else:
                with open("./fab1/wga_sx_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        elif "DOT53" in GDS_NAME[i]:
            if glob.glob("./fab1/dot53_input"):
                with open("./fab1/dot53_input", "a", encoding="utf8") as f:
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            else:
                with open("./fab1/dot53_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        elif "SPM53" in GDS_NAME[i]:
            if "SSPM53" in GDS_NAME[i]:
                if glob.glob("./fab1/sspm53_input"):
                    with open("./fab1/sspm53_input", "a", encoding="utf8") as f:
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                else:
                    with open("./fab1/sspm53_input", "w", encoding="utf8") as f:
                        f.write("PROCESS "+PROCESS[0]+'\n')
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            else:
                if glob.glob("./fab1/spm53_input"):
                    with open("./fab1/spm53_input", "a", encoding="utf8") as f:
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                else:
                    with open("./fab1/spm53_input", "w", encoding="utf8") as f:
                        f.write("PROCESS "+PROCESS[0]+'\n')
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        elif "AA157" in GDS_NAME[i]:
            if glob.glob("./fab1/aa157_input"):
                with open("./fab1/aa157_input", "a", encoding="utf8") as f:
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            else:
                with open("./fab1/aa157_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        elif "SPM11" in GDS_NAME[i]:
            if glob.glob("./fab1/spm11_input"):
                with open("./fab1/spm11_input", "a", encoding="utf8") as f:
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            else:
                with open("./fab1/spm11_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        elif "THIN32" in GDS_NAME[i]:
            if glob.glob("./fab1/thin32_input"):
                with open("./fab1/thin32_input", "a", encoding="utf8") as f:
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            else:
                with open("./fab1/thin32_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        elif "LSA" in GDS_NAME[i]:
            if glob.glob("./fab1/lsa_input"):
                with open("./fab1/lsa_input", "a", encoding="utf8") as f:
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            else:
                with open("./fab1/lsa_input", "w", encoding="utf8") as f:
                    f.write("PROCESS "+PROCESS[0]+'\n')
                    f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
        elif "FIA" in GDS_NAME[i]:
            if "FIA_2D" in GDS_NAME[i]:
                if glob.glob("./fab1/fia_2d_input"):
                    with open("./fab1/fia_2d_input", "a", encoding="utf8") as f:
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                else:
                    with open("./fab1/fia_2d_input", "w", encoding="utf8") as f:
                        f.write("PROCESS "+PROCESS[0]+'\n')
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            elif "FIA_S2" in GDS_NAME[i]:
                if glob.glob("./fab1/fia_s2_input"):
                    with open("./fab1/fia_s2_input", "a", encoding="utf8") as f:
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                else:
                    with open("./fab1/fia_s2_input", "w", encoding="utf8") as f:
                        f.write("PROCESS "+PROCESS[0]+'\n')
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
            else:
                if glob.glob("./fab1/fia_input"):
                    with open("./fab1/fia_input", "a", encoding="utf8") as f:
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
                else:
                    with open("./fab1/fia_input", "w", encoding="utf8") as f:
                        f.write("PROCESS "+PROCESS[0]+'\n')
                        f.write(PRORITY[i]+' '+LAYER_NO[i]+' '+GDS_NAME[i]+' '+PAD_NO[i]+' '+HOT_SPOT_NAME[i]+'\n')
    
    # 프로그램 실행
    if glob.glob("./fab1/wga_z_input"):
        wga_z_maker.start()
    if glob.glob("./fab1/wga_x_input"):
        wga_x_maker.start()
    #if glob.glob("./fab1/wga_s_input"):
    #    wga_sx_maker.start()
    if glob.glob("./fab1/dot53_input"):
        dot53_maker.start()
    if glob.glob("./fab1/sspm53_input"):
        sspm53_maker.start()
    if glob.glob("./fab1/spm53_input"):
        spm53_maker.start()
    if glob.glob("./fab1/aa157_input"):
        aa157_maker.start()
    if glob.glob("./fab1/spm11_input"):
        spm11_maker.start()
    if glob.glob("./fab1/thin32_input"):
        thin32_maker.start()
    if glob.glob("./fab1/lsa_input"):
        lsa_maker.start()
    if glob.glob("./fab1/fia_2d_input"):
        fia_2d_maker.start()
    if glob.glob("./fab1/fia_s2_input"):
        fia_s2_maker.start()
    if glob.glob("./fab1/fia_input"):
        fia_maker.start()
    
    # BD15
     # LSA 400,0 FIA2D 400,100 FIAS2 400,200 FIA 400,300 WGAZ 400,400 SPM53 400,500 3045,500 DOT53 400,600 3045,600 SSPM53 400,700 1956,700 4013.994,700 
     # THIN32 400,800 3045,800 6545.264,800 WGAX 400,900
    #BD18
     # LSA 400,0 FIA2D 400,72.019 FIAS2 400,172.019 FIA 400,272.019 WGAZ 400,372.019 SPM53 400,472.019 3045,472.019 FDOTBSPM(DOT53+SPM53_S) 400,572.019 3045,572.019 WGAX 400,872.019
    #XH18
     # LSA 395,0 FIA2D 395,100 FIAS2 395,200 FIA 395,300 WGAZ 395,400 SPM(SPM53+SPM11) 395,500 3176.219,500 FDOTBSPM(DOT53+SPM53_S+AA157) 395,600 3174.478,600 WGAX 395,900
    #GEN2
     # FIA2D 550,0 LSA 550,100 FIA 550,200 FIAS2 550,300 WGAZ 550,400 SPM11 546.979,500 AA157 546.979,600 SPM53 550,700 3195,700 DOT53 550,800 3195,800 SSPM53 500,900 3195,900
     # THIN32  550,1000 3195,1000 WGAX 550,1100
    #GEN3
     # FIAS2 0,0 LSA 0,100 WGAZ 0,200 FIA2D 0,300 FIAS2 0,400 FIA 0,500 SPM53 0,600 2645,600 DOT53 0,700 2645,700 SSPM53 0,800 2645,800 THIN32 0,900 2645,900
     # AA157 765.271,1000 SPM11 765.271,1100 WGAX 265.271,1000 

    # FDOT 병합
    if PROCESS[0] == "1830AN18BA" or PROCESS[0] == "181ABD18BA" or PROCESS[0] == "1830BD15BA":
        Pho_merge.start()
    else:
        if "SJ" in PROCESS[0]:
            if PROCESS[0] == "0650SJ00BD":
                Pho_merge_SJ_GEN3.start()
            else:
                Pho_merge_SJ.start()
        else:
            Pho_merge.start()

    # XOR를 위한 GDS 병합
    lib = gdstk.Library()
    cell = lib.new_cell(PROCESS[0])
    #NIKON
    if glob.glob("./fab1/f1_gdsout/WGA_Z.gds"):
        library=gdstk.read_gds("./fab1/f1_gdsout/WGA_Z.gds")
        cells = library.top_level()
        if PROCESS[0] == "1830BD15BA":
            cell.add(gdstk.Reference(*cells,(400,400)))
        elif PROCESS[0] == "1830AN18BA":
            cell.add(gdstk.Reference(*cells,(400,372.019)))
        elif PROCESS[0] == "181ABD18BA":
            cell.add(gdstk.Reference(*cells,(395,400)))
        elif PROCESS[0] == "0600SJ00BB":
            cell.add(gdstk.Reference(*cells,(550,400)))
        elif PROCESS[0] == "0650SJ00BD":
            cell.add(gdstk.Reference(*cells,(0,200)))
        cell_lib = library.cells
        for j in range(0,len(cell_lib)):
            lib.add(cell_lib[j])
    if glob.glob("./fab1/f1_gdsout/WGA_X.gds"): 
        library=gdstk.read_gds("./fab1/f1_gdsout/WGA_X.gds")
        wga_x_cells = library.top_level()
        if PROCESS[0] == "1830BD15BA":
            cell.add(gdstk.Reference(*wga_x_cells,(400,900)))
        elif PROCESS[0] == "1830AN18BA":
            cell.add(gdstk.Reference(*wga_x_cells,(400,872.019)))
        elif PROCESS[0] == "181ABD18BA":
            cell.add(gdstk.Reference(*wga_x_cells,(395,900)))
        elif PROCESS[0] == "0600SJ00BB":
            cell.add(gdstk.Reference(*wga_x_cells,(550,1100)))
        elif PROCESS[0] == "0650SJ00BD":
            cell.add(gdstk.Reference(*wga_x_cells,(265.271,1000)))
        cell_lib = library.cells
        for j in range(0,len(cell_lib)):
            lib.add(cell_lib[j])
    if glob.glob("./fab1/f1_gdsout/LSA.gds"): 
        library=gdstk.read_gds("./fab1/f1_gdsout/LSA.gds")
        lsa_cells = library.top_level()
        if PROCESS[0] == "1830BD15BA":
            cell.add(gdstk.Reference(*lsa_cells,(400,0)))
        elif PROCESS[0] == "1830AN18BA":
            cell.add(gdstk.Reference(*lsa_cells,(400,0)))
        elif PROCESS[0] == "181ABD18BA":
            cell.add(gdstk.Reference(*lsa_cells,(395,0)))
        elif PROCESS[0] == "0600SJ00BB":
            cell.add(gdstk.Reference(*lsa_cells,(550,100)))
        elif PROCESS[0] == "0650SJ00BD":
            cell.add(gdstk.Reference(*lsa_cells,(0,100)))
        cell_lib = library.cells
        for j in range(0,len(cell_lib)):
            lib.add(cell_lib[j])
    if glob.glob("./fab1/f1_gdsout/FIA.gds"):
        library=gdstk.read_gds("./fab1/f1_gdsout/FIA.gds")
        fia_cells = library.top_level()
        if PROCESS[0] == "1830BD15BA":
            cell.add(gdstk.Reference(*fia_cells,(400,300)))
        elif PROCESS[0] == "1830AN18BA":
            cell.add(gdstk.Reference(*fia_cells,(400,272.019)))
        elif PROCESS[0] == "181ABD18BA":
            cell.add(gdstk.Reference(*fia_cells,(395,300)))
        elif PROCESS[0] == "0600SJ00BB":
            cell.add(gdstk.Reference(*fia_cells,(550,200)))
        elif PROCESS[0] == "0650SJ00BD":
            cell.add(gdstk.Reference(*fia_cells,(0,500)))
        cell_lib = library.cells
        for j in range(0,len(cell_lib)):
            lib.add(cell_lib[j])
    if glob.glob("./fab1/f1_gdsout/FIA_S2.gds"):
        library=gdstk.read_gds("./fab1/f1_gdsout/FIA_S2.gds")
        fia_s2_cells = library.top_level()
        if PROCESS[0] == "1830BD15BA":
            cell.add(gdstk.Reference(*fia_s2_cells,(400,200)))
        elif PROCESS[0] == "1830AN18BA":
            cell.add(gdstk.Reference(*fia_s2_cells,(400,172.019)))
        elif PROCESS[0] == "181ABD18BA":
            cell.add(gdstk.Reference(*fia_s2_cells,(395,200)))
        elif PROCESS[0] == "0600SJ00BB":
            cell.add(gdstk.Reference(*fia_s2_cells,(550,300)))
        elif PROCESS[0] == "0650SJ00BD":
            cell.add(gdstk.Reference(*fia_s2_cells,(0,400)))
        cell_lib = library.cells
        for j in range(0,len(cell_lib)):
            lib.add(cell_lib[j])
    if glob.glob("./fab1/f1_gdsout/FIA_2D.gds"):
        library=gdstk.read_gds("./fab1/f1_gdsout/FIA_2D.gds")
        fia_2d_cells = library.top_level()
        if PROCESS[0] == "1830BD15BA":
            cell.add(gdstk.Reference(*fia_2d_cells,(400,100)))
        elif PROCESS[0] == "1830AN18BA":
            cell.add(gdstk.Reference(*fia_2d_cells,(400,72.019)))
        elif PROCESS[0] == "181ABD18BA":
            cell.add(gdstk.Reference(*fia_2d_cells,(395,100)))
        elif PROCESS[0] == "0600SJ00BB":
            cell.add(gdstk.Reference(*fia_2d_cells,(550,0)))
        elif PROCESS[0] == "0650SJ00BD":
            cell.add(gdstk.Reference(*fia_2d_cells,(0,300)))
        cell_lib = library.cells
        for j in range(0,len(cell_lib)):
            lib.add(cell_lib[j])
    #ASML
    if PROCESS[0] == "0600SJ00BB":
        for i in range(1,3):
            if glob.glob("./fab1/f1_gdsout/AA157_"+str(i)+".gds"): 
                library=gdstk.read_gds("./fab1/f1_gdsout/AA157_"+str(i)+".gds")
                aa157_cells = library.top_level()
                cell.add(gdstk.Reference(*aa157_cells,(546.979,600)))
                cell_lib = library.cells
                for j in range(0,len(cell_lib)):
                    lib.add(cell_lib[j])
            if glob.glob("./fab1/f1_gdsout/SPM11_"+str(i)+".gds"):  
                library=gdstk.read_gds("./fab1/f1_gdsout/SPM11_"+str(i)+".gds")
                spm11_cells = library.top_level()
                cell.add(gdstk.Reference(*spm11_cells,(546.979,500)))
                cell_lib = library.cells
                for j in range(0,len(cell_lib)):
                    lib.add(cell_lib[j])
            if glob.glob("./fab1/f1_gdsout/SPM53_"+str(i)+".gds"):
                library=gdstk.read_gds("./fab1/f1_gdsout/SPM53_"+str(i)+".gds")
                spm53_cells = library.top_level()
                if i == 1:
                    cell.add(gdstk.Reference(*spm53_cells,(550,700)))
                else:
                    cell.add(gdstk.Reference(*spm53_cells,(3195,700)))
                cell_lib = library.cells
                for j in range(0,len(cell_lib)):
                    lib.add(cell_lib[j])
            if glob.glob("./fab1/f1_gdsout/SSPM53_"+str(i)+".gds"): 
                library=gdstk.read_gds("./fab1/f1_gdsout/SSPM53_"+str(i)+".gds")
                sspm53_cells = library.top_level()
                if i == 1:
                    cell.add(gdstk.Reference(*sspm53_cells,(550,900)))
                else:
                    cell.add(gdstk.Reference(*sspm53_cells,(3195,900)))
                cell_lib = library.cells
                for j in range(0,len(cell_lib)):
                    lib.add(cell_lib[j])
            if glob.glob("./fab1/f1_gdsout/DOT53_"+str(i)+".gds"):  
                library=gdstk.read_gds("./fab1/f1_gdsout/DOT53_"+str(i)+".gds")
                dot53_cells = library.top_level()
                if i == 1:
                    cell.add(gdstk.Reference(*dot53_cells,(550,800)))
                else:
                    cell.add(gdstk.Reference(*dot53_cells,(3195,800)))
                cell_lib = library.cells
                for j in range(0,len(cell_lib)):
                    lib.add(cell_lib[j])
            if glob.glob("./fab1/f1_gdsout/THIN32_"+str(i)+".gds"): 
                library=gdstk.read_gds("./fab1/f1_gdsout/THIN32_"+str(i)+".gds")
                thin32_cells = library.top_level()
                if i == 1:
                    cell.add(gdstk.Reference(*thin32_cells,(550,1000)))
                else:
                    cell.add(gdstk.Reference(*thin32_cells,(3195,1000)))
                cell_lib = library.cells
                for j in range(0,len(cell_lib)):
                    lib.add(cell_lib[j])
    elif PROCESS[0] == "0650SJ00BD":
        for i in range(1,10):
            if glob.glob("./fab1/f1_gdsout/AA157_"+str(i)+".gds"): 
                library=gdstk.read_gds("./fab1/f1_gdsout/AA157_"+str(i)+".gds")
                aa157_cells = library.top_level()
                cell.add(gdstk.Reference(*aa157_cells,(0+(865*(i-1)),700)))
                cell_lib = library.cells
                for j in range(0,len(cell_lib)):
                    lib.add(cell_lib[j])
            if glob.glob("./fab1/f1_gdsout/SPM11_"+str(i)+".gds"):  
                library=gdstk.read_gds("./fab1/f1_gdsout/SPM11_"+str(i)+".gds")
                spm11_cells = library.top_level()
                cell.add(gdstk.Reference(*spm11_cells,(0+(865*(i-1)),600)))
                cell_lib = library.cells
                for j in range(0,len(cell_lib)):
                    lib.add(cell_lib[j])
            if glob.glob("./fab1/f1_gdsout/SPM53_"+str(i)+".gds"):
                if i < 3:
                    pass
                else:
                    library=gdstk.read_gds("./fab1/f1_gdsout/SPM53_"+str(i)+".gds")
                    spm53_cells = library.top_level()
                    cell.add(gdstk.Reference(*spm53_cells,(1780+(865*(i-3)),600)))
                    cell_lib = library.cells
                    for j in range(0,len(cell_lib)):
                        lib.add(cell_lib[j])
            if glob.glob("./fab1/f1_gdsout/DOT53_"+str(i)+".gds"):  
                if i < 3:
                    pass
                else:
                    library=gdstk.read_gds("./fab1/f1_gdsout/DOT53_"+str(i)+".gds")
                    dot53_cells = library.top_level()
                    cell.add(gdstk.Reference(*dot53_cells,(1780+(865*(i-3)),700)))
                    cell_lib = library.cells
                    for j in range(0,len(cell_lib)):
                        lib.add(cell_lib[j])
    else:
        if PROCESS[0] == "1830BD15BA":
            for i in range(1,10):
                if glob.glob("./fab1/f1_gdsout/SPM53_"+str(i)+".gds"):
                    library=gdstk.read_gds("./fab1/f1_gdsout/SPM53_"+str(i)+".gds")
                    spm53_cells = library.top_level()
                    if i < 4:
                        cell.add(gdstk.Reference(*spm53_cells,(400+(865*(i-1)),500)))
                    else:
                        cell.add(gdstk.Reference(*spm53_cells,(3045+(865*(i-4)),500)))
                    cell_lib = library.cells
                    for j in range(0,len(cell_lib)):
                        lib.add(cell_lib[j])
            for i in range(1,10):
                if glob.glob("./fab1/f1_gdsout/SSPM53_"+str(i)+".gds"): 
                    library=gdstk.read_gds("./fab1/f1_gdsout/SSPM53_"+str(i)+".gds")
                    sspm53_cells = library.top_level()
                    if i < 4:
                        cell.add(gdstk.Reference(*sspm53_cells,(400+(502*(i-1)),700)))
                    else:
                        cell.add(gdstk.Reference(*sspm53_cells,(1956+(502*(i-4)),700)))
                    cell_lib = library.cells
                    for j in range(0,len(cell_lib)):
                        lib.add(cell_lib[j])
            for i in range(1,10):
                if glob.glob("./fab1/f1_gdsout/DOT53_"+str(i)+".gds"):  
                    library=gdstk.read_gds("./fab1/f1_gdsout/DOT53_"+str(i)+".gds")
                    dot53_cells = library.top_level()
                    if i < 4:
                        cell.add(gdstk.Reference(*dot53_cells,(400+(865*(i-1)),600)))
                    else:
                        cell.add(gdstk.Reference(*dot53_cells,(3045+(865*(i-4)),600)))
                    cell_lib = library.cells
                    for j in range(0,len(cell_lib)):
                        lib.add(cell_lib[j])
            for i in range(1,10):
                if glob.glob("./fab1/f1_gdsout/THIN32_"+str(i)+".gds"): 
                    library=gdstk.read_gds("./fab1/f1_gdsout/THIN32_"+str(i)+".gds")
                    thin32_cells = library.top_level()
                    if i < 4:
                        cell.add(gdstk.Reference(*thin32_cells,(400+(865*(i-1)),800)))
                    else:
                        cell.add(gdstk.Reference(*thin32_cells,(3045+(865*(i-4)),800)))
                    cell_lib = library.cells
                    for j in range(0,len(cell_lib)):
                        lib.add(cell_lib[j])
        if PROCESS[0] == "1830AN18BA" or PROCESS[0] == "181ABD18BA":
            if PROCESS[0] == "1830AN18BA":
                for i in range(1,10):
                    if glob.glob("./fab1/f1_gdsout/SPM53_"+str(i)+".gds"):
                        library=gdstk.read_gds("./fab1/f1_gdsout/SPM53_"+str(i)+".gds")
                        spm53_cells = library.top_level()
                        if i < 4:
                            cell.add(gdstk.Reference(*spm53_cells,(400+(865*(i-1)),472.019)))
                        else:
                            cell.add(gdstk.Reference(*spm53_cells,(3045+(865*(i-4)),472.019)))
                        cell_lib = library.cells
                        for j in range(0,len(cell_lib)):
                            lib.add(cell_lib[j])
            else:
                for i in range(1,10):
                    if glob.glob("./fab1/f1_gdsout/SPM53_SPM11_"+str(i)+".gds"): 
                        library=gdstk.read_gds("./fab1/f1_gdsout/SPM53_SPM11_"+str(i)+".gds")
                        spm_cells = library.top_level()
                        if i < 4:
                            cell.add(gdstk.Reference(*spm_cells,(395+(865*(i-1)),500)))
                        else:
                            cell.add(gdstk.Reference(*spm_cells,(3176.219+(865*(i-4)),500)))
                        cell_lib = library.cells
                        for j in range(0,len(cell_lib)):
                            lib.add(cell_lib[j])
            for i in range(1,10):
                if glob.glob("./fab1/f1_gdsout/FDOT_"+str(i)+".gds"): 
                    library=gdstk.read_gds("./fab1/f1_gdsout/FDOT_"+str(i)+".gds")
                    fdot_cells = library.top_level()
                    if PROCESS[0] == "1830AN18BA":
                        if i < 4:
                            cell.add(gdstk.Reference(*fdot_cells,(400+(865*(i-1)),572.019)))
                        else:
                            cell.add(gdstk.Reference(*fdot_cells,(3045+(865*(i-4)),572.019)))
                    else:
                        if i < 4:
                            cell.add(gdstk.Reference(*fdot_cells,(395+(865*(i-1)),600)))
                        else:
                            cell.add(gdstk.Reference(*fdot_cells,(3174.478+(865*(i-4)),600)))
                    cell_lib = library.cells
                    for j in range(0,len(cell_lib)):
                        lib.add(cell_lib[j])
    lib.write_gds("./fab1/f1_gdsout/"+str(PROCESS[0]) +"_Web_ALL_"+ time.strftime("%Y%m%d") + ".gds")
    # GDS Naming
    if glob.glob("./fab1/f1_gdsout/WGA_Z.gds"):
        gds_name="./fab1/f1_gdsout/WGA_Z.gds"
        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_WGAZ_50_"+time.strftime("%Y%m%d")+".gds"
        os.rename(gds_name,re_gds_name)
    if glob.glob("./fab1/f1_gdsout/WGA_X.gds"):
        gds_name="./fab1/f1_gdsout/WGA_X.gds"
        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_WGAX_50_"+time.strftime("%Y%m%d")+".gds"
        os.rename(gds_name,re_gds_name)
    if glob.glob("./fab1/f1_gdsout/LSA.gds"): 
        gds_name="./fab1/f1_gdsout/LSA.gds"
        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_LSA_50_"+time.strftime("%Y%m%d")+".gds"
        os.rename(gds_name,re_gds_name)
    if glob.glob("./fab1/f1_gdsout/FIA.gds"):
        gds_name="./fab1/f1_gdsout/FIA.gds"
        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_FIA_50_"+time.strftime("%Y%m%d")+".gds"
        os.rename(gds_name,re_gds_name)
    if glob.glob("./fab1/f1_gdsout/FIA_S2.gds"):
        gds_name="./fab1/f1_gdsout/FIA_S2.gds"
        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_FIA_S2_50_"+time.strftime("%Y%m%d")+".gds"
        os.rename(gds_name,re_gds_name)
    if glob.glob("./fab1/f1_gdsout/FIA_2D.gds"):
        gds_name="./fab1/f1_gdsout/FIA_2D.gds"
        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_FIA_2D_50_"+time.strftime("%Y%m%d")+".gds"
        os.rename(gds_name,re_gds_name)

    for i in range(1,10):
        if glob.glob("./fab1/f1_gdsout/AA157_"+str(i)+".gds"):
            gds_name="./fab1/f1_gdsout/AA157_"+str(i)+".gds"
            if PROCESS[0] == "0600SJ00BB":
                re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_AA157_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
            else:
                if PROCESS[0] == "0650SJ00BD":
                    if i < 3:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_AA157_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_AA157_2_"+str(i-2)+"_50_"+time.strftime("%Y%m%d")+".gds"
                else:
                    if i < 4:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_AA157_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_AA157_2_"+str(i-3)+"_50_"+time.strftime("%Y%m%d")+".gds"
            os.rename(gds_name,re_gds_name)
        if glob.glob("./fab1/f1_gdsout/SPM11_"+str(i)+".gds"): 
            gds_name="./fab1/f1_gdsout/SPM11_"+str(i)+".gds"
            if PROCESS[0] == "0600SJ00BB":
                re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM11_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
            else:
                if PROCESS[0] == "0650SJ00BD":
                    if i < 3:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM11_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM11_2_"+str(i-2)+"_50_"+time.strftime("%Y%m%d")+".gds"
                else:
                    if i < 4:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM11_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM11_2_"+str(i-3)+"_50_"+time.strftime("%Y%m%d")+".gds"
            os.rename(gds_name,re_gds_name)
        if glob.glob("./fab1/f1_gdsout/SPM53_"+str(i)+".gds"):
            gds_name="./fab1/f1_gdsout/SPM53_"+str(i)+".gds"
            if PROCESS[0] == "0600SJ00BB":
                re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM53_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
            else:
                if PROCESS[0] == "0650SJ00BD":
                    if i < 3:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM53_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM53_2_"+str(i-2)+"_50_"+time.strftime("%Y%m%d")+".gds"
                else:
                    if i < 4:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM53_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM53_2_"+str(i-3)+"_50_"+time.strftime("%Y%m%d")+".gds"
            os.rename(gds_name,re_gds_name)
        if glob.glob("./fab1/f1_gdsout/SSPM53_"+str(i)+".gds"):
            gds_name="./fab1/f1_gdsout/SSPM53_"+str(i)+".gds"
            if PROCESS[0] == "0600SJ00BB":
                re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SSPM53_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
            else:
                if PROCESS[0] == "0650SJ00BD":
                    if i < 3:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SSPM53_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SSPM53_2_"+str(i-2)+"_50_"+time.strftime("%Y%m%d")+".gds"
                else:
                    if i < 4:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SSPM53_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SSPM53_2_"+str(i-3)+"_50_"+time.strftime("%Y%m%d")+".gds"
            os.rename(gds_name,re_gds_name)
        if glob.glob("./fab1/f1_gdsout/DOT53_"+str(i)+".gds"): 
            gds_name="./fab1/f1_gdsout/DOT53_"+str(i)+".gds"
            if PROCESS[0] == "0600SJ00BB":
                re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_DOT53_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
            else:
                if PROCESS[0] == "0650SJ00BD":
                    if i < 3:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_DOT53_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_DOT53_2_"+str(i-2)+"_50_"+time.strftime("%Y%m%d")+".gds"
                else:
                    if i < 4:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_DOT53_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_DOT53_2_"+str(i-3)+"_50_"+time.strftime("%Y%m%d")+".gds"
            os.rename(gds_name,re_gds_name)
        if glob.glob("./fab1/f1_gdsout/THIN32_"+str(i)+".gds"): 
            gds_name="./fab1/f1_gdsout/THIN32_"+str(i)+".gds"
            if PROCESS[0] == "0600SJ00BB":
                re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_THIN32_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
            else:
                if i < 4:
                    re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_THIN32_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                else:
                    re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_THIN32_2_"+str(i-3)+"_50_"+time.strftime("%Y%m%d")+".gds"
            os.rename(gds_name,re_gds_name)
        if glob.glob("./fab1/f1_gdsout/SPM53_SPM11_"+str(i)+".gds"):
            gds_name="./fab1/f1_gdsout/SPM53_SPM11_"+str(i)+".gds"
            if PROCESS[0] == "0600SJ00BB":
                re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM53_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
            else:
                if PROCESS[0] == "0650SJ00BD":
                    if i < 3:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM53_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM53_2_"+str(i-2)+"_50_"+time.strftime("%Y%m%d")+".gds"
                else:
                    if i < 4:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM53_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_SPM53_2_"+str(i-3)+"_50_"+time.strftime("%Y%m%d")+".gds"
            os.rename(gds_name,re_gds_name)
        if glob.glob("./fab1/f1_gdsout/FDOT_"+str(i)+".gds"):
            gds_name="./fab1/f1_gdsout/FDOT_"+str(i)+".gds"
            if PROCESS[0] == "0600SJ00BB":
                re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_FDOT_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
            else:
                if PROCESS[0] == "0650SJ00BD":
                    if i < 3:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_FDOT_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_FDOT_2_"+str(i-2)+"_50_"+time.strftime("%Y%m%d")+".gds"
                else:
                    if i < 4:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_FDOT_1_"+str(i)+"_50_"+time.strftime("%Y%m%d")+".gds"
                    else:
                        re_gds_name="./fab1/f1_gdsout/"+PROCESS[0]+"_FDOT_2_"+str(i-3)+"_50_"+time.strftime("%Y%m%d")+".gds"
            os.rename(gds_name,re_gds_name)
    
    external_maker.main()

    gds_list = glob.glob("./fab1/f1_gdsout/*.gds")
    key_list = glob.glob("./fab1/f1_gdsout/*.KEY")
    for i in range(0,len(key_list)):
        gds_list.append(key_list[i])
    tar = tarfile.open("./fab1/f1_gdsout/"+str(PROCESS[0]) +"_Web_"+ time.strftime("%Y%m%d") + ".tar", "w")
    for name in gds_list:
        tar.add(name)
    tar.close()
    return ("./fab1/f1_gdsout/"+str(PROCESS[0]) +"_Web_"+ time.strftime("%Y%m%d") + ".tar")

if __name__ == "__main__":
    main()