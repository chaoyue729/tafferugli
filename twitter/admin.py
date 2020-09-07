from django.contrib import admin
from .models import *
from twitter.models.operations import OperationConstructNetwork

admin.site.register(TwitterAccount)
admin.site.register(Entity)
admin.site.register(Campaign)
admin.site.register(TwitterUser)
admin.site.register(Operation)
admin.site.register(Location)
admin.site.register(Hashtag)
admin.site.register(Community)
admin.site.register(Fact)
admin.site.register(URL)
admin.site.register(Streamer)
admin.site.register(TweetSource)
admin.site.register(Tweet)
admin.site.register(CommunityGraph)
admin.site.register(MetricDefaultProfilePicture)
admin.site.register(MetricDuplicateTweet)
admin.site.register(MetricDefaultTwitterProfile)
admin.site.register(MetricRecentCreationDate)
admin.site.register(MetricCreationDateDistribution)
admin.site.register(MetricTweetRatio)
admin.site.register(MetricFriendsFollowersRatio)
admin.site.register(MetricNameWithRegex)
admin.site.register(MetricGraphTweetNetwork)
admin.site.register(MetricTweetTimeDistribution)
admin.site.register(OperationConstructNetwork)
admin.site.register(MetricGraphCommunityNetwork)
