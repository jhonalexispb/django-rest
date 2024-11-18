from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    """ def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'user_id': self.user.id})
        data.update({'email': self.user.email})
        return data """
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        token['email'] = user.email
        return token