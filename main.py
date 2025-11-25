import os
from pydub import AudioSegment

# ================= 設定 (Configuration) =================
# ルートディレクトリ (Root Directory)
# すべてのユニットが含まれる親フォルダを指定
BASE_FOLDER = os.path.join("raw_audio", "Shadowing_shochu_mp3")

# 文の間の空白時間（ミリ秒）
# 2500ms = 2.5秒 (シャドーイングに最適な間隔)
GAP_DURATION = 2500 
# ========================================================

def process_one_unit(unit_folder_path, unit_name):
    """
    単一ユニットの処理関数
    フォルダ内のMP3を結合し、間に空白を挿入する
    """
    print(f"\n📂 処理開始: {unit_name} ...")
    
    # MP3ファイルのみを取得
    files = [f for f in os.listdir(unit_folder_path) if f.endswith(".mp3")]
    
    # ファイル名順にソート (01.mp3, 02.mp3...)
    files.sort()
    
    if not files:
        print(f"   ⚠️ 警告: {unit_name} は空です。スキップします。")
        return

    # 空白パーツの生成
    silence_gap = AudioSegment.silent(duration=GAP_DURATION)
    
    combined = AudioSegment.empty()
    count = 0
    
    # メインループ (Main Loop)
    for file_name in files:
        file_path = os.path.join(unit_folder_path, file_name)
        try:
            sound = AudioSegment.from_mp3(file_path)
            
            # 音声結合: 原音 + 空白
            combined += sound + silence_gap
            count += 1
            
        except Exception as e:
            # エラーハンドリング (Error Handling)
            print(f"   ❌ 読み込みエラー: {file_name} - {e}")

    # ファイル書き出し (Export)
    output_filename = os.path.join("output", f"{unit_name}_Shadowing.mp3")
    print(f"   -> {count} 個のファイルを結合しました")
    print(f"💾 保存中: {output_filename}")
    
    combined.export(output_filename, format="mp3")
    print(f"✅ {unit_name} 完了！")

def main():
    # ディレクトリ存在確認
    if not os.path.exists(BASE_FOLDER):
        print("❌ エラー: 指定されたフォルダが見つかりません。")
        return

    # 出力フォルダ作成
    if not os.path.exists("output"):
        os.makedirs("output")

    # 全ユニットをスキャン
    all_items = os.listdir(BASE_FOLDER)
    # "Unit"を含むフォルダのみをフィルタリング
    unit_folders = [d for d in all_items if os.path.isdir(os.path.join(BASE_FOLDER, d)) and "Unit" in d]
    unit_folders.sort()

    print(f"🚀 バッチ処理を開始します。対象ユニット数: {len(unit_folders)}\n")

    # 各ユニットに対して処理を実行
    for unit_name in unit_folders:
        full_path = os.path.join(BASE_FOLDER, unit_name)
        process_one_unit(full_path, unit_name)

    print("\n" + "="*30)
    print("🎉 すべての処理が完了しました。outputフォルダを確認してください。")

if __name__ == "__main__":
    main()