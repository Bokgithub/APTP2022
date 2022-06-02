from src.campus.sinchon import NodeSinchon as n

row = len(n)
print('self.tableWidget.setColumnCount(2)')
print('self.tableWidget.setRowCount('f"{row}"')')
print("self.tableWidget.setHorizontalHeaderLabels(['Node', '건물 이름'])")
i = 0
for k, v in n.items():
    if '노드' not in k:
        print("self.tableWidget.setItem(" + f'{i}' + ", 0, QtWidgets.QTableWidgetItem(" + "'" + f'{k}' + "'" + "))")
        print("self.tableWidget.setItem("f'{i}'", 1, QtWidgets.QTableWidgetItem(" + "'" + f'{v[0]}' + "'" + "))")
        i += 1