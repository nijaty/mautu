import html
import re

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtWidgets import QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QWidget


def _make_snippet(content, query, radius=80):
    """Return a short plain-text excerpt of content around the first match of query."""
    text = re.sub(r'<[^>]+>', '', content or '')              # HTML tags
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)            # images
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)         # links -> text
    text = re.sub(r'[#*`>|_~]+', ' ', text)                    # markdown symbols
    text = html.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    idx = text.lower().find(query.lower())
    if idx < 0:
        return text[:2 * radius] + ('…' if len(text) > 2 * radius else '')
    start = max(0, idx - radius)
    end = min(len(text), idx + len(query) + radius)
    return ('…' if start > 0 else '') + text[start:end] + ('…' if end < len(text) else '')


def _highlight(text, query):
    """HTML-escape text and bold every case-insensitive occurrence of query."""
    escaped = html.escape(text)
    pattern = re.compile(re.escape(html.escape(query)), re.IGNORECASE)
    return pattern.sub(lambda m: f'<b style="color: rgb(112, 163, 94);">{m.group(0)}</b>', escaped)


class SearchResultsWidget(QWidget):
    """Lists every manual matching a search query; clicking one opens it."""

    manual_selected = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        self.header = QLabel()
        self.header.setStyleSheet("color: rgb(112, 163, 94); font-size: 18px; font-weight: bold;")
        layout.addWidget(self.header)

        self.list = QListWidget()
        self.list.setStyleSheet("""
            QListWidget {
                background-color: white;
                color: black;
                border: none;
            }
            QListWidget::item {
                border-bottom: 1px solid #dddddd;
            }
            QListWidget::item:hover {
                background-color: #f0f7ed;
            }
            QListWidget::item:selected {
                background-color: #e1efdb;
            }
        """)
        self.list.setVerticalScrollMode(QListWidget.ScrollMode.ScrollPerPixel)
        self.list.itemActivated.connect(self._on_item_activated)
        self.list.itemClicked.connect(self._on_item_activated)
        layout.addWidget(self.list)

    def set_results(self, query, results):
        """results: rows of (id, title, category_name, content)."""
        self.list.clear()
        self.header.setText(f"Found {len(results)} manual(s) for “{query}”")
        for row in results:
            manual_id, title, category, content = row[0], row[1], row[2], row[3]
            snippet = _make_snippet(content, query)
            label = QLabel(
                f'<div style="font-size: 15px; font-weight: bold;">{_highlight(title, query)}</div>'
                f'<div style="color: #777777; font-size: 12px;">{html.escape(category or "")}</div>'
                f'<div style="color: #333333; font-size: 13px;">{_highlight(snippet, query)}</div>'
            )
            label.setTextFormat(Qt.TextFormat.RichText)
            label.setWordWrap(True)
            label.setStyleSheet("background: transparent; color: black; padding: 8px;")
            label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, manual_id)
            self.list.addItem(item)
            self.list.setItemWidget(item, label)
        self._update_item_heights()

    def _update_item_heights(self):
        width = self.list.viewport().width()
        for i in range(self.list.count()):
            item = self.list.item(i)
            label = self.list.itemWidget(item)
            if label is not None:
                item.setSizeHint(QSize(width, label.heightForWidth(width)))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_item_heights()

    def _on_item_activated(self, item):
        self.manual_selected.emit(item.data(Qt.ItemDataRole.UserRole))
