# Generated by Django 5.0.6 on 2024-06-24 08:53

import bounties.models
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bounty',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('vault_tvl', models.FloatField()),
                ('max_bounty', models.FloatField()),
                ('total_paid', models.FloatField()),
                ('last_updated', models.DateField(auto_now=True)),
                ('owner_address', models.CharField(default='', max_length=100)),
                ('index', models.IntegerField(default=0)),
                ('vault_address', models.CharField(max_length=100)),
                ('program_overview_html', models.TextField(default='')),
                ('rewards_by_threat_level_html', models.TextField(default='')),
                ('optional_assets_in_scope_html', models.TextField(default='')),
                ('optional_impacts_in_scope_html', models.TextField(default='')),
                ('out_of_scope_html', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='BountyAssetInScope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('bounty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='bounties.bounty')),
            ],
        ),
        migrations.CreateModel(
            name='BountyImpactInScope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threat_level', models.CharField(choices=[('Critical', 'Critical'), ('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Low', max_length=100)),
                ('impact', models.TextField()),
                ('bounty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impacts', to='bounties.bounty')),
            ],
        ),
        migrations.CreateModel(
            name='BountyReport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('short_description', models.TextField(default='')),
                ('owner_address', models.CharField(default='', max_length=100)),
                ('pdf', models.FileField(upload_to=bounties.models.bounty_report_path)),
                ('index', models.IntegerField(default=0)),
                ('bounty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='bounties.bounty')),
            ],
        ),
        migrations.CreateModel(
            name='BountyRewardCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('bounty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='bounties.bounty')),
            ],
        ),
        migrations.CreateModel(
            name='BountyReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threat_level', models.CharField(choices=[('Critical', 'Critical'), ('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Low', max_length=100)),
                ('reward_start', models.FloatField(default=0.0)),
                ('reward_end', models.FloatField(default=0.0)),
                ('bounty_reward_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='bounties.bountyrewardcategory')),
            ],
        ),
    ]
