해당 Readme는 py파일 실행을 위해 작성되었습니다.

ipynb는 그냥 실행해도 됩니다.

# 1. 형태소 분석기를 사용을 위한 KoNLPy 다운로드

## > pip install konlpy

Konlpy를 사용하기 위해선 JDK가 설치되어야 합니다.

혹시 JDK8이 설치되지 않았다면 https://www.oracle.com/java/technologies/downloads/#java8를 통해 설치 후

환경변수 중 사용자변수에 CLASSPATH와 JAVA_HOME 설정을 하여야 합니다.

각자의 jdk 버전과 위치에 맞게 tools.jar와 server의 경로를 복사하여 등록하면 됩니다.

▼하단 예시▼

>CLASSPATH : C:\Program Files\Java\jdk1.8.0_333\lib\tools.jar

>JAVA_HOME : C:\Program Files\Java\jdk1.8.0_333\jre\bin\server

추가사항으로 pip 버전이 최신이 아닐 시 upgrade요청 메세지가 뜹니다.

그러나 pip접근을 위한 관리자의 권한을 부여받지 못했으므로 다음을 입력하면 됩니다.

## > python -m pip install --upgrade pip
-----------------------------------------------------------------------

# 2. 수식을 사용하기 위한 Numpy 다운로드

## > pip install numpy
-----------------------------------------------------------------------

# 3. 데이터 확인을 위한 Pandas 다운로드

## > pip install pandas

이는 데이터 확인용이기에 import pandas as pd를 삭제해도 됩니다.

-----------------------------------------------------------------------
# 4. SearchEngineSys.py 실행

Google Colab으로 실행하면 Query Time 부분만 반복적으로 실행하면 되기에 실행시간이 빠르지만

Python으로 전체를 실행 시 Indexing time으로 인해 입력창이 뜨기까지 시간이 걸리므로 기다려야 합니다.

검색창에 full_corpus.txt에 있는 내용을 검색하여 관련있는 상위 5개의 document를 검색결과로 번호로 불러옵니다.
