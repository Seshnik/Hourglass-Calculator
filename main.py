import math
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFontDatabase, QIntValidator, QDoubleValidator
from hourglass_ui import Ui_MainWindow

# --- Constants ---
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 400
FONT_FAMILY = "True Winds"
FONT_SIZE_LARGE = 24
FONT_SIZE_MEDIUM = 18
FONT_SIZE_SMALL = 14

# --- Color Scheme ---
BG_COLOR = "#23192f"
TEXT_COLOR = "#1fe3b1"
ACCENT_COLOR = "#ff5733"  # ?

# --- Exp Boost Constants ---
BOOST_OPTIONS = [
    "None",
    "Gold & Glory",
    "Community Day"
]

BOOST_VALUES = {
    "Gold & Glory Weekend": 2,
    "Community Day": 2.5,
}

appVersion = "v1.0"


# --- Function to calculate Hourglass XP needed ---
# def calculate_hourglass_xp():
#     try:
#         current_level = int(current_level_entry.get())
#         target_level = int(target_level_entry.get())
#         winrate = float(winrate_entry.get()) / 100
#         selected_boost = boost_dropdown.get()
#         boost_multiplier = BOOST_VALUES.get(selected_boost, 1)
#
#         # Calculate total XP needed
#         total_xp_needed = 0
#         for i in range(current_level + 1, target_level + 1):
#             total_xp_needed += math.ceil(50 * i * 1.15)
#
#         # Calculate XP per Hourglass (adjusted for winrate and boost)
#         xp_per_hourglass = 500 * winrate * boost_multiplier
#
#         # Calculate number of Hourglasses needed
#         hourglasses_needed = math.ceil(total_xp_needed / xp_per_hourglass)
#
#         # Update results# --- Main GUI Window ---

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up the UI Elements and direct them to the correct functions.
        self.setWindowTitle(f"Hourglass Calculator - {appVersion}")

        # Set input fields to accept only numbers
        int_validator = QIntValidator()
        self.ui.textEdit_C_LVL.setValidator(int_validator)
        self.ui.textEdit_T_LVL.setValidator(int_validator)
        double_validator = QDoubleValidator()
        self.ui.textEdit_WINRATE.setValidator(double_validator)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Load the font from the resource file
    font_database = QtGui.QFontDatabase()
    font_id = font_database.addApplicationFont(":/font/TradeWinds-Regular.ttf")
    if font_id == -1:
        print("Failed to load Trade Winds font!")
    else:
        print("Trade Winds font loaded successfully!")
    font_family = font_database.applicationFontFamilies(font_id)[0]

    # Set the global font
    font = QtGui.QFont(font_family)
    app.setFont(font)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
