from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from blog.models import Post


class LatestPostsFeed(Feed):
    title = 'Matt\'s blog'
    link = '/blog'

    num_posts = 5

    description = str(num_posts) + ' newest posts from my blog'

    def items(self):
        return Post.published.all()[:self.num_posts]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
