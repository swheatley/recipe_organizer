from main.models import Recipe, Cookie, Cake, Dessert_Bar, Picture


class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeModelForm2(forms.Form):
    title = forms.CharField(required=True)


class RecipeModelForm(forms.Form):
    title = forms.CharField(required= False)
    info = forms.CharField(required=False, widget=forms.Textarea)
    image = forms.ImageField(required=False)


class UserSignUp(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())