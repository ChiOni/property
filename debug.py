import pandas as pd

# CSV 파일 불러오기
#file_path = "db/items.csv"
#df = pd.read_csv(file_path, dtype=str)  # 모든 컬럼을 문자열(str)로 로드

# 🔹 모든 컬럼에서 따옴표(")와 백슬래시(\) 제거
#df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)

# 🔹 CSV 파일 저장 (절대 따옴표 없이 저장)
#df.to_csv(file_path, index=False, encoding="utf-8-sig", quoting=3)
