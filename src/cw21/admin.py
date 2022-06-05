from django.contrib import admin

from cw21.models import Student, Person, Group, ContactInfo, Hobby, MusicBand, Album, Track



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'profession')
    fields = ('first_name', 'last_name', 'age')
    readonly_fields = ('age',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'start_data', 'finish_data')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address')


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MusicBand)
class MusicBandAdmin(admin.ModelAdmin):
    list_display = ('name', 'style_music', 'album')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name_album', 'year', 'track')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name_track', 'value_track')