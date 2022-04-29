from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from .views import OfferViewSet
from .models import Offer


def fill_db():
    offers = []
    offers.append(Offer.objects.create(bank_name='bank1',
                                       term_min= 5,
                                       term_max= 24,
                                       rate_min=2,
                                       rate_max=12,
                                       payment_min=1000000,
                                       payment_max=10000000
                                       ))
    offers.append(Offer.objects.create(bank_name='bank2',
                                       term_min=15,
                                       term_max=24,
                                       rate_min=2,
                                       rate_max=14,
                                       payment_min=1000000,
                                       payment_max=10000000
                                       ))
    offers.append(Offer.objects.create(bank_name='bank3',
                                       term_min=1,
                                       term_max=44,
                                       rate_min=2,
                                       rate_max=12,
                                       payment_min=1000000,
                                       payment_max=10000000
                                       ))
    offers.append(Offer.objects.create(bank_name='bank4',
                                       term_min=5,
                                       term_max=24,
                                       rate_min=2,
                                       rate_max=12,
                                       payment_min=1000000,
                                       payment_max=10000000
                                       ))
    return offers


class OfferApiTestCase(APITestCase):

    def setUp(self):
        self.offers = fill_db()

    def test_create(self):
         factory = APIRequestFactory()
         request = factory.post('/api/offer/', {'bank_name': 'bank5', 'term_min': 5, 'term_max': 14, 'rate_min': 2, 'rate_max': 22, 'payment_min': 1000000, 'payment_max':100000000})
         view = OfferViewSet.as_view({'post': 'create'})
         response = view(request)
         self.assertEqual(response.data['bank_name'], 'bank5')

    def test_update(self):
        factory = APIRequestFactory()
        request = factory.patch('/api/offer/',
                               {'bank_name': 'bank5', 'term_min': 10, 'term_max': 14, 'rate_min': 2, 'rate_max': 22,
                                'payment_min': 1000000, 'payment_max': 100000000})
        view = OfferViewSet.as_view({'patch': 'update'})
        response = view(request, pk=self.offers[0].pk)
        self.assertEqual(response.data['term_min'], 10)

    def test_list(self):
         factory = APIRequestFactory()
         request = factory.get('/api/offer/')
         view = OfferViewSet.as_view({'get': 'list'})
         response = view(request)
         self.assertEqual(response.status_code, 200)

    def test_check_payment(self):
        factory = APIRequestFactory()
        request = factory.get('/api/offer/?price=10000000&deposit=1000000&term=10')
        view = OfferViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data[0]['payment'], 129123.85)



