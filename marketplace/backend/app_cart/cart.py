from django.conf import settings



class Cart(object):
    """Класс корзина"""


    def __init__(self, request):
        """
        Инициализация корзины
        """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product, count=1, update_quantity=False):
        """
        Добавление товаров в корзину
        """

        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'id': product_id,
                'count': 0,
                'price': str(product.price),
                "category": product.category.pk,
                "date": str(product.date),
                "title": product.title,
                "description": product.description,
                "href": product.href,
                "freeDelivery": product.freeDelivery,
                "reviews": len(product.reviews.all()),
                "rating": float(product.rating),
                'images': [str(image.image.url) for image in product.images.all()],
            }

        if update_quantity:
            self.cart[product_id]['count'] = count
        else:
            self.cart[product_id]['count'] += count

        total = product.price * self.cart[product_id]['count']
        self.cart[product_id]['price'] = float(total)

        self.save()


    def save(self):
        """
        Сохранение корзины в сессии
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def remove(self, product, count):
        """
        Удаление товара из корзины
        """

        product_id = str(product.id)

        if product_id in self.cart:

            if self.cart[product_id]['count'] > count:
                self.cart[product_id]['price'] -= float(product.price) * count
                self.cart[product_id]['count'] -= count
            else:
                del self.cart[product_id]


            self.save()


    def clear(self):
        """
        Удаление корзины из сессии
        """

        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
