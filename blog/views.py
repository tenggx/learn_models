from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse

from blog import models
from blog.models import Article


def hello_world(request):
    return HttpResponse('Hello World')


def article_content(request):
    # article = models.Article.objects.get(tile='零基础Django3小时开发个人博客系统')
    # article = Article.objects.get(tile='零基础Django3小时开发个人博客系统')
    article = Article.objects.all()[0]
    tile = article.tile
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title: %s, brief_content:%s, content:%s, article_id=%s, publish_date=%s' % (tile, brief_content, content, article_id, publish_date)
    return HttpResponse(return_str)


def get_index_page(request):
    page = request.GET.get("page")
    if page:
        page = int(page)
    else:
        page = 1
    print("page_num ", page)

    all_article = Article.objects.all()
    top5_article_list = Article.objects.order_by('-publish_date')[:10]
    paginator = Paginator(all_article, 6)
    page_num = paginator.num_pages
    print('page_num:', page_num)

    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous = page - 1
    else:
        previous = page

    return render(request, 'blog/index.html',
                      {'article_list': page_article_list, 'page_num': range(1, page_num + 1), 'curr_page': page,
                       'next_page': next_page, 'previous': previous, 'top5_article_list': top5_article_list})
    # return render(request, 'blog/index.html', {'article_list': all_article})
    # return render(request, 'blog:index.html', {'article_list': all_article})
    # return render(request, 'blog/index.html', locals())
    # return HttpResponse('get_index_page')


def get_detail_page(request, article_id):
    all_article  = Article.objects.all()
    cur_article = None
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_article_index = 0
            next_article_index = index+1
        elif index == len(all_article)-1:
            previous_article_index = index-1
            next_article_index = index
        else:
            previous_article_index = index-1
            next_article_index = index+1
        if article.article_id == article_id:
            cur_article = article
            previous_article = all_article[previous_article_index]
            next_article = all_article[next_article_index]
            break
    section_list = cur_article.content.split('\n')
    return render(request, 'detail.html', {'curr_article': cur_article, 'section_list': section_list, 'previous_article': previous_article,'next_article': next_article})
