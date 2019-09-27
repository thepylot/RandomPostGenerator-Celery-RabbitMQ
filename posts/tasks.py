from faker import Faker
from .models import Post
from celery import shared_task

@shared_task
def create_random_posts(number_of_posts):
    fake = Faker()
    for i in range(number_of_posts):
        title = fake.sentence()
        description = fake.text()
        author = fake.name()
        Post.objects.create(
            title = title,
            description = description,
            author = author

        )

    return f'{number_of_posts} posts successfully generated!'