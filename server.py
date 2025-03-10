# server.py
import pandas as pd
from shiny import render
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 로컬 폰트 경로 (배포된 프로젝트 폴더 내 위치)
font_path = "/NanumGothic.ttf"
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()
plt.rcParams["axes.unicode_minus"] = False  # 음수 기호 깨짐 방지

def server(input, output, session):

    from data import load_shift1_change
    shift1_change = load_shift1_change()

    @output
    @render.plot
    def price_change_chart():
        selected_date = pd.to_datetime(input.selected_date())
        if selected_date is None:
            return None

        daily_ratio = shift1_change[shift1_change["날짜"] == selected_date]["변화"].value_counts(normalize=True)

        plt.figure(figsize=(8, 5))
        daily_ratio.plot(kind="bar", color=["red", "blue", "green", "gray"][len(daily_ratio)])
        plt.title(f"{selected_date.date()} 최저가 변화 비율")
        plt.ylabel("비율 (%)")
        plt.xticks(rotation=0)
        plt.grid(axis="y")
        return plt.gcf()

    @output
    @render.data_frame
    def price_change_table():
        selected_date = pd.to_datetime(input.selected_date())
        if selected_date is None:
            return None
        return shift1_change[shift1_change["날짜"] == selected_date][["이름", "면적", "가격", "직전일", "변화", "변화량"]].sort_values(by="변화량", ascending=True)
