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
    lib1 = gdstk.Library()
    cell1 = lib1.new_cell(PROCESS[0]+"_FDOT_1_1_50_"+time.strftime("%Y%m%d"))
    lib2 = gdstk.Library()
    cell2 = lib2.new_cell(PROCESS[0]+"_FDOT_1_2_50_"+time.strftime("%Y%m%d"))
    lib3 = gdstk.Library()
    cell3 = lib3.new_cell(PROCESS[0]+"_FDOT_1_3_50_"+time.strftime("%Y%m%d"))
    lib4 = gdstk.Library()
    cell4 = lib4.new_cell(PROCESS[0]+"_FDOT_2_1_50_"+time.strftime("%Y%m%d"))
    lib5 = gdstk.Library()
    cell5 = lib5.new_cell(PROCESS[0]+"_FDOT_2_2_50_"+time.strftime("%Y%m%d"))
    lib6 = gdstk.Library()
    cell6 = lib6.new_cell(PROCESS[0]+"_FDOT_2_3_50_"+time.strftime("%Y%m%d"))
    lib7 = gdstk.Library()
    cell7 = lib7.new_cell(PROCESS[0]+"_FDOT_2_4_50_"+time.strftime("%Y%m%d"))
    lib8 = gdstk.Library()
    cell8 = lib8.new_cell(PROCESS[0]+"_FDOT_2_5_50_"+time.strftime("%Y%m%d"))
    lib9 = gdstk.Library()
    cell9 = lib9.new_cell(PROCESS[0]+"_FDOT_2_6_50_"+time.strftime("%Y%m%d"))
    lib11 = gdstk.Library()
    cell11 = lib11.new_cell(PROCESS[0]+"_SPM53_1_1_50_"+time.strftime("%Y%m%d"))
    lib12 = gdstk.Library()
    cell12 = lib12.new_cell(PROCESS[0]+"_SPM53_1_2_50_"+time.strftime("%Y%m%d"))
    lib13 = gdstk.Library()
    cell13 = lib13.new_cell(PROCESS[0]+"_SPM53_1_3_50_"+time.strftime("%Y%m%d"))
    lib14 = gdstk.Library()
    cell14 = lib14.new_cell(PROCESS[0]+"_SPM53_2_1_50_"+time.strftime("%Y%m%d"))
    lib15 = gdstk.Library()
    cell15 = lib15.new_cell(PROCESS[0]+"_SPM53_2_2_50_"+time.strftime("%Y%m%d"))
    lib16 = gdstk.Library()
    cell16 = lib16.new_cell(PROCESS[0]+"_SPM53_2_3_50_"+time.strftime("%Y%m%d"))
    lib17 = gdstk.Library()
    cell17 = lib17.new_cell(PROCESS[0]+"_SPM53_2_4_50_"+time.strftime("%Y%m%d"))
    lib18 = gdstk.Library()
    cell18 = lib18.new_cell(PROCESS[0]+"_SPM53_2_5_50_"+time.strftime("%Y%m%d"))
    lib19 = gdstk.Library()
    cell19 = lib19.new_cell(PROCESS[0]+"_SPM53_2_6_50_"+time.strftime("%Y%m%d"))

    # BD18(FDOT:DOT53+SPM53_S), XH18(FDOT:DOT53+AA157+SPM53_S),(SPM53:SPM53+SPM11).
    if PROCESS[0] == "1830AN18BA":
        if glob.glob("./fab1/f1_gdsout/pre_dot53_*.gds") and glob.glob("./fab1/f1_gdsout/pre_spm53_*_size.gds"):
            for i in range(1,10):
                dot53_gds_name="./fab1/f1_gdsout/pre_dot53_"+str(i)+".gds"
                spm53_gds_name="./fab1/f1_gdsout/pre_spm53_"+str(i)+"_size.gds"
                if i == 1:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell1.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib1 = library.cells
                            for i in range(0,len(cell_lib1)):
                                lib1.add(cell_lib1[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell1.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib1 = library.cells
                            for i in range(0,len(cell_lib1)):
                                lib1.add(cell_lib1[i])
                        except:
                            pass
                elif i == 2:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell2.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib2 = library.cells
                            for i in range(0,len(cell_lib2)):
                                lib2.add(cell_lib2[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell2.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib2 = library.cells
                            for i in range(0,len(cell_lib2)):
                                lib2.add(cell_lib2[i])
                        except:
                            pass
                elif i == 3:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell3.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib3 = library.cells
                            for i in range(0,len(cell_lib3)):
                                lib3.add(cell_lib3[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell3.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib3 = library.cells
                            for i in range(0,len(cell_lib3)):
                                lib3.add(cell_lib3[i])
                        except:
                            pass
                elif i == 4:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell4.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib4 = library.cells
                            for i in range(0,len(cell_lib4)):
                                lib4.add(cell_lib4[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell4.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib4 = library.cells
                            for i in range(0,len(cell_lib4)):
                                lib4.add(cell_lib4[i])
                        except:
                            pass
                elif i == 5:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell5.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib5 = library.cells
                            for i in range(0,len(cell_lib5)):
                                lib5.add(cell_lib5[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell5.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib5 = library.cells
                            for i in range(0,len(cell_lib5)):
                                lib5.add(cell_lib5[i])
                        except:
                            pass
                elif i == 6:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell6.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib6 = library.cells
                            for i in range(0,len(cell_lib6)):
                                lib6.add(cell_lib6[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell6.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib6 = library.cells
                            for i in range(0,len(cell_lib6)):
                                lib6.add(cell_lib6[i])
                        except:
                            pass
                elif i == 7:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell7.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib7 = library.cells
                            for i in range(0,len(cell_lib7)):
                                lib7.add(cell_lib7[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell7.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib7 = library.cells
                            for i in range(0,len(cell_lib7)):
                                lib7.add(cell_lib7[i])
                        except:
                            pass
                elif i == 8:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell8.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib8 = library.cells
                            for i in range(0,len(cell_lib8)):
                                lib8.add(cell_lib8[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell8.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib8 = library.cells
                            for i in range(0,len(cell_lib8)):
                                lib8.add(cell_lib8[i])
                        except:
                            pass
                elif i == 9:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell9.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib9 = library.cells
                            for i in range(0,len(cell_lib9)):
                                lib9.add(cell_lib9[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell9.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib9 = library.cells
                            for i in range(0,len(cell_lib9)):
                                lib9.add(cell_lib9[i])
                        except:
                            pass
        else:
            print("BD18 : DOT53 and SPM53 Can't Merge. Check GDS")
    elif PROCESS[0] == "181ABD18BA":
    # XH18(FDOT:DOT53+AA157+SPM53_S),(SPM53:SPM53+SPM11).
        if glob.glob("./fab1/f1_gdsout/pre_dot53_*.gds") and glob.glob("./fab1/f1_gdsout/pre_spm53_*_size.gds") and glob.glob("./fab1/f1_gdsout/pre_aa157_*.gds"):
            for i in range(1,10):
                dot53_gds_name="./fab1/f1_gdsout/pre_dot53_"+str(i)+".gds"
                spm53_gds_name="./fab1/f1_gdsout/pre_spm53_"+str(i)+"_size.gds"
                aa157_gds_name="./fab1/f1_gdsout/pre_aa157_"+str(i)+".gds"
                if i == 1:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell1.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib1 = library.cells
                            for i in range(0,len(cell_lib1)):
                                lib1.add(cell_lib1[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell1.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib1 = library.cells
                            for i in range(0,len(cell_lib1)):
                                lib1.add(cell_lib1[i])
                        except:
                            pass
                    if glob.glob(aa157_gds_name):
                        try:
                            library=gdstk.read_gds(aa157_gds_name)
                            aa157_cells = library.top_level()
                            cell1.add(gdstk.Reference(*aa157_cells,(0,0)))
                            cell_lib1 = library.cells
                            for i in range(0,len(cell_lib1)):
                                lib1.add(cell_lib1[i])
                        except:
                            pass
                elif i == 2:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell2.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib2 = library.cells
                            for i in range(0,len(cell_lib2)):
                                lib2.add(cell_lib2[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell2.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib2 = library.cells
                            for i in range(0,len(cell_lib2)):
                                lib2.add(cell_lib2[i])
                        except:
                            pass
                    if glob.glob(aa157_gds_name):
                        try:
                            library=gdstk.read_gds(aa157_gds_name)
                            aa157_cells = library.top_level()
                            cell2.add(gdstk.Reference(*aa157_cells,(0,0)))
                            cell_lib2 = library.cells
                            for i in range(0,len(cell_lib2)):
                                lib2.add(cell_lib2[i])
                        except:
                            pass
                elif i == 3:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell3.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib3 = library.cells
                            for i in range(0,len(cell_lib3)):
                                lib3.add(cell_lib3[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell3.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib3 = library.cells
                            for i in range(0,len(cell_lib3)):
                                lib3.add(cell_lib3[i])
                        except:
                            pass
                    if glob.glob(aa157_gds_name):
                        try:
                            library=gdstk.read_gds(aa157_gds_name)
                            aa157_cells = library.top_level()
                            cell3.add(gdstk.Reference(*aa157_cells,(0,0)))
                            cell_lib3 = library.cells
                            for i in range(0,len(cell_lib3)):
                                lib3.add(cell_lib3[i])
                        except:
                            pass
                elif i == 4:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell4.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib4 = library.cells
                            for i in range(0,len(cell_lib4)):
                                lib4.add(cell_lib4[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell4.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib4 = library.cells
                            for i in range(0,len(cell_lib4)):
                                lib4.add(cell_lib4[i])
                        except:
                            pass
                    if glob.glob(aa157_gds_name):
                        try:
                            library=gdstk.read_gds(aa157_gds_name)
                            aa157_cells = library.top_level()
                            cell4.add(gdstk.Reference(*aa157_cells,(0,0)))
                            cell_lib4 = library.cells
                            for i in range(0,len(cell_lib4)):
                                lib4.add(cell_lib4[i])
                        except:
                            pass
                elif i == 5:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell5.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib5 = library.cells
                            for i in range(0,len(cell_lib5)):
                                lib5.add(cell_lib5[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell5.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib5 = library.cells
                            for i in range(0,len(cell_lib5)):
                                lib5.add(cell_lib5[i])
                        except:
                            pass
                    if glob.glob(aa157_gds_name):
                        try:
                            library=gdstk.read_gds(aa157_gds_name)
                            aa157_cells = library.top_level()
                            cell5.add(gdstk.Reference(*aa157_cells,(0,0)))
                            cell_lib5 = library.cells
                            for i in range(0,len(cell_lib5)):
                                lib5.add(cell_lib5[i])
                        except:
                            pass
                elif i == 6:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell6.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib6 = library.cells
                            for i in range(0,len(cell_lib6)):
                                lib6.add(cell_lib6[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell6.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib6 = library.cells
                            for i in range(0,len(cell_lib6)):
                                lib6.add(cell_lib6[i])
                        except:
                            pass
                    if glob.glob(aa157_gds_name):
                        try:
                            library=gdstk.read_gds(aa157_gds_name)
                            aa157_cells = library.top_level()
                            cell6.add(gdstk.Reference(*aa157_cells,(0,0)))
                            cell_lib6 = library.cells
                            for i in range(0,len(cell_lib6)):
                                lib6.add(cell_lib6[i])
                        except:
                            pass
                elif i == 7:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell7.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib7 = library.cells
                            for i in range(0,len(cell_lib7)):
                                lib7.add(cell_lib7[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell7.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib7 = library.cells
                            for i in range(0,len(cell_lib7)):
                                lib7.add(cell_lib7[i])
                        except:
                            pass
                    if glob.glob(aa157_gds_name):
                        try:
                            library=gdstk.read_gds(aa157_gds_name)
                            aa157_cells = library.top_level()
                            cell7.add(gdstk.Reference(*aa157_cells,(0,0)))
                            cell_lib7 = library.cells
                            for i in range(0,len(cell_lib7)):
                                lib7.add(cell_lib7[i])
                        except:
                            pass
                elif i == 8:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell8.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib8 = library.cells
                            for i in range(0,len(cell_lib8)):
                                lib8.add(cell_lib8[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell8.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib8 = library.cells
                            for i in range(0,len(cell_lib8)):
                                lib8.add(cell_lib8[i])
                        except:
                            pass
                    if glob.glob(aa157_gds_name):
                        try:
                            library=gdstk.read_gds(aa157_gds_name)
                            aa157_cells = library.top_level()
                            cell8.add(gdstk.Reference(*aa157_cells,(0,0)))
                            cell_lib8 = library.cells
                            for i in range(0,len(cell_lib8)):
                                lib8.add(cell_lib8[i])
                        except:
                            pass
                elif i == 9:
                    if glob.glob(dot53_gds_name):
                        try:
                            library=gdstk.read_gds(dot53_gds_name)
                            dot53_cells = library.top_level()
                            cell9.add(gdstk.Reference(*dot53_cells,(0,0)))
                            cell_lib8 = library.cells
                            for i in range(0,len(cell_lib8)):
                                lib8.add(cell_lib8[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell9.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib9 = library.cells
                            for i in range(0,len(cell_lib9)):
                                lib9.add(cell_lib9[i])
                        except:
                            pass
                    if glob.glob(aa157_gds_name):
                        try:
                            library=gdstk.read_gds(aa157_gds_name)
                            aa157_cells = library.top_level()
                            cell9.add(gdstk.Reference(*aa157_cells,(0,0)))
                            cell_lib9 = library.cells
                            for i in range(0,len(cell_lib9)):
                                lib9.add(cell_lib9[i])
                        except:
                            pass
        else:
            print("XH18 : DOT53 and SPM53_SIZE and AA157 Can't Merge. Check GDS")
        if glob.glob("./fab1/f1_gdsout/pre_spm53_*.gds") and glob.glob("./fab1/f1_gdsout/pre_spm11_*.gds"):
            for i in range(1,10):
                spm11_gds_name="./fab1/f1_gdsout/pre_spm11_"+str(i)+".gds"
                spm53_gds_name="./fab1/f1_gdsout/pre_spm53_"+str(i)+".gds"
                if i == 1:
                    if glob.glob(spm11_gds_name):
                        try:
                            library=gdstk.read_gds(spm11_gds_name)
                            spm11_cells = library.top_level()
                            cell11.add(gdstk.Reference(*spm11_cells,(0,0)))
                            cell_lib11 = library.cells
                            for i in range(0,len(cell_lib11)):
                                lib11.add(cell_lib11[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell11.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib11 = library.cells
                            for i in range(0,len(cell_lib11)):
                                lib11.add(cell_lib11[i])
                        except:
                            pass
                elif i == 2:
                    if glob.glob(spm11_gds_name):
                        try:
                            library=gdstk.read_gds(spm11_gds_name)
                            spm11_cells = library.top_level()
                            cell12.add(gdstk.Reference(*spm11_cells,(0,0)))
                            cell_lib12 = library.cells
                            for i in range(0,len(cell_lib12)):
                                lib12.add(cell_lib12[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell12.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib12 = library.cells
                            for i in range(0,len(cell_lib12)):
                                lib12.add(cell_lib12[i])
                        except:
                            pass
                elif i == 3:
                    if glob.glob(spm11_gds_name):
                        try:
                            library=gdstk.read_gds(spm11_gds_name)
                            spm11_cells = library.top_level()
                            cell13.add(gdstk.Reference(*spm11_cells,(0,0)))
                            cell_lib13 = library.cells
                            for i in range(0,len(cell_lib13)):
                                lib13.add(cell_lib13[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell13.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib13 = library.cells
                            for i in range(0,len(cell_lib13)):
                                lib13.add(cell_lib13[i])
                        except:
                            pass
                elif i == 4:
                    if glob.glob(spm11_gds_name):
                        try:
                            library=gdstk.read_gds(spm11_gds_name)
                            spm11_cells = library.top_level()
                            cell14.add(gdstk.Reference(*spm11_cells,(0,0)))
                            cell_lib14 = library.cells
                            for i in range(0,len(cell_lib14)):
                                lib14.add(cell_lib14[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell14.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib14 = library.cells
                            for i in range(0,len(cell_lib14)):
                                lib14.add(cell_lib14[i])
                        except:
                            pass
                elif i == 5:
                    if glob.glob(spm11_gds_name):
                        try:
                            library=gdstk.read_gds(spm11_gds_name)
                            spm11_cells = library.top_level()
                            cell15.add(gdstk.Reference(*spm11_cells,(0,0)))
                            cell_lib15 = library.cells
                            for i in range(0,len(cell_lib15)):
                                lib15.add(cell_lib15[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell15.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib15 = library.cells
                            for i in range(0,len(cell_lib15)):
                                lib15.add(cell_lib15[i])
                        except:
                            pass
                elif i == 6:
                    if glob.glob(spm11_gds_name):
                        try:
                            library=gdstk.read_gds(spm11_gds_name)
                            spm11_cells = library.top_level()
                            cell16.add(gdstk.Reference(*spm11_cells,(0,0)))
                            cell_lib16 = library.cells
                            for i in range(0,len(cell_lib16)):
                                lib16.add(cell_lib16[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell16.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib16 = library.cells
                            for i in range(0,len(cell_lib16)):
                                lib16.add(cell_lib16[i])
                        except:
                            pass
                elif i == 7:
                    if glob.glob(spm11_gds_name):
                        try:
                            library=gdstk.read_gds(spm11_gds_name)
                            spm11_cells = library.top_level()
                            cell17.add(gdstk.Reference(*spm11_cells,(0,0)))
                            cell_lib17 = library.cells
                            for i in range(0,len(cell_lib17)):
                                lib17.add(cell_lib17[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell17.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib17 = library.cells
                            for i in range(0,len(cell_lib17)):
                                lib17.add(cell_lib17[i])
                        except:
                            pass
                elif i == 8:
                    if glob.glob(spm11_gds_name):
                        try:
                            library=gdstk.read_gds(spm11_gds_name)
                            spm11_cells = library.top_level()
                            cell18.add(gdstk.Reference(*spm11_cells,(0,0)))
                            cell_lib18 = library.cells
                            for i in range(0,len(cell_lib18)):
                                lib18.add(cell_lib18[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell18.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib18 = library.cells
                            for i in range(0,len(cell_lib18)):
                                lib18.add(cell_lib18[i])
                        except:
                            pass
                elif i == 9:
                    if glob.glob(spm11_gds_name):
                        try:
                            library=gdstk.read_gds(spm11_gds_name)
                            spm11_cells = library.top_level()
                            cell19.add(gdstk.Reference(*spm11_cells,(0,0)))
                            cell_lib19 = library.cells
                            for i in range(0,len(cell_lib19)):
                                lib19.add(cell_lib19[i])
                        except:
                            pass
                    if glob.glob(spm53_gds_name):
                        try:
                            library=gdstk.read_gds(spm53_gds_name)
                            spm53_cells = library.top_level()
                            cell19.add(gdstk.Reference(*spm53_cells,(0,0)))
                            cell_lib19 = library.cells
                            for i in range(0,len(cell_lib19)):
                                lib19.add(cell_lib19[i])
                        except:
                            pass
        else:
            print("XH18 : SPM53 and SPM11 Can't Merge. Check GDS")
    
    if PROCESS[0] == "1830AN18BA" or PROCESS[0] == "181ABD18BA":
        if cell1.references != [] :
            lib1.write_gds("./fab1/f1_gdsout/FDOT_1.gds")
        if cell2.references != [] :
            lib2.write_gds("./fab1/f1_gdsout/FDOT_2.gds")
        if cell3.references != [] :
            lib3.write_gds("./fab1/f1_gdsout/FDOT_3.gds")
        if cell4.references != [] :
            lib4.write_gds("./fab1/f1_gdsout/FDOT_4.gds")
        if cell5.references != [] :
            lib5.write_gds("./fab1/f1_gdsout/FDOT_5.gds")
        if cell6.references != [] :
            lib6.write_gds("./fab1/f1_gdsout/FDOT_6.gds")
        if cell7.references != [] :
            lib7.write_gds("./fab1/f1_gdsout/FDOT_7.gds")
        if cell8.references != [] :
            lib8.write_gds("./fab1/f1_gdsout/FDOT_8.gds")
        if cell9.references != [] :
            lib9.write_gds("./fab1/f1_gdsout/FDOT_9.gds")
        if cell11.references != [] :
            lib11.write_gds("./fab1/f1_gdsout/SPM53_SPM11_1.gds")
        if cell12.references != [] :
            lib12.write_gds("./fab1/f1_gdsout/SPM53_SPM11_2.gds")
        if cell13.references != [] :
            lib13.write_gds("./fab1/f1_gdsout/SPM53_SPM11_3.gds")
        if cell14.references != [] :
            lib14.write_gds("./fab1/f1_gdsout/SPM53_SPM11_4.gds")
        if cell15.references != [] :
            lib15.write_gds("./fab1/f1_gdsout/SPM53_SPM11_5.gds")
        if cell16.references != [] :
            lib16.write_gds("./fab1/f1_gdsout/SPM53_SPM11_6.gds")
        if cell17.references != [] :
            lib17.write_gds("./fab1/f1_gdsout/SPM53_SPM11_7.gds")
        if cell18.references != [] :
            lib18.write_gds("./fab1/f1_gdsout/SPM53_SPM11_8.gds")
        if cell19.references != [] :
            lib19.write_gds("./fab1/f1_gdsout/SPM53_SPM11_9.gds")

    if PROCESS[0] == "1830AN18BA":
        for i in range(0,10):
            gds_name="./fab1/f1_gdsout/pre_SPM53_"+str(i)+".gds"
            re_gds_name="./fab1/f1_gdsout/SPM53_"+str(i)+".gds"
            if glob.glob(gds_name):
                os.rename(gds_name,re_gds_name)
    elif PROCESS[0] == "1830BD15BA":
        gds_pre = glob.glob("./fab1/f1_gdsout/pre_*.gds")
        for i in range(0,len(gds_pre)):
            re_gds_name=gds_pre[i].replace("pre_","")
            if glob.glob(gds_pre[i]):
                os.rename(gds_pre[i],re_gds_name)
    elif PROCESS[0] == "181ABD18BA":
        pass
    else:
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