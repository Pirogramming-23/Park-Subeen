from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    # models.Model을 상속, 이 클래스를 장고가 DB 테이블로 인식함
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 이 글(Post)의 작성자를 저장
    title = models.CharField(max_length=200) # 글의 제목 , VARCHAR(200) 같은 컬럼이 생성
    text = models.TextField() # 글 본문 내용, TEXT 타입 컬럼이 생성
    created_date = models.DateTimeField( # 글을 "작성"한 시간
            default=timezone.now) # 글을 만들 때 자동으로 현재 시간 저장
    published_date = models.DateTimeField( # 글을 "발행"한 시간
            blank=True, null=True)

    def publish(self): # 글을 발행할 때 이 메서드를 호출
        self.published_date = timezone.now() # 현재 시간을 published_date에 저장
        self.save() # DB에 저장

    def __str__(self): # 장고 관리자(admin)나 쉘에서 객체를 볼 때 표시되는 문자열
        return self.title
