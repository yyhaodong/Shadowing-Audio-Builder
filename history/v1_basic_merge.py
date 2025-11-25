import os
from pydub import AudioSegment

# === 設定エリア (Config) ===
# ターゲットフォルダ (Target Folder)
SOURCE_FOLDER = "raw_audio/Shadowing_shochu_mp3/Unit1"
# 出力ファイル名 (Output Filename)
OUTPUT_FILE = "output/v1_test.mp3"

def merge_audio():
    # ファイルリストを取得 (Get file list)
    files = [f for f in os.listdir(SOURCE_FOLDER) if f.endswith(".mp3")]
    files.sort()
    
    combined = AudioSegment.empty()
    
    # ループ処理 (Loop processing)
    for file_name in files:
        file_path = os.path.join(SOURCE_FOLDER, file_name)
        print(f"処理中: {file_name}")
        
        # 音声を読み込む (Load audio)
        sound = AudioSegment.from_mp3(file_path)
        combined += sound

    # 保存 (Save)
    combined.export(OUTPUT_FILE, format="mp3")
    print("完了しました。")

if __name__ == "__main__":
    merge_audio()