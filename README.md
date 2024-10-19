# NTIS-patent-data-filtering
- NTIS 국가연구개발정보시스템으로부터 기업에서 국가R&D사업을 통해 개발한 등록특허 데이터를 추출하는 방법 (테크니컬 포트폴리오 기술평가항목 : 1, 3, 4)

# Code structure
- '1.2013.(6).xls' 파일은 NTIS 사이트로부터 다운로드 받은 2013년도에 수행한 국가 R&D 특허성과 리스트임
   (해당 파일에는 중복특허 기록도 있고, 출원만 되었을 뿐 등록되지 않은 특허 기록도 다수 포함되어 있음)
- '1. 중복제거.py' 코드를 통해, '1.2013.(6).xls' 시트에 있는 국가사업 특허출원번호(전담기관 등록(기탁)번호) 중복 제거함
- '2. 키프리스 등록특허 필터링.py' 코드를 통해, 특허청 KIPRIS API로 '2.2013(6)-중복제거.csv' 시트에 있는 특허정보 조회 후 실제 등록된 특허만을 필터링함
- '3. 연구사업 정보 추가.py' 코드를 통해, NTIS 시스템 API로 '3.2013(6)-등록특허(최종).csv' 시트에 있는 등록특허의 상세 사업정보 크롤링함
- '4. 피인용수 추가.py' 코드를 통해, 다시 특허청 KIPRIS API로 '4.2013(6)-연구정보포함(최종).csv' 시트에 있는 등록특허의 피인용지수를 크롤링함
- 최종적으로, 국가연구개발 성과를 통해 기업이 창출한 등록특허 데이터셋 파일 '5.2013(6)-피인용수 추가(최종).csv' 완성
