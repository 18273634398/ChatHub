import tkinter as tk
import markdown
from tkhtmlview import HTMLLabel
from server.model import templateModel
from tkinter import messagebox,ttk  # 导入消息框模块
import threading  # 导入线程模块

# 加载窗口类
class LoadingWindow:
    def __init__(self):
        self.root = tk.Toplevel()  # 创建新的顶层窗口
        self.root.title("加载中")
        self.root.geometry("200x100")
        self.root.configure(bg="#f0f0f0")

        # 创建标签
        self.label = tk.Label(self.root, text="正在加载，请稍候...", font=("Arial", 12))
        self.label.pack(pady=10)  # 添加间距

        # 创建进度条
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=250, mode="indeterminate")
        self.progress.pack(pady=10)  # 添加间距
        self.progress.start()  # 启动进度条

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # 防止用户关闭窗口

    def on_closing(self):
        pass  # 禁用关闭按钮

    def close(self):
        self.root.destroy()  # 关闭加载窗口


class chatClient:
    def __init__(self, text, model: templateModel.TemplateModel, message):
        self.message = message
        self.model = model
        self.root = tk.Tk()  # 创建主窗口
        self.root.title(f"正在与{self.model.model}对话")  # 设置窗口标题
        self.root.configure(bg="#f0f0f0")  # 设置背景为浅灰色

        # 创建内容区域的框架，带有内边距
        self.content_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        self.content_frame.pack(fill=tk.BOTH, expand=True)  # 填满父容器并扩展
        self.html_label = HTMLLabel(self.content_frame, background="#fff", foreground="#333")  # 创建HTML标签
        self.html_label.pack(fill=tk.BOTH, expand=True)  # 填满父容器并扩展

        self.dialog_content = text  # 初始化对话内容
        self.set_html_content(self.dialog_content)  # 设置初始HTML内容

        # 输入区域框架
        input_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=10)
        input_frame.pack(fill=tk.X)  # 横向填满

        # 创建输入框
        self.input_box = tk.Entry(input_frame, font=('Arial', 14), width=50, bg="white", relief="flat")
        self.input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))  # 填满并扩展
        self.input_box.bind("<Return>", self.process_input)  # 绑定回车键处理输入

        # 创建绿色的发送按钮
        self.send_button = tk.Button(input_frame, text="发送", height=2, width=10, bg="#4CAF50", fg="white", relief="flat",
                                     command=self.process_input)  # 绑定按钮点击事件
        self.send_button.pack(side=tk.RIGHT)  # 将按钮放到右边

        self.root.minsize(600, 400)  # 设置窗口的最小尺寸
        self.root.mainloop()

    def set_html_content(self, text):
        """设置HTML内容并更新显示"""
        html_content = markdown.markdown(text)  # 将文本转换为HTML格式
        self.html_label.set_html(html_content)  # 设置HTML内容

    def process_input(self, event=None):
        # 从输入框获取内容
        input_content = self.input_box.get()
        if input_content.strip():  # 检查输入内容是否为空
            print(f"输入框内容: {input_content}")  # 输出输入框内容到控制台
            self.display_message("你", input_content)  # 显示输入内容
        else:
            # 提示用户输入框为空
            messagebox.showwarning("输入错误", "输入框不能为空!")  # 弹出警告窗口

    def display_message(self, userName, message_text):
        """将消息文本添加到对话框中"""
        self.dialog_content += f"<br><strong>{userName}:</strong> {message_text}<br><strong>{self.model.model}:</strong> 正在生成回复..."  # 添加新消息
        self.set_html_content(self.dialog_content)  # 更新HTML内容

        # 显示加载窗口
        loading_window = LoadingWindow()  # 创建加载窗口

        # 使用线程来调用 chat 函数，避免阻塞主线程
        threading.Thread(target=self.generate_response, args=(message_text, loading_window)).start()

    def generate_response(self, message_text, loading_window):
        """生成聊天回复并关闭加载窗口"""
        chat(message_text, self.message, self.model)  # 调用聊天函数
        loading_window.close()  # 关闭加载窗口







