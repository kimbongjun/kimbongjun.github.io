import openai
import os
from datetime import datetime

# API 키 설정
openai.api_key = os.getenv("API_KEY")

def generate_post():
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "특정 주제(예: 최신 AI 뉴스)에 대해 GitHub 블로그용 마크다운 포스팅을 작성해줘."}]
    )
    content = response.choices[0].message.content
    
    # 파일명 생성 (예: 2024-05-20-ai-news.md)
    filename = f"_posts/{datetime.now().strftime('%Y-%m-%d')}-auto-post.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_post()