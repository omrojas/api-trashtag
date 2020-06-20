import graphene
import garbagecollector.graphql.query
import garbagecollector.graphql.mutation


class Query(garbagecollector.graphql.query.Query, graphene.ObjectType):
    pass


class Mutation(garbagecollector.graphql.mutation.Mutation, graphene.ObjectType):
   pass


schema = graphene.Schema(query=Query, mutation=Mutation)

