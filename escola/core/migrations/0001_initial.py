# Generated by Django 3.0.7 on 2020-06-20 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('matricula', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=11)),
                ('titulacao', models.CharField(choices=[('G', 'Graduado'), ('E', 'Especialista'), ('M', 'Mestre'), ('D', 'Doutor')], max_length=1)),
            ],
        ),
    ]
