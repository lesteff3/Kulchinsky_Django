from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=35)
    age = models.PositiveSmallIntegerField()
    profession = models.CharField(max_length=40, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'


class ContactInfo(models.Model):
    phone = models.CharField(max_length=50, null=True, default=None)
    address = models.CharField(max_length=50, null=True, default=None)


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=35)
    age = models.PositiveSmallIntegerField()
    group = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL, related_name='person')
    contact_info = models.OneToOneField(ContactInfo, null=True, related_name='person', on_delete=models.SET_NULL)
    hobbies = models.ManyToManyField('Hobby', related_name='person')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'


class Group (models.Model):
    serial_number = models.CharField(max_length=4)
    start_data = models.DateField(null=False)
    finish_data = models.DateField(null=False)

    def __str__(self):
        return self.serial_number


class Hobby(models.Model):
    name = models.CharField(max_length=255, default=None)


class MusicBand(models.Model):
    name = models.CharField(max_length=20)
    style_music = models.CharField(max_length=35)
    year = models.PositiveSmallIntegerField()
    album = models.ForeignKey('Album', null=True, on_delete=models.SET_NULL, related_name='musicband')

    def __str__(self):
        return f'{self.name} {self.style_music} {self.year}'


class Album(models.Model):
    name_album = models.CharField(max_length=255, default=None)
    year = models.PositiveSmallIntegerField()
    track = models.ForeignKey('Track', null=True, on_delete=models.SET_NULL, related_name='album')

    def __str__(self):
        return self.name_album


class Track(models.Model):
    name_track = models.CharField(max_length=255, default=None)
    value_track = models.FloatField(max_length=10, default=None)

    def __str__(self):
        return self.name_track

