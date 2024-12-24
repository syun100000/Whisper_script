import whisper
import os
import pyperclip

# モデルをロード
model = whisper.load_model("base")

# ユーザーから音声ファイルのパスを入力として受け取る
audio_file_path = input("音声ファイルのパスを入力してください: ")

# 絶対パスを取得
audio_file_path = os.path.abspath(audio_file_path.strip("'"))

# ファイルパスが存在するか確認
if not os.path.isfile(audio_file_path):
    print(f"エラー: ファイルが見つかりません: {audio_file_path}")
else:
    # 音声ファイルをテキストに変換
    result = model.transcribe(audio_file_path)

    # 結果を表示
    print(result["text"])

    # 音声ファイル名からテキストファイル名を生成
    text_file_path = os.path.splitext(audio_file_path)[0] + ".txt"

    # 結果をテキストファイルに出力
    with open(text_file_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"テキストファイルを保存しました: {text_file_path}")
    # テキストをクリップボードにコピー
    try:
        pyperclip.copy(result["text"])
        print("テキストがクリップボードにコピーされました。")
    except ImportError:
        print("pyperclipモジュールがインストールされていません。クリップボードへのコピーはスキップされました。")
    print("処理が完了しました。")