

from django.db import migrations

def role_status(apps, schemaeditor):
    entries = {
        "developer": "the person on the team who works on issues",
        "product owner": "the person on the team who writes issues",
        "scrum master": "the team's coach"
    }
    Role = apps.get_model("role", "description")
    for key, value in entries.items():
        role_obj = Role(name=key, description=value)
        role_obj.save()


        def team_status(apps, schemaeditor):
            entries = {
                "alpha": "the A team",
                "bravo": "the B team",
                "charlie": "the team's coach"
            }
            Team = apps.get_model("team", "description")
            for key, value in entries.items():
                team_obj = Team(name=key, description=value)
                team_obj.save()


class Migration(migrations.Migration):
