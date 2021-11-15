from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.

oylar = [
    (1, "1 oy"),
    (2, "2 oy"),
    (3, "3 oy"),
    (4, "4 oy"),
    (5, "5 oy"),
    (6, "6 oy"),
    (7, "7 oy"),
    (8, "8 oy"),
    (9, "9 oy"),
    (10, "10 oy"),
    (11, "11 oy"),
    (12, "12 oy")
]

class Kategoriya(models.Model):
    nomi = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Kategoriyalar"
        ordering = ['nomi']

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse('Kategoriyalar')

class Tovar(models.Model):
    nomi = models.CharField(max_length=255)
    narxi = models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
    rangi = models.CharField(max_length=100)
    xotirasi = models.CharField(max_length=100,null=True,blank=True)
    rasm = models.ImageField(upload_to = 'images', null=True,blank=True)
    category = models.ForeignKey(
        Kategoriya,
        on_delete=CASCADE
    )

    def __str__(self):
        return self.nomi
    
    class Meta:
        verbose_name_plural = 'Tovarlar'
        ordering = ['nomi']

    def get_absolute_url(self):
        return reverse('tovarXaqida',args=[str(self.id)])


class Xaridor(models.Model):
    ism = models.CharField(max_length=200)
    familiya = models.CharField(max_length=200)
    OtasiningIsmi = models.CharField(max_length=200)
    manzil = models.CharField(max_length=250)
    pasportSeriyaRaqami = models.CharField(max_length=9)
    telefon = models.CharField(max_length=14)
    rasm = models.ImageField(upload_to='userImages', null=True,blank=True)
    tovarKategoriyasi = models.ForeignKey(
        Kategoriya,
        on_delete=models.CASCADE
    )
    tanlanganTovar = models.ForeignKey(
        Tovar,
        on_delete=models.CASCADE,
        null=True
    )
    qolganSumma = models.DecimalField(max_digits=17,decimal_places=2,default=0.0)
    umumiyTolanganPul = models.DecimalField(max_digits=17,decimal_places=2,default=0.0)
    muddat = models.IntegerField(choices=oylar)
    oylikTolovMiqdori = models.PositiveIntegerField(null=True,blank=True)



    def save(self, *args, **kwargs):
        self.oylikTolovMiqdori = self.tanlanganTovar.narxi/self.muddat
        self.qolganSumma = self.tanlanganTovar.narxi
        self.qolganSumma = int(self.qolganSumma) - int(self.umumiyTolanganPul)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Xaridorlar'
        ordering = ['-ism']

    def __str__(self):
        return self.ism + ' | Krediti: ' + str(self.tanlanganTovar.nomi)
    
    def get_absolute_url(self):
        return reverse('xaridorXaqida',args=[str(self.id)])


class Tolov(models.Model):
    xaridor = models.ForeignKey(
        Xaridor,
        on_delete=models.CASCADE,
        blank=True,related_name='Tolov'
    )
    miqdori = models.DecimalField(max_digits=17,decimal_places=2,default=0.0)
    vaqti = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.xaridor.umumiyTolanganPul = self.xaridor.umumiyTolanganPul+self.miqdori
        self.xaridor.save()
        super(Tolov,self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.xaridor.umumiyTolanganPul = self.xaridor.umumiyTolanganPul - self.miqdori
        self.xaridor.save()
        super(Tolov, self).delete(*args, **kwargs)


    class Meta:
        verbose_name_plural = "Barcha to'lovlar"
        ordering = ['-vaqti']
    
    def __str__(self):
        return str(self.xaridor.ism) + " - miqdori: " + str(self.miqdori)

    def get_absolute_url(self):
        return reverse('BarchaXaridorlar')

class Users_Message(models.Model):
    Ism = models.CharField(max_length=50)
    Familiya = models.CharField(max_length=50)
    Telefon_raqam = models.CharField(max_length=13)
    Xabar = models.TextField()
    Xabar_vaqti = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name_plural = 'Foydalanuvchilardan kelgan xabarlar'
        ordering = ['-Xabar_vaqti']

    def __str__(self):
        return self.Ism