import os, datetime, glob, tarfile, shutil
from fab2 import NIKON_FIA_LSA_WGA_MAIN,NIKON_WGA_MAIN, NIKON_WGA_FIA_LSA_MAIN, NIKON_WGA_FIA_LSA_HC18
from fab2 import ASML_DOT_SPM_VSPM_MAIN, ASML_DOT_SPM_VSPM_HC18, NIKON_FIAB_MAIN, NIKON_WGAB_MAIN, ASML_DOTB_SPMB_VSPMB_MAIN

PRIORITY = []
LAYER_NO = []
KEY_TYPE = []
BOUNDARY = []
ETCH_TYPE= []
MAIN_X   = []
MAIN_Y   = []
BAR_X    = []
BAR_Y    = []
    
def split_file():
    with open('./fab2/text/input_key.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    count_dict = {}
    current_content = []
    output_file = None
    is_recording = False
    previous_name = None

    for line in lines:
        line = line.strip()
        if not line:
            continue 
        parts = line.split()
        if len(parts) < 5 :
            continue
        if parts[0] == '00' and parts[1] == 'Priority':
            continue
        out_line = f'{parts[1]}\t{parts[2]}\t{parts[3]}\t{parts[4]}'
        current_content.append(out_line)
        if len(parts) > 2:                  
            if parts[0] == '01':
                name = parts[3].split('_')[0]
                if name != previous_name:
                    if name not in count_dict:
                        count_dict[name] = 0 # NAME_Define
                    count_dict[name] += 1  # count+1
                    output_file = f'./fab2/text/{name}_{count_dict[name]:02d}.txt'
                    previous_name = name 
                    is_recording = True
                else:
                    is_recording = True
            if is_recording :
                if output_file is not None and current_content:
                    with open(output_file, 'a') as out_file:
                        out_file.write('\n'.join(current_content)+'\n')
                    current_content = []
                    previous_name = None
    
    # 파일 끝내용 저장
    if output_file is not None and current_content:
        with open(output_file, 'a') as out_file:
            out_file.write('\n'.join(current_content)+'\n')

def split_spd_file():
    with open('./fab2/text/input_key1.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()    
        count_dict = {}
        output_file = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue 
            parts = line.split()
            if len(parts) > 1 and parts[1] == 'Priority':
                continue
            number = parts[0]
            if len(parts) >= 5:
                save_parts = parts[1:5]
            else:
                save_parts = parts[1:]
            if number not in count_dict:
                count_dict[number] = []
            count_dict[number].append(save_parts)

        for number, lines in count_dict.items():
            output_file = f'./fab2/text/NIKON_{number}.txt'
            with open(output_file, 'a', encoding='utf-8') as outfile:
                for line_parts in lines:
                    outfile.write(' '.join(line_parts) + '\n')

    with open('./fab2/text/input_key2.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()      
        count_dict = {}
        output_file = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue 
            parts = line.split()
            if len(parts) > 1 and parts[1] == 'Priority':
                continue
            number = parts[0]
            if len(parts) >= 5:
                save_parts = parts[1:5]
            else:
                save_parts = parts[1:]
            if number not in count_dict:
                count_dict[number] = []
            count_dict[number].append(save_parts)

        for number, lines in count_dict.items():
            output_file = f'./fab2/text/ASML_{number}.txt'
            with open(output_file, 'a', encoding='utf-8') as outfile:
                for line_parts in lines:
                    outfile.write(' '.join(line_parts) + '\n')

def main(process):
    # Si-Capacitor process nikon/asml. (Normal GDS)
    if process.find("HC18") == 0 : 
        split_spd_file()
        date = datetime.datetime.now().strftime("%y%m%d")
        key_name = process+"_PHOTOKEY_"+ date 
        path = ('./fab2/f2_gdsout/'+key_name)
        if os.path.isdir(path):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name)
        path2 = ('./fab2/f2_gdsout/'+key_name+'/'+key_name+'/')
        if os.path.isdir(path2):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name+'/'+key_name+'/')    
        files_key = glob.glob('./fab2/text/*_??.txt')
       
        for file in files_key:
            with open(file,'r') as f:           
                file_st=str(file).strip()
                file_sp = os.path.basename(file_st)
                file_n=file_sp.split('.')[0]
                PRIORITY = []
                LAYER_NO = []
                KEY_TYPE = []
                BOUNDARY = []
                lines = f.readlines()
                for line in lines:
                    line_st=line.strip()
                    line_sp=line_st.split()
                    PRIORITY.append(line_sp[0])
                    LAYER_NO.append(line_sp[1])
                    KEY_TYPE.append(line_sp[2])
                    temp = []
                    temp.append(line_sp[3])
                    str_tmp = temp[0].split(',')
                    BOUNDARY.append(str_tmp)
            f.close()
            if 'NIKON' in file:
                NIKON_WGA_FIA_LSA_MAIN.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n)
            elif 'ASML' in file:
                ASML_DOT_SPM_VSPM_MAIN.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n)
        
        # Si-Capacitor process nikon/asml. (SPD GDS)
        date = datetime.datetime.now().strftime("%y%m%d")
        process_spd = process+"_SPD"  
        key_name_spd = process_spd+"_PHOTOKEY_"+date
        path3 = ('./fab2/f2_gdsout/'+key_name_spd)
        if os.path.isdir(path3):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name_spd)
        path4 = ('./fab2/f2_gdsout/'+key_name_spd+'/'+key_name_spd)
        if os.path.isdir(path4):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name_spd+'/'+key_name_spd+'/')  
        files_key = glob.glob('./fab2/text/*_??.txt')

        for file in files_key:
            with open(file,'r') as f:
                file_st=str(file).strip()
                file_sp = os.path.basename(file_st)
                file_n=file_sp.split('.')[0]
                PRIORITY = []
                LAYER_NO = []
                KEY_TYPE = []
                BOUNDARY = []
                lines = f.readlines()
                for line in lines:
                    line_st=line.strip()
                    line_sp=line_st.split()
                    PRIORITY.append(line_sp[0])
                    LAYER_NO.append(line_sp[1])
                    KEY_TYPE.append(line_sp[2])
                    temp = []
                    temp.append(line_sp[3])
                    str_tmp = temp[0].split(',')
                    BOUNDARY.append(str_tmp)
            f.close()
            if 'NIKON' in file:
                NIKON_WGA_FIA_LSA_HC18.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n)
            elif 'ASML' in file:
                ASML_DOT_SPM_VSPM_HC18.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n)
    # SPD/NORMAL process nikon/asml GDS. 
    elif process.find("SPD") != -1 or process.find("NORMAL") != -1 : 
        split_spd_file()
        date = datetime.datetime.now().strftime("%y%m%d")
        key_name = process+"_PHOTOKEY_"+date
        #key_name = process+"_PHOTOKEY_"+'240423' 
        path = ('./fab2/f2_gdsout/'+key_name)
        if os.path.isdir(path):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name)
        path2 = ('./fab2/f2_gdsout/'+key_name+'/'+key_name)
        if os.path.isdir(path2):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name+'/'+key_name+'/')  
        files_key = glob.glob('./fab2/text/*_??.txt')
  
        for file in files_key:
            with open(file,'r') as f:
                file_st=str(file).strip()
                file_sp = os.path.basename(file_st)
                file_n=file_sp.split('.')[0]
            
                PRIORITY = []
                LAYER_NO = []
                KEY_TYPE = []
                BOUNDARY = []

                lines = f.readlines()
                for line in lines:
                    line_st=line.strip()
                    line_sp=line_st.split()
                    PRIORITY.append(line_sp[0])
                    LAYER_NO.append(line_sp[1])
                    KEY_TYPE.append(line_sp[2])
                    temp = []
                    temp.append(line_sp[3])
                    str_tmp = temp[0].split(',')
                    BOUNDARY.append(str_tmp)
            f.close()
            if 'NIKON' in file:
                NIKON_WGA_FIA_LSA_MAIN.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n)
            elif 'ASML' in file:
                ASML_DOT_SPM_VSPM_MAIN.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n)    
    # Normal & SiC process nikon/asml GDS.
    else:
        split_file()
        date = datetime.datetime.now().strftime("%y%m%d")
        key_name = process+"_PHOTOKEY_"+ date
        #key_name = process+"_PHOTOKEY_"+'240423'   
        path = ('./fab2/f2_gdsout/'+key_name)
        if os.path.isdir(path):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name)
        path2 = ('./fab2/f2_gdsout/'+key_name+'/'+key_name+'/')
        if os.path.isdir(path2):
            pass
        else:
            os.makedirs('./fab2/f2_gdsout/'+key_name+'/'+key_name+'/')    
        files_key = glob.glob('./fab2/text/*_??.txt')

        for file in files_key:
            with open(file,'r') as f:
                file_st=str(file).strip()
                file_sp = os.path.basename(file_st)
                file_n=file_sp.split('.')[0]
                PRIORITY = []
                LAYER_NO = []
                KEY_TYPE = []
                BOUNDARY = []
                lines = f.readlines()
                
                for line in lines:
                    line_st=line.strip()
                    line_sp=line_st.split()
                    PRIORITY.append(line_sp[0])
                    LAYER_NO.append(line_sp[1])
                    KEY_TYPE.append(line_sp[2])
                    temp = []
                    temp.append(line_sp[3])
                    str_tmp = temp[0].split(',')
                    BOUNDARY.append(str_tmp)
            f.close()
            if 'FIAB' in file:
                NIKON_FIAB_MAIN.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n)
            elif 'FIA' in file or 'LSA' in file:
                #NIKON_FIA_LSA_MAIN.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n)
                #CIS_NIKON_TV(FIA_LSA_WGA)
                NIKON_FIA_LSA_WGA_MAIN.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n) 
            if 'WGAB' in file:
                NIKON_WGAB_MAIN.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n)
            elif 'WGA' in file:
                NIKON_WGA_MAIN.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n)
            if 'DOT53B' in file or 'SPM53B' in file or 'VSPM157B' in file or 'SPM11B' in file:
                ASML_DOTB_SPMB_VSPMB_MAIN.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n)
            elif 'DOT53' in file or 'DOT32' in file or 'SPM53' in file or 'VSPM157' in file or 'SPM11' in file:
                ASML_DOT_SPM_VSPM_MAIN.main(process,PRIORITY,LAYER_NO,KEY_TYPE,BOUNDARY,file_n) 
   
    dir_path = "./fab2/f2_gdsout/"+key_name
    tar_file = "./fab2/f2_gdsout/"+key_name+'.tar'
    #tar_file = "/user/scad_md/frame/PROGRAM/util/PHOTOKEY_SYSTEM/fab2/f2_gdsout/"+key_name+'.tar'
    with tarfile.open(tar_file, "w") as tar:
        for path, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(path,file)
                arcname = os.path.relpath(file_path, start=dir_path)
                tar.add(file_path, arcname=os.path.join(key_name,arcname))

    out= "./fab2/f2_gdsout/"+key_name+"/"+key_name+"/"+key_name+'.txt'
    out2= "./fab2/f2_gdsout/"+key_name+'.txt'
    shutil.copy2(out,out2)

    if process.find("HC18") == 0 : 
        process_spd = process+"_SPD"  
        key_name_spd = process_spd+"_PHOTOKEY_"+date
        if os.path.isdir("./fab2/f2_gdsout/"+key_name_spd):
            dir_path2 = ("./fab2/f2_gdsout/"+key_name_spd)
            tar_file2 = "./fab2/f2_gdsout/"+key_name_spd+'.tar'
            #tar_file2 = "/user/scad_md/frame/PROGRAM/util/PHOTOKEY_SYSTEM/fab2/f2_gdsout/"+key_name_spd+'.tar'
            with tarfile.open(tar_file2, "w") as tar:
                for path, dirs, files in os.walk(dir_path2):
                    for file in files:
                        file_path = os.path.join(path,file)
                        arcname = os.path.relpath(file_path, start=dir_path)
                        tar.add(file_path, arcname=os.path.join(key_name_spd,arcname))
            out3= "./fab2/f2_gdsout/"+key_name_spd+"/"+key_name_spd+"/"+key_name_spd+'.txt'
            out4= "./fab2/f2_gdsout/"+key_name_spd+'.txt'
            shutil.copy2(out3,out4)
    else:
        pass
    [os.remove(f) for f in glob.glob('./fab2/text/*txt')]
    return tar_file

if __name__ == '__main__':
    process  = "BD130S_60um"
    priority = [1,2,3,5,4,6]
    layer_no = [9,13,17,11,15,9]
    key_type = ["DOT53_800_54_1_6_1_6_T","DOT53_800_54_1_6_1_6_T","DOT53_800_54_1_6_1_6_T","DOT53_800_54_1_6_1_6_T","DOT53_800_54_1_6_1_6_T","DOT32_800_54_2_6_2_6_T"]
    boundary = [[63,3,10,12],[63,3,10,12],[63,3,10,123],[63,3,10,12],[63,3,10,12],[63,3]]
    res = main(process,priority,layer_no,key_type,boundary)