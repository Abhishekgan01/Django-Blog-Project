from django import forms
from blogs.models import Category,Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured')

#If we use UserCreation form , it will retrieve password as it is a required field
class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active', 'is_staff','is_superuser','groups','user_permissions')

#Hence we are using the forms.ModelForm 
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active', 'is_staff','is_superuser','groups','user_permissions')