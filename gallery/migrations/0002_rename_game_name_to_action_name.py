from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mediaitem",
            old_name="game_name",
            new_name="action_name",
        ),
        migrations.AlterField(
            model_name="mediaitem",
            name="action_name",
            field=models.CharField(max_length=255, verbose_name="Назва події"),
        ),
    ]
