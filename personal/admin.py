from django.contrib import admin
from personal.models import Event, Caption, Image


class CaptionInline(admin.TabularInline):
	model = Caption


class CaptionAdmin(admin.ModelAdmin):
	search_fields = ['description']
	list_display = ['id', 'description']

admin.site.register(Caption, CaptionAdmin)


class ImageAdmin(admin.ModelAdmin):
	list_display = ['id', 'filename']

admin.site.register(Image, ImageAdmin)


class EventAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'get_image', 'get_caption']
	inlines = [
		CaptionInline,
	]

	readonly_fields = ('image_filename',)

	def image_filename(self, obj):
		return obj.image.filename

	def get_image(self, obj):
		return obj.image.filename

	get_image.short_description = 'Image'
	get_image.admin_order_field = 'image__filename'

	def get_caption(self, obj):
		return ' '.join([caption.description for caption in obj.captions.all().order_by('id')])

	get_caption.short_description = 'Captions'
	get_caption.admin_order_field = 'captions__description'

admin.site.register(Event, EventAdmin)