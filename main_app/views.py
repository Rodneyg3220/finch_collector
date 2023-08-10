from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Player, Shoe
from .forms import FeedingForm





# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def players_index(request):
#   return render(request, 'players/index.html', {
#     'players': players
#   })

@login_required
def players_index(request):
    players = Player.objects.filter(user=request.user) 
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

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class PlayerCreate(CreateView):
  model = Player
  fields = ['name', 'position', 'age']

  # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  

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

@login_required
def assoc_shoe(request, player_id, shoe_id):
  Player.objects.get(id=player_id).shoes.add(shoe_id)
  return redirect('detail', player_id=player_id)

@login_required
def unassoc_shoe(request, player_id, shoe_id):
  Player.objects.get(id=player_id).shoes.remove(shoe_id)
  return redirect('detail', player_id=player_id)