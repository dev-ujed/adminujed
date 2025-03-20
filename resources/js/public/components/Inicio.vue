<template>
	<div class="content">
		<div class="login">
			<div class="login__fondo"></div>
			<div class="login__container">
				<div class="login__img">
					<img src="../../../../static/img/LogoUJEDvertical.png" alt="">
				</div>
				<div class="login__form">
					<form @submit.prevent="submitForm">
						<label for="correo">Correo electrónico</label>
						<div class="input-container">
							<img src="../../../../static/img/Icon mail.png" alt="icono" class="icon">
							<input v-model="form.email" type="email" id="email" name="email" required>
						</div>

						<label for="password">Contraseña</label>
						<div class="input-container">
							<img src="../../../../static/img/Icon tabler key.png" alt="icono" class="icon">
							<input v-model="form.password" type="password" id="password" name="password" required>
						</div>

						<!-- Mostrar el mensaje de error aquí -->
						<div v-if="errors.message" class="error-message">
							{{ errors.message }}
						</div>

						<button type="submit">Ingresar</button>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'inicio',
		data() {
			return {
				form: {
					email: '',
					password: ''
				},
				errors: {
					message: '' // Aquí se almacenará el mensaje de error
				}
			};
		},
		methods: {
			async submitForm() {
				console.log(document.body.getAttribute("data-root"));
				try {
					const response = await window.axios.post('/login/', this.form);
					const currentUrl = window.location.href;
					window.location.href = currentUrl + 'admi/';
				} catch (error) {
					this.errors.message = error.response?.data?.error || 'Ocurrió un error desconocido.';
				}
			}
		}
	};
</script>

<style scoped>
	.error-message {
		color: red;
		font-size: 14px;
		margin-top: 5px;
		text-align: center;
	}
</style>