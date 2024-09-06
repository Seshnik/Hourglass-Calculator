import math
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QFontDatabase, QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QMessageBox
from packaging import version
from hourglass_ui import Ui_MainWindow
import webbrowser
import requests

# Pyinstaller:
# pyinstaller --onefile --windowed --add-data "res_rc.py;." --add-data "hourglass_ui.py;." --name HourglassCalc main.py

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

BOOST_VALUES = {
    "None": 1,
    "Gold & Glory": 2,
    "Community Day": 2.5,
}

# --- Exp Constants ---
xp_required = {
    1: 0,
    2: 2000,
    3: 3278,
    4: 4033,
    5: 4618,
    6: 5108,
    7: 5535,
    8: 5919,
    9: 6267,
    10: 6590,
    11: 6890,
    12: 7171,
    13: 7437,
    14: 7690,
    15: 7929,
    16: 8160,
    17: 8381,
    18: 8593,
    19: 8797,
    20: 8995,
    21: 9187,
    22: 9373,
    23: 9552,
    24: 9728,
    25: 9899,
    26: 10065,
    27: 10227,
    28: 10386,
    29: 10541,
    30: 10693,
    31: 10842,
    32: 10986,
    33: 11130,
    34: 11270,
    35: 11407,
    36: 11542,
    37: 11674,
    38: 11805,
    39: 11934,
    40: 12060,
    41: 12184,
    42: 12306,
    43: 12428,
    44: 12546,
    45: 12663,
    46: 12779,
    47: 12894,
    48: 13005,
    49: 13117,
    50: 13227,
    51: 13335,
    52: 13443,
    53: 13556,
    54: 13652,
    55: 13726,
    56: 13800,
    57: 13960,
    58: 14059,
    59: 14159,
    60: 14257,
    61: 14353,
    62: 14450,
    63: 14545,
    64: 14639,
    65: 14732,
    66: 14825,
    67: 14916,
    68: 15006,
    69: 15097,
    70: 15186,
    71: 15274,
    72: 15361,
    73: 15435,
    74: 15535,
    75: 15619,
    76: 15705,
    77: 15788,
    78: 15872,
    79: 15954,
    80: 16036,
    81: 16118,
    82: 16198,
    83: 16279,
    84: 16359,
    85: 16437,
    86: 16516,
    87: 16593,
    88: 16672,
    89: 16747,
    90: 16825,
    91: 16900,
    92: 16975,
    93: 17050,
    94: 17124,
    95: 17199,
    96: 17271,
    97: 17344,
    98: 17417,
    99: 17489,
    100: 17560,
    101: 12600
}

# --- App Version ---
appVersion = "v1.1.0"


