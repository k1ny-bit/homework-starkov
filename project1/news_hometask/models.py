from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user_id = models.IntegerField(default=0)
    username = models.CharField(max_length=20)
    rating = models.FloatField(max_length=5.0, default=0.0)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        sum_comment_rate = 0
        sum_posts_rate = 0
        sum_posts_comments_rate = 0
        for p in self.posts:
            sum_posts_rate += p.rating
        for comment in self.user.comments:
            sum_comment_rate += comment.rating
        for p in self.posts:
            for comment in p.comments:
                sum_posts_comments_rate += comment.rating
        self.rating = sum_posts_rate * 3 + sum_comment_rate + sum_posts_comments_rate


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_article = models.BooleanField(default=0)
    posted = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(default=20)
    text = models.CharField(default=255)
    rating = models.IntegerField(default=5)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

    def preview(self):
        return self.text[0:124] + '...'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(default=255)
    post_date = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=5)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1


