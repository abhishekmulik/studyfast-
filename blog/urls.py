from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^post_list$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    # url(r'add/category/$',views.AddCategoryView.as_view(),name='add_category'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_published, name='post_published'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approved, name='comment_approved'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^$',views.SubjectListView.as_view(),name='subjectList'),
    url(r'^category/(?P<pk>\d+)/$',views.categorylist,name='categorylist'),
    # url(r'^postview/(?P<pk>\d+)$', views.postlist, name='cate_posts'),
    url(r'^add_subject/$',views.CreateSubjectView.as_view(),name='subjectlist_form'),
    url(r'^add_category/$',views.CreateCategoryView.as_view(),name='category_form'),
    url(r'^category_post/(?P<pk>\d+)/$',views.postview,name='postview'),
    url(r'^contribute/',views.contribute.as_view(),name='contribute')
    # path('<int:pk>/',views.CategorizedPostView.as_view(),name='categorized_post'),
    # path('category/<str:cats>/',views.CategoryView,name='category'),
    # path('post/<int:pk>/category/',views.CategoryListView,name='category_list'),
]
