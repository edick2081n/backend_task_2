from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from mortgage.models import Offer
from mortgage.serializers import OfferSerializer
from rest_framework.exceptions import ValidationError


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [AllowAny]

    def list(self, request, **kwargs):
        try:
            price = int(self.request.query_params.get('price'))
            deposit = int(self.request.query_params.get('deposit'))
            term = int(self.request.query_params.get('term'))
            loan_sum = price - deposit
            if loan_sum<=0:
                raise ValidationError('the loan amount is less than or equal to 0')
            queryset = self.get_queryset().filter(
                payment_min__lte=loan_sum, payment_max__gte=loan_sum,
                term_min__lte=term, term_max__gte=term)

        except:
            queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True, context={'request':request})
        return Response(serializer.data)



