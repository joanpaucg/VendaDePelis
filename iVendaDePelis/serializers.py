from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from models import *
class FilmSerializer(HyperlinkedModelSerializer):
    uri= HyperlinkedIdentityField(view_name='ivendadepelis:film-detail')
    user=CharField(read_only=True)
    reviews = HyperlinkedRelatedField(many=True, read_only=True, view_name='ivendadepelis:filmreview-detail')
    class Meta:
        model=Film
        fields=('uri','title','year','duration','genre','plot','price','reviews','user')
class FilmReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='ivendadepelis:filmreview-detail')
    film = HyperlinkedRelatedField(view_name='ivendadepelis:film-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Review
        fields = ('uri', 'rating', 'opinion', 'user','film')
class ActorSerializer(HyperlinkedModelSerializer):
    uri=HyperlinkedIdentityField(view_name='ivendadepelis:actor-detail')
    films=HyperlinkedRelatedField(many=True,read_only=True,view_name='ivendadepelis:film-detail')
    class Meta:
        model= Actor
        fields=('uri','films','name','country','birthday','country','biography')


