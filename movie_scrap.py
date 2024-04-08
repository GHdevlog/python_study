import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
from PyQt5.QtCore import Qt
import requests
from bs4 import BeautifulSoup

class MovieInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CGV 영화 정보")
        self.setGeometry(100, 100, 800, 1000)

        # 표 생성 및 설정
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["제목", "개봉일", "예매율"])

        # 영화 정보 가져오기
        movies_info = self.get_movies_info()

        # 표에 데이터 추가
        self.populate_table(movies_info)

        # 표의 열 너비 자동 조정
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def get_movies_info(self):
        url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        movies_info = []
        movies = soup.select(".box-contents")

        for movie in movies:
            title = movie.select_one("strong.title").text.strip()
            release_date = movie.select_one(".txt-info:nth-of-type(1)").text.strip()[:10]
            booking_rate = movie.select_one(".percent span").text.strip()

            movies_info.append((title, release_date, booking_rate))

        return movies_info

    def populate_table(self, movies_info):
        self.table_widget.setRowCount(len(movies_info))

        for row, movie_info in enumerate(movies_info):
            for col, data in enumerate(movie_info):
                item = QTableWidgetItem(data)
                item.setTextAlignment(Qt.AlignCenter)
                self.table_widget.setItem(row, col, item)

        # 제목 열의 너비 더 넓게 설정
        self.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.table_widget.setColumnWidth(0, 400)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieInfoApp()
    window.show()
    sys.exit(app.exec_())
