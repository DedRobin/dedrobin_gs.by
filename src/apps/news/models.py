from django.db import models


class Company(models.Model):
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    name = models.CharField()

    def __str__(self):
        return f"Company '{self.name}'"


class News(models.Model):
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    topic = models.CharField(max_length=150)
    link = models.URLField()
    image_src = models.URLField()
    text = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(db_index=True)

    # Foreign key
    company = models.ForeignKey(
        to=Company, on_delete=models.CASCADE, related_name="news"
    )

    def __str__(self):
        return f"News from '{self.topic}' (Date: {self.created_at})"
