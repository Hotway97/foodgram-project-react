# Generated by Django 4.0.4 on 2022-05-28 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_amountingredient_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amountingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amountingredient', to='api.ingredient', verbose_name='Ингридиент'),
        ),
        migrations.AlterField(
            model_name='amountingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amountingredient', to='api.recipe', verbose_name='Рецепт'),
        ),
    ]
