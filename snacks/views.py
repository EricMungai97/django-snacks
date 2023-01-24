from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": 'https://en.wikipedia.org/wiki/Lay%27s#/media/File:Lays_brand_logo.png',
                "title": "Lays Potato Chips",
                "description": "Lay's is a brand of potato chips with different flavors.",

            }, {
                "image_url": "https://unsplash.com/photos/Y-VDI9vQS3M",
                "title": "Granola Bar",
                "description": " bar made of a mixture of oats and other ingredients (such as brown sugar, raisins, coconut, or nuts) that is eaten as a snack.",

            }, {
                "image_url": "https://en.wikipedia.org/wiki/Apple#/media/File:Pink_lady_and_cross_section.jpg",
                "title": "Apple",
                "description": "an edible fruit produced by an apple tree",

            }, {
                "image_url": "https://en.wikipedia.org/wiki/Mango#/media/File:Hapus_Mango.jpg",
                "title": "Mango",
                "description": "is an edible stone fruit produced by the tropical tree Mangifera indica",

            }
        ]

        return context


class AboutView(TemplateView):
    template_name = 'about.html'