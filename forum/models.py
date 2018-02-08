from django.db import models
from django.contrib.auth.models import User
from base64 import b16encode


class DialogManager(models.Manager):
    def by_user(self, user):
        """
        Возвращает все сообщения пользователя (идет во вьюхи)
        """
        return self.filter(models.Q(sender=user) | models.Q(recipient=user))


class Section(models.Model):
    section_header = models.CharField(max_length=40)

    class Meta:
        db_table = 'section'

    def __str__(self):
        return self.section_header


def upload_location(i, imgname):
    enc = b16encode(imgname.encode('utf-8'))
    enc = enc.decode('utf-8')
    return '%s/%s/%s' % (enc[:2], enc[2:4], imgname)


class Topic(models.Model): # Here should be relations to category.
    topic_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    topic_header = models.CharField(max_length=30)
    topic_text = models.TextField()
    topic_rate_plus = models.IntegerField(default=0)
    topic_rate_minus = models.IntegerField(default=0)
    topic_pub_date = models.DateTimeField(auto_now_add=True)
    topic_edit_date = models.DateTimeField(null=True)
    topic_pic = models.ImageField(default='default_topic_pic.png',
                                  upload_to=upload_location,
                                  width_field='width',
                                  height_field='height')
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    class Meta:
        db_table = 'topic'

    def __str__(self):
        return self.topic_header


class TopicComments(models.Model):
    comments_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comments_text = models.TextField(max_length=800)
    comments_pub_date = models.DateTimeField(auto_now_add=True)
    comments_edit_date = models.DateTimeField(null=True)
    comments_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.comments_text


class Dialog(models.Model):
    sender = models.ForeignKey(User, related_name='pm_sender')
    recipient = models.ForeignKey(User, related_name='pm_recipient')
    subject = models.CharField(max_length=255)

    objects = DialogManager()

    class Meta:
        db_table = 'dialog'

    def __str__(self):
        return 'dialog %s' % self.id

    def get_absolute_url(self):
        return 'pm_dialog-' + str(self.pk)


class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    dialog = models.ForeignKey(Dialog, related_name='messages')
    text = models.TextField(max_length=1500)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'messages'

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return '%s#message-%s' % (self.dialog.get_absolute_url(), self.pk)


class Category(models.Model): # Here should be MPTT module. But not in this "project".
    category_name = models.CharField(max_length=100)
    category_related = models.ForeignKey('self', null=True, blank=True)
    category_included = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return '>>' * self.category_included + ' %s' % self.category_name
