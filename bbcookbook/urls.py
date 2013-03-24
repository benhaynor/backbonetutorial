from bbcookbook.views import IndexView 
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from bbcookbook.views import MealList, MealDetail 

urlpatterns = patterns('',
    url(r'^meals/$', MealList.as_view(), name='meal-list'),
    url(r'^meals/(?P<pk>\d+)/$', MealDetail.as_view(), name='meal-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns += patterns('',
    url('^$', IndexView.as_view())
)

