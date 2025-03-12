<template>
	<div class="content">
		<div class="login">
			<div class="login__fondo"></div>
			<div class="login__container">
				<div class="login__img">
					<img src="../../../../static/img/LogoUJEDvertical.png" alt="">
				</div>
				<div class="login__form">
					<form action="">
						<label for="correo">Correo electrónico</label>
						<div class="input-container">
							<img src="../../../../static/img/Icon mail.png" alt="icono" class="icon">
							<input type="email" id="email" name="email" required>
						</div>

						<label for="password">Contraseña</label>
						<div class="input-container">
							<img src="../../../../static/img/Icon tabler key.png" alt="icono" class="icon">
							<input type="password" id="password" name="password" required>
						</div>

						<button type="submit">Ingresar</button>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	export default{
		name:'inicio',
	};
</script>