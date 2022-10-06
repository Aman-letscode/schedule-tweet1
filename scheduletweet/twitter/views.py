from django.shortcuts import render, HttpResponse
from twitter.models import TwitterSchedulerModel
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"index.html")


def tweet(request):
    if request.method == "POST":
        content = request.POST['tweet']
        tweet_at = request.POST['tweettime']

        if content is None:
            return HttpResponse('Tweet Content is empty!!')
        else:
            tweetwork = TwitterSchedulerModel(tweet=content,tweet_at=tweet_at)
            tweetwork.save()
    return render(request,"index.html")