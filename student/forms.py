from django import forms



class StudnetForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(
        attrs={"placeholder":"Your name"},
        )
    )
    email=forms.EmailField()
    bio=forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder":"Say something about yourself",
        }
        )
    )