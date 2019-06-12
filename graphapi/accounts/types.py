import graphene


class ProfileInput(graphene.InputObjectType):

    first_name = graphene.String(description='First Name')
    last_name = graphene.String(description='First Name')
    age = graphene.Int(description='Age')
    city = graphene.String(description='City')
    address = graphene.String(description='Address')
    zip_code = graphene.Int(description='Zip Code')
    slogan = graphene.String(description='Slogan')
    bio = graphene.String(description='Bio')
