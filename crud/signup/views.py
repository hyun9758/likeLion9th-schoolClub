from django.shortcuts import render

# Create your views here.

def delete(request, people_id):
    cat =People.objects.get(id=people_id)
    cat.delete()
    return redirect('/')

def edit(request, people_id):
    people = people.objects.get(id=people_id)

    if request.method == "POST":
        form = PeoplePost(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            people.name = form.cleaned_data['name']
            people.age = form.cleaned_data['age']
            people.date = form.cleaned_data['date']
            people.email = form.cleaned_data['email']
            people.introduce = form.cleaned_data['introduce']
            people.save()
            return redirect('/detail/'+str(people.pk))
        
    else:
        form = PeoplePost()
        return render(request, 'postapp/edit_post.html',{'form':form})

    from .models import Profile


def people(request, username): 
	person = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/people.html', {'person': person})
