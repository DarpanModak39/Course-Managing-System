# Generated by Django 4.0 on 2022-01-21 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0009_rename_class_code_course_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='analyzeese',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='analyzet1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='analyzet2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='analyzetotal',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='applyese',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='applyt1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='applyt2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='applytotal',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po10',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po11',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po12',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po4',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po5',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po6',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po7',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po8',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1po9',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1pso1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1pso2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co1pso3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po10',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po11',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po12',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po4',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po5',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po6',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po7',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po8',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2po9',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2pso1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2pso2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co2pso3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po10',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po11',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po12',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po4',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po5',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po6',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po7',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po8',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3po9',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3pso1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3pso2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co3pso3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po10',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po11',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po12',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po4',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po5',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po6',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po7',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po8',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4po9',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4pso1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4pso2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co4pso3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po10',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po11',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po12',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po4',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po5',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po6',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po7',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po8',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5po9',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5pso1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5pso2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='co5pso3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseobjective1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseobjective2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseobjective3',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseobjective4',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseobjective5',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseoutcome1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseoutcome2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseoutcome3',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseoutcome4',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseoutcome5',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseoutcomelevel1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseoutcomelevel2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseoutcomelevel3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseoutcomelevel4',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseoutcomelevel5',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='createese',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='createt1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='createt2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='createtotal',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='credits',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='desired_requsite',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='evaluateese',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='evaluatet1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='evaluatet2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='evaluatetotal',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='faculty',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='hod',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='interaction',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='labexperiment',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='lecture',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='module1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='module2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='module3',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='module4',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='module5',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='module6',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='modulehour1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='modulehour2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='modulehour3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='modulehour4',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='modulehour5',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='modulehour6',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='practical',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='reference1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='reference2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='reference3',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='reference4',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='rememberese',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='remembert1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='remembert2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='remembertotal',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='textbook1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='textbook2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='textbook3',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='textbook4',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='tutorial',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='understandese',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='understandt1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='understandt2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='understandtotal',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='usefullink1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='usefullink2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='usefullink3',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='usefullink4',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
