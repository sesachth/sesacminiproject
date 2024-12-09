import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # 네이버 Maps API 사용을 위한 클라이언트 ID
    NAVER_CLIENT_ID = os.environ.get('NAVER_CLIENT_ID') or 'invalid_id'