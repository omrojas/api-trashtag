import graphql_jwt
import graphene
from django.contrib.auth import get_user_model
from graphql import GraphQLError
from .types import UserType


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        try:
            user = get_user_model()(
                username=username,
                email=email,
            )
            user.set_password(password)
            user.save()
            return CreateUser(user=user)
        except Exception as e:
            raise GraphQLError('A problem has occurred, check the data or try again.')


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()
