import re
import pandas as pd

def load_shift1_change():
    df = pd.read_csv("db/items.csv", parse_dates=["날짜"])
    df['가격'] = df['가격'].apply(lambda x: 
                            int(x.split(" ")[0].replace("억","")) if len(x.split(" "))==1 else 
                            int(x.split(" ")[0].replace("억","")) + round(int(x.split(" ")[1].replace(",",""))*0.0001,1))

    df['면적'] = df['면적'].apply(lambda x: str(int(int(re.sub(r'[^0-9]', '', x.split('/')[0]))/3.3)) + '평')


    data = df.groupby(["날짜", "이름", "면적"])["가격"].min().reset_index()
    data["직전일"] = data.groupby(["이름", "면적"])["가격"].shift(1).fillna("신규")
    data[["변화", "변화량"]] = data.apply(
        lambda row: pd.Series({
            "변화": "신규" if row["직전일"] == "신규"
            else "상승" if row["가격"] > row["직전일"]
            else "하락" if row["가격"] < row["직전일"]
            else "유지",
            "변화량": row["가격"] - row["직전일"] if row["직전일"] != "신규" else None
        }),
        axis=1
    )
    return data  # 가공된 데이터 반환
