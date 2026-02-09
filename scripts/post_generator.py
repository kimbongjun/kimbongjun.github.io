import google.generativeai as genai
import os
from datetime import datetime

# 1. 제미나이 설정
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash') # 가볍고 빠른 모델 추천

def generate_post():
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 2. 프롬프트 작성
    prompt = f"""
    주제: 최신 기술 트렌드 및 IT 뉴스
    형식: GitHub 블로그용 마크다운 포스트
    요구사항:
    - 반드시 아래 Front Matter를 포함할 것:
    ---
    layout: post
    title: "Gemini AI 인사이트: {today}"
    date: {today}
    categories: Technology
    ---
    - 한국어로 작성하고, 유익한 내용을 담아줘.
    """

    try:
        # 3. 콘텐츠 생성
        response = model.generate_content(prompt)
        content = response.text

        os.makedirs("_posts", exist_ok=True)
        filename = f"_posts/{today}-gemini-post.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"✅ 제미나이 포스팅 생성 성공: {filename}")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    generate_post()