var mix = {
    methods: {
        getCartItems() {
            this.getData("/api/basket/")
              .then(data => {
                this.cartProducts = data
              })
        },
        submitBasket () {
            this.postData('/api/orders/', Object.values(this.basket))
                .then(data => {
                    this.order.orderId = data.orderId
                    this.order.fullName = data.fullName
                    this.order.email = data.email
                    this.order.createdAt = data.createdAt
                    this.order.phone = data.phone
                    this.order.status = data.status
                    this.order.paymentType = data.paymentType
                    this.order.products = data.products
                    this.order.totalCost = data.totalCost
                    location.assign('/order/')
                }).catch(() => {
                    console.warn('Ошибка при создании заказа')
                })

        }
    },
    mounted() {
        this.getCartItems();
    },
    data() {
        return {
            cartProducts: [],
        }
    }
}