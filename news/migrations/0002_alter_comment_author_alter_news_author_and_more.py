# Generated by Django 4.2 on 2023-05-18 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_groups_alter_user_user_permissions'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.author'),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.author'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='commentstatus',
            unique_together={('author', 'comment')},
        ),
        migrations.AlterUniqueTogether(
            name='newsstatus',
            unique_together={('author', 'news')},
        ),
    ]
