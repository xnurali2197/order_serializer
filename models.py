class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
