import { createApp, nextTick } from "vue"; // Usa createApp en lugar de Vue
import Inicio from "./public/components/Inicio.vue";
import Admin from "./admin/components/dashboard/Admin.vue";
import axios from 'axios'; 

window.axios = axios;

function getCSRFToken() {
    const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return csrfToken ? csrfToken.split('=')[1] : null;
}
axios.defaults.headers.common['X-CSRFToken'] = getCSRFToken();
axios.defaults.headers.post['Content-Type'] = 'application/json';

// Crea la aplicación
createApp({
    data() {
        return {
            path: document.body.getAttribute("data-root"),
            iconsMap: {},
            isLoading: true,
            isResizing: false,
            menu: null,
            menuFocusTrap: null,
            menuIsVisible: false,
            menuIsCollapsed: false,
            menuIsOpen: false,
            queryMenuMd: false,
            queryMenuLg: false,
            screenSize: "",
            selectedGroups: [],
            hasSchedule: false,
        };
    },
    computed: {
        lowestHour() {
            let minHours = this.selectedGroups
                .filter((group) => group.length > 0)
                .map((group) =>
                    Math.min(...group.map((item) => Number(item.hora_inicio.split(":")[0])))
                );
            return minHours.length > 0 ? Math.min(...minHours) : 8;
        },
        highestHour() {
            let maxHours = this.selectedGroups
                .filter((group) => group.length > 0)
                .map((group) =>
                    Math.max(...group.map((item) => Number(item.hora_fin.split(":")[0])))
                );
            return maxHours.length > 0 ? Math.max(...maxHours) : 14;
        },
        getHours() {
            let hours = [];
            const STANDARD_MIN_HOUR = 8;
            const STANDARD_MAX_HOUR = 14;
            let minimumHour = Math.min(this.lowestHour, STANDARD_MIN_HOUR);
            let maximumHour = Math.max(this.highestHour, STANDARD_MAX_HOUR);

            for (let index = minimumHour; index <= maximumHour; index++) {
                hours.push(index + ":00");
            }

            return hours;
        },
    },
    mounted() {
        this.registerMenuBreakpoints();
        this.menu = document.querySelector("#db-menu");
		
        nextTick(() => (this.isLoading = false));
    },
    methods: {
        toggleMenu() {
            const isOpening = this.screenSize === "sm" ? !this.menuIsVisible : this.menuIsCollapsed;

            if (isOpening && this.screenSize !== "lg") {
                this.$emit("showMenuOverlay");
                nextTick(() => this.setMenuFocusTrap());
            }

            if (this.screenSize === "sm") {
                this.menuIsOpen = !this.menuIsOpen;
                this.menuIsVisible = !this.menuIsVisible;
                this.menuIsCollapsed = false;
            } else {
                this.menuIsOpen = this.menuIsCollapsed;
                this.menuIsVisible = true;
                this.menuIsCollapsed = !this.menuIsCollapsed;
            }

            if (this.screenSize === "lg") {
                sessionStorage.setItem("menuCollapsed", !isOpening);
            }

            nextTick(() => {
                this.handleMenuFocus(isOpening);
                if (!isOpening) {
                    this.destroyMenuFocusTrap();
                }
            });
        },
        handleMenuFocus(isOpening) {
            if (isOpening && this.screenSize === "lg") {
                return this.menu.querySelector("button, [href], input, [tabindex='0']").focus();
            }

            document.querySelector(isOpening ? "#main-menu-btn" : "#user-bar-btn").focus();
        },
        registerMenuBreakpoints() {
            this.queryMenuMd = window.matchMedia("(min-width:600px)");
            this.queryMenuLg = window.matchMedia("(min-width:1100px)");

            this.queryMenuMd.addListener(this.setMenuVisibility);
            this.queryMenuLg.addListener(this.setMenuVisibility);

            this.setMenuVisibility();
        },
        setMenuVisibility() {
            this.$emit("closeMenuOverlay");
            this.isResizing = true;

            if (this.queryMenuLg.matches) {
                this.menuIsCollapsed = sessionStorage.getItem("menuCollapsed") === "true";
                this.menuIsVisible = true;
                this.menuIsOpen = sessionStorage.getItem("menuCollapsed") !== "true";
                this.screenSize = "lg";
            } else if (this.queryMenuMd.matches) {
                this.menuIsCollapsed = true;
                this.menuIsVisible = true;
                this.menuIsOpen = false;
                this.screenSize = "md";
            } else {
                this.menuIsCollapsed = false;
                this.menuIsVisible = false;
                this.menuIsOpen = false;
                this.screenSize = "sm";
            }

            nextTick(() => (this.isResizing = false));
        },
    },
})
.component("inicio", Inicio)
.component("admin", Admin)
.mount("#dashboard");
