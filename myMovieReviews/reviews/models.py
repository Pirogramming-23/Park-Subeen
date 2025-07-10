from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=100)              # 영화 제목
    release_year = models.PositiveIntegerField()          # 개봉 년도
    genre = models.CharField(max_length=50)                # 장르
    director = models.CharField(max_length=50)             # 감독
    main_actor = models.CharField(max_length=50)           # 주연
    rating = models.DecimalField(max_digits=2, decimal_places=1)   # 별점 (1~5)
    running_time = models.PositiveIntegerField()           # 러닝타임 (분)
    content = models.TextField()                           # 리뷰 내용

    def __str__(self):
        return f"{self.title} ({self.release_year})"