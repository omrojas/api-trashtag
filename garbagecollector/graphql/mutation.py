import graphene
import graphql_jwt
from django.contrib.auth.models import User
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from garbagecollector.models import Organization, UserMessage

from .types import UserType


class SignUp(graphene.Mutation):
    class Arguments:
        firstName = graphene.String(required=True)
        lastName = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        organization_id = graphene.Int()

    saved = graphene.Boolean()
    
    def mutate(self, info, firstName, lastName, password, email, organization_id=None):
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=firstName, last_name=lastName)
            user.save()
            saved = user.id != None
            return SignUp(saved=saved)
        except Exception as e:
            print(e)
            raise GraphQLError('A problem has occurred, check the data or try again.')


class CreateOrganization(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        operation_area = graphene.String(required=True)
        phone_one = graphene.String(required=True)
        phone_two = graphene.String(required=True)
        address = graphene.String(required=True)
        manager_name = graphene.String(required=True)
        manager_phone = graphene.String(required=True)
        manager_email = graphene.String(required=True)
    
    saved = graphene.Boolean()

    def mutate(self, info, name, operation_area, phone_one, phone_two, address, manager_name, manager_phone, manager_email):
        try:
            organization = Organization(name=name, operation_area=operation_area, phone_one=phone_one, phone_two=phone_two, address=address, manager_name=manager_name, manager_phone=manager_phone, manager_email=manager_email)
            organization.save()
            saved = organization.id != None
            return CreateOrganization(saved=saved)
        except Exception as e:
            raise GraphQLError('A problem has occurred, check the data or try again.')


class CreateUserMessage(graphene.Mutation):
    class Arguments:
        subject = graphene.String(required=True)
        message = graphene.String(required=True)

    saved = graphene.Boolean()

    @login_required
    def mutate(self, info, subject, message):
        try:
            user = info.context.user
            message = UserMessage(user= user, subject=subject, message=message)
            message.save()
            saved = message.id != None
            return CreateUserMessage(saved=saved)
        except Exception as e:
            raise GraphQLError('A problem has occurred, check the data or try again.')


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    sign_up = SignUp.Field()
    create_organization = CreateOrganization.Field()
    create_user_message = CreateUserMessage.Field()
