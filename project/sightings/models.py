from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator

class Squirrel(models.Model):
     X = models.DecimalField(
         max_length=100,
         help_text=_('Longitude coordinate for squirrel sighting point'),
         blank = True,
         max_digits=18,
         decimal_places = 15,
         )

     Y = models.DecimalField(
         max_length=100,
         help_text=_('Latitude coordinate for squirrel sighting point'),
         blank = True,
         max_digits=18,
         decimal_places = 15,
         )
     
     unique-squirrel-id= models.CharField(
         max_length=100,
         validators=[MinLengthValidator(10)],
         help_text=_('Identification tag for each squirrel sightings. The tag is comprised of "Hectare ID" + "Shift" + "Date" + "Hectare Squirrel Number."'),
         primary_key= True,
         )
     AM = 'AM'
     PM = 'PM'
     SHIFT_CHOICES = (
            (AM,_('AM')),
            (PM,_('PM')),
            )
     Shift  = models.CharField(
         max_length=150,
         choices = SHIFT_CHOICES,
         help_text=_('Value is either "AM" or "PM," to communicate whether or not the sighting session occurred in the morning or late afternoon.'),
         blank = True,
         )
     Date = models.DateField(
         help_text=_('Concatenation of the sighting session day and month.'),
         )

     ADULT = 'Adult'
     JUVENILE = 'Juvenile'

     AGE_CHOICES = (
            (ADULT,_('Adult')),
            (JUVENILE,_('Juvenile')),
            ) 
     Age = models.CharField(
         max_length=100,
         choices = AGE_CHOICES,
         help_text=_('Value is either "Adult" or "Juvenile."'),
         blank = True,
         )
     GREY= 'Grey'
     CINNAMON= 'Cinnamon'
     BLACK = 'Black'
     COLOR_CHOICES = (
            (GREY,_('Grey')),
            (CINNAMON,_('Cinnamon')),
            (BLACK,_('Black')),
         )
     Primary_Fur_Color = models.CharField(
            max_length=100,
            blank=True,
            choices= COLOR_CHOICES,
            help_text=_('Value is either "Gray," "Cinnamon" or "Black."'),
         )
     GROUND_PLANE = 'Ground Plane'
     ABOVE_GROUND = 'Above Ground'
     LOCATION_CHOICES =(
            (GROUND_PLANE,_('Ground Plane')),
            (ABOVE_GROUND,_('Above Ground')),
            )
     Location = models.CharField(
            max_length=50,
            choices = LOCATION_CHOICES,
            blank=True,
            help_text=_('Value is either "Ground Plane" or "Above Ground." Sighters were instructed to indicate the location of where the squirrel was when first sighted.'),
         )
     Specific_Location = models.CharField(
            max_length=200,
            blank=True,
            help_text=_('Sighters occasionally added commentary on the squirrel location. These notes are provided here.'),
         )
     Running = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen running'),
            default = False,
            )
     Chasing = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen chasing another squirrel.'),
            default = False,
            )
     Climbing = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen climbing a tree or other environmental landmark.'),
            default= False,
            )
     Eating = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen eating'),
            default= False,
            )
     Foraging = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen  foraging for food'),
            default = False,
            )
     Other_activities = models.CharField(
            max_length=200,
            blank=True,
            help_text=_('Other activities '),
           )
     Kuks = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was heard kukking, a chirpy vocal communication used for a variety of reasons.'),
            default = False,
            )
     Quaas = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog.'),
            default= False,
            )


     Moans = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk.'),
            default = False,
            )
     Tail_flags = models.BooleanField(
            max_length = 10,
            help_text=_("Squirrel was seen flagging its tail. Flagging is a whipping motion used to exaggerate squirrel's size and confuse rivals or predators. Looks as if the squirrel is scribbling with tail into the air."),
            default = False,
            )
     Tail_twitches = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen twitching its tail. Looks like a wave running through the tail, like a breakdancer doing the arm wave. Often used to communicate interest, curiosity.'),
            default= False,
            )
     Approaches = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen approaching human, seeking food'),
            default= False,
            )
     Indifferent = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was indifferent to human presence'),
            default = False,
            )
     Runs_From = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen running from humans, seeing them as a threat'),
            default= False,
            )
     def __str__(self):
         return self.unique-squirrel-id

    
