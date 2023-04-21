1. Actor, Movie, Review 모델 생성
2. 전체 배우 목록, 단일 배우 정보 제공 하는 view 함수/
전체 영화 목록, 단일 영화 정보 제공하는 view 함수/
전체 리뷰 목록, 단일 영화 리뷰 제공하는 view 함수/
리뷰 생성하는 view 함수 생성
3. 각각의 함수에 사용할 serializer 생성

어려웠던 점
- serializer로 json 데이터를 생성할 때,
 model을 그대로 상속받아 만들면, 참조하는 속성 값들이 id로만 반환이 되는 문제가 있었다.
 (내가 원하는 것은 배우 이름 혹은 영화 이름인데, id값으로 출력)
 - 원하는 필드만 반환하는 serializer를 따로 만들어서 해결을 했는데,
 serializer가 너무 많아져서, 더 좋은 방법이 있을 것 같아 검색해봤다.
- chatgpt 코드에서 SerializerMethodField() 메서드와 get함수 사용법을 알게되서 serializer들을 좀 더 압축할 수 있었다.
- 아직 serialize 과정을 잘 이해하고 있지 못한것 같아서 연습을 많이 해봐야할 것 같다.