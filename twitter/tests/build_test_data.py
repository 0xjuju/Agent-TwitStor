from twitter.models import *


class Build:

    @staticmethod
    def build_accounts():

        accounts = [
            Account(
                username="bloktopia",
                website="Bloktopia.com",
                linkedin="https://www.linkedin.com/company/bloktopia/?originalSubdomain=uk",
                medium="https://medium.com/@bloktopia",
                follower_count=328_000,
            ),

            Account(
                username="AetherGamesInc",
                website="https://aethergames.io/",
                medium="https://medium.com/@AetherGames",
                follower_count=105_000,
            ),
        ]

        Account.objects.bulk_create(accounts)

    @staticmethod
    def build_posts():
        posts = [
            Post(

            )
        ]
