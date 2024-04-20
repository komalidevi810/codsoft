import sys
import json
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TodoItem(QListWidgetItem):
    def __init__(self, text, is_completed=False):
        super().__init__(text)
        self.setCheckState(Qt.Checked if is_completed else Qt.Unchecked)
        self.setFlags(self.flags() | Qt.ItemIsUserCheckable)

    def toggle_completion(self):
        self.setCheckState(Qt.Unchecked if self.checkState() == Qt.Checked else Qt.Checked)

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.load_tasks()

    def initializeUI(self):
        # Main widget properties
        self.setWindowTitle('My Todo List')
        self.setFixedSize(400, 500)
        self.setStyleSheet("""
            background-color: #fff5e9;
            font-size: 16px;
        """)

        self.titleLabel = QLabel('My Todo List')
        self.titleLabel.setFont(QFont('Arial', 24, QFont.Bold))

        self.inputBox = QLineEdit()
        self.inputBox.setStyleSheet('QLineEdit {background: white;}')
        self.inputBox.setMinimumHeight(40)
        self.inputBox.setPlaceholderText("Enter a new task...")

        self.addButton = QPushButton('Add')
        self.addButton.setStyleSheet('QPushButton {background: #4CAF50; color: white;}')
        self.addButton.clicked.connect(self.add_todo)

        self.updateButton = QPushButton('Update')
        self.updateButton.setStyleSheet('QPushButton {background: #2196f3; color: white;}')
        self.updateButton.clicked.connect(self.update_todo)

        self.deleteButton = QPushButton('Delete')
        self.deleteButton.setStyleSheet('QPushButton {background: #f44336; color: white;}')
        self.deleteButton.clicked.connect(self.delete_todo)

        self.todoList = QListWidget()
        self.todoList.setStyleSheet('QListWidget {background: white;}')
        self.todoList.itemDoubleClicked.connect(self.toggle_todo_completion)
        self.todoList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.todoList.customContextMenuRequested.connect(self.show_context_menu)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.titleLabel, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.inputBox)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.addButton)
        self.buttonLayout.addWidget(self.updateButton)
        self.buttonLayout.addWidget(self.deleteButton)

        self.mainLayout.addLayout(self.buttonLayout)
        self.mainLayout.addWidget(self.todoList)

        self.setLayout(self.mainLayout)

    def add_todo(self):
        task_text = self.inputBox.text().strip()
        if task_text:
            todo_item = TodoItem(task_text)
            self.todoList.addItem(todo_item)
            self.inputBox.clear()
            self.save_tasks()

    def update_todo(self):
        current_item = self.todoList.currentItem()
        if current_item:
            item_text = self.inputBox.text().strip()
            if item_text:
                current_item.setText(item_text)
                self.inputBox.clear()
                self.save_tasks()

    def delete_todo(self):
        selected_items = self.todoList.selectedItems()
        if selected_items:
            for item in selected_items:
                self.todoList.takeItem(self.todoList.row(item))
            self.save_tasks()

    def toggle_todo_completion(self, item):
        if isinstance(item, TodoItem):
            item.toggle_completion()
            self.save_tasks()

    def show_context_menu(self, position):
        current_item = self.todoList.currentItem()
        if current_item:
            menu = QMenu()
            toggle_action = menu.addAction("Toggle Completion")
            delete_action = menu.addAction("Delete")
            action = menu.exec_(self.todoList.mapToGlobal(position))

            if action == toggle_action:
                self.toggle_todo_completion(current_item)
            elif action == delete_action:
                self.delete_todo()

    def load_tasks(self):
        tasks_file = "tasks.json"
        if os.path.exists(tasks_file):
            with open(tasks_file, "r") as file:
                tasks = json.load(file)
                for task_text, is_completed in tasks:
                    todo_item = TodoItem(task_text, is_completed)
                    self.todoList.addItem(todo_item)

    def save_tasks(self):
        tasks = [(self.todoList.item(i).text(), self.todoList.item(i).checkState() == Qt.Checked) for i in range(self.todoList.count())]
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    app.exec()