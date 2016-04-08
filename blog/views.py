from django.shortcuts import render
def post_list(request):
    # return "Hello"
    return render(request, 'blog/post_list.html', {})
