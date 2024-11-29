import tkinter as tk
import markdown
from tkhtmlview import HTMLLabel
from server.model import templateModel
from tkinter import messagebox  # 导入消息框模块

class display:
    def __init__(self, text, model: templateModel.TemplateModel):
        self.root = tk.Tk()  # 创建主窗口
        self.root.title(f"正在与{model.model}对话")  # 设置窗口标题
        self.root.configure(bg="#f0f0f0")  # 设置背景为浅灰色

        # 创建内容区域的框架，带有内边距
        content_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)  # 填满父容器并扩展
        html_content = markdown.markdown(text)  # 将文本转换为HTML格式
        self.html_label = HTMLLabel(content_frame, background="#fff",
                                    foreground="#333")  # 创建HTML标签，背景为白色，文本为深灰色
        self.html_label.pack(fill=tk.BOTH, expand=True)  # 填满父容器并扩展
        self.html_label.set_html(html_content)  # 设置HTML内容

        # 输入区域框架
        input_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=10)
        input_frame.pack(fill=tk.X)  # 横向填满

        # 创建输入框，使用平坦样式显示
        self.input_box = tk.Entry(input_frame, font=('Arial', 14), width=50, bg="white", relief="flat")
        self.input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))  # 填满并扩展
        self.input_box.bind("<Return>", self.process_input)  # 绑定回车键处理输入

        # 创建绿色的发送按钮
        self.send_button = tk.Button(input_frame, text="发送", height=2, width=10, bg="#4CAF50", fg="white", relief="flat",
                                     command=self.process_input)  # 绑定按钮点击事件
        self.send_button.pack(side=tk.RIGHT)  # 将按钮放到右边

        self.root.minsize(600, 400)  # 设置窗口的最小尺寸
        self.root.mainloop()  # 启动主循环


    def process_input(self, event=None):
        # 从输入框获取内容
        input_content = self.input_box.get()
        if input_content.strip():  # 检查输入内容是否为空
            print(f"输入框内容: {input_content}")  # 输出输入框内容到控制台
            # 处理后清空输入框
            self.input_box.delete(0, tk.END)  # 清除输入框内容
            return input_content
        else:
            # 提示用户输入框为空
            messagebox.showwarning("输入错误", "输入框不能为空!")  # 弹出警告窗口

if __name__ == '__main__':
    try:
        model = templateModel.TemplateModel()  # 创建模型实例
        model.model = "小明"  # 设置模型名称
        display_dialog = display(markdown.markdown(f"欢迎与{model.model}对话！"), model)  # 初始化对话框并显示欢迎信息
    except Exception as e:
        print(f"发生错误: {e}")  # 输出错误信息
