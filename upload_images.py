
import os
import django
from pathlib import Path

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "hospital.settings"
)

django.setup()

from nurses.models import Nurse

media_root = Path("media")

for nurse in Nurse.objects.all():

    if not nurse.image:
        print(f"SKIPPED: {nurse.name} - No image")
        continue

    image_path = media_root / nurse.image.name

    if not image_path.exists():
        print(f"NOT FOUND: {nurse.name} - {image_path}")
        continue

    try:
        with image_path.open("rb") as image_file:
            nurse.image.save(
                image_path.name,
                image_file,
                save=True
            )

        print(f"UPLOADED: {nurse.name}")

    except Exception as error:
        print(f"ERROR: {nurse.name} - {error}")

print("Image upload process completed.")
