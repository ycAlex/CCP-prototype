import os
import zipfile
from io import BytesIO

from django.views.generic import DetailView, ListView, View
from .models import Post, Student, Teacher, Parent, Class
from django.db.models import Q
from django.http.response import HttpResponse
from django.conf import settings


class StudentList(ListView):
    context_object_name = 'student_list'
    template_name = 'post/student_list.html'

    def get_queryset(self):
        if Teacher.objects.filter(user=self.request.user).count():
            teacher = Teacher.objects.get(user=self.request.user)
            return Student.objects.filter(joined_class__in=teacher.classes.all()).order_by('joined_class')


class StudentDetail(DetailView):
    model = Student
    template_name = 'post/student_detail.html'

    def get(self, request, *args, **kwargs):
        if Teacher.objects.filter(user=request.user).count():
            self.queryset = Student.objects.filter(joined_class__in=Teacher.objects.get(user=request.user).classes.all())
        elif Student.objects.filter(user=request.user).count():
            self.queryset = Student.objects.filter(user=request.user)
        elif Parent.objects.filter(user=request.user).count():
            self.queryset = Student.objects.filter(parents=Parent.objects.get(user=request.user))
        return super(StudentDetail, self).get(request, *args, **kwargs)


class Download(View):

    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        posts = student.related_posts.all()
        allowed = False
        if Teacher.objects.filter(user=request.user).count():
            teacher = Teacher.objects.get(user=request.user)
            if Student.objects.filter(joined_class__in=teacher.classes.all(), pk=pk).count():
                allowed = True
        elif Student.objects.filter(user=request.user).count():
            if Student.objects.get(user=request.user).id == int(pk):
                allowed = True
        elif Parent.objects.filter(user=request.user).count():
            if Student.objects.filter(parents=Parent.objects.get(user=request.user), pk=pk).count():
                allowed = True
        b = BytesIO()
        zip_file = zipfile.ZipFile(b, "w")
        if allowed:
            for post in posts:
                basename = os.path.basename(post.image.name)
                zip_path = os.path.join('posts', basename)
                zip_file.write(os.path.join(settings.MEDIA_ROOT, post.image.name), zip_path)
        zip_file.close()
        resp = HttpResponse(b.getvalue(), content_type="application/x-zip-compressed")
        resp['Content-Disposition'] = 'attachment; filename=posts.zip'
        return resp
