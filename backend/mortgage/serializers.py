from rest_framework import serializers
from mortgage.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    payment = serializers.SerializerMethodField()

    def validate(self, raw_data):
        term_min = raw_data.get('term_min')
        term_max = raw_data.get('term_max')
        rate_min = raw_data.get('rate_min')
        rate_max = raw_data.get('rate_max')
        payment_min = raw_data.get('payment_min')
        payment_max = raw_data.get('payment_max')
        if term_min>term_max or rate_min>rate_max or payment_min>payment_max :
            raise serializers.ValidationError(' min value of the number must be greater than nax value')

        return raw_data

    def get_payment(self, offer):
        price = self.context['request'].query_params.get('price', 0)
        deposit = self.context['request'].query_params.get('deposit', 0)
        term = self.context['request'].query_params.get('term', 0)
        if price == 0 and term == 0:
            if self.context['request'].stream!=None:
                if self.context['request'].stream.method == "PATCH":
                    return 0
            return None
        if price==None or term==None:
            raise serializers.ValidationError('incorrect client request')
        price = int(price)
        deposit = int(deposit)
        term = int(term)
        if price==0 and term!=0 or (term==0 and price!=0):
            raise serializers.ValidationError('price or term can not equal 0')
        if price <= deposit:
            raise serializers.ValidationError('price must be great than deposit')

        loan_sum = price - deposit
        p = offer.rate_max/100/12
        m = term*12
        loan_payment = round((loan_sum * p) / (1 - ((1 + p) **(-m))), 2)
        return loan_payment

    class Meta:
        model = Offer
        fields ="__all__"



