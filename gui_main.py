## History ##
# 2026/03/26 - Flask 기반 웹 서비스를 Tkinter GUI로 변환 및 통합
#            - 오리지널 Tkinter 사용 로컬 실행 파일(gui_main.py) 생성
#            - 결과 파일(.tar, .txt)의 루트 폴더 자동 복사 기능 추가
#            - fab2 패키지 내 파일 핸들 누수 수정(resource management)
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import shutil
import datetime
import sys

# 프로젝트 루트 경로를 path에 추가하여 fab2 모듈 임포트 가능하게 함
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from fab2 import EXCEL_TO_TEXT_SPD_NEW_r3, F2_NIKON_ASML_MERGE_SPD_NEW_r1
    from fab2 import F2_OVERLAY_MAIN_MERGE_HC18_r1, F2_OVERLAY_MAIN_MERGE_SPD_NEW_r3
except ImportError as e:
    # 실행 환경 오류 알림
    print(f"모듈 임포트 오류: {e}")

class PhotoKeyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FAB2 PHOTOKEY 제작 시스템")
        self.root.geometry("650x550")
        self.root.resizable(False, False)
        
        # 스타일 설정
        style = ttk.Style()
        style.configure("TButton", font=("Malgun Gothic", 10))
        style.configure("TLabel", font=("Malgun Gothic", 10))
        
        # UI 구성
        self.setup_ui()
        
    def setup_ui(self):
        # 상단 로고 이미지 (있는 경우)
        try:
            logo_path = os.path.join("static", "images", "logo.gif")
            if os.path.exists(logo_path):
                self.logo_img = tk.PhotoImage(file=logo_path)
                tk.Label(self.root, image=self.logo_img).pack(pady=10)
            else:
                # 로고가 없으면 텍스트로 대체
                tk.Label(self.root, text="DB HiTek", font=("Arial", 24, "bold"), fg="#00468b").pack(pady=10)
        except Exception:
            pass

        tk.Label(self.root, text="[ FAB2 PHOTOKEY 제작 시스템 ]", font=("Malgun Gothic", 16, "bold")).pack(pady=10)

        # 1. 파일 선택 프레임
        frame1 = tk.LabelFrame(self.root, text=" 1. PHOTOKEY DRAWING GUIDE 파일 첨부 ", font=("Malgun Gothic", 10, "bold"), padx=15, pady=15)
        frame1.pack(fill="x", padx=30, pady=10)

        self.file_path_var = tk.StringVar()
        tk.Entry(frame1, textvariable=self.file_path_var, width=55, font=("Malgun Gothic", 9)).pack(side="left", padx=(0, 10))
        tk.Button(frame1, text="파일 찾기", command=self.browse_file, width=10).pack(side="left")

        # 2. GDS Name 입력 프레임
        frame2 = tk.LabelFrame(self.root, text=" 2. GDS NAME (Process) 입력 ", font=("Malgun Gothic", 10, "bold"), padx=15, pady=15)
        frame2.pack(fill="x", padx=30, pady=10)

        self.process_var = tk.StringVar(value="BD130S_60um")
        tk.Entry(frame2, textvariable=self.process_var, width=68, font=("Malgun Gothic", 10)).pack(pady=(0, 10))
        
        info_text = (
            "-. PROCESS + S/L : BD130S_60UM\n"
            "-. PROCESS + S/L + 제품군 : BD180S_60UM_SPD\n\n"
            "[ GDS NAME에 'SPD' or 'NORMAL'을 쓰면 KEY 이름이 NIKON/ASML로 시작됩니다. ]"
        )
        tk.Label(frame2, text=info_text, justify="left", font=("Malgun Gothic", 9), fg="#555555").pack(anchor="w")

        # 하단 버튼부
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=25)

        self.exec_btn = tk.Button(btn_frame, text="제작 시작 (Run)", command=self.run_process, 
                                  width=18, height=2, bg="#00468b", fg="white", font=("Malgun Gothic", 11, "bold"))
        self.exec_btn.pack(side="left", padx=15)
        
        tk.Button(btn_frame, text="초기화", command=self.reset_fields, 
                  width=12, height=2, font=("Malgun Gothic", 10)).pack(side="left", padx=15)

        # 상태 표시줄
        self.status_var = tk.StringVar(value="준비됨")
        status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor="w", padx=10)
        status_bar.pack(side="bottom", fill="x")

    def browse_file(self):
        filename = filedialog.askopenfilename(
            title="엑셀 가이드 파일 선택",
            filetypes=[("Excel Files", "*.xlsx *.xlsm"), ("All Files", "*.*")]
        )
        if filename:
            self.file_path_var.set(filename)
            self.status_var.set(f"파일 선택됨: {os.path.basename(filename)}")

    def reset_fields(self):
        self.file_path_var.set("")
        self.process_var.set("BD130S_60um")
        self.status_var.set("초기화됨")

    def run_process(self):
        file_path = self.file_path_var.get()
        process = self.process_var.get()

        if not file_path or not os.path.exists(file_path):
            messagebox.showerror("입력 오류", "PHOTOKEY 가이드 파일을 선택해 주세요.")
            return

        if not process.strip():
            messagebox.showerror("입력 오류", "GDS NAME(Process)을 입력해 주세요.")
            return

        # 버튼 비활성화 (중복 실행 방지)
        self.exec_btn.config(state="disabled")
        self.status_var.set("처리 중... 잠시만 기다려 주세요.")
        self.root.update_idletasks()

        try:
            # 1. 업로드 폴더 준비 및 파일 복사
            upload_dir = "upload"
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            
            file_name = os.path.basename(file_path)
            upload_path = os.path.join(upload_dir, file_name)
            
            # 원본과 대상이 다른 경우에만 복사 진행 (WinError 32 방지)
            if os.path.abspath(file_path) != os.path.abspath(upload_path):
                shutil.copy2(file_path, upload_path)

            # 2. 기존 Flask 서버 로직 실행
            # EXCEL_TO_TEXT 실행
            EXCEL_TO_TEXT_SPD_NEW_r3.photokey_files(file_name, process)
            
            # 프로세스 명에 따른 오버레이 병합 로직
            if ('HC18' in process) or ('BD13' in process):
                F2_OVERLAY_MAIN_MERGE_HC18_r1.main(process)
            else:
                F2_OVERLAY_MAIN_MERGE_SPD_NEW_r3.main(process)
            
            # 최종 NIKON/ASML 병합 및 결과 파일 생성
            out_file = F2_NIKON_ASML_MERGE_SPD_NEW_r1.main(process)
            
            # 3. 결과 파일을 프로그램 실행 위치(루트)로 복사 (사용자 요청 사항)
            result_files = []
            if out_file and os.path.exists(out_file):
                # .tar 파일 복사
                shutil.copy2(out_file, "./")
                result_files.append(os.path.basename(out_file))
                
                # 대응하는 .txt 파일도 복사 (있다면)
                txt_file = out_file.replace(".tar", ".txt")
                if os.path.exists(txt_file):
                    shutil.copy2(txt_file, "./")
                    result_files.append(os.path.basename(txt_file))
                
                # HC18 등의 특별 케이스 (SPD 결과물이 추가로 있는 경우)
                if 'HC18' in process and not process.endswith('_SPD'):
                    spd_process = process + "_SPD"
                    # F2_NIKON_ASML_MERGE_SPD_NEW_r1 내부 로직에 따른 파일명 추측
                    date_str = datetime.datetime.now().strftime("%y%m%d")
                    spd_out_file = f"./fab2/f2_gdsout/{spd_process}_PHOTOKEY_{date_str}.tar"
                    if os.path.exists(spd_out_file):
                        shutil.copy2(spd_out_file, "./")
                        result_files.append(os.path.basename(spd_out_file))
                        spd_txt_file = spd_out_file.replace(".tar", ".txt")
                        if os.path.exists(spd_txt_file):
                            shutil.copy2(spd_txt_file, "./")
                            result_files.append(os.path.basename(spd_txt_file))

            # 4. 결과 확인 및 알림
            if result_files:
                self.status_var.set("완료: 결과 파일이 루트 폴더로 복사되었습니다.")
                files_str = "\n".join(result_files)
                messagebox.showinfo("성공", f"제작이 완료되었습니다!\n결과 파일들이 프로그램 폴더로 복사되었습니다.\n\n[생성된 파일]\n{files_str}")
                
                # 현재 폴더(루트) 열기
                try:
                    os.startfile(".")
                except:
                    pass
            else:
                self.status_var.set("오류: 결과 파일을 찾을 수 없습니다.")
                messagebox.showwarning("완료 확인 불가", "로직 수행은 끝났으나 결과 파일(.tar)을 찾을 수 없습니다.")

        except Exception as e:
            self.status_var.set("오류 발생")
            messagebox.showerror("실행 오류", f"처리 중 오류가 발생했습니다:\n{str(e)}")
        
        finally:
            self.exec_btn.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoKeyApp(root)
    root.mainloop()
