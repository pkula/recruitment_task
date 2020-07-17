from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    """
    Account model holds current balance of every user.
    """
    balance = models.DecimalField(_('Balance'), decimal_places=2, max_digits=12)


class Operation(models.Model):
    """
    Each change (deposit, purchase, etc..) of Account's balance should be reflected
    in the Operation model for auditing purposes.
    """
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='operation',
        verbose_name=_('Account'),
    )
    date = models.DateTimeField(_('created'), auto_now_add=True)
    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=12)
    # action


class Book(models.Model):
    """
    Model stores a title of the book and its price.
    """
    title = models.CharField(_('Title'), max_length=255)
    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=12)


class Purchase(models.Model):
    """
    Model stores data about purchases.
    """
    books = models.ManyToManyField(
        Book,
        verbose_name=_('Book'),
        blank=True,
        related_name='purchases',
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='purchase',
        verbose_name=_('Account'),
    )

    def get_price(self):
        pass
