# Generated by Django 2.2.1 on 2019-09-10 20:20

import django.db.models.deletion
from django.db import migrations, models

import pretix.base.models.fields
import pretix.base.models.giftcards


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0134_auto_20190909_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('issuance', models.DateTimeField(auto_now_add=True)),
                ('secret', models.CharField(db_index=True, default=pretix.base.models.giftcards.gen_giftcard_secret, max_length=190, unique=True)),
                ('currency', models.CharField(max_length=10)),
                ('issued_in', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issued_gift_cards', to='pretixbase.OrderPosition')),
                ('issuer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issued_gift_cards', to='pretixbase.Organizer')),
            ],
        ),
        migrations.CreateModel(
            name='GiftCardTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='pretixbase.GiftCard')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gift_card_transactions', to='pretixbase.Order')),
                ('payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gift_card_transactions', to='pretixbase.OrderPayment')),
                ('refund', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gift_card_transactions', to='pretixbase.OrderRefund')),
            ],
        ),
        migrations.CreateModel(
            name='GiftCardAcceptance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_card_issuer_acceptance', to='pretixbase.Organizer')),
                ('issuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_card_collector_acceptance', to='pretixbase.Organizer')),
            ],
        ),
    ]
