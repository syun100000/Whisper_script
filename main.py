import whisper
import os

# モデルをロード
model = whisper.load_model("turbo")

# ユーザーから音声ファイルのパスを入力として受け取る
audio_file_path = input("音声ファイルのパスを入力してください: ")


# 音声ファイルをテキストに変換
result = model.transcribe(audio_file_path)

# 結果を表示
print(result["text"])

# 音声ファイル名からテキストファイル名を生成
text_file_path = os.path.splitext(audio_file_path)[0] + ".txt"

# 結果をテキストファイルに出力
with open(text_file_path, "w", encoding="utf-8") as f:
    f.write(result["text"])