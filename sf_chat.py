import requests
import json

class SFChat:
    def __init__(self, config):
        # 设置默认参数
        default_config = {
            "api_url": "https://api.siliconflow.cn/v1/chat/completions",
            "model": "deepseek-ai/deepseek-llm-67b-chat",
            "api_key": None,
            "temperature": 1.0,
            "top_p": 1.0,
            "max_tokens": 16,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0,
            "role": "user"
        }
        
        # 合并用户配置和默认配置，用户配置优先
        self.config = {**default_config, **config}
        
        # 设置请求头
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.config['api_key']}"
        }

    def chat_completion(self, messages):
        # 构建请求的payload
        payload = {
            "model": self.config["model"],
            "messages": messages,
            "temperature": self.config["temperature"],
            "top_p": self.config["top_p"],
            "max_tokens": self.config["max_tokens"],
            "frequency_penalty": self.config["frequency_penalty"],
            "presence_penalty": self.config["presence_penalty"],
            "role": self.config["role"]
        }
        
        # 发送POST请求
        response = requests.post(self.config["api_url"], json=payload, headers=self.headers)
        return response.json()