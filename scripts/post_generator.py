import openai
import os
from datetime import datetime

# 1. API 키 설정 (GitHub Secrets에서 불러옴)
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_post():
    # 오늘 날짜
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 2. AI에게 포스팅 요청 (프론트 매터 형식을 포함하도록 프롬프트 수정)
    prompt = f"""
    주제: 최신 AI 뉴스 및 트렌드 요약
    형식: GitHub Jekyll 블로그 마크다운 포스트
    요구사항:
    - 파일 최상단에 아래와 같은 Front Matter를 포함해줘.
    ---
    layout: post
    title: "AI 자동 생성 포스트: {today}"
    date: {today}
    categories: AI-Updates
    ---
    - 내용은 한국어로 전문적이고 흥미롭게 작성해줘.
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        
        content = response.choices[0].message.content

        # 3. _posts 폴더가 없으면 생성 (에러 방지)
        os.makedirs("_posts", exist_ok=True)

        # 4. 파일명 생성 및 저장
        filename = f"_posts/{today}-auto-post.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"✅ 성공: {filename} 파일이 생성되었습니다.")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    generate_post()