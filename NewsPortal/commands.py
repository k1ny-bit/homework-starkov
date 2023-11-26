from NewsPortal_hometask_app.models import *

user1 = User.objects.create_user('maxflex')
user2 = User.objects.create_user('k1ny')

author1 = Author.objects.create(username='Kulew', rating=5.0, user=user1)
author2 = Author.objects.create(username='AntoxaPudge', rating=2.3, user=user2)

cat1 = Category.objects.create(category_name='Фантастика')
cat2 = Category.objects.create(category_name='Роман')
cat3 = Category.objects.create(category_name='Юмор')
cat4 = Category.objects.create(category_name='ФанФик')

article1 = Post.objects.create(is_article=True, author=author1, title='Политика в России', text='random text')
article2 = Post.objects.create(is_article=True, author=author2, title='Политика в России 2', text='random text')
news1 = Post.objects.create(is_article=False, author=author1, title='Политика в России 3', text='random text')

article1.category.add(cat1, cat4)
article2.category.add(cat2, cat3)
news1.category.add(cat2)

com1 = Comment.objects.create(post=article1, user=user1, comment_text='Класс!')
com2 = Comment.objects.create(post=article2, user=user1, comment_text='Класс!2')
Comment.objects.create(post=news1, user=user2, comment_text='Шляпа')
Comment.objects.create(post=news1, user=user2, comment_text='Шляпа2')

article1.like()
news1.dislike()
article2.like()
com1.dislike()
com2.like()

author1.update_rating()
user2.author.update_rating()

best_author = Author.objects.order_by('-rating').first()
print(best_author.username)
print(best_author.rating)

best_article = Post.objects.order_by('-rating').first()
print(best_article.author.username)
print(best_article.rating)
print(best_article.title)
print(best_article.preview())
print(best_article.posted)

for c in best_article.comment_set.all():
    print(c.post_date)
    print(c.user)
    print(c.rating)
    print(c.comment_text)
