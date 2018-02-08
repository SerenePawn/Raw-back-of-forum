from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from forum.models import Topic, TopicComments, PrivateMessage, Dialog
from django.db.models import F
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forum.forms import CommentsForm, NewDialogForm, MessageSendForm


def indexpage(request):
    """ Список топиков (пока что) """
    args = {
        'topics': Topic.objects.all(),
    }
    return render(request, 'forum/index.html', args)


def contopic(request, topic_id):
    """ Открывает выбранный топик """
    args = {
        'topic': get_object_or_404(Topic, id=topic_id),
        'comments': TopicComments.objects.filter(comments_topic=topic_id),
        'form': CommentsForm,
    }
    args.update(csrf(request))
    return render(request, 'forum/topic.html', args)


def addlike(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.topic_rate_plus=F('topic_rate_plus') + 1
    topic.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def adddislike(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.topic_rate_minus=F('topic_rate_minus') + 1
    topic.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def viewacc(request, name_or_id):
    if name_or_id.isnumeric():
        args = {'userview': get_object_or_404(User, id=name_or_id), 'req': request}
    else:
        args = {'userview': get_object_or_404(User, username=name_or_id), 'req': request}
    return render(request, 'forum/userprofile.html', args)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            args['login_error'] = 'User not found'
            return render(request, 'forum/login.html', args)
    else:
        return render(request, 'forum/login.html', args)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def addcomment(request, topic_id):
    if request.POST:
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_topic = Topic.objects.get(id=topic_id)
            comment.comments_by = request.user
            form.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm
    if request.POST:
        newuser = UserCreationForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            newuser = auth.authenticate(
                username=newuser.cleaned_data['username'],
                password=newuser.cleaned_data['password1']
            )
            auth.login(request, newuser)
            return HttpResponseRedirect('/')
        else:
            args['form'] = newuser
    return render(request, 'forum/register.html', args)

# Отсюда идут вьюхи для теста и понимания устройства нового модуля


#def messages(request):
#    """ Возвращает пользователю все его отправленные/полученные сообщения """
#    args = {'messages': PrivateMessage.objects.by_user(request.user)}
#   # Пытаюсь заставить джангу достать все сообщения пользователя
#    return render(request, 'forum/privatemessages.html', args)


def dialogs(request):
    return render(request, 'forum/dialog/dialogs.html', {
        'dialogs': Dialog.objects.by_user(request.user)
    })


def dialog_read(request, dialog_id):
    dialog = get_object_or_404(Dialog.objects.by_user(request.user), id=dialog_id)

    if request.method == 'POST':
        form = MessageSendForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.dialog = dialog
            message.sender = request.user
            message.save()

            dialog.save()

            return HttpResponseRedirect(message.get_absolute_url())
    else:
        form = MessageSendForm()

        # помечаем сообщения как прочитанные
    # PrivateMessage.objects.mark_read(request.user, dialog)

    return render(request, 'forum/dialog/dialog_read.html', {
        'pm_topic': dialog,
        'pm_form': form,
    })


def dialog_new(request):
    if request.method == 'POST':
        form = NewDialogForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)

            dialog = Dialog(sender=request.user)
            dialog.recipient = form.cleaned_data['recipient']
            dialog.subject = form.cleaned_data['subject']
            dialog.save()

            message.dialog = dialog
            message.sender = request.user
            message.save()

            return HttpResponseRedirect('/')
    else:
        initial = {}
        if request.GET.__contains__('recipient'):
            initial['recipient'] = request.GET['recipient']

        form = NewDialogForm(initial=initial)

    return render(request, 'forum/dialog/dialog_new.html', {
        'pm_form': form
    })


def ajaxtest(request):
    if request.GET:
        if request.GET['de_wei'] == 'de wei':
            return HttpResponse('You do not know de wei...')
        else:
            return HttpResponse(request.GET['de_wei'])
    return render(request, 'forum/ajax/ajax.html')
