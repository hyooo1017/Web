from django.db import models

# Create your models here.
class Article(models.Model):
    # id = models.AutoField(primary_key = True)             -> 자동으로 추가되기 때문에 따로 작성하지 않음
    title = models.CharField(max_length = 10)
    content = models.TextField()                             # text타입은 길이에 제한 없이 문자열을 받을 수 있음
    created_at = models.DateTimeField(auto_now_add = True)    # 데이터가 생긴 시간
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):                  # __로 시작하고 __로 끝나는 메서드들을 매직 메서드라 함 (특수 목적)
        return f'{self.id}번 글 - {self.title} : {self.content}'    # str()은 str으로 변환해주는 메서드이므로 반환값은 문자열
    # str(), print()



# 1. models.py 작성/수정
# 2. python manage.py makemigrations
#       => models.py 바탕으로 설계도(migration 파일) 생성
# 3. python manage.py migrate
#       => 실제 DB(db.sqlite3)에 설계도 적용 (테이블 생성)


### DB에 데이터를 생성하는 방법 3가지
# 1. 

# 2. article = Article(title = '두 번째', content = '두 번째 내용')
#    article.save()

# 3. article = Article.objects.create(title = '세 번째', content = '내용입니다!!!')


### Read
# 1. All - Article.objects.all()        -> DB에 저장된 객체를 모두 볼 수 있음 (쿼리형으로)

# 2. 1개 - Article.objects.get(id=1)    -> 한 개의 인스턴스만 출력
#          Article.objects.get(title = '세 번째')   -> 제목이 같은 경우가 있을 수 있기 때문에 그 경우 에러 발생
#     -> unique한 컬럼(PK) & not null인 컬럼으로 get 사용

# 3. 조건 - Article.objects.filter(title='세 번째')     -> 복수형 쿼리로 반환
#     -> WHERE 키워드와 같은 기능을 함

# 4-1. QuerySet + .first(), .last()                      -> 하나의 인스턴스만 출력
#      ex) Article.objects.filter(title='세 번째').first() -> title이 '세 번째'인 인스턴스가 많다면 그 중 첫 번째 인스턴스만 반환
# 4-2. .order_by(컬럼명)
#      ex) Article.objects.all().order_by('title')      -> 오름차순
#      ex) Article.objects.all().order_by('-title')     -> 내름차순
# 4-3. offset, limit  (OFFSET, LIMIT)  [offset:offset+limit]
#      ex) Article.objects.all()[1:3]           -> [2, 3]


### Update
# 1. 데이터 가져오기
#   ex) a = Article.objects.get(id=1)
# 2. 수정할 값 할당하기
#   ex) a.title = 'First!'
# 3. 저장하기 (DB에 반영하기)
#   ex) a.save()


### Delete
# . 데이터 가져오기
#   ex) a = Article.objects.get(id=1)
# 2. 삭제하기 (DB에 반영)
#   ex) a.delete()
