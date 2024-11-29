def load():
    import os

    def parse_txt_file(file_path):
        data_dict = {}

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    # 移除行尾的换行符
                    line = line.strip()

                    # 检查行是否符合 key:value 格式
                    if ':' in line:
                        key, value = line.split(':')
                        data_dict[key.strip()] = value.strip()
                    else:
                        print(f"警告: 行格式不正确，跳过 - '{line}'")

            return data_dict

        except FileNotFoundError:
            print(f"错误: 文件 '{file_path}' 未找到。")
        except Exception as e:
            print(f"错误: 解析文件时发生异常 - {e}")

    def main(directory_path, file_name):
        global BaiChuan_api_key, Kimi_api_key, ZeroOne_api_key, BigModel_api_key, DeepSeek_api_key
        # 构建完整的文件路径
        file_path = os.path.join(directory_path, file_name)

        # 解析文本文件
        parsed_data = parse_txt_file(file_path)
        for key,value in parsed_data.items():
            print(f"{key}: {value}")
            globals()[key] = value


        print(BaiChuan_api_key)
            #update_api_key()

    # 使用示例
    main("D:\\Desktop", "config.txt")

if __name__ == '__main__':
    load()