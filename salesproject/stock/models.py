from django.db import models
from web.models import Product


class StockReceipt(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=100)
    quantity_received = models.PositiveIntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    supplier_paid = models.BooleanField(default=False)
    date_received = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_amount_due = self.quantity_received * self.unit_cost

        self.product.unit_price = self.unit_cost
        self.product.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity_received}"