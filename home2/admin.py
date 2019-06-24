

# Register your models here.
from django.contrib import admin
from home2.models import Book,Genre,Author,customer

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Genre)
#admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields=('id','name')
    #note:RelatedOnlyFieldListFilter=>applicable hn some fields are related to other tables
    list_filter = ('name','purchase_date',('author',admin.RelatedOnlyFieldListFilter))
    list_filter = ('name','purchase_date')
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

