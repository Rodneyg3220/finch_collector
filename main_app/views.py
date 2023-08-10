from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Player, Shoe
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
  id_list = player.shoes.all().values_list('id')
  shoes_player_doesnt_have = Shoe.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'players/detail.html', { 'player': player, 'feeding_form': feeding_form, 'shoes': shoes_player_doesnt_have })

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
  fields = ['name', 'position', 'age']
  

class PlayerUpdate(UpdateView):
  model = Player
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'position', 'age']

class PlayerDelete(DeleteView):
  model = Player
  success_url = '/players'


class ShoeList(ListView):
  model = Shoe

class ShoeDetail(DetailView):
  model = Shoe

class ShoeCreate(CreateView):
  model = Shoe
  fields = '__all__'

class ShoeUpdate(UpdateView):
  model = Shoe
  fields = ['name', 'color']

class ShoeDelete(DeleteView):
  model = Shoe
  success_url = '/shoes'

def assoc_shoe(request, player_id, shoe_id):
  Player.objects.get(id=player_id).shoes.add(shoe_id)
  return redirect('detail', player_id=player_id)

def unassoc_shoe(request, player_id, shoe_id):
  Player.objects.get(id=player_id).shoes.remove(shoe_id)
  return redirect('detail', player_id=player_id)