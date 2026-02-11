import google.generativeai as genai
import os
import re
from datetime import datetime

# 1. API 키 설정
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_post():
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 2. 모델 설정 (models/ 를 생략하거나 포함하는 방식 중 가장 안정적인 형태)
    # 404 에러가 계속된다면 'gemini-1.5-flash-latest'로 적어보세요.
    model_name = 'models/gemini-2.5-flash' 
    
    try:
        model = genai.GenerativeModel(model_name)
        
        prompt = f"""
        주제: Figma,Jenkins 등 UX 툴 동향과 노하우
        형식: GitHub Jekyll 블로그 마크다운 포스트
        요구사항:
        - 아래 Front Matter를 포함할 것:
        ---
        layout: post
        title: "[여기에 본문 내용과 어울리는 매력적인 제목을 지어서 넣어줘]"
        date: {today}
        categories: AI-Tech
        ---
        - 한국어로 작성하고 가독성 좋게 마크다운 문법을 활용해줘.
        """

        # 3. 콘텐츠 생성
        response = model.generate_content(prompt)
        
        if not response.text:
            print("❌ 생성된 내용이 없습니다.")
            return

        content = response.text
        
        # 3. 제목(title) 추출 및 파일명 정제
        # Front Matter 내의 title: "제목" 부분을 찾아냅니다.
        title_match = re.search(r'title:\s*["\']?(.*?)["\']?\n', content)
        
        if title_match:
            raw_title = title_match.group(1)
            # 파일명으로 부적절한 특수문자 제거 및 공백을 대시(-)로 변경
            clean_title = re.sub(r'[^\w\s-]', '', raw_title).strip()
            clean_title = re.sub(r'\s+', '-', clean_title)
            post_name = clean_title
        else:
            # 제목 추출 실패 시 기본값 설정
            post_name = "ai-news-update"

        # 4. 파일 저장 (날짜-제목.md 형식)
        os.makedirs("_posts", exist_ok=True)
        filename = f"{today}-{post_name}.md"
        file_path = os.path.join("_posts", filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"✅ 성공: {file_path} 생성 완료")

    except Exception as e:
        print(f"❌ 오류 상세: {e}")
        print("사용 가능한 모델 목록을 확인해 보세요:")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)

if __name__ == "__main__":
    generate_post()