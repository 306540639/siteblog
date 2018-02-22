from django.contrib.syndication.views import Feed
from .models import Post



class AllPostsRssFeed(Feed):

    title = '张枪枪的blog'
    link = '/'
    description = '猫精'

    def items(self):
        Post.objects.all()
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body

