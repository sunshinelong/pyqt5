# 开发时间： 2022/11/4 14:18
import sys
from PyQt5.QtWidgets import QApplication, QWidget
# demo
if __name__ == '__main__':
    # 创建QApplacation类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(400, 200)
    # 移动窗口
    w.move(300, 300)
    # 设置窗口标题
    w.setWindowTitle('PyQt5')
    # 显示窗口
    w.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
