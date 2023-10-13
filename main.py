import pandas as pd
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFileDialog,
                               QMessageBox, QApplication, QMainWindow, QStatusBar,
                               QLabel, QHBoxLayout)
from classes import ConfigurationWindow
import sys
import os

CONFIGURATION_FILEPATH = 'data/configuration-tables.xlsx'
CHOICES_TABLES_FILEPATH = 'data/choices-tables.xlsx'
REQUIRED_WORKSHEETS = ['Social Roles', 'Social Contexts',
                       'Social Interaction Choices',
                       'Social Interaction Results']
DIFFICULTY_VARIATIONS = ['A', 'B', 'C', 'D']
INDIVIDUAL_LEVEL = ['Low', 'Moderate', 'Advanced', 'Elite']


class StartupWindow(QMainWindow):
    def __init__(self, filepath=CONFIGURATION_FILEPATH):
        super().__init__()
        # Initialize to None the attributes handled by methods.
        # init_ui, load_configuration_tables, validate_tables,
        # and start_npc_interaction_window.
        self.config_path = filepath
        self.vbox = None
        self.statusbar = None
        self.required_config_dfs = None
        self.config_window = None
        self.npc_reactions_window = None
        self.init_ui()
        self.load_configuration_tables()
        self.validate_tables()

    def init_ui(self):
        self.setWindowTitle('NPC Reactions Modeler')
        self.setMinimumSize(300, 400)

        # Add main buttons.
        show_button = QPushButton("Show Configuration Tables")
        show_button.clicked.connect(self.show_configuration_tables)
        reload_config_button = QPushButton("Reload Configuration Tables")
        reload_config_button.clicked.connect(self.load_configuration_tables)
        start_button = QPushButton("Start NPC Interactions")
        start_button.clicked.connect(self.start_npc_interaction_window)
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit_app)
        self.setCentralWidget(QWidget(self))
        self.vbox = QVBoxLayout()
        self.centralWidget().setLayout(self.vbox)
        self.vbox.addWidget(show_button)
        self.vbox.addWidget(reload_config_button)
        self.vbox.addWidget(start_button)
        self.vbox.addWidget(exit_button)

        # Create status bar.
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

    def load_configuration_tables(self):
        if os.path.exists(self.config_path):
            # Load Excel sheets into pandas DataFrames.
            xls = pd.ExcelFile(self.config_path)
            required_worksheets = REQUIRED_WORKSHEETS
            self.required_config_dfs = {}
            for worksheet in required_worksheets:
                try:
                    self.required_config_dfs[worksheet] = pd.read_excel(xls, worksheet)
                except ValueError:
                    QMessageBox.critical(self, "Error",
                                         f"Required {worksheet} not found in "
                                         f"{self.config_path}")
            print(f"self.required_config_dfs: {self.required_config_dfs}")
            config_found_label = QLabel('Config loaded successfully.')
            self.statusbar.addWidget(config_found_label)

        else:
            QMessageBox.critical(self, 'Fatal Error',
                                 'Required Configuration file, '
                                 'configuration-tables.xlsx not found in /data')

    def validate_tables(self):
        pass

    def show_configuration_tables(self):
        self.config_window = ConfigurationWindow(self.required_config_dfs)
        self.config_window.exec()

    def start_npc_interaction_window(self):
        pass

    def exit_app(self):
        sys.exit()


if __name__ == "__main__":
    sys.argv += ['-platform', 'windows:darkmode=2']
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = StartupWindow()
    window.show()
    sys.exit(app.exec())