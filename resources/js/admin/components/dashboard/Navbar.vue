<template>
    <div>
        <section class="user-bar-admin">
            <button id="user-bar-btn" class="user-bar-admin__btn" @click="$emit('toggle-sidebar')">
                <img class="user-bar-admin__btn-icon" src="/static/img/Hamburger.png" alt="Menú Icon">
                <span class="user-bar-admin__btn-text">S.I.M</span>
                <span class="user-bar-admin__btn-text-large">Sistema de Indicadores y Monitoreo</span>
            </button>
            <div class="user-bar-admin__profile">
                <div class="user-bar-admin__avatar-container">
                    <img class="user-bar-admin__avatar" src="/static/img/icono-user.png" alt="Icono user">
                </div>
                <p class="user-bar-admin__user-name">Litzy Yulissa Nevarez García</p>
                <ul class="user-bar-admin__profile-menu">
                    <li class="user-bar-admin__profile-menu-item user--info center-text">
                        <div class="user-bar-admin__menu-avatar-container">
                            <img class="user-bar-admin__menu-avatar" src="/static/img/icono-user.png" alt="Icono user">
                            <p class="mt-2 mb-3">Litzy Yulissa Nevarez García</p>
                        </div>
                    </li>
                    <li class="user-bar-admin__profile-menu-item">
                        <a href="" class="user-bar-admin__profile-menu-link">Modificar perfil</a>
                    </li>
                    <li class="user-bar-admin__profile-menu-item">
                        <a href="" class="user-bar-admin__profile-menu-link">
                            Cerrar sesión
                        </a>
                    </li>
                </ul>
            </div>
        </section>
    </div>
</template>
<script>
    export default {
		name: 'navbar',
    }
</script>