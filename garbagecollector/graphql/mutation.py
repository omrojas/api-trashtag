import graphene
import graphql_jwt
from django.contrib.auth.models import User
from django.db.models import Min, Sum
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from garbagecollector.models import (Cleanup, Level, Organization, Trash,
                                     TrashCleanup, UserMessage, UserProfile)

from .types import TrashQuantity


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
            level = Level.objects.get(id=1)

            user = User.objects.create_user(username=email, email=email, password=password, first_name=firstName, last_name=lastName)
            user.save()
            saved = user.id != None

            profile = UserProfile(user=user, level=level)
            profile.save()

            if saved and organization_id is not None:
                # TODO linkt organization id and user
                print(organization_id)

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


class CleanUp(graphene.Mutation):
    class Arguments:
        trashes = graphene.List(TrashQuantity, required=True)

    saved = graphene.Boolean()

    @login_required
    def mutate(self, info, trashes):
        try:
            user = info.context.user
            if len(trashes) > 0:
                cleanup = Cleanup(user=user)
                cleanup.save()
                
                for e in trashes:
                    trash = Trash.objects.get(id=e.trashId)
                    trashCleanup = TrashCleanup(cleanup=cleanup, trash=trash, quantity=e.quantity)
                    trashCleanup.save()

                update_user_level(user)
                return CleanUp(saved=True)

            return CleanUp(saved=False)
        except Exception as e:
            raise GraphQLError('A problem has occurred, check the data or try again.')


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    sign_up = SignUp.Field()
    create_organization = CreateOrganization.Field()
    create_user_message = CreateUserMessage.Field()
    cleanup = CleanUp.Field()


def update_user_level(user):
    try:
        profile = UserProfile.objects.filter(user=user).first()
        garbageCollected = TrashCleanup.objects.filter(cleanup__user=user).aggregate(Sum('quantity'))['quantity__sum']
        nextLevelCleanups= Level.objects.filter(cleanups__gte=garbageCollected).aggregate(Min('cleanups'))['cleanups__min']
        nextLevel = Level.objects.filter(cleanups=nextLevelCleanups).first()
        if (profile.level is not None) and (nextLevel is not None) and (profile.level.id != nextLevel.id):
            profile.level = nextLevel
            profile.save()
    except Exception as e:
        print(e)
