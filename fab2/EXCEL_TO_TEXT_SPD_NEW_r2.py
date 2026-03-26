import pandas as pd

def photokey_files(excel_file,process):
    input_file = pd.ExcelFile('./upload/'+excel_file)
    if process.find("SPD") == -1 and process.find("NORMAL") == -1 and process.find("HC") == -1 :
        output1 = './fab2/text/input_key.txt'
        output2 = './fab2/text/input_overlay.txt'
        output3 = './fab2/text/1st_overlay.txt'
        output4 = './fab2/text/dicer.txt'
        sheets = ['NIKON-WGA', 'NIKON-FIA', 'NIKON-LSA','ASML1','ASML2']

        data_save = []
        data2_save = []
        data3_save = []
        data4_save = []

        # nikon & asml data read
        count = 0
        for sheet in sheets: 
            key_df = pd.read_excel(input_file, sheet_name=sheet, usecols='AF:AI', skiprows=0)
            for index, row in key_df.iterrows():  # 현재 행에 값이 있는지 체크
                if index >= 0:  # 3행 시작
                    if not row.isnull().all():
                        if 'Priority' in row.values:
                            count_str = '00'
                            data = count_str + '\t' + '\t'.join(map(str, row))
                            data_save.append(data)
                            count = 0
                        else:
                            if count == 0:
                                count = 1
                            else:
                                count += 1
                            count_str = f"{count:02d}"
                            data = count_str + '\t' + '\t'.join(map(str, row))
                            data_save.append(data)               
                    else:
                        count = 0

        # overlay data read (N~Q, 4행)
        overlay_df = pd.read_excel(input_file, sheet_name='OVERLAY', usecols='AH:AM')
        for index, row in overlay_df.iterrows():
            if index >= 2:  # 4행 시작
                if not row.isnull().all():
                    data2_save.append('\t'.join(map(str, row)))

        # 1st_overlay data read (N~Q, 4행)
        over_1st_df = pd.read_excel(input_file, sheet_name='1ST_OVERLAY', usecols='U:Y')
        for index, row in over_1st_df.iterrows():
            if index >= 2:  # 4행 시작
                if not row.isnull().all():
                    data3_save.append('\t'.join(map(str, row)))
            
        # dicer data read (N~Q, 4행)
        dicer_df = pd.read_excel(input_file, sheet_name='DICER(Origin)', usecols='B:G')
        for index, row in dicer_df.iterrows():
            if index >= 3:  # 5행 시작
                if not row.isnull().all():
                    data4_save.append('\t'.join(map(str, row)))
        
        # overlay_block base_pad data read (AF:2행)
        basepad_df = pd.read_excel(input_file, sheet_name='OVERLAY', usecols='AF', nrows=2).iloc[0,0]
        basepad = basepad_df

        # overlay_box_type (AA:2행)
        overtype_df = pd.read_excel(input_file, sheet_name='OVERLAY', usecols='AA', nrows=2).iloc[0,0]
        overlay_type = overtype_df

        # save as text1 file
        with open(output1, 'w', encoding='utf-8') as f:
            for line in data_save:
                f.write(line + '\n')
        # save as text2 file
        with open(output2, 'w', encoding='utf-8') as f:
            for line in data2_save:
                f.write(line + '\n')
        # save as text3 file
        with open(output3, 'w', encoding='utf-8') as f:
            for line in data3_save:
                f.write(line + '\n')
        # save as text4 file
        with open(output4, 'w', encoding='utf-8') as f:
            for line in data4_save:
                f.write(line + '\n')
        with open(output4, 'a+') as f:
            f.write("BASEPAD\t%s \n"%(basepad))
        with open(output4, 'a+') as f:
            f.write("OVERTYPE\t%s \n"%(overlay_type))
    else: 
        output1 = './fab2/text/input_key1.txt'
        output2 = './fab2/text/input_key2.txt'
        output3 = './fab2/text/input_overlay.txt'
        output4 = './fab2/text/1st_overlay.txt'
        output5 = './fab2/text/dicer.txt'
        sheets1 = ['NIKON-WGA', 'NIKON-FIA', 'NIKON-LSA']
        sheets2 = ['ASML1','ASML2']

        data1_save = []
        data2_save = []
        data3_save = []
        data4_save = []
        data5_save = []

        # nikon data read
        count = 0
        prev_row = False
        for sheet in sheets1: 
            key1_df = pd.read_excel(input_file, sheet_name=sheet, usecols='AF:AI', skiprows=0)
            prev_row = False
            for index, row in key1_df.iterrows():  # 현재 행에 값이 있는지 체크
                if not row.isnull().all():
                    if not prev_row:
                        count += 1
                        count_str = f"{count:02d}"
                    data1 = count_str + '\t' + '\t'.join(map(str, row))
                    data1_save.append(data1)
                    prev_row = True
                else:
                      prev_row = False
                        
        # asml data read
        count = 0
        prev_row = False
        for sheet in sheets2: 
            key2_df = pd.read_excel(input_file, sheet_name=sheet, usecols='AF:AI', skiprows=0)
            prev_row = False
            for index, row in key2_df.iterrows():  # 현재 행에 값이 있는지 체크
                if not row.isnull().all():
                    if not prev_row:
                        count += 1
                        count_str = f"{count:02d}"
                    data2 = count_str + '\t' + '\t'.join(map(str, row))
                    data2_save.append(data2)
                    prev_row = True
                else:
                      prev_row = False

        # overlay data read
        overlay_df = pd.read_excel(input_file, sheet_name='OVERLAY', usecols='AH:AM')
        for index, row in overlay_df.iterrows():
            if index >= 2:
                if not row.isnull().all():
                    data3_save.append('\t'.join(map(str, row)))

        # overlay_block base_pad data read (AF:2행)
        basepad_df = pd.read_excel(input_file, sheet_name='OVERLAY',  usecols='AF', nrows=2).iloc[0,0]
        basepad = basepad_df

        # overlay_box_type (AA:2행)
        overtype_df = pd.read_excel(input_file, sheet_name='OVERLAY',  usecols='AA', nrows=2).iloc[0,0]
        overlay_type = overtype_df
        
        # 1st_overlay data read
        over_1st_df = pd.read_excel(input_file, sheet_name='1ST_OVERLAY', usecols='U:Y')
        for index, row in over_1st_df.iterrows():
            if index >= 2:
                if not row.isnull().all():
                    data4_save.append('\t'.join(map(str, row)))

        # dicer data read 
        dicer_df = pd.read_excel(input_file, sheet_name='DICER(Origin)', usecols='B:G')
        for index, row in dicer_df.iterrows():
            if index >= 3:  # 5행 시작
                if not row.isnull().all():
                    data5_save.append('\t'.join(map(str, row)))     
  
        # save as text1 file
        with open(output1, 'w', encoding='utf-8') as f:
            for line in data1_save:
                f.write(line + '\n')      
        # save as text2 file
        with open(output2, 'w', encoding='utf-8') as f:
            for line in data2_save:
                f.write(line + '\n')
        # save as text3 file
        with open(output3, 'w', encoding='utf-8') as f:
            for line in data3_save:
                f.write(line + '\n')
        # save as text4 file
        with open(output4, 'w', encoding='utf-8') as f:
            for line in data4_save:
                f.write(line + '\n')
        # save as text5 file
        with open(output5, 'w', encoding='utf-8') as f:
            for line in data5_save:
                f.write(line + '\n')
        with open(output5, 'a+') as f:
            f.write("BASEPAD\t%s \n"%(basepad))
        with open(output5, 'a+') as f:
            f.write("OVERTYPE\t%s \n"%(overlay_type))

if __name__ == '__main__':
    photokey_files('./Photokey_Autodrawing_Guide_BD130_60um_250401_r0.xlsx')
    process='BD130_60UM'