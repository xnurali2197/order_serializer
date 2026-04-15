class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.product.price * obj.quantity
