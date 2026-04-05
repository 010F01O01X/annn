from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QLabel, QListWidget, QTextEdit
)
from PyQt5.QtCore import QTimer

from core.price import get_price
from core.news import get_news
from core.analyzer import analyze


def run_app():
    app = QApplication([])

    window = QWidget()
    window.setWindowTitle("Trading Assistant PRO")

    main_layout = QHBoxLayout()

    # 🔹 SOL PANEL (PORTFÖY)
    left_layout = QVBoxLayout()
    stock_input = QLineEdit()
    stock_input.setPlaceholderText("Hisse ekle (ASELS)")

    add_button = QPushButton("Takibe Ekle")
    stock_list = QListWidget()

    left_layout.addWidget(stock_input)
    left_layout.addWidget(add_button)
    left_layout.addWidget(QLabel("Portföy"))
    left_layout.addWidget(stock_list)

    # 🔹 ORTA PANEL (HABERLER)
    middle_layout = QVBoxLayout()
    news_button = QPushButton("Haberleri Getir")
    news_area = QTextEdit()
    news_area.setReadOnly(True)

    middle_layout.addWidget(news_button)
    middle_layout.addWidget(QLabel("Haberler"))
    middle_layout.addWidget(news_area)

    # 🔹 SAĞ PANEL (ANALİZ)
    right_layout = QVBoxLayout()
    price_label = QLabel("Fiyatlar burada")
    analysis_label = QLabel("Analiz burada")

    right_layout.addWidget(QLabel("Canlı Fiyatlar"))
    right_layout.addWidget(price_label)
    right_layout.addWidget(QLabel("Analiz"))
    right_layout.addWidget(analysis_label)

    # Layoutları birleştir
    main_layout.addLayout(left_layout)
    main_layout.addLayout(middle_layout)
    main_layout.addLayout(right_layout)

    window.setLayout(main_layout)

    stocks = []

    # 🔹 HİSSE EKLEME
    def add_stock():
        stock = stock_input.text().upper()

        if stock and stock not in stocks:
            stocks.append(stock)
            stock_list.addItem(stock)

    add_button.clicked.connect(add_stock)

    # 🔹 CANLI FİYAT GÜNCELLEME (SİLMEZ!)
    def update_prices():
        text = ""

        for stock in stocks:
            price = get_price(stock)
            if price:
                text += f"{stock}: {price} TL\n"

        price_label.setText(text)

    timer = QTimer()
    timer.timeout.connect(update_prices)
    timer.start(5000)

    # 🔹 HABERLERİ GÖSTER (AYRI PANEL)
    def show_news():
        selected = stock_list.currentItem()

        if not selected:
            news_area.setText("Lütfen bir hisse seç")
            return

        stock = selected.text()

        news = get_news(stock)
        decision = analyze(news)

        news_text = ""

        for n in news:
            news_text += f"{n['title']}\n({n['sentiment']})\n\n"

        news_area.setText(news_text)
        analysis_label.setText(f"GENEL KARAR: {decision}")

    news_button.clicked.connect(show_news)

    window.resize(900, 500)
    window.show()

    app.exec_()