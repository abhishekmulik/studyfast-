from django import forms
from blog.models import Post,Comment,Category,SubjectList
# choices=[('Group A','Group A'),('Group B','Group B'),('Group C','Group C'),('Group D','Group D')]
# choices=Category.objects.all().values_list('name','name') #This is a query list so for normal list iterate n append
# choice_list=[i for i in choices]
class PostForm(forms.ModelForm):

    class Meta():
        model=Post
        fields=('author','title','subject','category','text')

        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass','class':'form-container'}),
            # 'category':forms.Select(choices=choice_list,attrs={'class':'form-container'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent','class':'form-container'})
        }
class CategoryForm(forms.ModelForm):
    class Meta():
        model=Category 
        fields=('subject','newCategory','description')
        widgets={
            'subject':forms.Select(attrs={'class':'textinputclass','class':'form-container'}),
        }

class SubjectListForm(forms.ModelForm):
    class Meta():
        model=SubjectList
        fields=('subject',)

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment 
        fields=('author','text')

        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
            }