class WinRateDialog(QtWidgets.QDialog):
    def __init__(self, main_window, parent=None):
        super(WinRateDialog, self).__init__(parent)
        self.main_window = main_window

        # Set window title and flags
        self.setWindowTitle("Win Rate Calculator")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        # Set fixed size for the dialog to prevent resizing
        self.setFixedSize(400, 400)  # Adjust size as needed

        # Create widgets
        self.instructions_label = QtWidgets.QLabel(
            "Go to your specific Hourglass faction milestones (In-Game or on the SoT Website) "
            "and locate the 3 required values needed below.")
        self.instructions_label.setWordWrap(True)
        self.label_completed = QtWidgets.QLabel("Battles Completed:")
        self.label_won_invade = QtWidgets.QLabel("Battles Won by Seeking:")
        self.label_won_repel = QtWidgets.QLabel("Battles Won by Repelling:")
        self.input_completed = QtWidgets.QLineEdit()
        self.input_won_invade = QtWidgets.QLineEdit()
        self.input_won_repel = QtWidgets.QLineEdit()
        # Set 0 in each input field by default
        self.input_completed.setText("0")
        self.input_won_invade.setText("0")
        self.input_won_repel.setText("0")
        self.button_calculate = QtWidgets.QPushButton("Calculate")
        self.result_label = QtWidgets.QLabel("Win Rate: N/A")
        self.button_help = QtWidgets.QPushButton("Open SoT Milestones Site")  # Custom help button

        # Set up layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.instructions_label)
        layout.addWidget(self.label_completed)
        layout.addWidget(self.input_completed)
        layout.addWidget(self.label_won_invade)
        layout.addWidget(self.input_won_invade)
        layout.addWidget(self.label_won_repel)
        layout.addWidget(self.input_won_repel)
        layout.addWidget(self.button_calculate)
        layout.addWidget(self.result_label)
        layout.addWidget(self.button_help)  # Add the custom help button
        self.setLayout(layout)

        # Apply CSS styling
        self.setStyleSheet("""
            QDialog {
                background-image: url(:/bg/bg.png);  /* Background image from the main GUI */
                background-color: #23192f;  /* Fallback background color */
                color: #1fe3b1;
            }
            QLabel {
                color: #1fe3b1;
            }
            QLineEdit {
                border-radius: 5px;
                border: 2px solid #1fe3b1;
                background-color: #23192f;
                color: #1fe3b1;
            }
            QPushButton {
                background-color: #1fe3b1;
                color: #23192f;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #fff;
                color: #23192f;
            }
            QPushButton:pressed {
                background-color: #23192f;
                color: #1fe3b1;
            }
        """)

        # Input validators
        int_validator = QtGui.QIntValidator()  # Allows only integers
        self.input_completed.setValidator(int_validator)
        self.input_won_invade.setValidator(int_validator)
        self.input_won_repel.setValidator(int_validator)

        # Connect the calculate button and help button to their functions
        self.button_calculate.clicked.connect(self.calculate_win_rate)
        self.button_help.clicked.connect(self.open_help_url)  # Connect custom help button to URL opening

    def open_help_url(self):
        url = "https://www.seaofthieves.com/profile/captaincy/milestones/"
        webbrowser.open(url)

    def calculate_win_rate(self):
        def get_valid_int(value):
            try:
                return int(value)
            except ValueError:
                return 0

        try:
            # Retrieve and convert input values, defaulting to 0 if invalid
            completed = get_valid_int(self.input_completed.text())
            won_invade = get_valid_int(self.input_won_invade.text())
            won_repel = get_valid_int(self.input_won_repel.text())

            # Calculate total wins
            total_wins = won_invade + won_repel

            # Calculate win rate
            if completed == 0:
                win_rate = 0
            else:
                win_rate = (total_wins / completed) * 100

            if completed < total_wins:
                self.result_label.setText("Win Rate: Invalid input!\nWins cannot exceed battles completed.")
            else:
                # Update result label with formatted win rate
                self.result_label.setText(f"Win Rate: {win_rate:.2f}%")
                self.main_window.ui.textEdit_WINRATE.setText(str(win_rate))

        except ValueError:
            # Handle invalid input (e.g., non-numeric values)
            self.result_label.setText("Win Rate: Invalid input")


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

        # Connect actions
        self.ui.actionUpdate.triggered.connect(self.check_for_updates)
        self.ui.actionEvents.triggered.connect(self.show_events_popup)
        self.ui.actionWin_Rate.triggered.connect(self.show_win_rate_dialog)

        # Calculate button
        self.ui.pushButton_CALC.clicked.connect(self.main_calc)

        # Save Button
        self.ui.pushButton_SAVE.setEnabled(False)
        self.ui.pushButton_SAVE.clicked.connect(self.save_data)

        # Set up the checkbox
        self.ui.checkbox.setStyleSheet("""
QCheckBox {
    font-size: 14px;
    color: #1fe3b1;
}
QCheckBox::indicator {
    width: 20px;
    height: 20px;
}
QCheckBox::indicator:checked {
    background-color: #1fe3b1;
}
QCheckBox::indicator:unchecked {
    background-color: #fff;
}
""")

    def check_for_updates(self):
        repo_url = "Seshnik/Hourglass-Calculator"
        current_version = appVersion
        my_StyleSheet = ("""
                           QMessageBox {
                               background-image: url(:/bg/bg.png);  /* Background image from the main GUI */
                               background-color: #23192f;  /* Fallback background color */
                               color: #1fe3b1;
                           }
                           QMessageBox QLabel {
                               color: #1fe3b1;
                           }
                           QMessageBox QPushButton {
                               background-color: #1fe3b1;
                               color: #23192f;
                               border-radius: 5px;
                           }
                           QMessageBox QPushButton:hover {
                               background-color: #fff;
                               color: #23192f;
                           }
                           QMessageBox QPushButton:pressed {
                               background-color: #23192f;
                               color: #1fe3b1;
                           }
                       """)
        latest_version = self.get_latest_version(repo_url)
        if latest_version:
            msg = QMessageBox(self)

            if self.is_update_available(current_version, latest_version):
                msg.setIcon(QMessageBox.Information)
                msg.setText(f"A new version ({latest_version}) is available. Please update your application.")
                msg.setWindowTitle("Update Available")
                msg.setStandardButtons(QMessageBox.Ok)

                # Apply custom style sheet
                msg.setStyleSheet(my_StyleSheet)
                result = msg.exec_()

                if result == QMessageBox.Ok:
                    release_url = f"https://github.com/{repo_url}/releases"
                    webbrowser.open(release_url)
            else:
                msg.setIcon(QMessageBox.Information)
                msg.setText("Your application is up-to-date.")
                msg.setWindowTitle("Up-to-Date")
                msg.setStandardButtons(QMessageBox.Ok)

                # Apply custom style sheet
                msg.setStyleSheet(my_StyleSheet)

                msg.exec_()

    def is_update_available(self, current_version, latest_version):
        return version.parse(latest_version) > version.parse(current_version)

    def get_latest_version(self, repo_url):
        try:
            # GitHub API URL for latest release
            api_url = f"https://api.github.com/repos/{repo_url}/releases/latest"
            response = requests.get(api_url)
            response.raise_for_status()  # Check if request was successful
            latest_release = response.json()
            latest_version = latest_release['tag_name']
            return latest_version
        except requests.RequestException as e:
            print(f"Error fetching latest version: {e}")
            return None

    def save_data(self):
        # Grab the data from the label
        data = self.ui.label.text()
        date = QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd_hh-mm-ss")
        filename = f"saved_{date}.txt"
        with open(filename, "w") as file:
            file.write(data)
        print(f"Data saved to {filename}")
        self.ui.pushButton_SAVE.setText("Saved!")
        self.ui.pushButton_SAVE.setEnabled(False)

    def open_update_url(self):
        webbrowser.open("https://github.com/Seshnik/Hourglass-Calculator/releases")

    def show_events_popup(self):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle("Events / EXP")

        # Use HTML to format text with right alignment
        msg_box.setText("""
            <div style="text-align: left;">
                <h3>Events</h3>
                <p>Some events can give you a boost in Hourglass EXP.<br>
                Select the relevant Event if it's listed in the app.</p>
                <p>If I missed an event, please let me know by raising an issue on the GitHub repo.</p>
            </div>
        """)
        msg_box.setIcon(QtWidgets.QMessageBox.Information)

        # Apply CSS styling
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #23192f;
            }
            QMessageBox QLabel {
                color: #1fe3b1;  /* This sets the text color */
                font-size: 14px;
            }
            QPushButton {
                background-color: #1fe3b1;
                color: #23192f;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1fe3b1;
                color: #23192f;
            }
        """)

        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    def show_win_rate_dialog(self):
        dialog = WinRateDialog(self)
        dialog.exec_()

    def calculate_best_streak(self, win_rate):
        # XP values for each streak level
        WIN_XP = {
            1: 4200,
            2: 4675,
            3: 5190,
            4: 5688,
            5: 6600,
            6: 6600
        }

        #win_rate = win_rate / 100

        # Initialize variables to track the best streak
        best_streak = 1
        highest_expected_xp = WIN_XP[1] * win_rate

        # Iterate through possible streak levels
        for streak in range(2, 7):
            # Calculate probability of maintaining the streak
            streak_probability = win_rate ** streak

            # Calculate expected XP per battle for this streak level
            expected_xp = WIN_XP[streak] * streak_probability

            # Update the best streak if this one has a higher expected XP
            if expected_xp > highest_expected_xp:
                highest_expected_xp = expected_xp
                best_streak = streak

        return best_streak, highest_expected_xp

    def main_calc(self):
        # Default Button Settings
        button_text = "Calculate"
        button_style = "background-color: #1fe3b1; color: #23192f;"

        # LossFarm
        if self.ui.checkbox.isChecked():
            lossFarming = True
        else:
            lossFarming = False

        # Disable the calc button
        self.ui.pushButton_CALC.setEnabled(False)
        self.ui.pushButton_CALC.setText("Processing")
        self.ui.pushButton_CALC.setStyleSheet("background-color: #ff5733; color: #23192f;")
        self.ui.pushButton_SAVE.setEnabled(False)
        self.ui.pushButton_SAVE.setText("Save")

        # Grab the values from the input fields
        try:
            current_lvl = int(self.ui.textEdit_C_LVL.text())
            target_lvl = int(self.ui.textEdit_T_LVL.text())
            win_rate = float(self.ui.textEdit_WINRATE.text()) / 100
            boost = self.ui.comboBox.currentText()
        except ValueError:
            self.ui.label.setText("Please enter valid numbers.")
            self.ui.label.setStyleSheet("color: #ff5733; padding: 2px;")
            self.ui.label.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.pushButton_CALC.setEnabled(True)
            self.ui.pushButton_CALC.setText(button_text)
            self.ui.pushButton_CALC.setStyleSheet(button_style)
            return

        # Check boost against the dictionary and set the value
        boost_value = float(BOOST_VALUES.get(boost, 1))
        print(f"Boost Value: {boost_value}")

        # Check if the input fields are empty
        if current_lvl == "" or target_lvl == "" or win_rate == "":
            self.ui.label.setText("Please fill in all fields.")
            self.ui.label.setStyleSheet("color: #ff5733; padding: 2px;")
            self.ui.label.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.pushButton_CALC.setEnabled(True)
            self.ui.pushButton_CALC.setText(button_text)
            self.ui.pushButton_CALC.setStyleSheet(button_style)
            return

        # default label stuff
        # self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        # padding: 2px; color: #1fe3b1;

        # Define constants
        GAME_TIME = 10  # minutes per battle
        LOWER_TIME = 10  # minutes to lower streak
        LOSS_EXP = 700  # Experience for a loss

        # XP for winning streaks and lowering bonuses
        WIN_XP = {
            1: 4200,
            2: 4675,
            3: 5190,
            4: 5688,
            5: 6600,
            6: 6600
        }

        # Bonus XP when lowering a streak
        LOWER_XP = {
            1: 1100,
            2: 2640,
            3: 4680,
            4: 7800,
            5: 10800,
            6: 13800,
            7: 16800,
            8: 19800,
            9: 22800,
            10: 25800,
            11: 28800,
            12: 31800,
            13: 34800,
            14: 37800,
            15: 40800,
            16: 43800,
            17: 46800,
            18: 49800,
            19: 52800,
            20: 55800
        }

        if current_lvl < 1 or target_lvl < 1 or current_lvl > target_lvl:
            self.ui.label.setText("Invalid level range entered.")
            self.ui.label.setStyleSheet("color: #ff5733; padding: 2px;")
            self.ui.label.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.pushButton_CALC.setEnabled(True)
            self.ui.pushButton_CALC.setText(button_text)
            self.ui.pushButton_CALC.setStyleSheet(button_style)
            self.ui.pushButton_SAVE.setEnabled(False)
            return

        optimal_streaks = {
            0.10: 2,
            0.30: 2,
            0.50: 4,
            0.60: 4,
            0.70: 5,
            0.80: 6,  # 8
            0.90: 6,  # 12
            0.95: 6  # 17
        }

        def get_recommended_streak(winrate):
            # Find the closest win rate in the dictionary
            closest_winrate = min(optimal_streaks.keys(), key=lambda k: abs(k - winrate))
            return optimal_streaks[closest_winrate]

        recommended_streak = get_recommended_streak(win_rate)
        print(f"Recommended Streak for Winrate {win_rate}: {recommended_streak}")

        def calculate_xp_required(start_lvl, end_lvl):
            print(f"Calculating XP required from level {start_lvl} to level {end_lvl}")
            total_xp = 0
            for lvl in range(start_lvl, end_lvl):
                if lvl <= 100:
                    # XP required to reach the next level
                    next_lvl_xp = xp_required.get(lvl + 1, 0)
                    total_xp += next_lvl_xp
                else:
                    # Linear XP calculation for levels beyond 101
                    total_xp += 12600
            return total_xp

        # Calculate XP required to reach target level
        xp_required_to_target = calculate_xp_required(current_lvl, target_lvl)
        print(f"Total XP required to reach level {target_lvl} from level {current_lvl}: {xp_required_to_target}")

        total_xp = 0
        battles = 0
        streak = 0

        while total_xp < xp_required_to_target:
            if streak == 0:
                if lossFarming:
                    xp_per_win = 700 * boost_value
                else:
                    xp_per_win = WIN_XP.get(1, 4200) * boost_value
            else:
                if lossFarming:
                    xp_per_win = 700 * boost_value
                else:
                    xp_per_win = WIN_XP.get(min(streak + 1, recommended_streak), 6600) * boost_value

            # Add XP for the win
            total_xp += xp_per_win
            battles += 1
            if lossFarming:
                streak = 0
            else:
                streak += 1

            # Apply lower streak bonus and reset when reaching the recommended streak
            if streak >= recommended_streak:
                add_xp = LOWER_XP.get(recommended_streak, 55800) * boost_value
                total_xp += add_xp
                streak = 0

        total_time_with_lowering_minutes = battles * GAME_TIME + (battles // recommended_streak) * LOWER_TIME
        hours = total_time_with_lowering_minutes // 60
        minutes = total_time_with_lowering_minutes % 60

        # Debug Prints
        print(f"Total battles needed: {battles}")
        print(f"Total XP earned: {total_xp}")
        print(f"Total time needed: {battles * GAME_TIME} minutes")
        print(f"Total time needed with streak lowering: {hours} hours, {minutes} minutes")

        # Label
        # Format the label text
        if lossFarming:
            label_text = (
                f"Current Level: {current_lvl}\n"
                f"Target Level: {target_lvl}\n"
                f"Total XP: {total_xp}\n"
                f"XP Bonus: {boost_value}\n"
                f"Total Battles: {battles}\n"
                f"Estimated Time: {hours} hours and {minutes} minutes"
            )
        else:
            label_text = (
                f"Current Level: {current_lvl}\n"
                f"Target Level: {target_lvl}\n"
                f"Total XP: {total_xp}\n"
                f"XP Bonus: {boost_value}\n"
                f"Total Battles: {battles}\n"
                f"Recommended Streak: {recommended_streak}\n"
                f"Estimated Time: {hours} hours and {minutes} minutes."

            )
        # Update the label with the formatted text
        self.ui.label.setText(label_text)
        self.ui.label.setStyleSheet("padding: 2px; color: #1fe3b1;")
        self.ui.label.setAlignment(QtCore.Qt.AlignCenter)

        # Re-enable and reset button
        self.ui.pushButton_CALC.setEnabled(True)
        self.ui.pushButton_CALC.setText(button_text)
        self.ui.pushButton_CALC.setStyleSheet(button_style)

        # Enable the save button
        self.ui.pushButton_SAVE.setEnabled(True)


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
