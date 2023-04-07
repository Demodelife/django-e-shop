var mix = {
    methods: {
        submitPayment () {
            this.postData('/api/payment/', {
                name: this.name,
                number: this.number,
                year: this.year,
                month: this.month,
                code: this.code
            }).then(() => {
                alert('Успешная оплата')
                this.number = ''
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
            number: '',
            month: '',
            year: '',
            name: '',
            code: ''
        }
    }
}