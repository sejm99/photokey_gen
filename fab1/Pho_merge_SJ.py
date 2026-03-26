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
    #AA157 TEST
    lib1 = gdstk.Library()
    cell1 = lib1.new_cell(PROCESS[0]+"_AA157_1_50_"+time.strftime("%Y%m%d"))
    lib2 = gdstk.Library()
    cell2 = lib2.new_cell(PROCESS[0]+"_AA157_2_50_"+time.strftime("%Y%m%d"))
    lib3 = gdstk.Library()
    cell3 = lib3.new_cell(PROCESS[0]+"_SPM11_1_50_"+time.strftime("%Y%m%d"))
    lib4 = gdstk.Library()
    cell4 = lib4.new_cell(PROCESS[0]+"_SPM11_2_50_"+time.strftime("%Y%m%d"))
    lib5 = gdstk.Library()
    cell5 = lib5.new_cell(PROCESS[0]+"_SPM53_1_50_"+time.strftime("%Y%m%d"))
    lib6 = gdstk.Library()
    cell6 = lib6.new_cell(PROCESS[0]+"_SPM53_2_50_"+time.strftime("%Y%m%d"))
    lib7 = gdstk.Library()
    cell7 = lib7.new_cell(PROCESS[0]+"_SSPM53_1_50_"+time.strftime("%Y%m%d"))
    lib8 = gdstk.Library()
    cell8 = lib8.new_cell(PROCESS[0]+"_SSPM53_2_50_"+time.strftime("%Y%m%d"))
    lib9 = gdstk.Library()
    cell9 = lib9.new_cell(PROCESS[0]+"_THIN32_1_50_"+time.strftime("%Y%m%d"))
    lib10 = gdstk.Library()
    cell10 = lib10.new_cell(PROCESS[0]+"_THIN32_2_50_"+time.strftime("%Y%m%d"))
    lib11 = gdstk.Library()
    cell11 = lib11.new_cell(PROCESS[0]+"_DOT53_1_50_"+time.strftime("%Y%m%d"))
    lib12 = gdstk.Library()
    cell12 = lib12.new_cell(PROCESS[0]+"_DOT53_2_50_"+time.strftime("%Y%m%d"))

    # BD15
     # LAS 400,0 FIA2D 400,100 FIAS2 400,200 FIA 400,300 WGAZ 400,400 SPM53 400,500 3045,500 6539.928,500 DOT53 400,600 3045,600 6544.64,600 SSPM53 400,700 1956,700 4013.994,700 
     # THIN32 400,800 3045,800 6545.264,800 WGAX 400,900
    #GEN2
     # FIA2D 550,0 LSA 550,100 FIA 550,200 FIAS2 550,300 WGAZ 500,400 SPM11 546.979,500 AA157 546.979,600 SPM53 550,700 3195,700 DOT53 550,800 3195,800 SSPM53 500,900 3195,900
     # THIN32  550,1000 3195,1000 WGAX 550,1100
    #GEN3
     # FIAS2 0,0 LSA 0,100 WGAZ 0,200 FIA2D 0,300 FIAS2 0,400 FIA 0,500 SPM53 0,600 2645,600 DOT53 0,700 2645,700 SSPM53 0,800 2645,800 THIN32 0,900 2645,900
     # AA157 765.271,1000 SPM11 765.271,1000 WGAX 265.271,1000 
    if PROCESS[0] == "0600SJ00BB" or PROCESS[0] == "0650SJ00BD":
        #2개 분리
        if glob.glob("./fab1/f1_gdsout/pre_AA157_*.gds"):
            if PROCESS[0] == "0650SJ00BD":
                for i in range(1,3):
                    gds_name="./fab1/f1_gdsout/pre_AA157_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        aa157_cells = library.top_level()
                        cell1.add(gdstk.Reference(*aa157_cells,((i-1)*865,0)))
                        cell_lib1 = library.cells
                        for i in range(0,len(cell_lib1)):
                            lib1.add(cell_lib1[i])
                for i in range(3,9):
                    gds_name="./fab1/f1_gdsout/pre_AA157_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        aa157_cells = library.top_level()
                        cell2.add(gdstk.Reference(*aa157_cells,((i-3)*865,0)))
                        cell_lib2 = library.cells
                        for i in range(0,len(cell_lib2)):
                            lib2.add(cell_lib2[i])
            else:
                for i in range(1,4):
                    gds_name="./fab1/f1_gdsout/pre_AA157_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        aa157_cells = library.top_level()
                        cell1.add(gdstk.Reference(*aa157_cells,((i-1)*865,0)))
                        cell_lib1 = library.cells
                        for i in range(0,len(cell_lib1)):
                            lib1.add(cell_lib1[i])
                for i in range(4,9):
                    gds_name="./fab1/f1_gdsout/pre_AA157_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        aa157_cells = library.top_level()
                        cell2.add(gdstk.Reference(*aa157_cells,((i-4)*865,0)))
                        cell_lib2 = library.cells
                        for i in range(0,len(cell_lib2)):
                            lib2.add(cell_lib2[i])
        if glob.glob("./fab1/f1_gdsout/pre_SPM11_*.gds"):
            if PROCESS[0] == "0650SJ00BD":
                for i in range(1,3):
                    gds_name="./fab1/f1_gdsout/pre_SPM11_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        spm11_cells = library.top_level()
                        cell3.add(gdstk.Reference(*spm11_cells,((i-1)*865,0)))
                        cell_lib3 = library.cells
                        for i in range(0,len(cell_lib3)):
                            lib3.add(cell_lib3[i])
                for i in range(3,9):
                    gds_name="./fab1/f1_gdsout/pre_SPM11_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        spm11_cells = library.top_level()
                        cell4.add(gdstk.Reference(*spm11_cells,((i-3)*865,0)))
                        cell_lib4 = library.cells
                        for i in range(0,len(cell_lib4)):
                            lib4.add(cell_lib4[i])
            else:
                for i in range(1,4):
                    gds_name="./fab1/f1_gdsout/pre_SPM11_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        spm11_cells = library.top_level()
                        cell3.add(gdstk.Reference(*spm11_cells,((i-1)*865,0)))
                        cell_lib3 = library.cells
                        for i in range(0,len(cell_lib3)):
                            lib3.add(cell_lib3[i])
                for i in range(4,9):
                    gds_name="./fab1/f1_gdsout/pre_SPM11_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        spm11_cells = library.top_level()
                        cell4.add(gdstk.Reference(*spm11_cells,((i-4)*865,0)))
                        cell_lib4 = library.cells
                        for i in range(0,len(cell_lib4)):
                            lib4.add(cell_lib4[i])
        if glob.glob("./fab1/f1_gdsout/pre_SPM53_*.gds"):
            if PROCESS[0] == "0650SJ00BD":
                for i in range(1,3):
                    gds_name="./fab1/f1_gdsout/pre_SPM53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        spm53_cells = library.top_level()
                        cell5.add(gdstk.Reference(*spm53_cells,((i-1)*865,0)))
                        cell_lib5 = library.cells
                        for i in range(0,len(cell_lib5)):
                            lib5.add(cell_lib5[i])
                for i in range(3,9):
                    gds_name="./fab1/f1_gdsout/pre_SPM53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        spm53_cells = library.top_level()
                        cell6.add(gdstk.Reference(*spm53_cells,((i-3)*865,0)))
                        cell_lib6 = library.cells
                        for i in range(0,len(cell_lib6)):
                            lib6.add(cell_lib6[i])
            else:
                for i in range(1,4):
                    gds_name="./fab1/f1_gdsout/pre_SPM53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        spm53_cells = library.top_level()
                        cell5.add(gdstk.Reference(*spm53_cells,((i-1)*865,0)))
                        cell_lib5 = library.cells
                        for i in range(0,len(cell_lib5)):
                            lib5.add(cell_lib5[i])
                for i in range(4,9):
                    gds_name="./fab1/f1_gdsout/pre_SPM53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        spm53_cells = library.top_level()
                        cell6.add(gdstk.Reference(*spm53_cells,((i-4)*865,0)))
                        cell_lib6 = library.cells
                        for i in range(0,len(cell_lib6)):
                            lib6.add(cell_lib6[i])
        if glob.glob("./fab1/f1_gdsout/pre_SSPM53_*.gds"):
            if PROCESS[0] == "0650SJ00BD":
                for i in range(1,3):
                    gds_name="./fab1/f1_gdsout/pre_SSPM53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        sspm53_cells = library.top_level()
                        cell7.add(gdstk.Reference(*sspm53_cells,((i-1)*502,0)))
                        cell_lib7 = library.cells
                        for i in range(0,len(cell_lib7)):
                            lib7.add(cell_lib7[i])
                for i in range(3,9):
                    gds_name="./fab1/f1_gdsout/pre_SSPM53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        sspm53_cells = library.top_level()
                        cell8.add(gdstk.Reference(*sspm53_cells,((i-3)*502,0)))
                        cell_lib8 = library.cells
                        for i in range(0,len(cell_lib8)):
                            lib8.add(cell_lib8[i])
            else:
                for i in range(1,4):
                    gds_name="./fab1/f1_gdsout/pre_SSPM53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        sspm53_cells = library.top_level()
                        cell7.add(gdstk.Reference(*sspm53_cells,((i-1)*502,0)))
                        cell_lib7 = library.cells
                        for i in range(0,len(cell_lib7)):
                            lib7.add(cell_lib7[i])
                for i in range(4,9):
                    gds_name="./fab1/f1_gdsout/pre_SSPM53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        sspm53_cells = library.top_level()
                        cell8.add(gdstk.Reference(*sspm53_cells,((i-4)*502,0)))
                        cell_lib8 = library.cells
                        for i in range(0,len(cell_lib8)):
                            lib8.add(cell_lib8[i])
        if glob.glob("./fab1/f1_gdsout/pre_THIN32_*.gds"): 
            for i in range(1,4):
                gds_name="./fab1/f1_gdsout/pre_THIN32_"+str(i)+".gds"
                if glob.glob(gds_name):
                    library=gdstk.read_gds(gds_name)
                    thin32_cells = library.top_level()
                    cell9.add(gdstk.Reference(*thin32_cells,((i-1)*865,0)))
                    cell_lib9 = library.cells
                    for i in range(0,len(cell_lib9)):
                        lib9.add(cell_lib9[i])
            for i in range(4,9):
                gds_name="./fab1/f1_gdsout/pre_THIN32_"+str(i)+".gds"
                if glob.glob(gds_name):
                    library=gdstk.read_gds(gds_name)
                    thin32_cells = library.top_level()
                    cell10.add(gdstk.Reference(*thin32_cells,((i-4)*865,0)))
                    cell_lib10 = library.cells
                    for i in range(0,len(cell_lib10)):
                        lib10.add(cell_lib10[i])
        if glob.glob("./fab1/f1_gdsout/pre_DOT53_*.gds"):
            if PROCESS[0] == "0650SJ00BD":
                for i in range(1,3):
                    gds_name="./fab1/f1_gdsout/pre_DOT53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        dot53_cells = library.top_level()
                        cell11.add(gdstk.Reference(*dot53_cells,((i-1)*865,0)))
                        cell_lib11= library.cells
                        for i in range(0,len(cell_lib11)):
                            lib11.add(cell_lib11[i])
                for i in range(3,9):
                    gds_name="./fab1/f1_gdsout/pre_DOT53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        dot53_cells = library.top_level()
                        cell12.add(gdstk.Reference(*dot53_cells,((i-3)*865,0)))
                        cell_lib12 = library.cells
                        for i in range(0,len(cell_lib12)):
                            lib12.add(cell_lib12[i])
            else:
                for i in range(1,4):
                    gds_name="./fab1/f1_gdsout/pre_DOT53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        dot53_cells = library.top_level()
                        cell11.add(gdstk.Reference(*dot53_cells,((i-1)*865,0)))
                        cell_lib11= library.cells
                        for i in range(0,len(cell_lib11)):
                            lib11.add(cell_lib11[i])
                for i in range(4,9):
                    gds_name="./fab1/f1_gdsout/pre_DOT53_"+str(i)+".gds"
                    if glob.glob(gds_name):
                        library=gdstk.read_gds(gds_name)
                        dot53_cells = library.top_level()
                        cell12.add(gdstk.Reference(*dot53_cells,((i-4)*865,0)))
                        cell_lib12 = library.cells
                        for i in range(0,len(cell_lib12)):
                            lib12.add(cell_lib12[i])

    if cell1.references != [] :
        lib1.write_gds("./fab1/f1_gdsout/AA157_1.gds")
    if cell2.references != [] :
        lib2.write_gds("./fab1/f1_gdsout/AA157_2.gds")
    if cell3.references != [] :
        lib3.write_gds("./fab1/f1_gdsout/SPM11_1.gds")
    if cell4.references != [] :
        lib4.write_gds("./fab1/f1_gdsout/SPM11_2.gds")
    if cell5.references != [] :
        lib5.write_gds("./fab1/f1_gdsout/SPM53_1.gds")
    if cell6.references != [] :
        lib6.write_gds("./fab1/f1_gdsout/SPM53_2.gds")
    if cell7.references != [] :
        lib7.write_gds("./fab1/f1_gdsout/SSPM53_1.gds")
    if cell8.references != [] :
        lib8.write_gds("./fab1/f1_gdsout/SSPM53_2.gds")
    if cell9.references != [] :
        lib9.write_gds("./fab1/f1_gdsout/THIN32_1.gds")
    if cell10.references != [] :
        lib10.write_gds("./fab1/f1_gdsout/THIN32_2.gds")
    if cell11.references != [] :
        lib11.write_gds("./fab1/f1_gdsout/DOT53_1.gds")
    if cell12.references != [] :
        lib12.write_gds("./fab1/f1_gdsout/DOT53_2.gds")

    rem_file_list = glob.glob('./fab1/f1_gdsout/pre_*.gds')
    for i in range(0,len(rem_file_list)):
        try:
            os.remove(rem_file_list[i])
        except:
            pass

if __name__ == "__main__":
    start()