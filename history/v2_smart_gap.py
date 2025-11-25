import os
from pydub import AudioSegment

# === 設定エリア ===
SOURCE_FOLDER = "raw_audio/Shadowing_shochu_mp3/Unit1"
OUTPUT_FILE = "output/v2_test.mp3"

# 空白の長さ（ミリ秒）: 2.5秒
# シャドーイングのための時間を確保する
GAP_DURATION = 2500 

def merge_with_gap():
    files = [f for f in os.listdir(SOURCE_FOLDER) if f.endswith(".mp3")]
    files.sort()
    
    # 空白を作成 (Create silence)
    silence = AudioSegment.silent(duration=GAP_DURATION)
    combined = AudioSegment.empty()
    
    for file_name in files:
        file_path = os.path.join(SOURCE_FOLDER, file_name)
        sound = AudioSegment.from_mp3(file_path)
        
        # 音声 + 空白 を結合 (Combine audio and silence)
        combined += sound + silence
        print(f"結合中: {file_name} (+2.5s blank)")

    combined.export(OUTPUT_FILE, format="mp3")
    print("V2 出力完了")

if __name__ == "__main__":
    merge_with_gap()