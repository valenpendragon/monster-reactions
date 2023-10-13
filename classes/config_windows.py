import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox, \
    QApplication, QMainWindow, QStatusBar, QLabel, QHBoxLayout, QDialog, QTableView, \
    QGridLayout, QDialogButtonBox
import sys
import os

CONFIGURATION_FILEPATH = '../data/configuration-tables.xlsx'
REQUIRED_WORKSHEETS = ['Social Roles', 'Social Contexts',
                       'Social Interaction Choices',
                       'Social Interaction Results']


class ConfigurationWindow(QDialog):
    def __init__(self, required_config_dfs):
        super().__init__()
        pass
