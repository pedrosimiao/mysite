import pytest

from blog.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_post_published(post_published):
    assert post_published.title == 'pytest with factory'
    assert post_published.status == 0
    assert post_published.id is not None
    assert post_published.created_on is not None

