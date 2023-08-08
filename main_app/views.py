from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player
from .forms import FeedingForm





# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def players_index(request):
  return render(request, 'players/index.html', {
    'players': players
  })

def players_index(request):
    players = Player.objects.all() 
    return render(request, 'players/index.html', 
    { 
        'players': players 
    })

def players_detail(request, player_id):
  player = Player.objects.get(id=player_id)
  feeding_form = FeedingForm()
  return render(request, 'players/detail.html', { 'player': player, 'feeding_form': feeding_form })

def add_feeding(request, player_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.player_id = player_id
    new_feeding.save()
  return redirect('detail', player_id=player_id)

class PlayerCreate(CreateView):
  model = Player
  fields = '__all__'
  success_url = '/players/{player_id}'

class PlayerUpdate(UpdateView):
  model = Player
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'position', 'age']

class PlayerDelete(DeleteView):
  model = Player
  success_url = '/players'