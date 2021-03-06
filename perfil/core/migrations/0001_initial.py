# Generated by Django 2.1.1 on 2018-09-09 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Affiliation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, default="", max_length=127)),
                ("voter_id", models.CharField(blank=True, default="", max_length=12)),
                ("started_in", models.DateField()),
                ("electoral_section", models.IntegerField()),
                ("electoral_zone", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("R", "Regular"),
                            ("C", "Cancelado"),
                            ("D", "Desfiliado"),
                            ("S", "Sub judice"),
                        ],
                        max_length=1,
                    ),
                ),
                ("ended_in", models.DateField(null=True)),
                ("canceled_in", models.DateField(null=True)),
                ("regularized_in", models.DateField(null=True)),
                ("processed_in", models.DateField(null=True)),
                ("extracted_in", models.DateTimeField(null=True)),
                (
                    "cancel_reason",
                    models.CharField(blank=True, default="", max_length=31),
                ),
            ],
            options={
                "verbose_name": "historical political affiliation",
                "verbose_name_plural": "historical political affiliations",
            },
        ),
        migrations.CreateModel(
            name="Candidate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "taxpayer_id",
                    models.CharField(blank=True, default="", max_length=11),
                ),
                ("date_of_birth", models.DateField(null=True)),
                ("gender", models.CharField(blank=True, default="", max_length=16)),
                ("email", models.CharField(blank=True, default="", max_length=128)),
                ("age", models.CharField(blank=True, default="", max_length=16)),
                ("ethinicity", models.CharField(blank=True, default="", max_length=16)),
                (
                    "ethinicity_code",
                    models.CharField(blank=True, default="", max_length=2),
                ),
                (
                    "marital_status",
                    models.CharField(blank=True, default="", max_length=32),
                ),
                (
                    "marital_status_code",
                    models.CharField(blank=True, default="", max_length=32),
                ),
                ("education", models.CharField(blank=True, default="", max_length=32)),
                (
                    "education_code",
                    models.CharField(blank=True, default="", max_length=16),
                ),
                (
                    "nationality",
                    models.CharField(blank=True, default="", max_length=64),
                ),
                (
                    "nationality_code",
                    models.CharField(blank=True, default="", max_length=32),
                ),
                (
                    "occupation",
                    models.CharField(blank=True, default="", max_length=128),
                ),
                (
                    "occupation_code",
                    models.CharField(blank=True, default="", max_length=64),
                ),
                ("election", models.CharField(blank=True, default="", max_length=64)),
                ("year", models.IntegerField()),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("AC", "Acre"),
                            ("AL", "Alagoas"),
                            ("AP", "Amapá"),
                            ("AM", "Amazonas"),
                            ("BA", "Bahia"),
                            ("CE", "Ceará"),
                            ("DF", "Distrito Federal"),
                            ("ES", "Espírito Santo"),
                            ("GO", "Goiás"),
                            ("MA", "Maranhão"),
                            ("MT", "Mato Grosso"),
                            ("MS", "Mato Grosso do Sul"),
                            ("MG", "Minas Gerais"),
                            ("PA", "Pará"),
                            ("PB", "Paraíba"),
                            ("PR", "Paraná"),
                            ("PE", "Pernambuco"),
                            ("PI", "Piauí"),
                            ("RJ", "Rio de Janeiro"),
                            ("RN", "Rio Grande do Norte"),
                            ("RS", "Rio Grande do Sul"),
                            ("RO", "Rondônia"),
                            ("RR", "Roraima"),
                            ("SC", "Santa Catarina"),
                            ("SP", "São Paulo"),
                            ("SE", "Sergipe"),
                            ("TO", "Tocantins"),
                        ],
                        max_length=2,
                    ),
                ),
                ("round", models.IntegerField()),
                ("post", models.CharField(blank=True, default="", max_length=128)),
                ("post_code", models.IntegerField()),
                ("status", models.CharField(blank=True, default="", max_length=64)),
                (
                    "ballot_name",
                    models.CharField(blank=True, default="", max_length=32),
                ),
                ("number", models.IntegerField()),
                ("sequential", models.CharField(blank=True, default="", max_length=16)),
                (
                    "coalition_name",
                    models.CharField(blank=True, default="", max_length=128),
                ),
                (
                    "coalition_description",
                    models.CharField(blank=True, default="", max_length=256),
                ),
                (
                    "coalition_short_name",
                    models.CharField(blank=True, default="", max_length=16),
                ),
                ("max_budget", models.CharField(blank=True, default="", max_length=16)),
                (
                    "round_result",
                    models.CharField(blank=True, default="", max_length=64),
                ),
                ("round_result_code", models.IntegerField(null=True)),
            ],
            options={
                "verbose_name": "candidate",
                "verbose_name_plural": "candidates",
                "ordering": ("-year", "ballot_name"),
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.IntegerField()),
                ("name", models.CharField(blank=True, default="", max_length=63)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("AC", "Acre"),
                            ("AL", "Alagoas"),
                            ("AP", "Amapá"),
                            ("AM", "Amazonas"),
                            ("BA", "Bahia"),
                            ("CE", "Ceará"),
                            ("DF", "Distrito Federal"),
                            ("ES", "Espírito Santo"),
                            ("GO", "Goiás"),
                            ("MA", "Maranhão"),
                            ("MT", "Mato Grosso"),
                            ("MS", "Mato Grosso do Sul"),
                            ("MG", "Minas Gerais"),
                            ("PA", "Pará"),
                            ("PB", "Paraíba"),
                            ("PR", "Paraná"),
                            ("PE", "Pernambuco"),
                            ("PI", "Piauí"),
                            ("RJ", "Rio de Janeiro"),
                            ("RN", "Rio Grande do Norte"),
                            ("RS", "Rio Grande do Sul"),
                            ("RO", "Rondônia"),
                            ("RR", "Roraima"),
                            ("SC", "Santa Catarina"),
                            ("SP", "São Paulo"),
                            ("SE", "Sergipe"),
                            ("TO", "Tocantins"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
            options={
                "verbose_name": "city",
                "verbose_name_plural": "cities",
                "ordering": ("name", "state"),
            },
        ),
        migrations.CreateModel(
            name="Party",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, default="", max_length=63)),
                (
                    "abbreviation",
                    models.CharField(blank=True, default="", max_length=15),
                ),
            ],
            options={
                "verbose_name": "party",
                "verbose_name_plural": "parties",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Politician",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "affiliation_history",
                    models.ManyToManyField(
                        related_name="affiliation_history", to="core.Party"
                    ),
                ),
                (
                    "current_affiliation",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="politician",
                        to="core.Affiliation",
                    ),
                ),
            ],
            options={
                "verbose_name": "politician",
                "verbose_name_plural": "politicians",
                "ordering": ("current_affiliation__name",),
            },
        ),
        migrations.AddIndex(
            model_name="party",
            index=models.Index(
                fields=["abbreviation"], name="core_party_abbrevi_08b18f_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="city",
            index=models.Index(
                fields=["name", "state"], name="core_city_name_b6d716_idx"
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="party",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.Party"
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="place_of_birth",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="core.City"
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="politician",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.Politician",
            ),
        ),
        migrations.AddField(
            model_name="affiliation",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="affiliated",
                to="core.City",
            ),
        ),
        migrations.AddField(
            model_name="affiliation",
            name="party",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="affiliated",
                to="core.Party",
            ),
        ),
        migrations.AddIndex(
            model_name="candidate",
            index=models.Index(fields=["year"], name="core_candid_year_e20107_idx"),
        ),
        migrations.AddIndex(
            model_name="candidate",
            index=models.Index(fields=["state"], name="core_candid_state_6d2ad7_idx"),
        ),
        migrations.AddIndex(
            model_name="candidate",
            index=models.Index(
                fields=["sequential"], name="core_candid_sequent_6bfcea_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="affiliation",
            index=models.Index(fields=["name"], name="core_affili_name_cc96a9_idx"),
        ),
        migrations.AddIndex(
            model_name="affiliation",
            index=models.Index(
                fields=["voter_id"], name="core_affili_voter_i_2c41ae_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="affiliation",
            index=models.Index(fields=["status"], name="core_affili_status_bb7bee_idx"),
        ),
        migrations.AddIndex(
            model_name="affiliation",
            index=models.Index(
                fields=["started_in"], name="core_affili_started_db9e71_idx"
            ),
        ),
    ]
