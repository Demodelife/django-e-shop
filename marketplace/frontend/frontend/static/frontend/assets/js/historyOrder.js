var mix = {
    methods: {
        getHistoryOrder() {
            this.getData("/api/orders")
              .then(data => {
                this.orders = data.orders
              }).catch(() => {
                this.orders = []
                console.warn('Ошибка при получении списка заказов')
            })
        }
    },
    mounted() {
        this.getHistoryOrder();
    },
    data() {
        return {
            orders: [],
        }
    }
}