from django.db import models


class User(models.Model):

	username = models.CharField(max_length=10)
	password = models.CharField(max_length=8)
	email = models.EmailField()


	def __str__(self):
		return self.username



class Poll(models.Model):
    writer = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    question = models.TextField(max_length=100)
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_four = models.CharField(max_length=30,null=True)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count 

    def __str__(self):
        return self.question + str(self.option_one_count)
