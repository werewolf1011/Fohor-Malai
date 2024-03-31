from django.contrib.auth.tokens import PasswordResetTokenGenerator

from six import text_type
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # We need to ensure that the password is a string before we hash it because
        # the 'string' type in Python2 is not the same as the 'str' 
        # type in Python3 so we must be sure that 'password' is always a string.
            
        return(text_type(user.pk)+text_type(timestamp))

generate_token = TokenGenerator()