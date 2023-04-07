var mix = {
    methods: {
        getCartItems() {
            this.getData("/api/cart")
              .then(data => {
                this.cartProducts = data.items
              })
        },
        submitBasket () {
            this.postData('/api/orders', Object.values(this.basket))
                .then(data => {
                    this.order.id = data.id
                    this.order.products = data.products
                    this.basket = {}
                    location.assign('/order')
                }).catch(() => {
                    console.warn('Ошибка при создании заказа')
                })
        }
    },
    mounted() {
        // this.getCartItems();
    },
    data() {
        return {
            cartProducts: [],
        }
    }
}