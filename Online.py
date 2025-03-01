# -*- coding: utf-8 -*-
import requests
import math
import time
import random
from bs4 import BeautifulSoup
from urllib.parse import quote

# ⚠️ 重要警告 ⚠️
# 本实现违反Google服务条款，仅供学习研究使用
# 长期使用可能导致IP被封禁，生产环境请使用官方API

class WebTranslator:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Referer': 'https://translate.google.com/'
        }
        self._init_cookies()

    def _init_cookies(self):
        """初始化必要cookies"""
        self.session.get('https://translate.google.com/', timeout=10)

    def _safe_delay(self):
        """添加随机延迟防止封禁"""
        time.sleep(random.uniform(1.2, 3.8))

    def translate(self, text, dest='zh-CN'):
        """执行网页翻译的核心方法"""
        self._safe_delay()
        
        try:
            # 构造翻译URL
            encoded_text = quote(text)
            url = f"https://translate.google.com/?sl=auto&tl={dest}&text={encoded_text}&op=translate"
            
            response = self.session.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()
            
            # 解析翻译结果
            soup = BeautifulSoup(response.text, 'html.parser')
            result_div = soup.find('div', class_='NqnNQd')
            
            if result_div:
                return result_div.text.strip()
            return text
        except Exception as e:
            print(f"翻译失败: {str(e)}")
            return text

# 基础文本配置（使用英文作为基准）
BASE_TEXTS = {
    "title": "When to level 6",
    "lang_prompt": "Select Language (1-2):\n1. 中文\n2. English",
    "exp_prompt": "Current experience points:",
    "coin_prompt": "Current B-coins:",
    "result": "Days needed: {}"
}

# 初始化翻译器（谨慎使用）
translator = WebTranslator()

def get_translation(text, lang_code):
    """带语言映射的翻译函数"""
    lang_map = {
        'zh': 'zh-CN',
        'en': 'en'
    }
    if lang_code == 'en':
        return text
    return translator.translate(text, dest=lang_map.get(lang_code, 'en'))

# 主程序逻辑
def main():
    # 语言选择
    print("语言选择 / Language selection")
    lang_choice = input("请选择语言 (1.中文 2.English): ").strip()
    
    lang_code = 'zh' if lang_choice == '1' else 'en'
    
    # 动态生成界面
    title = get_translation(BASE_TEXTS["title"], lang_code)
    exp_prompt = get_translation(BASE_TEXTS["exp_prompt"], lang_code)
    coin_prompt = get_translation(BASE_TEXTS["coin_prompt"], lang_code)
    result_template = get_translation(BASE_TEXTS["result"], lang_code)

    print(f"\n{title}")
    
    # 获取用户输入
    try:
        exp = int(input(f"{exp_prompt}: "))
        coins = int(input(f"{coin_prompt}: "))
    except ValueError:
        print(get_translation("Invalid input!", lang_code))
        return

    # 计算逻辑（保持不变）
    required = 28800 - exp
    daily_gain = coins * 10 / 50
    days_needed = math.ceil(required / 60 - daily_gain)
    days_needed = max(days_needed, 0)

    # 输出结果
    print(result_template.format(days_needed))

if __name__ == "__main__":
    # 法律声明
    print("本程序仅供学习研究使用，请勿用于商业用途")
    print("Powered by meterax | Version: Omega_1.0\n")
    
    main()