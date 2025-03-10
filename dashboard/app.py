import datetime
import pandas as pd

from shiny import App
from ui import app_ui
from server import server

# Shiny 앱 실행
app = App(app_ui, server)

if __name__ == "__main__":
    app.run()