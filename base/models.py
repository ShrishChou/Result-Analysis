from django.db import models

# Create your models here.


    
def nullifs(x):
    if x is None:
        return ""
    else:
        return str(x)
def nulliftb(x):
    if x is None:
        return ""
    else:
        return "("+str(x)+")"
    
class Player(models.Model):
    url=models.URLField(default="")
    utrurl=models.URLField(default="")
    data = models.JSONField(default=list,null=True,blank=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    wins = models.PositiveBigIntegerField(default=0)
    game_played = models.PositiveBigIntegerField(default=0)
    def __str__(self):
        return self.name


class Score3set(models.Model):
    wset1 = models.PositiveBigIntegerField()
    lset1 = models.PositiveBigIntegerField()
    tb1 = models.PositiveBigIntegerField(blank=True,null=True)
    wset2 = models.PositiveBigIntegerField()
    lset2 = models.PositiveBigIntegerField()
    tb2 = models.PositiveBigIntegerField(blank=True,null=True)
    wset3 = models.PositiveBigIntegerField(blank=True,null=True)
    lset3 = models.PositiveBigIntegerField(blank=True,null=True)
    tb3= models.PositiveBigIntegerField(blank=True,null=True)
    day = models.DateField(auto_now_add=True)
    tb1s = nulliftb(tb1)
    tb2s = nulliftb(tb2)
    tb3s = nulliftb(tb3)
    wset3s =nullifs(wset3)
    lset3s=nullifs(lset3)
    
    def __str__(self):
        # return (str(self.wset1)+"-"+str(self.lset1)+self.tb1s+"\n"+
        #            str(self.wset2)+"-"+str(self.lset2)+self.tb2s+"\n"+
        #            self.wset3s+"-"+self.lset3s+self.tb3s +"\n" +
        #            "on "+ str(self.day))
        return str(self.day)
class Score8game(models.Model):
    wset1 = models.PositiveBigIntegerField()
    lset1 = models.PositiveBigIntegerField()
    tb1= models.PositiveBigIntegerField(blank=True)
    day = models.DateField(auto_now_add=True)

    def __str__(self):
        return (str(self.wset1)+"-"+str(self.lset1)+"("+str(self.tb1)+")"+"\n"+
                "on "+ str(self.day))

class Duel(models.Model):
    day=models.DateField(auto_now_add=True,blank=True,null=True)
    mitwin = models.BooleanField()
    versus = models.CharField(max_length=100)
    class Meta:
        ordering = ["-day"]

    def __str__(self):
        return "MIT vs "+ self.versus
    
class SinglesMatch(models.Model):
    day=models.DateField(auto_now_add=True,blank=True,null=True)
    duel = models.ForeignKey(Duel, on_delete=models.CASCADE, related_name='singles_matches',default="")
    win = models.BooleanField()
    player1=models.ForeignKey(Player, on_delete=models.CASCADE)
    player2=models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    # score=models.ForeignKey(Score3set,on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.player1.game_played+=1
        if self.win:
            self.player1.wins += 1
            self.player1.save()
    def __str__(self):
        return str(self.player1)+" vs "+str(self.player2)
class DoublesMatch(models.Model):
    duel = models.ForeignKey(Duel, on_delete=models.CASCADE, related_name='doubles_matches',default="")
    win = models.BooleanField()
    player1=models.ForeignKey(Player, related_name="player1", on_delete=models.CASCADE)
    player2=models.ForeignKey(Player, related_name="player2", on_delete=models.CASCADE)
    player3=models.CharField(max_length=100)
    player4=models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    day=models.DateField(auto_now_add=True,blank=True,null=True)
    # score = models.ForeignKey(Score8game,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.player1.game_played+=1
        self.player2.game_played+=1

        if self.win:
            self.player1.wins += 1
            self.player2.wins += 1
            self.player1.save()
            self.player2.save()

    def __str__(self):
        return str(self.player1)+" & "+str(self.player2)+" vs "+str(self.player3)+" & "+str(self.player4)



class Ranking(models.Model):
    ranking = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ranking
