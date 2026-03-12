import re
import markdown as md
from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import HtmlFormatter
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QToolBar
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal

from pygments.style import Style
from pygments.token import Keyword, Name, String, Number, Comment, Operator, Punctuation, Generic

class _MautuStyle(Style):
    background_color = 'transparent'
    styles = {
        Keyword:            'bold #e87d0d',  # orange
        Keyword.Declaration:'bold #e87d0d',
        String:             '#219161',
        Number:             '#ae81ff',
        Comment:            'italic #888888',
        Name.Builtin:       '#e87d0d',
        Operator:           '#666666',
        Generic.Heading:    'bold',
    }

_formatter = HtmlFormatter(noclasses=True, style=_MautuStyle)

def _highlight_code_blocks(html):
    """Replace fenced code blocks with Pygments inline-styled versions."""
    def _replace(match):
        lang = match.group(1) or ''
        code = match.group(2)
        code = code.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
        try:
            lexer = get_lexer_by_name(lang) if lang else TextLexer()
        except Exception:
            lexer = TextLexer()
        return highlight(code, lexer, _formatter)
    return re.sub(
        r'<pre><code(?:\s+class="language-([^"]*)")?>(.*?)</code></pre>',
        _replace, html, flags=re.DOTALL
    )

class ManualViewer(QWidget):
    """Widget for displaying manual content with formatting controls."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_manual_id = None
        self.font_size = 14
        self.setup_ui()

    def setup_ui(self):
        """Initialize the UI components."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Toolbar with font controls
        toolbar = QToolBar()
        toolbar.setStyleSheet("""
            QToolBar {
                background-color: transparent;
                border: none;
                spacing: 8px;
                padding: 5px;
            }
            QToolButton {
                background-color: transparent;
                color: rgb(112, 163, 94);
                border: none;
                border-radius: none;
                padding: 2px 2px;
                font-weight: bold;
                font-size: 20px;
                min-width: 40px;
            }
            QToolButton:hover {
                background-color: transparent;
            }
            QToolButton:pressed {
                background-color: transparent;
            }
        """)

        # Font size increase
        font_increase = QAction("A+", self)
        font_increase.setToolTip("Increase font size")
        font_increase.triggered.connect(self.increase_font)
        toolbar.addAction(font_increase)

        # Font size decrease
        font_decrease = QAction("A-", self)
        font_decrease.setToolTip("Decrease font size")
        font_decrease.triggered.connect(self.decrease_font)
        toolbar.addAction(font_decrease)

        layout.addWidget(toolbar)

        # Content viewer
        self.text_browser = QTextBrowser()
        self.text_browser.setOpenExternalLinks(True)
        self.text_browser.setStyleSheet(f"""
            QTextBrowser {{
                background-color: rgb(222, 221, 218);
                border-radius: 20px;
                padding: 20px;
                font-size: {self.font_size}px;
            }}
        """)
        layout.addWidget(self.text_browser)

    def set_content(self, manual_data):
        """Display manual content.

        Args:
            manual_data: Tuple of (id, title, content, category_name)
        """
        if manual_data:
            self.current_manual_id = manual_data[0]
            title = manual_data[1]
            content = manual_data[2]
            category = manual_data[3]

            body = md.markdown(content, extensions=['fenced_code', 'tables'])
            body = _highlight_code_blocks(body)
            html = f"""
            <h1>{title}</h1>
            <p style="color: #70a35e;"><i>{category}</i></p>
            <hr>
            {body}
            """
            self.text_browser.setHtml(html)

    def increase_font(self):
        """Increase the font size."""
        self.font_size += 2
        self.update_font_size()

    def decrease_font(self):
        """Decrease the font size."""
        if self.font_size > 8:
            self.font_size -= 2
            self.update_font_size()

    def update_font_size(self):
        """Apply the current font size to the text browser."""
        self.text_browser.setStyleSheet(f"""
            QTextBrowser {{
                background-color: rgb(222, 221, 218);
                border-radius: 20px;
                padding: 20px;
                font-size: {self.font_size}px;
            }}
        """)
