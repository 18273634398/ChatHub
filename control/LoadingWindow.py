import tkinter as tk
from tkinter import ttk
import time

class LoadingWindow:
    def __init__(self):
        self.root = tk.Tk()  # 创建顶级窗口
        self.root.title("加载中...")
        self.root.geometry("300x100")  # 设置窗口大小

        # 创建标签
        self.label = tk.Label(self.root, text="正在加载，请稍候...", font=("Arial", 12))
        self.label.pack(pady=10)  # 添加间距

        # 创建进度条
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=250, mode="indeterminate")
        self.progress.pack(pady=10)  # 添加间距
        self.progress.start()  # 启动进度条


    def on_loading_complete(self):
        self.progress.stop()  # 停止进度条
        self.label.config(text="加载完成！")  # 更新标签文本
        self.root.after(500, self.root.destroy)  # 1秒后关闭窗口

if __name__ == "__main__":
    root = tk.Tk()  # 创建主窗口
    loading_window = LoadingWindow()  # 创建加载窗口
    root.mainloop()  # 进入主循环