import requests
from openai import OpenAI
from control import settings, checkSystem
from server.model import DeepSeekModel, KimiModel, ZeroOneModel, BigModel, templateModel, BaiChuanModel,ChatGPTModel
modelList = [None,BigModel.BigModel(),DeepSeekModel.DeepSeekModel(),ZeroOneModel.ZeroOneModel(),KimiModel.KimiModel(),BaiChuanModel.BaiChuanModel(),ChatGPTModel.ChatGPTModel()]

# 用于单论对话或初次对话
def chat_init(text,model):
    # 初始化API
    client = OpenAI(api_key=model.api_key, base_url=model.base_url)
    # 提示词工程
    if model.Prompt:
        prompt = settings.Prompt + model.Prompt
    else:
        prompt = settings.Prompt
    messages=[
        {"role": "system", "content":prompt },
        {"role": "user", "content": text},
    ]
    # 调用API进行对话
    response = client.chat.completions.create(
        model=model.model,
        messages=messages,
        stream=True,
        tools=model.tools,
        temperature = settings.temperature
    )
    # Chat流式回复响应
    chatTempResponse = {"role": "assistant", "content":"" }
    print(settings.assistant_name,end='正在生产中...\n')
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content,end='')
            chatTempResponse["content"] += content
        if settings.showApiUsage and chunk.usage:
            print("\n[本次调用已使用 API 配额: "+str(chunk.usage.total_tokens)+" tokens],剩余配额:"+str(check_balance(model)))
    print(settings.assistant_name,end="生成完成！")
    messages.append(chatTempResponse)
    # if oldWindow:
    #     oldWindow.root.destroy()  # 关闭对话窗口
    chatClient(chatTempResponse["content"],model,messages)
    if settings.showHistory:
        print(f"\n\n\n【对话历史记录】\n{messages}")
    return messages


# 用于多轮对话进行回复
def chat(text,messages,model):

# try:
    # 进行model对象转化
    if not isinstance(model,templateModel.TemplateModel):
        model = modelList[int(model)]
    # 文本检查
    # 若未命中关键词，则返回True并继续运行下面的chat调用API
    if checkSystem.input_check(text,model):
        if messages == None or not(settings.longConversation):
            messages = chat_init(text,model)
        else:
            # 中间提示词
            if settings.haveIntervalPrompt:
                messages.append(settings.IntervalPrompt)
            messages.append({"role": "user", "content": text})
            client = OpenAI(api_key=model.api_key, base_url=model.base_url)
            response = client.chat.completions.create(
                model=model.model,
                messages=messages,
                stream=True,
                tools=model.tools,
                max_tokens=settings.max_tokens
            )
            print(settings.assistant_name,end='正在生成中...\n')
            chatTempResponse = {"role": "assistant", "content":"" }
            for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    print(content,end='')
                    chatTempResponse["content"] += content
                if settings.showApiUsage and chunk.usage:
                    print("\n[本次调用已使用 API 配额: "+str(chunk.usage.total_tokens)+" tokens],剩余配额:"+str(check_balance(model)))
            print(settings.assistant_name,end="生成完成！")
            messages.append(chatTempResponse)
            chatClient(chatTempResponse["content"],model,messages)
            if settings.showHistory:
                print(f"\n\n\n【对话历史记录】\n{messages}")
# except Exception as e:
#     print(f"错误信息:{e}")





# Check API Key Balance
# Return:
#   isAvailable: API Key是否可用
#   balance: API Key余额
def check_balance(model):
    url = model.balance_url
    payload={}
    headers = {
        'Accept': 'application/json',
        'Authorization': "Bearer "+model.api_key
    }
    if url:
        response = requests.request("GET", url, headers=headers, data=payload)
        # response = json.loads(response.text)
        response = response.json()
        isAvailable = response['is_available']
        balanceInfo = response['balance_infos'][0]
        return isAvailable, balanceInfo["total_balance"]+balanceInfo["currency"]
    else:
        return None, None



