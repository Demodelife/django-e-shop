var mix = {
    methods: {
        getProfile() {
            this.getData(`/api/profile/`).then(data => {
                this.fullName = data.fullName
                this.avatar = data.avatar
                this.phone = data.phone
                this.email = data.email
            }).catch(() => {
                console.warn('Ошибка при получении профиля')
            })
        },
        changeProfile() {
            if (!this.fullName.trim().length || !this.phone.trim().length || !this.email.trim().length) {
                alert('В форме присутствуют незаполненные поля')
                return
            }

            const formData = new FormData()
            formData.append('fullName', this.fullName)
            formData.append('phone', this.phone)
            formData.append('email', this.email)
            formData.append('avatar', this.avatar)

            this.postData('/api/profile/', formData).then(data => {
                this.fullName = data.FullName
                this.avatar = data.avatar
                this.phone = data.phone
                this.email = data.email
                alert('Успешно сохранено')
            }).catch(() => {
                console.warn('Ошибка при обновлении профиля')
            })
        },
        changePassword() {
            if (
                !this.passwordCurrent.trim().length ||
                !this.password.trim().length ||
                !this.passwordReply.trim().length ||
                this.password !== this.passwordReply
            ) {
                alert('В форме присутствуют незаполненные поля или пароли не совпадают')
                return
            }

            const formData = new FormData()
            formData.append('passwordCurrent', this.passwordCurrent)
            formData.append('password', this.password)
            formData.append('passwordReply', this.passwordReply)

            this.postData('/api/profile/password/', formData).then(() => {
                alert('Успешно сохранено')
                this.passwordCurrent = ''
                this.password = ''
                this.passwordReply = ''
            }).catch(() => {
                console.warn('Ошибка при сохранении пароля')
            })
        },
        setAvatar(event) {
            const target = event.target
            const file = target.files?.[0] ?? null
            if (!file) return

            const formData = new FormData();
            formData.append('avatar', file);

            this.postData('/api/profile/avatar/', formData, {
                    headers: {
                        'Content-Type': `multipart/form-data`,
                        'X-CSRFToken': this.getCookie('csrftoken')
                    },
                }).then((data) => {
                this.avatar = data.url
            }).catch(() => {
                console.warn('Ошибка при обновлении изображения')
            })
        }
    },
    created() {
        this.getProfile();
    },
    data() {
        return {
            fullName: null,
            phone: null,
            email: null,
            avatar: null,
            password: '',
            passwordCurrent: '',
            passwordReply: ''
        }
    },
}