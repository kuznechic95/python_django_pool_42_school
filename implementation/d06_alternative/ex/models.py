from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone

class Tip(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    author = models.ForeignKey(User)
    created = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)

    def upvote(self, user):
        try:
            self.tip_votes.create(user=user, tip=self, vote_type=1)
            self.votes += 1
            self.author.reputation.rep += 5
            self.author.reputation.save()
            self.save()
        except IntegrityError:
            try:
                self.tip_votes.get(user=user, vote_type=1).delete()
                self.votes -= 1
                self.author.reputation.rep -= 5
                self.author.reputation.save()
            except UserVotes.DoesNotExist:
                pass
            return 0
        return 1

    def downvote(self, user):
        try:
            self.tip_votes.create(user=user, tip=self, vote_type=-1)
            self.votes -= 1
            self.author.reputation.rep -= 2
            self.author.reputation.save()
            self.save()
        except IntegrityError:
            try:
                self.tip_votes.get(user=user, vote_type=-1).delete()
                self.votes += 1
                self.author.reputation.rep += 2
                self.author.reputation.save()
            except UserVotes.DoesNotExist:
                pass
            return 0
        return 1


class UserVotes(models.Model):
    user = models.ForeignKey(User, related_name="user_votes")
    tip = models.ForeignKey(Tip, related_name="tip_votes", on_delete=models.CASCADE)
    vote_type = models.IntegerField()

    class Meta:
        unique_together = ('user', 'tip')


class Reputation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rep = models.IntegerField(default=0)
