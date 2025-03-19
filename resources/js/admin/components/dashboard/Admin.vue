<template>
    <div class="admin-container">
        <Navbar @toggle-sidebar="toggleSidebar" />
        <div class="admin-main">
            <Sidebar :showSidebar="showSidebar" @close-sidebar="showSidebar = false" />
            <div class="admin-main__content">
                <h1>contenido main</h1>
            </div>
        </div>
    </div>
</template>
<script>

    import Navbar from './Navbar.vue';
    import Sidebar from './Sidebar.vue';

    export default {
		name: 'admin',

        components: {
            Navbar,
            Sidebar
        },

        data() {
            return {
                showSidebar: false
            };
        },
        methods: {
            toggleSidebar() {
                this.showSidebar = !this.showSidebar;
            }
        }
    }
</script>