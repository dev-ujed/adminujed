<template>
    <div>
        <nav id="dashboard-menu" class="dashboard-menu-admin" :class="{ 'dashboard-menu-admin--visible': showSidebar }">
            <button class="close-sidebar-btn" @click="$emit('close-sidebar')">
                ✖
            </button>
            <div class="dashboard-menu-admin__img">
                <img src="/static/img/LogoUJEDvertical.png" alt="Logo Ujed">
            </div>
            <ul class="dashboard-menu-admin__col-sections">
                <li v-for="(item, index) in menuItems" 
                    :key="index"
                    :class="['dashboard-menu-admin__section', { 'dashboard-menu-admin__section--active': activeIndex === index }]">
                    <button  type="button" class="dashboard-menu-admin__section-btn" @click="setActive(index, item.url)">
                        <img class="dashboard-menu-admin__title" :src="item.icon" :alt="item.text">
                        <span>{{ item.text }}</span>
                        
                    </button>
                </li>
            </ul>
        </nav>
    </div>
</template>
<script>
    export default {
		name: 'Sidebar',
        props: { showSidebar: Boolean },

        data() {
            return {
                activeIndex: 0,
                menuItems: [
                    { text: 'Profesores', icon: '/static/img/Icon users-outline_red.png', url:'/admi/profesor/' },
                    { text: 'Unidades', icon: '/static/img/Icon_red.png', url:'/admi/unidad/' }
                ],
                siteUrl : ''
            };
        },

        methods: {
            setActive(index,  url) {
                console.log(this.siteUrl+url)
                window.location.href = this.siteUrl+url
            }
        },
        mounted(){
            this.siteUrl = document.body.getAttribute('data-root')
            const path = window.location.pathname;

            if (path.includes('admi/profesor')) {
                this.activeIndex = 0;
            }
            else{
                this.activeIndex = 1;
            }
        }
    }
</script>