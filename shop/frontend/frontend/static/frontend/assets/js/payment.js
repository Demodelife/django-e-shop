var mix = {
    methods: {
        submitPayment () {
            this.postData('/api/payment/', {
                name: this.name,
                card: this.card,
                year: this.year,
                month: this.month,
                code: this.code
            }).then(() => {
                alert('Успешная оплата')
                this.card = ''
                this.name = ''
                this.year = ''
                this.month = ''
                this.code = ''
            }).catch(() => {
                console.warn('Ошибка при оплате')
            })
        }
    },
    data () {
        return {
            card: '',
            month: '',
            year: '',
            name: '',
            code: ''
        }
    }
}