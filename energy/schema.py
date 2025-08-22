import graphene
from decimal import Decimal
from graphene_django import DjangoObjectType
from .models import Customer, Tariff, UsageRecord

class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer

class TariffType(DjangoObjectType):
    class Meta:
        model = Tariff

class UsageRecordType(DjangoObjectType):
    total_cost = graphene.Float()

    class Meta:
        model = UsageRecord

    def resolve_total_cost(self, info):
        return float(Decimal(self.kwh_used) * self.tariff.price_per_kwh)

class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)
    all_tariffs = graphene.List(TariffType)
    customer_usage = graphene.List(
        UsageRecordType,
        customer_id=graphene.Int(required=True),
        start_date=graphene.Date(),
        end_date=graphene.Date(),
    )

    def resolve_all_customers(root, info):
        return Customer.objects.all()

    def resolve_all_tariffs(root, info):
        return Tariff.objects.all()

    def resolve_customer_usage(root, info, customer_id, start_date=None, end_date=None):
        qs = UsageRecord.objects.filter(customer_id=customer_id)
        if start_date:
            qs = qs.filter(timestamp__date__gte=start_date)
        if end_date:
            qs = qs.filter(timestamp__date__lte=end_date)
        return qs

class CreateUsage(graphene.Mutation):
    usage = graphene.Field(UsageRecordType)

    class Arguments:
        customer_id = graphene.Int()
        tariff_id = graphene.Int()
        kwh_used = graphene.Float()

    def mutate(root, info, customer_id, tariff_id, kwh_used):
        usage = UsageRecord.objects.create(
            customer_id=customer_id,
            tariff_id=tariff_id,
            kwh_used=kwh_used
        )
        return CreateUsage(usage=usage)

class Mutation(graphene.ObjectType):
    create_usage = CreateUsage.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
