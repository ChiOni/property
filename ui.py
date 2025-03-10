from shiny import ui

app_ui = ui.page_fluid(
    # 스타일 추가
    ui.tags.style("""
        body { 
            font-family: 'Malgun Gothic', 'AppleGothic', 'NanumGothic', sans-serif; 
            background-color: #f8f9fa;  /* 밝은 배경 */
            margin: 0; padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        h2 {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #ddd;
        }
        .input-section {
            text-align: left;
            margin-bottom: 20px;
        }
        .chart-section, .table-section {
            margin-top: 30px;
            padding: 20px;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
        }
        .table-section {
            margin-bottom: 20px;
        }
    """),

    # 전체 컨테이너
    ui.div(
        {"class": "container"},
        ui.h2("📊 부동산 가격 변화 분석"),

        # 날짜 선택
        ui.div(
            {"class": "input-section"},
            ui.input_date("selected_date", "📅 날짜 선택", value=None)
        ),

        # 차트 출력 섹션
        ui.div(
            {"class": "chart-section"},
            ui.output_plot("price_change_chart")
        ),

        # 테이블 출력 섹션
        ui.div(
            {"class": "table-section"},
            ui.output_data_frame("price_change_table")
        )
    )
)
