# Generated migration to remove avg_rating and review_count fields from User model
# These are now calculated properties instead of database fields

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_alter_cart_table_alter_cartitem_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avg_rating',
        ),
        migrations.RemoveField(
            model_name='user',
            name='review_count',
        ),
    ]
